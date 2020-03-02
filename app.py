from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

df = pd.read_csv('https://raw.githubusercontent.com/danielcaraway/data/master/only_year.csv', encoding='latin')

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/', methods=['POST', 'GET'])

def index():
    if request.method == 'POST':
        sm_df = df[df['RegionName'] == 90039]
        data = {'date': sm_df.columns.values.tolist()[2:], 'values':sm_df.values.tolist()[0][2:] }
        sm_df_df = pd.DataFrame(data)
        df_j = sm_df_df.to_dict('records')
        # csv = sm_df[[sm_df.columns[1:]]].T.to_json()
        # csv = sm_df.T
        # return sm_df.columns.values
        # return render_template('d3ex.html',zipdata=sm_df)
        return render_template('d3ex.html', zipdata=df_j)
        # return render_template('tables.html', tables=[sm_df.to_html(classes='data')], titles=sm_df.columns.values)
        # return df
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)


