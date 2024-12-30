from flask import Flask, jsonify
from app.utils.logging import logger
from app.config.settings import PORT, HOST, DEBUG

def create_app():
    app = Flask(__name__)
    
    @app.route('/health')
    def health_check():
        return jsonify({'status': 'healthy'})
    
    @app.route('/api/v1/version')
    def version():
        return jsonify({'version': '1.0'})
        
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host=HOST, port=PORT, debug=DEBUG)