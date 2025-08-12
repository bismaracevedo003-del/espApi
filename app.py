from flask import Flask, request, jsonify
import pyodbc
import os

app = Flask(__name__)

# Configuración de conexión (ajusta con tus datos de Azure SQL)
DB_SERVER = "tuservidor.database.windows.net"   # Cambia por tu servidor SQL
DB_NAME = "sensoresDB"                          # Cambia por tu base de datos
DB_USER = "adminsql"                            # Usuario SQL
DB_PASSWORD = "TuContraseñaSegura"              # Contraseña SQL

# Cadena de conexión
conn_str = (
    "Driver={ODBC Driver 17 for SQL Server};"
    f"Server={DB_SERVER};"
    f"Database={DB_NAME};"
    f"Uid={DB_USER};"
    f"Pwd={DB_PASSWORD};"
    "Encrypt=yes;"
)

@app.route('/movimiento', methods=['POST'])
def movimiento():
    try:
        data = request.get_json()
        estado = data.get("estado")  # 1 = movimiento, 0 = sin movimiento

        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO movimientos (estado) VALUES (?)", estado)
        conn.commit()
        conn.close()

        return jsonify({"status": "ok", "message": "Dato guardado"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/', methods=['GET'])
def home():
    return "API funcionando", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
