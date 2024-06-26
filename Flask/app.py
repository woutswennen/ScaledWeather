from flask import Flask, jsonify, request
from controller import Controller

controller = Controller()

def create_app():
    app = Flask(__name__)
    return app

app = create_app()

@app.route('/weather/<location>/<format>')
def get_weather(location, format):
    weather_info = controller.get_weather(location, format)
    return jsonify(weather_info)








if __name__=="__main__":
    app.run(debug=True)

