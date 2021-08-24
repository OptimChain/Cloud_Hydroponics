try:
    import json
    from flask import Flask, render_template,make_response
    import requests
    from random import *
    import json
    from serverhelper import simulated_read, production_read
    
    print("ALl modules Loaded ")
except Exception as e:
    print("Error : {} ".format(e))

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/pipe', methods=["GET", "POST"])
def pipe():
    payload = {}
    headers = {}
    
    print("Loading Json Stream")
    r = simulated_read()
        
    return {"res":r}


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=3000)
