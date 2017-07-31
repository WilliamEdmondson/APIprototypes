from flask import Flask, request, render_template
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonify
import dicom

db_connect = create_engine('sqlite:///ArrayDB.db')
app = Flask(__name__)

#server home
@app.route('/')
def home():
    dcm = dicom.read_file('data/sample.dcm')
    rs = dcm.PixelData

    return render_template('index.html', data = rs.encode('UTF=16'))

if __name__ == '__main__':
     app.run(port='5004')
