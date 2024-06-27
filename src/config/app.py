from flask_openapi3 import Info, OpenAPI

from src.config.routes import apis, root

from .database import db, migrate

from flask_cors import CORS


def create_app(environment_name: str):

    app = OpenAPI(
        __name__, info=Info(title="efood API", summary="Super efood", version="1.0.0"), doc_prefix="/docs", swagger_url="/"
    )
    CORS(app)

    app.config.from_object(environment_name)

    db.init_app(app)

    migrate.init_app(app, db)

    for api in apis:
        app.register_api(api)

    app.register_blueprint(root)
    return app
