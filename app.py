from flask import Flask, render_template, request
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib
import os

app = Flask(__name__)

@app.route('/')
def home():
    """Render the home page."""
    return render_template('home.html')

@app.route('/music')
def music():
    """Render the music page with data from the CSV file."""
    csv_file_path = os.path.join(os.path.dirname(__file__), 'music.csv')
    music_data = pd.read_csv(csv_file_path)
    music_table = music_data.to_html()
    return render_template('music.html', music_table=music_table)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    """Handle predictions based on user input."""
    if request.method == 'POST':
        age = int(request.form.get('age'))
        gender = request.form.get('gender')
        csv_file_path = os.path.join(os.path.dirname(__file__), 'music.csv')
        music_data = pd.read_csv(csv_file_path)
        filtered_data = music_data[(music_data['Gender'] == gender) & (music_data['Age'] == age)]
        if filtered_data.empty:
            predictions = 'No data found for the given gender and age.'
        else:
            predicted_data = filtered_data.iloc[0].to_dict()
            predicted_data.pop('Occupation', None)
            predictions = predicted_data
        return render_template('predict.html', predictions=predictions)
    return render_template('predict.html')

@app.route('/learn', methods=['GET', 'POST'])
def learn():
    """Handle learning and updating the CSV file with new data."""
    if request.method == 'POST':
        hours = request.form.get('age')  # X
        score = request.form.get('genre')  # y
        new_row = {'Hours': hours, 'Scores': score}
        csv_file_path = os.path.join(os.path.dirname(__file__), 'music.csv')
        music_data = pd.read_csv(csv_file_path)
        music_data = music_data.append(new_row, ignore_index=True)
        music_data.to_csv(csv_file_path, index=False)
        
        X = music_data.drop(columns=['Scores'])
        Y = music_data['Scores']
        model = DecisionTreeClassifier()
        model.fit(X, Y)
        age_input = [[hours]]
        predictions = model.predict(age_input)
        return render_template('predict.html', predictions=predictions)
    return render_template('learn.html')

if __name__ == '__main__':
    app.run(debug=True)
