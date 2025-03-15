from flask import Flask
from pyneutralino import PyNeutralino
app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello'

if __name__ == "__main__":
    pn=PyNeutralino(app, name="app", port=8000)
    pn.width = 100
    pn.height = 100
    pn.run()
