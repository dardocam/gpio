import os
import sys
import fcntl
import time

# Ruta del archivo de bloqueo
lock_file_path = 'my_script.lock'

def acquire_lock():
    try:
        # Abrimos el archivo de bloqueo
        lock_file = open(lock_file_path, 'w')
        # Intentamos obtener un bloqueo exclusivo en el archivo
        fcntl.flock(lock_file, fcntl.LOCK_EX | fcntl.LOCK_NB)
        return lock_file
    except IOError:
        # No se pudo obtener el bloqueo; otra instancia del script ya está en ejecución
        return None

def release_lock(lock_file):
    # Liberamos el bloqueo y cerramos el archivo
    fcntl.flock(lock_file, fcntl.LOCK_UN)
    lock_file.close()
    os.remove(lock_file_path)

def main():
    lock_file = acquire_lock()
    if lock_file is None:
        print("Otra instancia del script ya está en ejecución.")
        sys.exit(1)

    try:
                # Aquí va el código principal del script
        while True:
            print("Loop desde python", flush=True)
            time.sleep(1)
    except KeyboardInterrupt:
        # Manejo de interrupción del teclado (Ctrl+C)
        print("Interrumpido por el usuario.")
    finally:
        # Liberamos el archivo de bloqueo antes de salir
        release_lock(lock_file)

if __name__ == "__main__":
    main()
