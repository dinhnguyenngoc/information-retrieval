from .service_context import blueprint as service_context_blueprint
from .tfidf_controller import blueprint as tfidf_blueprint

def setup_blueprints(app) -> None:
    app.register_blueprint(service_context_blueprint, url_prefix="/v1")
    app.register_blueprint(tfidf_blueprint, url_prefix="/v1")
    return app


__all__ = ['setup_blueprints']
