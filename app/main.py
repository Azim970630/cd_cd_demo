from flask import Flask, jsonify

# Remove unused logger import if not used
from app.config.settings import PORT, HOST, DEBUG


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return jsonify({"status": "healthy"})

    @app.route("/health")
    def health_check():
        return jsonify({"status": "healthy"})

    @app.route("/api/v1/version")
    def version():
        return jsonify({"version": "1.0"})

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host=HOST, port=PORT, debug=DEBUG)
