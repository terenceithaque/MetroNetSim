"""networks.py provides a Network class representing a metro graph."""
import networkx as nx
import sqlite3


class Network:
    def __init__(self, file:str):
        """A network graph instance.
        - file: the database file (.db) used by that network."""
        

        self.file = file
        print("Network file: ", self.file)

        self.connection = sqlite3.connect(self.file)
        self.cursor = sqlite3.Cursor(self.connection)

        # Create the internal graph
        self.graph = nx.Graph()