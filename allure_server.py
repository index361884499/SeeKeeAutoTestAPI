from flask import Flask, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/<path:path>')
def serve_allure(path):
    return send_from_directory('allure/reports/20250416-225512', path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)