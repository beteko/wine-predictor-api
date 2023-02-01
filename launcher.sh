export PYTHONPATH="src"
export API_CONFIG="config.json"
export FLASK_DEBUG=true
export FLASK_APP="wine_predictor_api:create_app"

PORT=5000

python -m flask run -h 0.0.0.0 -p $PORT
