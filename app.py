from flask import Flask, Response
import json

app = Flask(__name__)

@app.route("/api", methods=["GET"])
def cancionFavorita():
    nombre = "Josseline Griselda Montecinos Hernández"
    cancionFavorita = "Good News - Mac Miller"

    data = {
        "nombre": nombre,
        "cancion_favorita": cancionFavorita
    }

    return Response(
        json.dumps(data, ensure_ascii=False),  
        content_type="application/json; charset=utf-8"
    )

if __name__ == "__main__":
    app.run(debug=True)
