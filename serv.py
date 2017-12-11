from bottle import route, run, get, request, response, hook
import os
import requests
from bs4 import BeautifulSoup

@get('/search/<term>')

def index(term):
    googlepage = requests.get('https://www.google.co.in/search?q=%22'+ term + '%22+site:shakespeare.mit.edu')
    soup = BeautifulSoup(googlepage.text, 'html.parser')
    number = 0
    for occurence in soup.find_all('b'):
        number += 1
    number = number - 2
    if number == 0:
        return " Don't be an idiot. Why would the dude use the word " + term + "?"
    else:
        return "The term " + term + " has been used by Shakespeare " + str(number) + " time(s) in his life (all works combined). So you can use it in your WT."

@route('/hello')
def hi():
    return 'hi, your results will show up here'

@route('/')
def search():
    return '''
    <html>
        <body>
            <script>
                function myFunction(){
                    document.getElementById("p1").innerHTML = document.getElementById('search').value;
                    document.getElementById("results").src = '/search/' + document.getElementById('search').value;
                }
            </script>
            <div align="center">    
            <img src="data:image/jpeg;base64,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"></img>
            </div>
            <br/><br/>
            <div align="center">
                <input id="search" placeholder="search here for a word Shakespeare'd use" style="width:300px"></input>
                <button onclick="myFunction()"> Search the Web!</button>
            </div>
            <div align="center">
                <p id="p1">
                if you searched for the word 'bard', this is what you'd get:
                </p>
                <iframe id="results" src="/search/bard">
            </div>
        </body>
    </html>
    '''

if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), server='paste')
else:
    run(host='localhost', port=8080, reloader=True)
