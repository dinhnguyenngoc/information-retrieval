from pyspark.sql import SparkSession
import logging

# Thiết lập mức độ log
logging.getLogger("py4j").setLevel(logging.ERROR)

logFile = "/Users/dinhnguyen/software/spark-3.5.1-bin-hadoop3/README.md"  # Should be some file on your system
spark = SparkSession.builder.appName("SimpleApp").getOrCreate()
logData = spark.read.text(logFile).cache()

# Thiết lập mức độ log cho SparkContext
spark.sparkContext.setLogLevel("WARN")

numAs = logData.filter(logData.value.contains('a')).count()
numBs = logData.filter(logData.value.contains('b')).count()

print("Lines with a: %i, lines with b: %i" % (numAs, numBs))

spark.stop()
