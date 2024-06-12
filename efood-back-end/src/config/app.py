from flask_openapi3 import Info, OpenAPI

from src.config.routes import apis, root

from .database import db, migrate


def create_app(environment_name: str):
    # Init flask openapi3
    app = OpenAPI(
        __name__, info=Info(title="IPC API", summary="Super IPC", version="1.0.0"), doc_prefix="/docs", swagger_url="/"
    )

    # Load settings
    app.config.from_object(environment_name)

    # Setup sql alchemy

    db.init_app(app)

    # Setup flask migrate
    migrate.init_app(app, db)

    # Register apis
    for api in apis:
        app.register_api(api)

    # Register redirect url
    app.register_blueprint(root)
    return app
