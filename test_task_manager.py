import unittest
from unittest.mock import patch, mock_open
import json
from task_manager import TaskManager

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.filename = "tasks.json"
        TaskManager.FILENAME = self.filename

    @patch("builtins.open", new_callable=mock_open, read_data="[]")
    @patch("builtins.print")
    def test_list_tasks_no_file(self, mock_print, mock_file):
        # Simula archivo vacío
        mgr = TaskManager()
        mgr.list_tasks()
        mock_print.assert_called_with("No hay tareas pendientes")

    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps([
        {"id": 1, "description": "tarea uno", "completed": False},
        {"id": 2, "description": "tarea dos", "completed": True}
    ]))
    @patch("builtins.print")
    def test_list_tasks_with_tasks(self, mock_print, mock_file):
        mgr = TaskManager()
        mgr.list_tasks()
        calls = [str(call.args[0]) for call in mock_print.call_args_list]
        self.assertIn("[ ] #1: tarea uno", calls)
        self.assertIn("[✓] #2: tarea dos", calls)

    @patch("builtins.open", new_callable=mock_open)
    @patch("builtins.print")
    def test_add_task(self, mock_print, mock_file):
        mgr = TaskManager()
        mgr.add_task("Nueva tarea")
        self.assertEqual(len(mgr._tasks), 1)
        self.assertEqual(mgr._tasks[0].description, "Nueva tarea")
        self.assertFalse(mgr._tasks[0].completed)
        mock_print.assert_called_with("Tarea añadida: Nueva tarea")

    @patch("builtins.open", new_callable=mock_open)
    @patch("builtins.print")
    def test_complete_task(self, mock_print, mock_file):
        from task_manager import Task
        mgr = TaskManager()
        tarea = Task(1, "Completar tarea", False)
        mgr._tasks = [tarea]
        mgr.complete_task(1)
        self.assertTrue(mgr._tasks[0].completed)
        self.assertIn("Tarea completada", mock_print.call_args[0][0])

    @patch("builtins.open", new_callable=mock_open)
    @patch("builtins.print")
    def test_delete_task(self, mock_print, mock_file):
        from task_manager import Task
        mgr = TaskManager()
        tarea = Task(1, "Eliminar tarea", False)
        mgr._tasks = [tarea]
        mgr.delete_task(1)
        self.assertEqual(len(mgr._tasks), 0)
        mock_print.assert_called_with("Tarea eliminada: #1")

if __name__ == "__main__":
    unittest.main()
