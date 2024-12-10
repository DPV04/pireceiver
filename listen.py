from flask import Flask, request, jsonify
from flask_cors import CORS

# Create Flask app
app = Flask(__name__)


CORS(app)

# Define a route
@app.route('/process/', methods=['POST'])
def process_request():
    try:
        # Parse JSON data from the incoming request
        data = request.get_json()
        print("Received data:", data)
        
        # Process the data and send a response
        print("Received data:", data)
        response_message = f"{data['message']}"
        return jsonify({"message": response_message}), 200
    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": str(e)}), 500

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000)