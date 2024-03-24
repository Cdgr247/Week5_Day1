from flask import Flask, request

app = Flask(__name__)

cars = {
    1:{
        'id' : 1,
        'modal' : 'Honda',
        'make' : 'Accord'
    },
    2 : {
        'id' : 2,
        'model' : 'Hyndai',
        'make' : 'Elantra'
    }
}
sale_receipts = {
    1 : {
        'car' : 2,
        'Condition' : 'New',
        'Color' : 'Sonic gray pearl'
    },
    2 : {
        'car' : 1,
        'Condition' : 'New',
        'Color' : 'Blue'
    }
}
@app.route('/')
def land():
    return {
        "Welcome to THE HONDA DEALERSHIP!!!!" : "Find anything you like!"
    }
@app.route('/cars')
def get_cars():
    return {
        'cars' : list(cars.values())
    }
@app.route('/car/<int:id>')
def get_ind_car(id):
    if id in cars:
        return {
            'car' : cars[id]
        }
    return {
        ' OH NO, something went wrong' : "invalid car id"
    }

@app.route('/car', methods=["POST"])
def create_car():
    data = request.get_json()
    print(data)
    cars[data['id']] = data
    return {
        'car created successfully': cars[data['id']]
    }

@app.route('/car', methods=["PUT"])
def update_car():
    data = request.get_json()
    if data['id'] in cars:
        cars[data['id']] = data
        return {
            'car updated' : cars[data['id']]
        }
    return {
        'err' : 'no car found with that id'
    }
    
@app.route('/car', methods=["DELETE"])
def del_car():
    data = request.get_json()
    if data['id'] in cars:
        del cars[data['id']]
        return {
            'car gone': f"{data['car']} is no more. . . "
        }
    return {
        'err' : "can't delete that car they aren't there. . . "
    }