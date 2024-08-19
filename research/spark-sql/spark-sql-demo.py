from pyspark.sql import SparkSession

# Khởi tạo SparkSession
spark = SparkSession.builder \
    .appName("Spark SQL Example") \
    .getOrCreate()

# Thiết lập mức độ log cho SparkContext
spark.sparkContext.setLogLevel("ERROR")

# Đọc file CSV vào DataFrame
df = spark.read.csv("posts.csv", header=True, inferSchema=True)

# Hiển thị schema của DataFrame
df.printSchema()

# Hiển thị một vài dòng dữ liệu
df.show()

# Tạo một bảng tạm thời từ DataFrame
df.createOrReplaceTempView("posts")

# Thực hiện truy vấn SQL
result = spark.sql("SELECT authorName, COUNT(*) as post_count FROM posts GROUP BY authorName ORDER BY post_count DESC")

# Hiển thị kết quả truy vấn
result.show()

# Dừng SparkSession
spark.stop()
