import sys
from PySide6.QtWidgets import (QApplication)
from Window import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("""
        QWidget {
            background-color: #2b2b2c;
            font-family: 'Segoe UI', Arial, sans-serif;
            font-size: 16px;
            color: #000000
        }
        QMainWindow {
            background-color: #2b2b2c;
        }
        QLineEdit {
            border-radius: 5px;
            padding: 5px;
            background-color: #ffffff;
            color: #000000
        }
        QPushButton {
            background-color: #33bd24;
            color: #2b2b2c;
            border-radius: 5px;
            padding: 5px 15px;
            font-size: 16px;
        }
        QPushButton:hover {
            background-color: #2faa20;
        }
        QListWidget {
            background-color: #ffffff;
            border-radius: 5px;
            padding: 5px;
           background-color: #151672;
        }
        QListWidget::item {
            padding: 5px;
            margin: 2px;
            border: 1px solid #33bd24;
            border-radius: 3px;
            color: #2b2b2c;
        }
        QListWidget::item:selected {
            background-color: #2b2b2c;
            color: #ffffff;
        }
        QLabel {
            font-weight: bold;
            margin-bottom: 5px;
            color: #33bd24;
        }
        """)
window = MainWindow()
window.resize(900, 500)
window.show()
sys.exit(app.exec())
