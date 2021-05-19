from flask import Flask
from flask import render_template
from flask import request
import requests
import validators
import cgi
from bs4 import BeautifulSoup as bs
import lxml

'''
Firstly I inspected several websites to see where company names are mostly located and as a result decided to seek them inside the <title> tag.

To perform this task I used BeautifulSoup library, which gave me an opportunity to use "html parser".

I created 2 functions and 2 html files to define the routes of these functions performance. I also gave the files a bit of styling using <style> inside the <head>.
'''

app = Flask(__name__)

@app.route('/')
def company_url():
    return render_template('index.html')

@app.route('/company', methods=['POST', 'GET'])
def company_name():
    s_url = request.form.get('s_url')
    page = requests.get(s_url)
    soup = bs(page.content, 'html.parser')
    title = soup.title.text
    return render_template('company.html', title = title)

if __name__ == '__main__':
    app.run(debug=True)