
# Este script de Python define una ruta principal '/' que renderiza el archivo index.html que acabamos de crear utilizando Flask.

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de libros (simulación de una base de datos)
libros = []


@app.route('/')
def index():
    return render_template('index.html', libros=libros)


@app.route('/agregar', methods=['GET', 'POST'])
def agregar_libro():
    if request.method == 'POST':
        titulo = request.form['titulo']
        editorial = request.form['editorial']
        autor = request.form['autor']
        version = request.form['version']
        disponible = request.form['disponible']
        # Agregar más campos si es necesario

        # Crear un diccionario para representar el libro
        libro = {
            'titulo': titulo,
            'editorial': editorial, 
            'autor': autor,
            'version': version,
            'disponible': disponible
            # Agregar más campos si es necesario
        }

        # Agregar el libro a la lista de libros
        libros.append(libro)

        # Redirigir a la página principal después de agregar el libro
        return redirect(url_for('index'))

    # Renderizar la plantilla HTML del formulario para agregar libro
    return render_template('agregar_libro.html')


@app.route('/buscar', methods=['GET', 'POST'])
def buscar_libro():
    if request.method == 'POST':
        titulo = request.form['titulo']

        # Buscar el libro en la lista de libros
        resultados = [
            libro for libro in libros if libro['titulo'].lower() == titulo.lower()]

        # Renderizar la plantilla HTML de resultados de búsqueda
        return render_template('buscar_libro.html', resultados=resultados)

    # Renderizar la plantilla HTML del formulario para buscar libro
    return render_template('buscar_formulario.html')


@app.route('/actualizar', methods=['GET', 'POST'])
def actualizar_libro():
    if request.method == 'POST':
        titulo = request.form['titulo']
        nuevo_autor = request.form['nuevo_autor']
        nueva_editorial = request.form['nueva_editorial']
        nueva_version = request.form['nueva_version']
        disponible = request.form['disponible']

        # Actualizar el autor del libro en la lista de libros
        for libro in libros:
            if libro['titulo'].lower() == titulo.lower():
                libro['autor'] = nuevo_autor
                libro['editorial'] = nueva_editorial
                libro['version'] = nueva_version
                libro['disponible'] = disponible
                break

        # Redirigir a la página principal después de actualizar el libro
        return redirect(url_for('index'))

    # Renderizar la plantilla HTML del formulario para actualizar libro
    return render_template('actualizar_libro.html')


@app.route('/eliminar', methods=['GET', 'POST'])
def eliminar_libro():
    if request.method == 'POST':
        titulo = request.form['titulo']

        # Eliminar el libro de la lista de libros
        for libro in libros:
            if libro['titulo'].lower() == titulo.lower():
                libros.remove(libro)
                break

        # Redirigir a la página principal después de eliminar el libro
        return redirect(url_for('index'))

    # Renderizar la plantilla HTML del formulario para eliminar libro
    return render_template('eliminar_libro.html')


if __name__ == '__main__':
    app.run(debug=True)
