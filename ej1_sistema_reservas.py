# Tupla: asientos disponibles (no se pueden modificar)
asientos_disponibles = ("A1", "A2", "A3", "B1", "B2")

reservas = {}  # diccionario: asiento -> pasajero

def reservar(asiento, pasajero):
    try:
        if asiento not in asientos_disponibles:
            raise ValueError(f"El asiento '{asiento}' no existe en este vuelo.")
        if asiento in reservas:
            raise ValueError(f"El asiento '{asiento}' ya está ocupado por {reservas[asiento]}.")

        reservas[asiento] = pasajero
        print(f"Reserva confirmada: {pasajero} -> asiento {asiento}")

    except ValueError as e:
        print(f"No se pudo reservar: {e}")

def cancelar(asiento):
    try:
        pasajero = reservas.pop(asiento)
        print(f"Reserva cancelada: {pasajero} liberó el asiento {asiento}")
    except KeyError:
        print(f"Error: el asiento '{asiento}' no tiene ninguna reserva.")

reservar("A1", "Javier")
reservar("A2", "Ana")
reservar("A1", "Luis")    # ya ocupado
reservar("C9", "Carlos")  # no existe
cancelar("A2")
cancelar("A2")            # ya fue cancelado
