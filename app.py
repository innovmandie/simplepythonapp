from flask import Flask, render_template
import tablib
import os
from flask_bootstrap import Bootstrap4
from flask import Flask

import pandas as pd

app = Flask (__name__)
dataset = pd.read_csv('titanic3.csv')
 
@app.route("/")
def index():
    data = dataset.head(n=10)
    data = data.to_html()
    #return dataset.html
    return render_template('index.html', data=data)
 
if __name__ == "__main__":
    app.run()