from pyspark.sql import SparkSession
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.linalg import Vectors

# Khởi tạo SparkSession
spark = SparkSession.builder \
    .appName("MLlib Example") \
    .getOrCreate()

# Thiết lập mức độ log cho SparkContext
spark.sparkContext.setLogLevel("ERROR")

# Tạo DataFrame từ dữ liệu mẫu
data = [
    (0, Vectors.dense([0.0, 1.1, 0.1]), 0.0),
    (1, Vectors.dense([2.0, 1.0, -1.0]), 1.0),
    (2, Vectors.dense([2.0, 1.3, 1.0]), 0.0),
    (3, Vectors.dense([0.0, 1.2, -0.5]), 0.0)
]

schema = ["id", "features", "label"]
df = spark.createDataFrame(data, schema=schema)

# Tạo VectorAssembler để kết hợp các cột thành một vector tính năng duy nhất
assembler = VectorAssembler(inputCols=["features"], outputCol="assembled_features")

# Chuyển đổi DataFrame
assembled_df = assembler.transform(df)

# Tạo một mô hình Logistic Regression
lr = LogisticRegression(featuresCol="assembled_features", labelCol="label")

# Huấn luyện mô hình
model = lr.fit(assembled_df)

# Dự đoán trên cùng tập dữ liệu
predictions = model.transform(assembled_df)

# Hiển thị kết quả dự đoán
predictions.select("id", "features", "label", "prediction").show()

# Đánh giá mô hình
evaluator = BinaryClassificationEvaluator(rawPredictionCol="rawPrediction", labelCol="label")
accuracy = evaluator.evaluate(predictions)
print(f"Accuracy: {accuracy}")

# Dừng SparkSession
spark.stop()
