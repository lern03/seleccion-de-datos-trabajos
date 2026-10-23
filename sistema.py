import sqlite3
import os

def crear_bd():
    os.makedirs("database", exist_ok=True)
    conexion = sqlite3.connect("database/empleados.db")
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS empleados (
            curp TEXT PRIMARY KEY,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            calle TEXT,
            colonia TEXT,
            telefono TEXT
        )
    """)

    conexion.commit()
    conexion.close()

def alta_empleado():
    conexion = sqlite3.connect("database/empleados.db")
    cursor = conexion.cursor()

    print("\n===== ALTA DE EMPLEADO =====")

    curp = input("CURP: ").strip().upper()
    nombre = input("Nombre: ").strip()
    apellido = input("Apellido: ").strip()
    calle = input("Calle: ").strip()
    colonia = input("Colonia: ").strip()
    telefono = input("Teléfono: ").strip()

    if not curp or not nombre or not apellido:
        print("Error: CURP, nombre y apellido son obligatorios.")
        conexion.close()
        return

    try:
        cursor.execute("""
            INSERT INTO empleados (
                curp,
                nombre,
                apellido,
                calle,
                colonia,
                telefono
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            curp,
            nombre,
            apellido,
            calle,
            colonia,
            telefono
        ))

        conexion.commit()
        print("Empleado registrado correctamente.")

    except sqlite3.IntegrityError:
        print("Error: La CURP ya existe.")

    except sqlite3.Error as error:
        print(f"Error al registrar al empleado: {error}")

    finally:
        conexion.close() 

if __name__ == "__main__":
    crear_bd()
    while True:
        alta_empleado()
        opcion = input("\n¿Desea registrar otro empleado? (s/n): ").strip().lower()
        if opcion != 's':
            break