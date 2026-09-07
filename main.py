"""main.py represents the core application and handles the main application window."""
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QAction


class MainAppWindow(QMainWindow):
    def __init__(self) -> None:
        """An instance of the main application window."""

        # Initialize the parent QMainWindow object
        super().__init__()

        self.setWindowTitle("MetroNetSim")

        # Set the menu bar
        menu_bar = self.menuBar()

        # Create the "File" menu
        file_menu = menu_bar.addMenu("File")

        # Set the actions of the "File" menu
        open_network_action = QAction("Open network database...", self)

        # Add the actions to the "File" menu
        file_menu.addAction(open_network_action)



app = QApplication([])
window = MainAppWindow()

window.show()
app.exec()
