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
    import pandas as pd
    import numpy as np
    import zipfile,nltk
    from nltk.corpus import PlaintextCorpusReader 
    import string
    from nltk.tokenize import word_tokenize
    nltk.download('punkt')
    import re
    from nltk.corpus import stopwords
    import heapq as hq
    import sys
    import nltk
    from nltk.stem import WordNetLemmatizer
    from nltk.tokenize import word_tokenize
    from nltk.corpus import stopwords
    import pandas as pd
    import csv
    import os
    import string
    import re
    from bs4 import BeautifulSoup
    from ast import literal_eval
    nltk.download('stopwords')
    from collections import Counter
    import math
    stopwords = set(stopwords.words('english'))
    print("hello")
    return {'1':'delhi','2':'Mumbai','3':'Chennai'}


if __name__=='__main__':
    app.run(debug=True)