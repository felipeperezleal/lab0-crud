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

    #Selecting persona objects
    cursor.execute("SELECT * FROM persona")
    myresult = cursor.fetchall()
    # Datos -> Dictionary
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))

    #Selecting vivienda objects
    cursor.execute("SELECT * FROM vivienda")
    myresult = cursor.fetchall()
    # Datos -> Dictionary
    insertObjectVivienda = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObjectVivienda.append(dict(zip(columnNames, record)))

    #Selecting persona objects
    cursor.execute("SELECT * FROM municipio")
    myresult = cursor.fetchall()
    # Datos -> Dictionary
    insertObjectMunicipio = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObjectMunicipio.append(dict(zip(columnNames, record)))

    cursor.close()
    return render_template('index.html', data=insertObject, dataVivienda=insertObjectVivienda, dataMunicipio=insertObjectMunicipio)

#-----------------------------------Rutas Persona------------------------------------#
#Ruta para añadir persona
@app.route('/persona', methods=['POST'])
def addPersona():
    #Haciendo request a los datos
    id = request.form['id_persona']
    nombre = request.form['nombre']
    telefono = request.form['telefono']
    edad = request.form['edad']
    sexo = request.form['sexo']

    if nombre and telefono and edad and sexo:
        cursor = db.database.cursor()
        sql = "INSERT INTO persona (id_persona, nombre, telefono, edad, sexo) VALUES (%s, %s, %s, %s, %s)"
        data = (id, nombre, telefono, edad, sexo)
        cursor.execute(sql, data)
        db.database.commit()
    
    return redirect(url_for('home'))

#Ruta para borrar persona
@app.route('/deletePersona/<string:id>')
def deletePersona(id):
    cursor = db.database.cursor()
    sql = "DELETE FROM persona WHERE id_persona=%s"
    data = (id,)
    cursor.execute(sql, data)
    db.database.commit()

    return redirect(url_for('home'))

#Ruta para actualizar persona
@app.route('/updatePersona/<string:id>', methods=['POST'])
def updatePersona(id):
    #Haciendo request a los datos
    nombre = request.form['nombre']
    telefono = request.form['telefono']
    edad = request.form['edad']
    sexo = request.form['sexo']
    cdf = request.form['cdf']
    hogar = request.form['hogar']

    if nombre and telefono and edad and sexo:
        cursor = db.database.cursor()
        sql = "UPDATE persona SET nombre = %s, telefono = %s, edad = %s, sexo = %s, cdf = %s, hogar = %s  WHERE id_persona = %s"
        data = (nombre, telefono, edad, sexo, cdf, hogar, id)
        cursor.execute(sql, data)
        db.database.commit()
    
    return redirect(url_for('home'))

#-----------------------------------Rutas Persona------------------------------------#

#-----------------------------------Rutas Vivienda------------------------------------#
#Ruta para añadir vivienda
@app.route('/vivienda', methods=['POST'])
def addVivienda():
    #Haciendo request a los datos
    id = request.form['id_vivienda']
    direccion = request.form['direccion']
    capacidad = request.form['capacidad']
    niveles = request.form['niveles']
    ubicacion = request.form['ubicacion']

    if direccion and capacidad and niveles:
        cursor = db.database.cursor()
        sql = "INSERT INTO vivienda (id_vivienda, direccion, capacidad, niveles, ubicacion) VALUES (%s, %s, %s, %s, %s)"
        data = (id, direccion, capacidad, niveles, ubicacion)
        cursor.execute(sql, data)
        db.database.commit()
    
    return redirect(url_for('home'))

#Ruta para borrar vivienda
@app.route('/deleteVivienda/<string:id>')
def deleteVivienda(id):
    cursor = db.database.cursor()
    sql = "DELETE FROM vivienda WHERE id_vivienda=%s"
    data = (id,)
    cursor.execute(sql, data)
    db.database.commit()

    return redirect(url_for('home'))

#Ruta para actualizar vivienda
@app.route('/updateVivienda/<string:id>', methods=['POST'])
def updateVivienda(id):
    #Haciendo request a los datos
    direccion = request.form['direccion']
    capacidad = request.form['capacidad']
    niveles = request.form['niveles']
    ubicacion = request.form['ubicacion']

    if direccion and capacidad and niveles:
        cursor = db.database.cursor()
        sql = "UPDATE vivienda SET direccion = %s, capacidad = %s, niveles = %s, ubicacion = %s WHERE id_vivienda = %s"
        data = (direccion, capacidad, niveles, ubicacion, id)
        cursor.execute(sql, data)
        db.database.commit()
    
    return redirect(url_for('home'))

#-----------------------------------Rutas Vivienda------------------------------------#

#-----------------------------------Rutas Municipio-----------------------------------#
#Ruta para añadir municipio
@app.route('/municipio', methods=['POST'])
def addMunicipio():
    #Haciendo request a los datos
    id = request.form['id_municipio']
    nombre = request.form['nombre']
    gobernador = request.form['gobernador']

    if nombre and gobernador:
        cursor = db.database.cursor()
        sql = "INSERT INTO municipio (id_municipio, nombre, gobernador) VALUES (%s, %s, %s)"
        dataMunicipio = (id, nombre, gobernador)
        cursor.execute(sql, dataMunicipio)
        db.database.commit()
    
    return redirect(url_for('home'))

#Ruta para borrar municipio
@app.route('/deleteMunicipio/<string:id>')
def deleteMunicipio(id):
    cursor = db.database.cursor()
    sql = "DELETE FROM municipio WHERE id_municipio=%s"
    dataMunicipio = (id,)
    cursor.execute(sql, dataMunicipio)
    db.database.commit()

    return redirect(url_for('home'))

#Ruta para actualizar municipio
@app.route('/updateMunicipio/<string:id>', methods=['POST'])
def updateMunicipio(id):
    #Haciendo request a los datos
    nombre = request.form['nombre']
    area = request.form['area']
    presupuesto = request.form['presupuesto']
    gobernador = request.form['gobernador']

    if nombre and area and presupuesto and gobernador:
        cursor = db.database.cursor()
        sql = "UPDATE municipio SET nombre = %s, area = %s, presupuesto = %s, gobernador = %s WHERE id_municipio = %s"
        data = (nombre, area, presupuesto, gobernador, id)
        cursor.execute(sql, data)
        db.database.commit()
    
    return redirect(url_for('home'))

#-----------------------------------Rutas Municipio-----------------------------------#

# Para ejecutar:
# Instalar Flask (en consola: pip install Flask)------> Flask lo instalé en un virtual environment llamado venv, si quieren usarlo también hagan: python -m venv venv, una vez creado escriban ./venv/Scripts/activate
# Archivo app.py ubicado en ./src/app.py
# Ejecutar el archivo en la consola con el comando "python app.py"


#Ejecutando la app
if __name__ == '__main__':
    app.run(debug=True)