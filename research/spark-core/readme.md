### 1. Spark Core:
- Thành phần chính của Spark, cung cấp các API cơ bản cho **RDD (Resilient Distributed Dataset)**, cho phép thao tác và xử lý dữ liệu phân tán.
- Hỗ trợ các thao tác như *map, filter, reduce, join, và group by*.

RDD là nền tảng của Spark, cung cấp khả năng xử lý dữ liệu phân tán mạnh mẽ và hiệu quả. Mặc dù các API cấp cao hơn như DataFrame và Dataset hiện đang được sử dụng phổ biến hơn, RDD vẫn là phần cốt lõi và được sử dụng trong các tình huống yêu cầu xử lý dữ liệu tùy chỉnh và tối ưu hóa cao.

### Ví dụ
Ví dụ về cách sử dụng Spark Core để thao tác và xử lý dữ liệu phân tán bằng RDD (Resilient Distributed Dataset). Ví dụ này minh họa các thao tác cơ bản như map, filter, reduce, join, và groupBy.

#### Ví dụ về Spark Core với PySpark

1. Khởi tạo SparkContext: Đây là bước đầu tiên để sử dụng Spark.
2. Tạo RDD: Chúng ta sẽ tạo một RDD từ một danh sách đơn giản.
3. Thực hiện các thao tác cơ bản trên RDD:
   - map: Áp dụng một hàm lên từng phần tử của RDD.
   - filter: Lọc các phần tử của RDD dựa trên một điều kiện.
   - reduce: Gộp các phần tử của RDD bằng cách sử dụng một hàm gộp (aggregate).
   - groupBy: Nhóm các phần tử của RDD dựa trên một khóa.
   - join: Thực hiện phép nối giữa hai RDD dựa trên một khóa chung.

#### Chạy ví dụ

`spark-submit --master local[4] spark-core-demo.py`

Lệnh --master local[4] chỉ định rằng ứng dụng sẽ chạy trên máy cục bộ với 4 luồng thực thi.

Do chạy trên local chỉ có 1 instance Spark, nên chạy lệnh sau:

`spark-submit --master local spark-core-demo.py`

