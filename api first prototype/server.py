from flask import Flask, request, render_template
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonify





db_connect = create_engine('sqlite:///ArrayDB.db')
app = Flask(__name__)
api = Api(app)

#server home
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/arrays')
def home():
    return render_template('array.html')

class Arrays(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from arrays") # This line performs query and returns json result
        rs = []
        for i in query.cursor.fetchall():
            temp = i[1].split(',')
            temp = list(map(lambda x: int(x), temp))
            rs.append(temp)
        return rs # Fetches first column that is Employee ID


class Array(Resource):
    def get(self, array_id):
        conn = db_connect.connect()
        query = conn.execute("select * from arrays where id = %d "  %int(array_id))
        for i in query.cursor:
            result = i[1]
        return result

class Doubles(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from arrays") # This line performs query and returns json result
        rs = []
        for i in query.cursor.fetchall():
            temp = i[1].split(',')
            temp = list(map(lambda x: int(x)*2, temp))
            rs.append(temp)
        return {'Array': rs} # Fetches first column that is Employee ID

class Double(Resource):
    def get(self, array_id):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from arrays where id = %d" %int(array_id)) # This line performs query and returns json result
        rs = []
        for i in query.cursor.fetchall():
            temp = i[1].split(',')
            temp = list(map(lambda x: int(x)*2, temp))
            rs.append(temp)
        return {'Array': rs} # Fetches first column that is Employee ID

api.add_resource(Arrays, '/arrays') # Route_1
api.add_resource(Doubles, '/double') # Route_2
api.add_resource(Array, '/arrays/<array_id>') # Route_3
api.add_resource(Double, '/double/<array_id>') # Route_4



if __name__ == '__main__':
     app.run(port='5004')
