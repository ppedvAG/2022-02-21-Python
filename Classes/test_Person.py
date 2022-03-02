from unittest import TestCase
from .Person import MyClass


class TestMyClass(TestCase):
    def test_return_one(self):
        instance = MyClass(1, 2, 3).returnOne()
        self.assertEqual(instance, 1)

    def test_MyClass(self):
        instance = MyClass(1, 2, 3)
        self.assertNotIsInstance(instance, MyClass, "Testfall") # Optionale Nachricht, die angezeigt wird
        # wenn der Test fehlschlägt

