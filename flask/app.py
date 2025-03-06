from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

# CORS(app, origins=["*"]) // crazy train
CORS(app, origins=["http://localhost:3000"], methods=['GET', 'POST', 'PUT', 'DELETE'], 
    allow_headers=["Content-Type", "Authorization"], expose_headers=["X-Token"], 
    supports_credentials=True)

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({"message": "Hello from Flask!"})

if __name__ == '__main__':
    app.run(debug=True)
