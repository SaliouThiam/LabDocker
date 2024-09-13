import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('/data/database.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS DIC2_GIT (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/api/items', methods=['POST'])
def add_item():
    try:
        data = request.get_json()
        nom = data.get('nom')
        conn = get_db_connection()
        conn.execute('INSERT INTO DIC2_GIT (nom) VALUES (?)', (nom,))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Item added!'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/items', methods=['GET'])
def get_items():
    conn = get_db_connection()
    items = conn.execute('SELECT * FROM DIC2_GIT').fetchall()
    conn.close()
    return jsonify([dict(item) for item in items])

if __name__ == '__main__':
    init_db()  # Appel de la fonction d'initialisation
    app.run(host='0.0.0.0')