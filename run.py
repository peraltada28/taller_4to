print("Hola mundo Nro 1")

from app import app

#decorador
#endpoint

@app.route("/")
def hello_world():
    return "<p>Mi primer hello word con flask</p>"

if __name__ == "master":
    app.run(debug = True)

