# Prompt: Hãy cho 1 ví dụ về tính toán độ tương đồng của câu truy vấn và tập dữ liệu văn bản dùng tf-idf và python chạy trên apache spark

from pyspark.sql import SparkSession
from pyspark.ml.feature import HashingTF, IDF, Tokenizer
from pyspark.sql.functions import col, udf
from pyspark.sql.types import DoubleType
from pyspark.ml.linalg import Vectors, DenseVector
import numpy as np

# Khởi tạo SparkSession
spark = SparkSession.builder.appName("TFIDF-Similarity").getOrCreate()

# Tập dữ liệu văn bản
documents = [
    "The quick brown fox jumps over the lazy dog",
    "Never jump over the lazy dog quickly",
    "A lazy dog does not jump over the quick brown fox",
    "Dogs are great pets",
    "Foxes are wild animals"
]

# Câu truy vấn
query = "quick brown fox"

# Tạo DataFrame từ danh sách văn bản
df = spark.createDataFrame([(doc,) for doc in documents], ["document"])

# Tokenize văn bản
tokenizer = Tokenizer(inputCol="document", outputCol="words")
wordsData = tokenizer.transform(df)

# Tính TF (Term Frequency)
hashingTF = HashingTF(inputCol="words", outputCol="rawFeatures", numFeatures=20)
featurizedData = hashingTF.transform(wordsData)

# Tính IDF (Inverse Document Frequency)
idf = IDF(inputCol="rawFeatures", outputCol="features")
idfModel = idf.fit(featurizedData)
rescaledData = idfModel.transform(featurizedData)

# Chuyển câu truy vấn thành DataFrame
query_df = spark.createDataFrame([(query,)], ["document"])
query_wordsData = tokenizer.transform(query_df)
query_featurizedData = hashingTF.transform(query_wordsData)
query_rescaledData = idfModel.transform(query_featurizedData)

# Lấy vector TF-IDF của câu truy vấn
query_vector = query_rescaledData.select("features").first().features

# Hàm tính độ tương đồng cosine
def cosine_similarity(v1, v2):
    v1_dense = np.array(v1.toArray())
    v2_dense = np.array(v2.toArray())
    dot_product = np.dot(v1_dense, v2_dense)
    norm_v1 = np.linalg.norm(v1_dense)
    norm_v2 = np.linalg.norm(v2_dense)
    return float(dot_product / (norm_v1 * norm_v2))

# Định nghĩa UDF để tính độ tương đồng cosine
cosine_similarity_udf = udf(lambda v: cosine_similarity(query_vector, v), DoubleType())
similarity_df = rescaledData.withColumn("similarity", cosine_similarity_udf(col("features")))

# Sắp xếp theo độ tương đồng và lấy văn bản có độ tương đồng cao nhất
most_similar_document = similarity_df.orderBy(col("similarity").desc()).first()

# In kết quả
print(f"TF-IDF using PySpark")
print(f"Document: {most_similar_document['document']}")
print(f"Cosine Similarity: {most_similar_document['similarity']}")

# Dừng SparkSession
spark.stop()
