from flask import Flask, jsonify, request
from controller import Controller
from flask_cors import CORS

controller = Controller()

def create_app():
    app = Flask(__name__)
    return app

app = create_app()
CORS(app)

@app.route('/weather/<location>/<format>')
def get_weather(location, format):
    weather_info = controller.get_weather(location, format)
    return jsonify(weather_info)








if __name__=="__main__":
    app.run(host='0.0.0.0', port=5000)

