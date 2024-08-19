### 2. Spark SQL:
- Hỗ trợ xử lý dữ liệu có cấu trúc và bán cấu trúc bằng ngôn ngữ SQL hoặc các API dữ liệu dạng bảng.
- Cung cấp công cụ Catalyst Optimizer để tối ưu hóa các truy vấn SQL.

### Ví dụ
Ví dụ về cách sử dụng Spark SQL để xử lý dữ liệu có cấu trúc và bán cấu trúc. Ví dụ này sẽ minh họa cách sử dụng DataFrame API của Spark SQL, thực hiện các truy vấn SQL, và tận dụng Catalyst Optimizer để tối ưu hóa các truy vấn.

#### Ví dụ về Spark SQL với PySpark
1. Khởi tạo SparkSession: Bước đầu tiên để sử dụng Spark SQL.
2. Tạo DataFrame từ một file CSV: Đọc dữ liệu từ file CSV vào DataFrame.
3. Thực hiện các thao tác SQL: Đăng ký DataFrame dưới dạng một bảng tạm thời và thực hiện các truy vấn SQL.
4. Sử dụng Catalyst Optimizer: Spark SQL tự động tối ưu hóa các truy vấn SQL.

### Chạy ví dụ

`spark-submit --master local spark-sql-demo.py`
