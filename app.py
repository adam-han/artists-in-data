from flask import Flask, render_template, request
import pandas as pd
import plotly.express as px

# load dataset
df = pd.read_csv('./data/dataset.csv')

app = Flask(__name__)


# generates the graphs and statistics
def visualize_data(artist_name):
    # extract the data specfic to the given artist
    artist_data = df.loc[df['Artist'] == artist_name]

    # creates a bar graph of the artist's top songs by streams
    bar_chart = px.bar(artist_data, x='Track', y='Stream')

    # Return the charts as HTML
    return bar_chart.to_html(full_html=False)



# route for home page
@app.route('/')
def home():
    return render_template('home.html')


# route for artist results page
@app.route('/results', methods=['POST'])
def results():
    # gets the user input from the form
    artist_name = request.form['artist_name']

    # gets the data visualizations
    bar_chart = visualize_data(artist_name)

    return render_template('results.html', artist_name=artist_name, bar_chart=bar_chart)



if __name__ == '__main__':
    app.run(debug=True)