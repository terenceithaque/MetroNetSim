"""new_station.py provides handles popups allowing the user to create a new station."""
from PyQt6.QtWidgets import QDialog, QWidget, QMainWindow, QLineEdit, QGridLayout, QLabel, QPushButton, QMessageBox


class AddNewStationPopup(QDialog):
    def __init__(self, parent_window:QMainWindow) -> None:
        """A popup allowing the player to create a new station.
        - parent_window: the parent QMainWindow (main window) of the popup."""

        # Initialize the parent QDialog object
        super().__init__()

        self.setWindowTitle("Add a new station")

        self.parent_window = parent_window
        self.parent_layout = QGridLayout()
        self.setLayout(self.parent_layout)
        

        self.station_name_label = QLabel("Station name:")
        self.station_name_edit = QLineEdit()
        self.station_name_edit.setPlaceholderText("Station name...")

        self.lines_label = QLabel("Connecting lines:")
        self.lines_edit = QLineEdit()
        self.lines_edit.setPlaceholderText("ex: 1,2,3,4")

        self.ok_button = QPushButton("Add station")
        self.ok_button.clicked.connect(lambda: self.handle_close(ok=True))

        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(lambda: self.handle_close(ok=False))

        self.parent_layout.addWidget(self.station_name_label, 0, 0)
        self.parent_layout.addWidget(self.station_name_edit, 0, 1)
        self.parent_layout.addWidget(self.lines_label, 1, 0)
        self.parent_layout.addWidget(self.lines_edit, 1, 1)
        self.parent_layout.addWidget(self.ok_button, 2, 0)
        self.parent_layout.addWidget(self.cancel_button, 2, 1)


    def handle_close(self, ok:bool=True) -> None:
        """Handles the closure of the popup depending on which button was clicked."""

        if ok:
            self.accept()

        else:
            self.reject()        
