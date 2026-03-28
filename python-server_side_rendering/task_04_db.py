#!/usr/bin/python3
from flask import Flask, render_template_string, request
import json
import csv
import sqlite3

app = Flask(__name__)

html = """<!doctype html>
<html lang="en">
<head>
    <title>Products</title>
</head>
<body>
    {% if error %}
        <p>{{ error }}</p>
    {% else %}
        <table border="1">
            <tr>
                <th>Name</th>
                <th>Category</th>
                <th>Price</th>
            </tr>
            {% for p in products %}
            <tr>
                <td>{{ p.name }}</td>
                <td>{{ p.category }}</td>
                <td>{{ p.price }}</td>
            </tr>
            {% endfor %}
        </table>
    {% endif %}
</body>
</html>
"""


def read_json():
    with open('products.json', 'r') as f:
        return json.load(f)


def read_csv():
    data = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return data


def read_sql():
    conn = sqlite3.connect('products.db')
    cur = conn.cursor()
    cur.execute("SELECT id, name, category, price FROM Products")
    rows = cur.fetchall()
    conn.close()
    return [{"id": r[0], "name": r[1], "category": r[2], "price": r[3]} for r in rows]


@app.route('/products')
def products():
    source = request.args.get('source')
    pid = request.args.get('id')

    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    elif source == 'sql':
        data = read_sql()
    else:
        return render_template_string(html, error="Wrong source")

    if pid:
        try:
            pid = int(pid)
        except Exception:
            return render_template_string(html, error="Product not found")
        data = [p for p in data if p["id"] == pid]
        if not data:
            return render_template_string(html, error="Product not found")

    return render_template_string(html, products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
