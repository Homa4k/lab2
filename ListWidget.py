from PySide6.QtWidgets import (QListWidget, QMenu, QMessageBox, QInputDialog)
from PySide6.QtCore import (Qt, QTimer)


class ListWidget(QListWidget):
    def __init__(self, column_index, db_manager, counter_label, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.column_index = column_index
        self.db_manager = db_manager
        self.counter_label = counter_label

        self.setAcceptDrops(True)
        self.setDragEnabled(True)
        self.setDefaultDropAction(Qt.MoveAction)
        self.setDragDropMode(QListWidget.DragDrop)
        self.setMinimumWidth(220)
        self.setSpacing(3)

    def update_counter(self):
        self.counter_label.setText(f"Кількість задач: {self.count()}")

    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat("application/x-qabstractitemmodeldatalist"):
            event.acceptProposedAction()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasFormat("application/x-qabstractitemmodeldatalist"):
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event):
        super().dropEvent(event)
        for index in range(self.count()):
            item = self.item(index)
            task_id = item.data(Qt.UserRole)
            self.db_manager.update_task_column(task_id, self.column_index)
        QTimer.singleShot(0, self.window().update_all_counters)

    def contextMenuEvent(self, event):
        item = self.itemAt(event.pos())
        if item:
            menu = QMenu(self)
            edit_action = menu.addAction("Редагувати")
            delete_action = menu.addAction("Видалити")
            action = menu.exec(event.globalPos())

            if action == delete_action:
                reply = QMessageBox.question(
                    self, "Підтвердіть видалення",
                    "Ви дійсно хочете видалити задачу?",
                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No
                )
                if reply == QMessageBox.Yes:
                    task_id = item.data(Qt.UserRole)
                    self.db_manager.delete_task(task_id)
                    self.takeItem(self.row(item))
                    self.window().update_all_counters()

            elif action == edit_action:
                current_text = item.text()
                new_text, ok = QInputDialog.getText(
                    self, "Редагувати задачу",
                    "Оновіть опис задачі:", text=current_text
                )
                if ok and new_text.strip():
                    item.setText(new_text.strip())
                    task_id = item.data(Qt.UserRole)
                    self.db_manager.update_task_description(task_id, new_text.strip())
                    self.window().update_all_counters()
