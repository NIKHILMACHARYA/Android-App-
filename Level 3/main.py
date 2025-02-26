from flask import Flask, render_template, request, jsonify
from app import app, db, Contact #Import from app.py
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Sample data for list view
items = [
    {"title": "Item 1", "description": "First item description"},
    {"title": "Item 2", "description": "Second item description"},
    {"title": "Item 3", "description": "Third item description"},
    {"title": "Item 4", "description": "Fourth item description"},
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/list')
def list_view():
    return render_template('list.html', items=items)

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    try:
        # Create new contact entry
        new_contact = Contact(
            name=request.form.get('name'),
            email=request.form.get('email'),
            message=request.form.get('message')
        )

        # Save to database
        db.session.add(new_contact)
        db.session.commit()

        app.logger.info(f"Form submitted and saved to database - Name: {new_contact.name}, Email: {new_contact.email}")
        return jsonify({"status": "success"})

    except Exception as e:
        app.logger.error(f"Error saving form submission: {str(e)}")
        db.session.rollback()
        return jsonify({"status": "error", "message": "Failed to save form submission"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)