import os
from typing import Dict, Any

import yaml
import json
import connexion
import logging.config
from wine_predictor_api import specs


def read_file(file_name: str):
    with open(file_name) as stream:
        return stream.read()


def init_logger(name=None):
    with open(os.getenv('LOGGING_CONFIG', "logging.yaml")) as stream:
        logging_config = yaml.safe_load(stream)
        logging.config.dictConfig(logging_config)
        return logging.getLogger(name)


def init_config():
    with open(os.getenv('API_CONFIG', "config.json")) as stream:
        return json.load(stream)


logger = init_logger()
api_config: Dict[str, Any] = dict()


def create_app():
    api_config = init_config()
    spec_options = api_config.get("spec_options", {})
    spec_options['version'] = read_file("VERSION")

    app = connexion.FlaskApp(__name__, specification_dir=specs.where())
    app.add_api("openapi_spec.yaml", arguments=spec_options)
    return app.app


__all__ = ['logger', 'api_config']