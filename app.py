from flask import Flask, render_template, jsonify 


app = Flask(__name__)

JOBS = [
    {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Calgary, Alberta',
    'salary': '$65000'
    },
    {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Winnipeg, Manitoba',

    },
    {
    'id': 3,
    'title': "Frontend Engineer",
    'location': 'Remote',
    'salary': '$75,000'
    },
    {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'Airdrie, Alberta',
    'salary': '$78000'
    }
]

@app.route("/")
def hello():
    return render_template('home.html', jobs=JOBS, company_name='Opare')

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)