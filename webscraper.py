from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

page = requests.get('https://gamek.vn/')
soup = BeautifulSoup(page.content, 'html.parser')

title = soup.head.title.text
version = 'v1.0'
status = 'developing'
shortcut = 'none'

users = [
   {'name': "Tom", 'age': 10},
   {'name': "Mark", 'age': 5},
   {'name': "Pam", 'age': 7}
]

app = Flask(__name__)
@app.route('/')
def index():
   return render_template('index.html', **globals())
app.run(debug=True)

