from flask import Flask, Response
import json

app = Flask(__name__)

@app.route("/api", methods=["GET"])
def cancionFavorita():
    nombre = "Josseline Griselda Montecinos Hernández"
    album_favorito = "Flakk Daniel's Lp"

    data = {
        "nombre": nombre,
        "album_favorito": album_favorito
    }

    return Response(
        json.dumps(data, ensure_ascii=False),  
        content_type="application/json; charset=utf-8"
    )

if __name__ == "__main__":
    app.run(debug=True)
