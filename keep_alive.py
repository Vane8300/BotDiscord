from flask import Flask 
# web server using flask
from threading import Thread
# separate thread

app = Flask('')

@app.route('/')
def home():
  return "Hello, I'm alive"

def run():
  app.run(host='0.0.0.0', port=8080)

def keep_alive(): 
  t = Thread(target=run)
  t.start()