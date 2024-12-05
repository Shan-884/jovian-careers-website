from flask import Flask, render_template,jsonify   #from minimal progrAM FROM QUICK Start flask

app = Flask(__name__)   #Flask application
JOBS=[ {
        'id':1,
        'title':'Data Analyst',
        'location':'Bengaluru, India',
        'salary':'Rs. 10,00,000'
    } 
    , {
        'id':2,
        'title':'Data Scientist',
        'location':'Delhi, India',
        'salary':'Rs. 15,00,000'
    },
    {
        'id':3,
        'title':'Frontend Engineer',
        'location':'Remote',
    },
    {
        'id':4,
        'title':'Backend Engineer',
        'location':'San Francisco, USA',
        'salary':'$120,000'
    }] #list of dictionaries for jobs dynamic data

@app.route("/")   #it is basically the path or name after domain name i.e google.com/pics in this pics is the route.
def hello_jovian():
    return render_template('home.html',jobs=JOBS,company_name='Jovian')

@app.route("/jobs")  #json api
def list_jobs():
    return jsonify(JOBS)
    

if __name__ == "__main__":
    app.run(host= '0.0.0.0', debug=True)