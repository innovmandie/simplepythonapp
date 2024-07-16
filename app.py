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
    data = dataset.head(n=7)
    data = data.to_html()
    #return dataset.html
    info_shape = dataset.shape
    data_columns = dataset.columns
    class_info = dataset.groupby('embarked')['embarked'].value_counts()
    class_info = class_info.to_frame()
    percent_genre = round(dataset.groupby('sex')['sex'].value_counts() / len(dataset)  * 100, 2)
    percent_genre =  percent_genre.astype(str) + ' %' 
    percent_genre = percent_genre.to_frame()
    
    return render_template('index.html', data=data, info_shape=info_shape, data_columns=data_columns, class_info=class_info, percent_genre=percent_genre)
 
if __name__ == "__main__":
    app.run()