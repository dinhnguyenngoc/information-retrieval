from pyspark.sql import SparkSession
from pyspark.ml.feature import HashingTF, IDF, Tokenizer
from pyspark.ml.linalg import Vectors, DenseVector
from pyspark.sql.functions import col, udf
from pyspark.sql.types import DoubleType

# Khởi tạo SparkSession
spark = SparkSession.builder \
    .appName("TF-IDF Similarity Example") \
    .getOrCreate()

# Dữ liệu văn bản mẫu
data = [
    (0, "this is a sample document"),
    (1, "this document is another sample"),
    (2, "and this is a third example document"),
]

# Tạo DataFrame từ dữ liệu mẫu
df = spark.createDataFrame(data, ["id", "text"])

# Tokenizer để tách các từ trong văn bản
tokenizer = Tokenizer(inputCol="text", outputCol="words")
wordsData = tokenizer.transform(df)

# HashingTF để tính toán TF (Term Frequency)
hashingTF = HashingTF(inputCol="words", outputCol="rawFeatures", numFeatures=20)
featurizedData = hashingTF.transform(wordsData)

# IDF để tính toán IDF (Inverse Document Frequency)
idf = IDF(inputCol="rawFeatures", outputCol="features")
idfModel = idf.fit(featurizedData)
rescaledData = idfModel.transform(featurizedData)

# Hiển thị kết quả TF-IDF
rescaledData.select("id", "features").show(truncate=False)

# Câu truy vấn
query = "sample document"

# Tạo DataFrame cho câu truy vấn
queryDF = spark.createDataFrame([(99, query)], ["id", "text"])
queryWordsData = tokenizer.transform(queryDF)
queryFeaturizedData = hashingTF.transform(queryWordsData)
queryRescaledData = idfModel.transform(queryFeaturizedData)

# Lấy vector TF-IDF của câu truy vấn
queryVector = queryRescaledData.select("features").collect()[0]["features"]

# Hàm tính Cosine Similarity
def cosine_similarity(v1, v2):
    dot_product = float(v1.dot(v2))
    magnitude = v1.norm(2) * v2.norm(2)
    return dot_product / magnitude if magnitude != 0 else 0.0

# Chuyển đổi hàm thành UDF
cosine_similarity_udf = udf(cosine_similarity, DoubleType())

# Thêm vector của câu truy vấn vào DataFrame chính
queryVectorDF = rescaledData.rdd.map(lambda row: (row.id, row.text, row.features, DenseVector(queryVector))).toDF(["id", "text", "features", "queryVector"])

# Tính độ tương đồng giữa câu truy vấn và các văn bản
similarityDF = queryVectorDF.withColumn("similarity", cosine_similarity_udf(col("features"), col("queryVector")))

# Hiển thị kết quả độ tương đồng
similarityDF.select("id", "text", "similarity").orderBy(col("similarity").desc()).show(truncate=False)

# Dừng SparkSession
spark.stop()
