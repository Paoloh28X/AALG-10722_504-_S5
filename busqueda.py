# Definimos la lista de números que vamos a buscar.
numeros = [6, 5, 2, 8, 9]

# Creamos una función para que el código sea más ordenado.
def buscar_numero():
    """Pide un número al usuario y lo busca en la lista 'numeros'."""
    try:
        # Pedimos el número al usuario. Usamos 'int()' para asegurarnos de que sea un número.
        n = int(input("Ingresa un número para buscar: "))

        # La parte clave: usamos 'in' para verificar si 'n' está dentro de 'numeros'.
        if n in numeros:
            print(f"¡El número {n} ha sido encontrado! 😊")
        else:
            print(f"El número {n} no está en la lista. 😞")
    except ValueError:
        # Esto maneja el error si el usuario no ingresa un número.
        print("¡Error! Por favor, ingresa solo números.")

# Llamamos a la función para ejecutar el código.
buscar_numero()