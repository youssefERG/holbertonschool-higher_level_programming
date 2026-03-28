#!/usr/bin/python3
from flask import Flask, render_template_string
import json

app = Flask(__name__)

items_html = """<!doctype html>
<html lang="en">
<head>
    <title>Items List</title>
</head>
<body>
    <h1>Items</h1>
    {% if items %}
    <ul>
        {% for item in items %}
        <li>{{ item }}</li>
        {% endfor %}
    </ul>
    {% else %}
    <p>No items found</p>
    {% endif %}
</body>
</html>
"""


@app.route('/items')
def items():
    with open('items.json', 'r') as f:
        data = json.load(f)
        items_list = data.get("items", [])
    return render_template_string(items_html, items=items_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
	