from pyspark import SparkContext

# Tạo SparkContext
sc = SparkContext("local", "RDD Example")

# Tạo một RDD từ một danh sách
data = [1, 2, 3, 4, 5]
rdd = sc.parallelize(data)

# Thực hiện một phép biến đổi (transformation)
rdd2 = rdd.map(lambda x: x * 2)

# Thực hiện một hành động (action)
result = rdd2.collect()

# In kết quả
print(result)

# Dừng SparkContext
sc.stop()
