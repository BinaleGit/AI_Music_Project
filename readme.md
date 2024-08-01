# AI Music Project

This project demonstrates how to use Flask to create a web application that reads and displays music-related data from a CSV file, predicts outcomes, and learns from new data.

## Project Structure

```plaintext
 AI_MUSIC/
│   ├── static/
│   │   └── style.css
│   ├── templates/
│   │   ├── home.html
│   │   ├── layout.html
│   │   ├── learn.html
│   │   ├── music.html
│   │   └── predict.html
│   ├── app.py
│   ├── music.csv
│   ├── requirements.txt
│   └── README.md
├── photos/
│   ├── hero.png
│   ├── mario_standing.png
│   └── star.png
```

## Setup Instructions

1. Clone the Repository

```plaintext
git clone https://github.com/BinaleGit/AI_Music_Project.git
cd AI_MUSIC
```

2. Create and Activate a Virtual Environment

```plaintext
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the Required Packages

```plaintext
pip install -r requirements.txt
```

4. Run the Application

```plaintext
python app.py
```

5. View the Application
   Open your web browser and go to http://127.0.0.1:5000/ to see the application in action.

## Project Details

- app.py: The main application file that initializes the Flask app and handles routes for displaying music data, predicting outcomes and learning from new data.
- music.csv: The CSV file containing the music-related data.
- templates/: HTML templates used to render the web pages.
- static/: Static files like CSS

## Author

Roee Bina
GitHub: [BinaleGit
]([https://](https://github.com/BinaleGit/))