from flask import Flask, render_template   #from minimal progrAM FROM QUICK Start flask

app = Flask(__name__)   #Flask application

@app.route("/")   #it is basically the path or name after domain name i.e google.com/pics in this pics is the route.
def hello_jovian():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(host= '0.0.0.0', debug=True)