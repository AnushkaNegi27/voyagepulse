import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ENV_PATH = os.path.join(BASE_DIR, ".env")
load_dotenv(ENV_PATH)

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    APP_NAME = os.getenv("APP_NAME", "VoyagePulse")
    APP_VERSION = os.getenv("APP_VERSION", "0.1.0")

    @app.get("/api/health")
    def health():
        return jsonify({"status": "ok", "service": APP_NAME})

    @app.get("/api/version")
    def version():
        return jsonify({"name": APP_NAME, "version": APP_VERSION})

    # 🔹 New route to handle file upload
    @app.post("/api/upload")
    def upload():
        if "file" not in request.files:
            return jsonify({"error": "No file uploaded"}), 400
        
        file = request.files["file"]
        text = file.read().decode(errors="ignore")  # read file content (works for txt/pdf/docx if plain text)

        found = "timings" in text.lower()
        return jsonify({
            "filename": file.filename,
            "contains_timings": found
        })

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=5000)
