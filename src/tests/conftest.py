import pytest
import os
from wine_predictor_api import create_app


@pytest.fixture()
def app():
    app = create_app()
    app.config.update(
        TESTING=True
    )
    yield app


@pytest.fixture()
def app_client(app):
    return app.test_client()


@pytest.fixture()
def app_runner(app):
    return app.test_cli_runner()


@pytest.hookimpl
def pytest_configure(config):
    os.environ["API_CONFIG"] = "config.template.json"
