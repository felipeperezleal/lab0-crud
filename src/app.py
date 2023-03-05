from flask import Flask, render_template, request, redirect, url_for
import os
import database as db

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
#Conectando la app de Flask con index.html
template_dir = os.path.join(template_dir, 'src', 'templates')

app = Flask(__name__, template_folder=template_dir)

#Rutas
@app.route('/')
def home():
    #Conectando con la base de datos
    #Para cambiar credenciales, dirigirse al archivo ./src/database.py
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM persona")
    myresult = cursor.fetchall()
    # Datos -> Dictionary
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cursor.close()
    return render_template('index.html', data=insertObject)

#-----------------------------------Rutas Persona------------------------------------#
#Ruta para añadir persona
@app.route('/persona', methods=['POST'])
def addPersona():
    #Haciendo request a los datos
    nombre = request.form['nombre']
    telefono = request.form['telefono']
    edad = request.form['edad']
    sexo = request.form['sexo']

    if nombre and telefono and edad and sexo:
        cursor = db.database.cursor()
        sql = "INSERT INTO persona (nombre, telefono, edad, sexo) VALUES (%s, %s, %s, %s)"
        data = (nombre, telefono, edad, sexo)
        cursor.execute(sql, data)
        db.database.commit()
    
    return redirect(url_for('home'))

#Ruta para borrar persona
@app.route('/delete/<string:id>')
def deletePersona(id):
    cursor = db.database.cursor()
    sql = "DELETE FROM persona WHERE id=%s"
    data = (id)
    cursor.execute(sql, data)
    db.database.commit()

    return redirect(url_for('home'))

#Ruta para actualizar persona
@app.route('/update/<string:id>', methods=['POST'])
def updatePersona(id):
    #Haciendo request a los datos
    nombre = request.form['nombre']
    telefono = request.form['telefono']
    edad = request.form['edad']
    sexo = request.form['sexo']

    if nombre and telefono and edad and sexo:
        cursor = db.database.cursor()
        sql = "UPDATE persona SET nombre = %s, telefono = %s, edad = %s, sexo = %s WHERE id = %s"
        data = (nombre, telefono, edad, sexo, id)
        cursor.execute(sql, data)
        db.database.commit()
    
    return redirect(url_for('home'))

#-----------------------------------Rutas Persona------------------------------------#

# Para ejecutar:
# Instalar Flask (en consola: pip install Flask)
# Archivo app.py ubicado en ./src/app.py
# Ejecutar el archivo en la consola con el comando "python app.py"

#Ejecutando la app
if __name__ == '__main__':
    app.run(debug=True)