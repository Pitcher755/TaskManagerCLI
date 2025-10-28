# TaskManagerCLI

Un gestor de tareas simple por línea de comandos desarrollado en Python.

## Integración de IA

TaskManagerCLI incluye capacidades de inteligencia artificial a través del módulo `ai_service.py`, exclusivamente para dividir tareas complejas en subtareas manejables.

### Añadir tarea compleja

Si tienes una tarea que requiere varios pasos, puedes usar el comando especial para que la IA la divida automáticamente:

```bash
python main.py add_complex "Preparar presentación para el cliente"
```

La IA analizará la tarea y generará una lista de subtareas, indicando los pasos recomendados para completarla. Cada subtarea se añadirá como una tarea independiente en tu lista.

## Características

- Añadir nuevas tareas
- Marcar tareas como completadas
- Eliminar tareas
- Listar todas las tareas
- Persistencia de datos en archivo JSON

## Requisitos

- Python 3.x
- No se requieren dependencias externas

## Instalación

1. Clona este repositorio:
```bash
git clone https://github.com/Pitcher755/TaskManagerCLI.git
cd TaskManagerCLI
```

## Uso

El programa permite gestionar una lista de tareas mediante comandos simples:

### Añadir una tarea
```bash
python main.py add "Descripción de la tarea"
```

### Listar todas las tareas
```bash
python main.py list
```

### Marcar una tarea como completada
```bash
python main.py complete <id>
```

### Eliminar una tarea
```bash
python main.py delete <id>
```

## Estructura del Proyecto

```
TaskManagerCLI/
├── main.py                # Punto de entrada de la aplicación
├── task_manager.py        # Lógica principal del gestor de tareas
├── ai_service.py          # (Opcional) Servicio de IA
├── tasks.json             # Archivo de almacenamiento de tareas
├── test_task_manager.py   # Tests unitarios
└── README.md              # Documentación
```

## Tests

El proyecto incluye tests unitarios para verificar su funcionamiento. Para ejecutarlos:

```bash
python -m unittest test_task_manager.py
```

## Formato de Datos

Las tareas se almacenan en `tasks.json` con el siguiente formato:

```json
[
	{
		"id": 1,
		"description": "Descripción de la tarea",
		"completed": false
	}
]
```

## Contribuir

1. Haz fork del proyecto
2. Crea una rama para tu característica (`git checkout -b feature/NuevaFeature`)
3. Commit tus cambios (`git commit -m 'Agrega NuevaFeature'`)
4. Push a la rama (`git push origin feature/NuevaFeature`)
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## Autor

**PitcherDev** - [GitHub](https://github.com/Pitcher755)
