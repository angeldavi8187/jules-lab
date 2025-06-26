# app.py
from flask import Flask, render_template, request, redirect, url_for

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Base de datos en memoria para los platos del menú
menu_items = [
    {"nombre": "Pizza Margherita", "precio": 12.50},
    {"nombre": "Pasta Carbonara", "precio": 10.00},
    {"nombre": "Ensalada César", "precio": 8.75}
]

# Ruta principal para mostrar el menú
@app.route('/')
def index():
    """
    Renderiza la página principal (index.html) y muestra todos los platos del menú.
    """
    return render_template('index.html', menu_items=menu_items)

# Ruta para agregar un nuevo plato al menú
@app.route('/agregar', methods=['POST'])
def agregar_plato():
    """
    Agrega un nuevo plato a la lista menu_items basado en los datos del formulario.
    Redirige de vuelta a la página principal.
    """
    if request.method == 'POST':
        nombre_plato = request.form.get('nombre')
        precio_plato_str = request.form.get('precio')

        # Es una buena práctica validar las entradas
        if nombre_plato and precio_plato_str:
            try:
                precio_plato = float(precio_plato_str)
                nuevo_plato = {"nombre": nombre_plato, "precio": precio_plato}
                menu_items.append(nuevo_plato)
            except ValueError:
                # Manejar el caso donde el precio no es un número válido
                # (Podríamos agregar un mensaje flash para el usuario aquí)
                pass 
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
