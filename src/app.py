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
    # cursor = db.database().cursor()
    # cursor.execute("SELECT * FROM Persona")
    # myresult = cursor.fetchall()
    #Datos -> Dictionary
    insertObject = []
    # columnNames = [column[0] for column in cursor.description]
    # for record in myresult:
    #     insertObject.append(dict(zip(columnNames, record)))
    # cursor.close()
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
        sql = "INSERT INTO PERSONA (nombre, telefono, edad, sexo) VALUES (%s, %s, %s, %s)"
        data = (nombre, telefono, edad, sexo)
        cursor.execute(sql, data)
        db.database.commit()
    
    return redirect(url_for('home'))

@app.route('/delete/<string:id>')
def delete(id):
    cursor = db.database.cursor()
    sql = "DELETE FROM PERSONA WHERE id=%s"
    data = (id)
    cursor.execute(sql, data)
    db.database.commit()

    return redirect(url_for('home'))

@app.route('/edit/<string:id>', methods=['POST'])
def edit(id):
    #Haciendo request a los datos
    nombre = request.form['nombre']
    telefono = request.form['telefono']
    edad = request.form['edad']
    sexo = request.form['sexo']

    if nombre and telefono and edad and sexo:
        cursor = db.database.cursor()
        sql = "UPDATE PERSONA SET nombre = %s, telefono = %s, edad = %s, sexo = %s WHERE id = %s"
        data = (nombre, telefono, edad, sexo, id)
        cursor.execute(sql, data)
        db.database.commit()
    
    return redirect(url_for('home'))

#-----------------------------------Rutas Persona------------------------------------#

#Ejecutando la app
if __name__ == '__main__':
    app.run(debug=True)