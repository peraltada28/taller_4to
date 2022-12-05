from app import app

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p> <a class='nav-link' href='/clientes'>Clientes</a>"

if __name__ == "__main__":
    app.run(debug = True)

