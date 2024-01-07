#начни тут создавать приложение с умными заметками
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QListWidget, QPushButton, QVBoxLayout

app = QApplication([])
window = QWidget()

input_field = QLineEdit()
notes_list = QListWidget()
add_button = QPushButton("Добавить")
delete_button = QPushButton("Удалить")

layout = QVBoxLayout()
layout.addWidget(input_field)
layout.addWidget(notes_list)
layout.addWidget(add_button)
layout.addWidget(delete_button)

window.setLayout(layout)

window.show()
app.exec_()