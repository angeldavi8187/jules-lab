from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Base de datos en memoria
menu_items = [
    {'nombre': 'Pizza Margarita', 'precio': 12.50},
    {'nombre': 'Pasta Carbonara', 'precio': 10.00},
    {'nombre': 'Ensalada César', 'precio': 8.75}
]

@app.route('/')
def index():
    return render_template('index.html', menu_items=menu_items)

@app.route('/agregar', methods=['POST'])
def agregar_plato():
    nombre = request.form.get('nombre')
    precio = request.form.get('precio')
    if nombre and precio:
        try:
            precio_float = float(precio)
            menu_items.append({'nombre': nombre, 'precio': precio_float})
        except ValueError:
            # Manejar el caso en que el precio no sea un número válido
            pass  # O podrías enviar un mensaje de error al usuario
    return redirect(url_for('index'))

@app.route('/eliminar/<string:nombre_del_plato>', methods=['POST'])
def eliminar_plato(nombre_del_plato):
    global menu_items
    menu_items = [item for item in menu_items if item['nombre'] != nombre_del_plato]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
