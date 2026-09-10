"""main.py represents the core application and handles the main application window."""
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt6.QtGui import QAction
from network import *
import popups.new_station as new_station


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

        # Create the "Network" menu
        network_menu = menu_bar.addMenu("Network")

        # Set the actions of the "Network" menu

        add_line_action = QAction("Add a new line...", self)

        add_station_action = QAction("Add a new station...", self)
        add_station_action.triggered.connect(self.create_new_station)

        network_menu.addAction(add_line_action)
        network_menu.addAction(add_station_action)


        self.current_network = None # Currently opened network


    def new_network(self) -> None:
        """Creates a new metro network graph based on informations provided by the user."""

        save_location, _ = QFileDialog.getSaveFileName(self, "Select save location for your network", "", "Network database (*.db)")

        if save_location:
            self.current_network = Network(save_location)


    def create_new_station(self) -> None:
        """Displays a popup allowing the user to create a new station on the network."""
        create_station = new_station.AddNewStationPopup(self)
        create_station.exec()        
            



app = QApplication([])
window = MainAppWindow()

window.show()
app.exec()
