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
# Non repository-based implementation
class TfidfService:
    def calculate_tfidf(self, text):
        # Implement your TF-IDF calculation logic here
        return {"data": text, "tfidf_score": 0.5, "page_rank": 0.8}