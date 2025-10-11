import unittest
from PySide6.QtWidgets import QApplication, QLabel, QListWidgetItem
from PySide6.QtCore import Qt
from Data import DatabaseManager
from ListWidget import ListWidget
import sys

app = QApplication(sys.argv)

class TestListWidget(unittest.TestCase):

    def setUp(self):
        self.db = DatabaseManager()
        self.label = QLabel()
        self.lw = ListWidget(0, self.db, self.label)

    def test_task_counter(self):
        self.lw.addItem("Task A")
        self.lw.addItem("Task B")
        self.lw.update_counter()
        self.assertEqual(self.label.text(), "Кількість задач: 1")

    def test_edit_task(self):
        item = QListWidgetItem("Old Task")
        item.setData(Qt.UserRole, 1)
        self.lw.addItem(item)

        new_text = "Updated Task"
        item.setText(new_text)
        self.db.update_task_description(1, new_text)

        self.assertEqual(self.lw.item(self.lw.count() - 1).text(), "Updated Task2")


if __name__ == "__main__":
    unittest.main()
