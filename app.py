from flask import Flask, request, jsonify
import mysql.connector
import os

app = Flask(__name__)

# Datos de conexión MySQL en Azure
DB_HOST = "esp-server.mysql.database.azure.com"
DB_NAME = "esp-database"
DB_USER = "qfccvopgga"
DB_PASSWORD = "$tJThXDxihRMiNXg"

@app.route('/movimiento', methods=['POST'])
def movimiento():
    try:
        data = request.get_json()
        estado = data.get("estado")

        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            ssl_disabled=False
        )
        cursor = conn.cursor()
        cursor.execute("INSERT INTO movimientos (estado) VALUES (%s)", (estado,))
        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({"status": "ok", "message": "Dato guardado"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/', methods=['GET'])
def home():
    return "API funcionando", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

