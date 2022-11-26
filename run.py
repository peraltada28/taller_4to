from app import app

#decorador
#endpoint

@app.route("/")
def hello_world():
    return "/app/base.html"

if __name__ == "__master__":
    app.run(debug = True)

