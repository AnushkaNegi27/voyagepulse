import os
import re
from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
from docx import Document

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ENV_PATH = os.path.join(BASE_DIR, ".env")
load_dotenv(ENV_PATH)


def extract_text(file):
    """Extract text from txt or docx file"""
    filename = file.filename.lower()

    if filename.endswith(".txt"):
        return file.read().decode(errors="ignore")

    elif filename.endswith(".docx"):
        doc = Document(file)
        return "\n".join([p.text for p in doc.paragraphs])

    else:
        return file.read().decode(errors="ignore")


def extract_timings(text):
    """Find all timings in text like 10:00, 14:30, 18:00 etc"""
    pattern = r"\b(?:[01]?\d|2[0-3]):[0-5]\d\b"
    return re.findall(pattern, text)


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

    # 🔹 File upload + extraction
    @app.post("/api/upload")
    def upload():
        if "file" not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        file = request.files["file"]

        try:
            text = extract_text(file)
        except Exception as e:
            return jsonify({"error": f"Failed to extract text: {str(e)}"}), 500

        timings = extract_timings(text)

        return jsonify({
            "filename": file.filename,
            "contains_timings": len(timings) > 0,
            "preview": text[:500],   # show first 500 chars
            "extracted_timings": timings
        })

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

