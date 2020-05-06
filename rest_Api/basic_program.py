from flask import Flask
from flask_restful import Resource,Api

app = Flask(__name__) #creating flask app
api = Api(app) #converting our application to API app

#a sample dict made, usually db is used for resource/data 
emp_info={ 
    'emp_1': {
        'name' : 'xyz',
        'salary':'12000',
    },
    'emp_2':{
        'name':'abc',
        'salary':'40000',
    }
}

class Employee(Resource):
    def get(self):
        return emp_info

api.add_resource(Employee,"/info")

if __name__ == '__main__':
    app.run(debug=True)