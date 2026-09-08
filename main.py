"""main.py represents the core application and handles the main application window."""
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt6.QtGui import QAction
from network import *


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

        create_network_action = QAction("New network...", self)
        create_network_action.setShortcut("Ctrl+N")
        create_network_action.triggered.connect(self.new_network)

        open_network_action = QAction("Open network database...", self)
        open_network_action.setShortcut("Ctrl+O")

        # Add the actions to the "File" menu
        file_menu.addAction(create_network_action)
        file_menu.addAction(open_network_action)


        self.current_network = None # Currently opened network


    def new_network(self) -> None:
        """Creates a new metro network graph based on informations provided by the user."""

        save_location, _ = QFileDialog.getSaveFileName(self, "Select save location for your network", "", "Network database (*.db)")

        if save_location:
            self.current_network = Network(save_location)
            



app = QApplication([])
window = MainAppWindow()

window.show()
app.exec()
