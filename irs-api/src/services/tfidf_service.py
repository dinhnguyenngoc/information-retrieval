# tfidf.py
# from src.services.repository_service import RepositoryService
# from src.infrastructure.repositories.repository import Repository

# class TfidfService(RepositoryService):
#     def __init__(self, repository: Repository):
#         super().__init__(repository)

#     def calculate_tfidf(self, text):
#         # Implement your TF-IDF calculation logic here
#         # You can use the self.repository to interact with the database if needed
#         return {"tfidf_score": 0.5}


# src/services/tfidf_service.py

# import math
# import numpy as np
# # Module distance từ thư viện scipy để tính toán các loại khoản cách giữa các điểm
# from scipy.spatial import distance
# # Module TfidfVectorizer để biến đổi text thành ma trận các đặc trưng TF-IDF
# from sklearn.feature_extraction.text import TfidfVectorizer


# Non repository-based implementation
class TfidfService:
    def calculate_tfidf(self, text):
        docs = [
            'data mining is awesome. data mining helps to find frequent itemsets in database.',
            'information retrieval is cool. information retrieval helps to search data quickly.',
            'natural language processing is interesting. it helps computer to better understand text.'
        ];

        query = text['query']
        

        # Implement your TF-IDF calculation logic here
        return {"data": text['query'], "tfidf_score": 0.5, "page_rank": 0.8}