from task_manager import TaskManager

def print_menu():
    print("\n--- Gestor de Tareas Inteligente ---")
    print("1. Añadir tarea")
    print("2. Listar tareas")
    print("3. Completar terea")
    print("4. Eliminar tarea")
    print("5. Salir")

def main():

    manager = TaskManager()

    while True:

        print_menu()

        try:
            
            choice = int(input("Elige una opción: "))

            match choice:
                case 1:
                    description = input("Descripción de la tarea: ")
                    manager.add_task(description)

                case 2:
                    manager.list_tasks()

                case 3:
                    id = int(input("Id de la tarea completada: "))
                    manager.complete_task(id)

                case 4:
                    id = int(input("Id de la tarea a eliminar: "))
                    manager.delete_task(id)
                case 5:
                    print("Saliendo...")
                    break
                case _:
                    print("Opción no válida. Selecciona otra.")
        except ValueError:
            print("Opción no válida. Selecciona otra.")            

if __name__ == "__main__":
    main()

