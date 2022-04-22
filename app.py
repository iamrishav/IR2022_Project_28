from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/process',methods=('POST','GET'))
def process():
    if request.method == 'POST':
        city = request.form['city']
        preferences = request.form['preferences']
        num_days = request.form['num_days']
        recommendations = get_recommendations(city,preferences,num_days)
        return render_template('result.html',recommendations=recommendations)

def get_recommendations(city,preferences,num_days):
    return {'1':'Delhi','2':'Mumbai','3':'Chennai'}


if __name__=='__main__':
    app.run(debug=True)