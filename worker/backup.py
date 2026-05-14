import mysql.connector
import json
import time
from datetime import datetime

while True:

    try:
        conexion = mysql.connector.connect(
            host="nginx",
            port=3306,
            user="usuario_app",
            password="app123",
            database="clima_db"
        )

        cursor = conexion.cursor(dictionary=True)

        cursor.execute("SELECT * FROM ciudades")

        datos = cursor.fetchall()

        nombre_archivo = f"/app/backups/backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

        with open(nombre_archivo, "w") as archivo:
            json.dump(datos, archivo, indent=4, default=str)

        print(f"Backup creado: {nombre_archivo}")

        cursor.close()
        conexion.close()

    except Exception as e:
        print("Error:", e)

    time.sleep(30)