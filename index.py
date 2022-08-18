
#from crypt import methods
from flask import Flask,render_template,url_for,request,redirect, make_response,jsonify
#import random
import json
from time import time
#from random import random
from flask import Flask, render_template, make_response
app = Flask(__name__)
newData = False

@app.route('/', methods=["GET", "POST"])
def main():
   return render_template('live_chart.html')


#@app.route('/data', methods=["GET", "POST"])
#def data():
#    data = [time() * 1000, random() * 100]
 #   response = make_response(json.dumps(data))
  #  response.content_type = 'application/json'
   # return response

@app.route('/data', methods =["POST" , "GET"])
def data():
    global newData
    if request.method== "post":
        data = request.form
        newData =True
        for k,v in data.items():
            sensor_data [k] =v

    

@app.route('/get_data')
def get_data():
    global newData, sensor_data
    if newData:
        return jsonify({'data':sensor_data})
    else:
        return jsonify({'data': None})

if __name__ == "__main__":
    app.run(debug=True)