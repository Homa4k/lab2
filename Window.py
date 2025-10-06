from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QPushButton, QListWidgetItem, QLabel, QMessageBox)
from PySide6.QtCore import Qt
from Data import DatabaseManager
from ListWidget import ListWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To-Do List")
        self.db_manager = DatabaseManager()

        main_widget = QWidget()
        main_layout = QVBoxLayout(main_widget)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(10)

        input_layout = QHBoxLayout()
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Add task...")
        add_button = QPushButton("Додати")
        add_button.clicked.connect(self.add_task)
        input_layout.addWidget(self.task_input)
        input_layout.addWidget(add_button)

        main_layout.addLayout(input_layout)

        self.columns_layout = QHBoxLayout()
        self.columns_layout.setSpacing(15)

        self.list_widgets = []
        self.counter_labels = []
        headers = ["To Do", "In Progress", "Done", "Canceled"]

        for i in range(4):
            col_widget = QWidget()
            col_layout = QVBoxLayout(col_widget)
            col_layout.setContentsMargins(5, 5, 5, 5)

            label = QLabel(headers[i])
            label.setAlignment(Qt.AlignCenter)

            counter_label = QLabel("Кількість задач: 0")
            counter_label.setAlignment(Qt.AlignCenter)

            list_widget = ListWidget(i, self.db_manager, counter_label)
            list_widget.setParent(self)

            col_layout.addWidget(label)
            col_layout.addWidget(counter_label)
            col_layout.addWidget(list_widget)

            self.list_widgets.append(list_widget)
            self.counter_labels.append(counter_label)

            self.columns_layout.addWidget(col_widget)

        main_layout.addLayout(self.columns_layout)
        self.setCentralWidget(main_widget)

        self.load_tasks()

    def add_task(self):
        description = self.task_input.text().strip()
        if not description:
            QMessageBox.warning(self, "Помилка", "Опис задачі не може бути порожнім!")
            return
        task_id, created_at = self.db_manager.add_task(description, 0)
        item = QListWidgetItem(description)
        item.setData(Qt.UserRole, task_id)
        item.setToolTip(f"Створено: {created_at}")
        self.list_widgets[0].addItem(item)
        self.task_input.clear()
        self.update_all_counters()

    def load_tasks(self):
        tasks = self.db_manager.fetch_tasks()
        for task_id, description, column, created_at in tasks:
            if 0 <= column < len(self.list_widgets):
                item = QListWidgetItem(description)
                item.setData(Qt.UserRole, task_id)
                item.setToolTip(f"Створено: {created_at}")
                self.list_widgets[column].addItem(item)
        self.update_all_counters()

    def update_all_counters(self):
        for widget in self.list_widgets:
            widget.update_counter()
