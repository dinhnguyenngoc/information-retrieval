from flask import Blueprint, request, jsonify
from dependency_injector.wiring import inject, Provide
from src.dependency_container import DependencyContainer
from src.services.tfidf_service import TfidfService

blueprint = Blueprint('tfidf', __name__)

@blueprint.route('/search', methods=['POST'])
@inject
def get_tfidf(tfidf_service: TfidfService = Provide[DependencyContainer.tfidf_service]):
    input_data = request.json
    result = tfidf_service.calculate_tfidf(input_data)
    return jsonify(result)