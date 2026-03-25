from flask import Flask, jsonify, request
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Unka API Endpoint (Verify this from Network Tab)
API_URL = "https://vibrantacademykotaapi.akamai.net.in/v1/get_content"

@app.route('/api/lectures', methods=['GET'])
def get_lectures():
    class_id = request.args.get('class', '11') # Default Class 11
    
    # Headers to bypass security
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Referer": "https://vibrantacademy.com/",
        "Origin": "https://vibrantacademy.com",
        "Accept": "application/json"
    }
    
    # In parameters ko unki API ke hisab se change karein
    params = {
        "class": class_id,
        "token": "YOUR_TOKEN_IF_ANY" 
    }

    try:
        response = requests.get(API_URL, headers=headers, params=params, timeout=10)
        # Agar JSON mil raha hai toh return karein
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e), "status": "failed"}), 500

if __name__ == '__main__':
    print("DevCoderz Server Running on http://127.0.0.1:5000")
    app.run(port=5000, debug=True)
