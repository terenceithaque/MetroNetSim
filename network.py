"""networks.py provides a Network class representing a metro graph."""
import networkx
import sqlite3


class Network(networkx.Graph):
    def __init__(self, file:str):
        """A network graph instance.
        - file: the database file (.db) used by that network."""
        
        # Initialize the parent Graph object
        super().__init__()

        self.file = file
        print("Network file: ", self.file)

        self.connection = sqlite3.Connection(self.file)
        self.cursor = sqlite3.Cursor(self.connection)