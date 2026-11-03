import os
from flask import Flask, render_template

# This finds the exact folder your app.py is sitting in
base_dir = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(base_dir, 'templates')

app = Flask(__name__, template_folder=templates_dir)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    # Using port 8080 avoids any hidden background blocks
    print("====================================================")
    print(" Server is loading up perfectly...")
    print(" Open your browser and go to: http://127.0.0.1:8080")
    print("====================================================")
    app.run(debug=True, port=8080)
