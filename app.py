from flask import Flask, render_template
import tablib
import os
from flask_bootstrap import Bootstrap4
from flask import Flask

import pandas as pd

app = Flask (__name__)
bootstrap = Bootstrap4(app)
dataset = pd.read_csv('titanic3.csv')

 
@app.route("/")
def index():
    data = dataset.head(n=10)
    data = data.to_html()
    #return dataset.html
    info_shape = dataset.shape
    data_columns = dataset.columns
    class_info = dataset.groupby('embarked')['embarked'].value_counts()
    class_info = class_info.to_frame()
    
    return render_template('index.html', data=data, info_shape=info_shape, data_columns=data_columns, class_info=class_info)
 
if __name__ == "__main__":
    app.run()