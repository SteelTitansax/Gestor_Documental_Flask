from flask import Flask, render_template, request , redirect, url_for ,flash
from flask_mysqldb import MySQL

app = Flask(__name__)

#MYSQL Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'Gestor_Documental'

mysql = MySQL(app)

# Settings
app.secret_key = 'mysecretkey'

#Routes

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
       fullname = request.form['fullname']
       phone = request.form['phone']
       email = request.form['email']
       cur = mysql.connection.cursor()
       cur.execute('INSERT INTO contacts (fullname,phone,email) VALUES(%s,%s,%s)',
       (fullname,phone, email))
       mysql.connection.commit()
       flash('Contact added successfully')
       return redirect(url_for('Index'))

@app.route('/edit/<id>')
def edit_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts WHERE id = %s', (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit-contact.html', contact = data[0])

@app.route('/update/<id>', methods=['POST'])
def update_contact(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE contacts 
            SET fullname = %s,
                email = %s,
                phone = %s
            WHERE id = %s
        """, (fullname,email,phone,id))
        mysql.connection.commit()
        flash('Contact Updated Succesfully')
        return redirect(url_for('Index'))

@app.route('/delete/<string:id>')
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM contacts WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Contact deleted successfully')
    return redirect(url_for('Index'))

#Routes Developer

@app.route('/index_developer')
def Index_Developer():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Desarrollador')
    data = cur.fetchall()
    return render_template('index-developer.html', desarrollador = data)


@app.route('/add_developer', methods=['POST'])
def add_developer():
    if request.method == 'POST':
       name = request.form['Nombre']
       area = request.form['Area']
       range = request.form['Rango']
       idDocument = request.form['idDocumento']
       idSala = request.form['idSala']

       cur = mysql.connection.cursor()
       cur.execute('INSERT INTO Desarrollador (Nombre,Area,Rango,idDocumento,idSala) VALUES(%s,%s,%s,%s,%s)',
       (name,area, range,idDocument,idSala))
       mysql.connection.commit()
       flash('Developer added successfully')
       return redirect(url_for('Index_Developer'))

@app.route('/edit_developer/<id>')
def edit_developer(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Desarrollador WHERE idDesarrollador = %s', (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit-developer.html', developer = data[0])

@app.route('/update_developer/<id>', methods=['POST'])
def update_developer(id):
    if request.method == 'POST':
        name = request.form['Nombre']
        area = request.form['Area']
        range = request.form['Rango']
        idDocument = request.form['idDocumento']
        idSala = request.form['idSala']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE Desarrollador 
            SET Nombre = %s,
                Area = %s,
                Rango = %s,
                idDocumento = %s,
                idSala = %s
            WHERE idDesarrollador = %s
        """, (name,area,range,idDocument,idSala,id))
        mysql.connection.commit()
        flash('Developer Updated Succesfully')
        return redirect(url_for('Index_Developer'))
@app.route('/delete_developer/<string:id>')
def delete_developer(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM Desarrollador WHERE idDesarrollador = {0}'.format(id))
    mysql.connection.commit()
    flash('Developer deleted successfully')
    return redirect(url_for('Index_Developer'))

#Routes Materials

@app.route('/index_material')
def index_material():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Material')
    data = cur.fetchall()
    return render_template('index-material.html', materiales = data)

@app.route('/add_material', methods=['POST'])
def add_material():
    if request.method == 'POST':
        tipo = request.form['Tipo']
        modelo = request.form['Modelo']
        idDesarrollador = request.form['IdDesarrollador']

        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO Material (Tipo,Modelo,IdDesarrollador) VALUES(%s,%s,%s)',
        (tipo,modelo,idDesarrollador))
        mysql.connection.commit()
        flash('Material added successfully')
        return redirect(url_for('index_material'))

@app.route('/edit_material/<id>')
def edit_material(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Material WHERE idMaterial = %s', (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit-material.html', material = data[0])

@app.route('/update_material/<id>', methods=['POST'])
def update_material(id):
    if request.method == 'POST':
        Tipo = request.form['Tipo']
        Modelo = request.form['Modelo']
        IdDesarrollador = request.form['IdDesarrollador']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE Material 
            SET Tipo = %s,
                Modelo = %s,
                IdDesarrollador = %s
            WHERE IdMaterial = %s
        """, (Tipo,Modelo,IdDesarrollador,id))
        mysql.connection.commit()
        flash('Material Updated Succesfully')
        return redirect(url_for('index_material'))

@app.route('/delete_material/<string:id>')
def delete_material(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM Material WHERE idMaterial = {0}'.format(id))
    mysql.connection.commit()
    flash('Material deleted successfully')
    return redirect(url_for('index_material'))

#Routes Documentos

@app.route('/index_documento')
def index_documento():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Documentos')
    data = cur.fetchall()
    return render_template('index-documento.html', documentos = data)

@app.route('/add_documento', methods=['POST'])
def add_documento():
    if request.method == 'POST':
        Nombre = request.form['Nombre']
        Tipo = request.form['Tipo']
        Tag = request.form['Tag']

        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO Documentos (Nombre,Tipo,Tag) VALUES(%s,%s,%s)',
        (Nombre,Tipo,Tag))
        mysql.connection.commit()
        flash('Documento added successfully')
        return redirect(url_for('index_documento'))

@app.route('/edit_documento/<id>')
def edit_documento(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Documentos WHERE idDocumentos = %s', (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit-documento.html', documento = data[0])

@app.route('/update_documento/<id>', methods=['POST'])
def update_documento(id):
    if request.method == 'POST':
        Nombre = request.form['Nombre']
        Tipo = request.form['Tipo']
        Tag = request.form['Tag']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE Documentos 
            SET Nombre = %s,
                Tipo = %s,
                Tag = %s
            WHERE IdDocumentos = %s
        """, (Nombre,Tipo,Tag,id))
        mysql.connection.commit()
        flash('Documento Updated Succesfully')
        return redirect(url_for('index_documento'))

@app.route('/delete_documento/<string:id>')
def delete_documento(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM Documentos WHERE idDocumentos = {0}'.format(id))
    mysql.connection.commit()
    flash('Documento deleted successfully')
    return redirect(url_for('index_documento'))

#Routes Sala

@app.route('/index_sala')
def index_sala():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Sala')
    data = cur.fetchall()
    return render_template('index-sala.html', salas = data)

@app.route('/add_sala', methods=['POST'])
def add_sala():
    if request.method == 'POST':
        Nombre = request.form['Nombre']
        Tamaño = request.form['Tamaño']
        Fecha = request.form['Fecha']

        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO Sala (Nombre,Tamaño,Fecha) VALUES(%s,%s,%s)',
        (Nombre,Tamaño,Fecha))
        mysql.connection.commit()
        flash('Sala added successfully')
        return redirect(url_for('index_sala'))

@app.route('/edit_sala/<id>')
def edit_sala(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Sala WHERE idsala = %s', (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit-sala.html', sala = data[0])

@app.route('/update_sala/<id>', methods=['POST'])
def update_sala(id):
    if request.method == 'POST':
        Nombre = request.form['Nombre']
        Tamaño = request.form['Tamaño']
        Fecha = request.form['Fecha']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE Sala 
            SET Nombre = %s,
                Tamaño = %s,
                Fecha = %s
            WHERE idsala = %s
        """, (Nombre,Tamaño,Fecha,id))
        mysql.connection.commit()
        flash('Sala Updated Succesfully')
        return redirect(url_for('index_sala'))

@app.route('/delete_sala/<string:id>')
def delete_sala(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM Sala WHERE idsala = {0}'.format(id))
    mysql.connection.commit()
    flash('Sala deleted successfully')
    return redirect(url_for('index_sala'))


#Routes ProjectManager

@app.route('/index_projectmanager')
def index_projectmanager():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM ProjectManager')
    data = cur.fetchall()
    return render_template('index-projectmanager.html', projectmanagers = data)

@app.route('/add_projectmanager', methods=['POST'])
def add_projectmanager():
    if request.method == 'POST':
        Tipo = request.form['Tipo']
        Area = request.form['Area']
        Rango = request.form['Rango']
        idDesarrollador = request.form['idDesarrollador']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO ProjectManager (Tipo,Area,Rango,idDesarrollador) VALUES(%s,%s,%s,%s)',
        (Tipo,Area,Rango,idDesarrollador))
        mysql.connection.commit()
        flash('Project Manager added successfully')
        return redirect(url_for('index_projectmanager'))

@app.route('/edit_projectmanager/<id>')
def edit_projectmanager(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM ProjectManager WHERE idProjectManager = %s', (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit-projectmanager.html', projectmanager = data[0])

@app.route('/update_projectmanager/<id>', methods=['POST'])
def update_projectmanager(id):
    if request.method == 'POST':
        Tipo = request.form['Tipo']
        Area = request.form['Area']
        Rango = request.form['Rango']
        idDesarrollador = request.form['idDesarrollador']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE ProjectManager 
            SET Tipo = %s,
                Area = %s,
                Rango = %s,
                idDesarrollador =%s
            WHERE idProjectManager = %s
        """,  (Tipo,Area,Rango,idDesarrollador,id))
        mysql.connection.commit()
        flash('Project Manager Updated Succesfully')
        return redirect(url_for('index_projectmanager'))

@app.route('/delete_projectmanager/<string:id>')
def delete_projectmanager(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM ProjectManager WHERE idProjectManager = {0}'.format(id))
    mysql.connection.commit()
    flash('Project Manager deleted successfully')
    return redirect(url_for('index_projectmanager'))

#Routes Repositorio

@app.route('/index_repositorio')
def index_repositorio():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Repositorios')
    data = cur.fetchall()
    return render_template('index-repositorio.html', repositorios = data)

@app.route('/add_repositorio', methods=['POST'])
def add_repositorio():
    if request.method == 'POST':
        Nombre = request.form['Nombre']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO Repositorios (Nombre) VALUES(%s)',
        [Nombre])
        mysql.connection.commit()
        flash('Repositorio added successfully')
        return redirect(url_for('index_repositorio'))

@app.route('/edit_repositorio/<id>')
def edit_repositorio(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Repositorios WHERE idRepositorios = %s', (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit-repositorio.html', repositorio = data[0])

@app.route('/update_repositorio/<id>', methods=['POST'])
def update_repositorio(id):
    if request.method == 'POST':
        Nombre = request.form['Nombre']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE Repositorios 
            SET Nombre = %s
            WHERE idRepositorios = %s
        """,  (Nombre,id))
        mysql.connection.commit()
        flash('Repositorio Updated Succesfully')
        return redirect(url_for('index_repositorio'))

@app.route('/delete_repositorio/<string:id>')
def delete_repositorio(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM Repositorios WHERE idRepositorios = {0}'.format(id))
    mysql.connection.commit()
    flash('Repositorio deleted successfully')
    return redirect(url_for('index_repositorio'))


#Server Start    
if __name__ == '__main__':
 app.run(port=3000, debug = True)