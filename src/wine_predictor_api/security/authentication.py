from wine_predictor_api import api_config

PASSWD = api_config.get("basic_cred")


def basic_auth(username, password):
    if PASSWD.get(username) == password:
        return {"sub": username}

    # optional: raise exception for custom error response
    return None
