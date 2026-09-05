# Módulo de gestión de libros e inventario

def registrar_libro(libro, inventario):
    inventario.append(libro)
    return libro


def consultar_libro(titulo, inventario):
    for libro in inventario:
        if libro["titulo"] == titulo:
            return libro
    return None
