from flask import Flask, render_template
import mysql.connector
import asyncio
import aiohttp

app = Flask(__name__)

async def consultar_clima(session, ciudad, lat, lon):

    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

    async with session.get(url) as respuesta:

        datos = await respuesta.json()

        return {
            "ciudad": ciudad,
            "temperatura": datos["current_weather"]["temperature"]
        }

async def obtener_climas():

    async with aiohttp.ClientSession() as session:

        tareas = [
            consultar_clima(session, "Bogotá", 4.71, -74.07),
            consultar_clima(session, "Medellín", 6.25, -75.56),
            consultar_clima(session, "Cali", 3.44, -76.52)
        ]

        resultados = await asyncio.gather(*tareas)

        return resultados

@app.route("/")
def inicio():

    ciudades = []

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

        ciudades = cursor.fetchall()

        cursor.close()
        conexion.close()

    except Exception as e:
        print(e)

    climas = asyncio.run(obtener_climas())

    return render_template(
        "index.html",
        ciudades=ciudades,
        climas=climas
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)