from pyspark import SparkContext

# Khởi tạo SparkContext
sc = SparkContext("local", "Spark Core Example")

# Thiết lập mức độ log cho SparkContext
sc.setLogLevel("ERROR")

# Tạo một RDD từ một danh sách
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rdd = sc.parallelize(data)

# Áp dụng hàm map để nhân đôi giá trị của mỗi phần tử
mapped_rdd = rdd.map(lambda x: x * 2)

# Lọc các phần tử chẵn
filtered_rdd = mapped_rdd.filter(lambda x: x % 2 == 0)

# Sử dụng reduce để tính tổng các phần tử
sum_of_elements = filtered_rdd.reduce(lambda x, y: x + y)

# Tạo một RDD từ các cặp khóa-giá trị
pair_rdd = sc.parallelize([("a", 1), ("b", 2), ("a", 3), ("b", 4)])

# Sử dụng groupBy để nhóm các phần tử theo khóa
grouped_rdd = pair_rdd.groupBy(lambda x: x[0])

# Hiển thị kết quả của groupBy
grouped_result = grouped_rdd.mapValues(lambda x: list(x)).collect()
print("Grouped RDD:", grouped_result)

# Tạo một RDD khác để thực hiện phép join
pair_rdd2 = sc.parallelize([("a", 5), ("b", 6)])

# Thực hiện phép join giữa hai RDD
joined_rdd = pair_rdd.join(pair_rdd2)

# Hiển thị kết quả của join
joined_result = joined_rdd.collect()
print("Joined RDD:", joined_result)

# Dừng SparkContext
sc.stop()
