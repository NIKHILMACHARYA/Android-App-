from flask import Flask, render_template
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Initialize Flask app
app = Flask(__name__)

# Sample data - similar to what would be used in Android ListView
items = [
    {"title": "Item 1", "description Hello 1": "First item description"},
    {"title": "Item 2", "description Hello 2": "Second item description"},
    {"title": "Item 3", "description Hello 3": "Third item description"},
    {"title": "Item 4", "description Hello 4": "Fourth item description"},
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/list')
def list_view():
    return render_template('list.html', items=items)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)