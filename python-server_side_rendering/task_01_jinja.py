#!/usr/bin/python3
from flask import Flask, render_template_string

app = Flask(__name__)

index_html = """<!doctype html>
<html lang="en">
<head>
    <title>My Flask App</title>
</head>
<body>
    <header>
        <h1>My Flask App</h1>
    </header>
    <h1>Welcome to My Flask App</h1>
    <p>This is a simple Flask application.</p>
    <ul>
        <li>Flask</li>
        <li>HTML</li>
        <li>Templates</li>
    </ul>
    <footer>
        <p>&copy; 2024 My Flask App</p>
    </footer>
</body>
</html>"""

about_html = """<!doctype html>
<html lang="en">
<head>
    <title>About</title>
</head>
<body>
    <header>
        <h1>My Flask App</h1>
    </header>
    <h1>About Us</h1>
    <p>This page contains information about us.</p>
    <footer>
        <p>&copy; 2024 My Flask App</p>
    </footer>
</body>
</html>"""

contact_html = """<!doctype html>
<html lang="en">
<head>
    <title>Contact</title>
</head>
<body>
    <header>
        <h1>My Flask App</h1>
    </header>
    <h1>Contact Us</h1>
    <p>This page contains contact information.</p>
    <footer>
        <p>&copy; 2024 My Flask App</p>
    </footer>
</body>
</html>"""


@app.route('/')
def home():
    return render_template_string(index_html)


@app.route('/about')
def about():
    return render_template_string(about_html)


@app.route('/contact')
def contact():
    return render_template_string(contact_html)


if __name__ == '__main__':
    app.run(debug=True, port=5000)