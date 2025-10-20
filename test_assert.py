from Data import DatabaseManager
from ListWidget import ListWidget
from PySide6.QtWidgets import QLabel, QListWidgetItem, QApplication
from PySide6.QtCore import Qt
import sys, os, pytest

app = QApplication(sys.argv)
if os.path.exists("tasks.db"):
    os.remove("tasks.db")

@pytest.mark.parametrize("a, b", [('Task A', "Кількість задач: 2")])

def test_addtask(a, b):
    # Тест 1 імітуємо додання задачі
    label = QLabel()
    lw = ListWidget(0, DatabaseManager(), label)
    lw.addItem(a)
    lw.update_counter()
    assert label.text() == b

@pytest.fixture
def list_data():
    return ListWidget(0, DatabaseManager(), QLabel())

def test_edittask(list_data):
    # Тест 2 імітуємо редагування тексту
    lw = list_data
    item = QListWidgetItem("Old Task")
    item.setData(Qt.UserRole, 1)
    lw.addItem(item)
    new_text = "Updated Task"
    item.setText(new_text)
    DatabaseManager().update_task_description(1, new_text)
    assert lw.item(lw.count() - 1).text() == "Updated Task"
