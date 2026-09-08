"""new_station.py provides handles popups allowing the user to create a new station."""
from PyQt6.QtWidgets import QDialog, QMainWindow, QLineEdit, QGridLayout, QLabel, QMessageBox


class AddNewStationPopup(QDialog):
    def __int__(self, parent_window:QMainWindow) -> None:
        """A popup allowing the player to create a new station.
        - parent_window: the parent QMainWindow (main window) of the popup."""

        # Initialize the parent QDialog object
        super().__init__()


        self.parent_window = parent_window