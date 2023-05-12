from flask import Flask, render_template, request
import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv('./data/dataset.csv')

app = Flask(__name__)





# route for home page
@app.route('/')
def home():
    return render_template('home.html')


# route for artist results page
@app.route('/results', methods=['POST'])
def results():
    # Get the user input from the form
    artist_name = request.form['artist_name']




if __name__ == '__main__':
    app.run(debug=True)