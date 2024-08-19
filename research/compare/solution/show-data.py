import pyorient
from pyspark.sql import SparkSession

# Khởi tạo Spark Session
spark = SparkSession.builder \
    .appName("TF-IDF Example") \
    .getOrCreate()

# Kết nối tới OrientDB
client = pyorient.OrientDB("localhost", 2424)
client.connect("root", "oracle")
client.db_open("tfidf", "root", "oracle")

# Truy vấn dữ liệu từ lớp Document
query = "SELECT text FROM Document"
documents = client.query(query)

# Chuyển đổi dữ liệu từ OrientDB sang RDD của Spark
documents_rdd = spark.sparkContext.parallelize([doc.oRecordData for doc in documents])
documents_df = spark.createDataFrame(documents_rdd)

# Hiển thị dữ liệu
documents_df.show()
