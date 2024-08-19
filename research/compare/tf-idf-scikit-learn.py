# Prompt: Hãy cho 1 ví dụ về tính toán độ tương đồng của câu truy vấn và tập dữ liệu văn bản dùng tf-idf và scikit-learn

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Tập dữ liệu văn bản
documents = [
    "The quick brown fox jumps over the lazy dog",
    "Never jump over the lazy dog quickly",
    "A lazy dog does not jump over the quick brown fox",
    "Dogs are great pets",
    "Foxes are wild animals"
]

# Câu truy vấn
query = "quick brown fox"

# Tạo đối tượng TfidfVectorizer và chuyển đổi văn bản thành ma trận TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents + [query])

# Tính toán độ tương đồng cosine giữa câu truy vấn và các văn bản
cosine_similarities = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])

# Lấy chỉ số của văn bản có độ tương đồng cao nhất
most_similar_document_idx = cosine_similarities.argsort()[0][-1]

# In ra văn bản có độ tương đồng cao nhất
print(f"TF-IDF using scikit-learn")
print(f"Document: {documents[most_similar_document_idx]}")
print(f"Cosine Similarity: {cosine_similarities[0][most_similar_document_idx]}")
