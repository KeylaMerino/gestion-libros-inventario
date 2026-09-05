from src.libros import registrar_libro, consultar_libro


def test_registrar_y_consultar_libro():
    inventario = []

    libro = {
        "titulo": "Cien años de soledad",
        "autor": "Gabriel García Márquez",
        "editorial": "Sudamericana",
        "categoria": "Novela",
        "precio": 15.00,
        "cantidad": 10
    }

    registrar_libro(libro, inventario)

    resultado = consultar_libro("Cien años de soledad", inventario)

    assert resultado == libro
