from Data import DatabaseManager
from ListWidget import ListWidget
from PySide6.QtWidgets import QLabel, QListWidgetItem, QApplication
from PySide6.QtCore import Qt
import sys, pytest

app = QApplication(sys.argv)

@pytest.mark.skip(reason="Функція має бути пропущена")
def test_edittask():
    # Тест 1 імітуємо редагування тексту
    label = QLabel()
    lw = ListWidget(0, DatabaseManager(), label)

    item = QListWidgetItem()
    item.setData(Qt.UserRole, 1)
    lw.addItem(item)
    new_text = "Updated Task"
    item.setText(new_text)
    DatabaseManager().update_task_description(1, new_text)
    assert lw.item(lw.count() - 1).text() == "Updated Task"


@pytest.mark.xfail(reason="Відомий дефект у підрахунках через початковий стан бази даних")
def test_addtask():
    # Тест 1 імітуємо додання задачі
    label = QLabel()
    lw = ListWidget(0, DatabaseManager(), label)
    lw.addItem("Task A")
    lw.update_counter()
    assert label.text() == "Кількість задач: 1"




