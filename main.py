"""
@author A.Garcia
@since 2022/05/10
@descript ejercicio flask
"""
# inclusion de moludos
from flask import Flask, request
#crear un app con nombre main
app = Flask('__main__')
"""
CODIGO DE PRUBE ES PURO COCHINERO
"""
device ={
    "code":"112233",
    "descrip": "Temp. Sensor",
    "value": 67
}

#te voy a indicar cuando el cliente ejecutando el metodo get has el def
@app.route('/devices', methods=['GET'])
#el / es el enpoint test y resolver lo que dice return
def go_home():
    return device 
#es para guardar users
@app.route('/user', methods=['POST'])
def save_user():
    user = request.json
    print(user)
    return user
#para guardar device
@app.route('/devices', methods=['POST'])
def save_device():
    device = request.json
    print(device)
    return device 

#si name es igual a main ejecuta l app 
if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
#el true reinicia el sefvicio de forma dinamica este esta pendiente para si hay un cambio reinicia el servidor el puerto es donde              