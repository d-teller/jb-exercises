from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import psycopg2
import time

app = Flask(__name__)
CORS(app)

# Database connection details from environment variables
DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_PORT = os.environ.get('DB_PORT', '5432')
DB_NAME = os.environ.get('DB_NAME', 'myapp')
DB_USER = os.environ.get('DB_USER', 'postgres')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'postgres')

def get_db_connection():
    """Create a connection to the PostgreSQL database"""
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    conn.autocommit = True
    return conn

@app.route('/api/users', methods=['GET'])
def get_users():
    """Get all users from the database"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, email, created_at FROM users ORDER BY id')
        users = []
        for row in cursor.fetchall():
            users.append({
                'id': row[0],
                'name': row[1],
                'email': row[2],
                'created_at': row[3].isoformat() if row[3] else None
            })
        cursor.close()
        conn.close()
        return jsonify(users)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/users', methods=['POST'])
def create_user():
    """Create a new user in the database"""
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        
        if not name or not email:
            return jsonify({'error': 'Name and email are required'}), 400
            
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id, created_at',
            (name, email)
        )
        user_id, created_at = cursor.fetchone()
        cursor.close()
        conn.close()
        
        return jsonify({
            'id': user_id,
            'name': name,
            'email': email,
            'created_at': created_at.isoformat() if created_at else None
        }), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint for container orchestration"""
    try:
        # Try to connect to the database
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT 1')
        cursor.close()
        conn.close()
        return jsonify({'status': 'healthy', 'database': 'connected'})
    except Exception as e:
        return jsonify({'status': 'unhealthy', 'error': str(e)}), 500

if __name__ == '__main__':
    # Wait for database to be ready
    retries = 5
    while retries > 0:
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('SELECT 1')
            cursor.close()
            conn.close()
            print("Database connection successful")
            break
        except Exception as e:
            retries -= 1
            print(f"Database connection failed: {e}")
            print(f"Retrying in 5 seconds... ({retries} attempts left)")
            time.sleep(5)
    
    # Get debug setting from environment
    debug = '--debug' in os.sys.argv or os.environ.get('FLASK_DEBUG') == '1'
    
    # Start the Flask app
    app.run(host='0.0.0.0', port=5000, debug=debug)