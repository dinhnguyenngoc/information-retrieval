from pyspark.sql import SparkSession
from pyspark.sql.functions import split, explode, col
import os

# Khởi tạo SparkSession
# .config("spark.submit.deployMode", "cluster") \
spark = SparkSession.builder \
    .appName("Word Count Example") \
    .master("yarn") \
    .getOrCreate()
    
# Hiển thị phiên bản của Spark
print(f"SPARK VERSION: {spark.version}")

# Hiển thị tên của Spark Master
print(f"SPARK MASTER: {spark.sparkContext.master}")

# Chuỗi văn bản trực tiếp
text = ["Hello world", "Hello Spark", "Hello from PySpark"]

# Tạo DataFrame từ danh sách chuỗi
text_df = spark.createDataFrame(text, "string").toDF("value")

# Chia nhỏ các dòng văn bản thành các từ
words = text_df.select(explode(split(col("value"), " ")).alias("word"))

# Đếm số lần xuất hiện của mỗi từ
word_counts = words.groupBy("word").count()

# Sắp xếp kết quả theo số lần xuất hiện
sorted_word_counts = word_counts.orderBy(col("count").desc())

# Hiển thị kết quả
print("Sorted Word Counts:")
sorted_word_counts.show()

# Thu thập kết quả vào một danh sách
results = sorted_word_counts.collect()

# Lấy cấu hình Spark
deploy_mode = spark.conf.get("spark.submit.deployMode", "unknown")

# Define the file name
file_name = "word-count.txt"

if deploy_mode == "client":
    # Get the current working directory
    current_directory = os.getcwd()

    # Create the full file path
    full_file_path = os.path.join(current_directory, file_name)

    # Ghi kết quả vào tập tin word-count.txt
    with open(full_file_path, "w") as file:    
        file.write("Sorted Word Counts:\n")
        for row in results:
            file.write(f"{row['word']}: {row['count']}\n")
    
    # Print the full file path
    print(f"File saved at (client): {full_file_path}")

if deploy_mode == "cluster":
    # Write the results to HDFS
    full_file_path = "hdfs://namenode:9000/user/root/output/word-count.txt"

    # Save results as text file on HDFS
    sorted_word_counts.write.mode("overwrite").csv(full_file_path, header=True)

    # Print the full file path
    print(f"File saved at (cluster): {full_file_path}")

# Dừng SparkSession
spark.stop()
