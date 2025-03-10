from flask import Flask, jsonify
from flask_cors import CORS
import os
import platform
import socket
import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Database configuration from environment variables
db_config = {
    'host': os.environ.get('DB_HOST', 'localhost'),
    'port': os.environ.get('DB_PORT', '5432'),
    'name': os.environ.get('DB_NAME', 'myapp'),
    'user': os.environ.get('DB_USER', 'postgres'),
    'password': os.environ.get('DB_PASSWORD', 'postgres')
}

@app.route('/api/data', methods=['GET'])
def get_data():
    """Return demo data for the frontend to display"""
    return jsonify({
        'message': 'Hello from Flask API!',
        'timestamp': datetime.datetime.now().isoformat(),
        'environment': os.environ.get('FLASK_ENV', 'production'),
        'system_info': {
            'hostname': socket.gethostname(),
            'platform': platform.platform(),
            'python_version': platform.python_version()
        },
        'database_config': {
            'host': db_config['host'],
            'port': db_config['port'],
            'database': db_config['name'],
            # Don't include username/password in response
        }
    })

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint for container orchestration"""
    return jsonify({'status': 'healthy', 'service': 'api'})

if __name__ == '__main__':
    # Get port from environment or default to 5000
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', 'False').lower() in ['true', '1', 't']
    
    app.run(host='0.0.0.0', port=port, debug=debug)