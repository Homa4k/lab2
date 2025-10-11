from Data import DatabaseManager
from ListWidget import ListWidget
from PySide6.QtWidgets import QLabel, QListWidgetItem, QApplication
from PySide6.QtCore import Qt
import sys
import os

app = QApplication(sys.argv)

if os.path.exists("tasks.db"):
    os.remove("tasks.db")

# Тест 1 імітуємо додання задачі
db = DatabaseManager()
label = QLabel()
lw = ListWidget(0, db, label)

lw.addItem("Task A")
lw.update_counter()
lw.addItem("Task B")
lw.update_counter()
try:
    assert label.text() == "Кількість задач: 1"
    print("Тест кількості задач пройшов успішно!")
except AssertionError:
    print("Тест кількості задач НЕ пройшов")

# Тест 2 імітуємо редагування тексту
item = QListWidgetItem("Old Task")
item.setData(Qt.UserRole, 1)
lw.addItem(item)

new_text = "Updated Task2"
item.setText(new_text)
db.update_task_description(1, new_text)

try:
    assert lw.item(lw.count() - 1).text() == "Updated Task"
    print("Тест редагування задачі пройшов успішно!")
except AssertionError:
    print("Тест редагування задачі НЕ пройшов")

