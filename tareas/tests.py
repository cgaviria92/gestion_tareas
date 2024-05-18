from django.test import TestCase
from .models import Tarea

class TareaModelTest(TestCase):
    
    def setUp(self):
        self.tarea1 = Tarea.objects.create(titulo="Tarea 1", descripcion="Descripción de la tarea 1", estado="pendiente")
        self.tarea2 = Tarea.objects.create(titulo="Tarea 2", descripcion="Descripción de la tarea 2", estado="en_progreso")

    def test_tarea_creada(self):
        tarea = Tarea.objects.get(titulo="Tarea 1")
        self.assertEqual(tarea.descripcion, "Descripción de la tarea 1")
        self.assertEqual(tarea.estado, "pendiente")

    def test_actualizar_tarea(self):
        tarea = Tarea.objects.get(titulo="Tarea 1")
        tarea.descripcion = "Descripción actualizada de la tarea 1"
        tarea.estado = "completada"
        tarea.save()
        tarea_actualizada = Tarea.objects.get(titulo="Tarea 1")
        self.assertEqual(tarea_actualizada.descripcion, "Descripción actualizada de la tarea 1")
        self.assertEqual(tarea_actualizada.estado, "completada")

    def test_eliminar_tarea(self):
        tarea = Tarea.objects.get(titulo="Tarea 1")
        tarea.delete()
        with self.assertRaises(Tarea.DoesNotExist):
            Tarea.objects.get(titulo="Tarea 1")

    def test_listar_tareas(self):
        tareas = Tarea.objects.all()
        self.assertEqual(tareas.count(), 2)

    def test_crear_tarea_sin_estado(self):
        tarea = Tarea.objects.create(titulo="Tarea 3", descripcion="Descripción de la tarea 3")
        self.assertEqual(tarea.estado, "pendiente")  # El estado por defecto es "pendiente"
