"""
@author A.Garcia
@since 2022/05/10
@descript ejercicio flasj
"""
# inclusion de moludos
from flask import Flask
#crear un app con nombre main
app = Flask('__main__')
#te voy a indicar cuando el cliente ejecutando el metodo get has el def
@app.route('/', methods=['GET'])
#el / es el enpoint test y resolver lo que dice return
def go_home():
    return 'HELLO WORLD!'

#si name es igual a main ejecuta l app 
if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
#el true reinicia el sefvicio de forma dinamica este esta pendiente para si hay un cambio reinicia el servidor el puerto es donde              