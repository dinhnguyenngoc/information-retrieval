from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark.graphx import Graph

# Khởi tạo Spark Context
sc = SparkContext("local", "GraphX Example")
spark = SparkSession.builder.appName("GraphX Example").getOrCreate()

# Dữ liệu cạnh (Edge) của đồ thị (dạng RDD)
edges = sc.parallelize([(1, 2), (2, 3), (3, 1), (3, 4), (4, 1)])

# Tạo Graph từ cạnh
graph = Graph.from_edges(edges)

# Tính toán PageRank
ranks = graph.pageRank(tol=0.01).vertices

# Hiển thị kết quả
for (id, rank) in ranks.collect():
    print(f"Vertex {id} has rank: {rank}")

# Dừng Spark Context
sc.stop()
