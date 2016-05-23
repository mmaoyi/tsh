from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def hello(name="none"):
    return render_template('test.html',name=name)

if __name__ == "__main__":
    app.run()
