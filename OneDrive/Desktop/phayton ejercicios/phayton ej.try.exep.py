def estadisticas(datos):
    try:
        if not isinstance(datos, list):
            raise TypeError("Se esperaba una lista.")
        if len(datos) == 0:
            raise ValueError("La lista no puede estar vacía.")

        numeros = [float(x) for x in datos]

        total    = sum(numeros)
        promedio = total / len(numeros)
        maximo   = max(numeros)
        minimo   = min(numeros)
        rango    = maximo - minimo

        print(f"Total:    {total}")
        print(f"Promedio: {promedio:.2f}")
        print(f"Máximo:   {maximo}")
        print(f"Mínimo:   {minimo}")
        print(f"Rango:    {rango}")

    except ValueError as e:
        print(f"Error de valor: {e}")
    except TypeError as e:
        print(f"Error de tipo: {e}")

print("=== Caso válido ===")
estadisticas([4, 7, 2, 9, 1, 5])

print("\n=== Lista con texto ===")
estadisticas([4, 7, "hola", 9])

print("\n=== Lista vacía ===")
estadisticas([])