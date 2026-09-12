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
        self.graph_nodes = []

    def add_station(self, station_name:str) -> None:
        """Adds a new station to the graph. If a station with a similar name already exists in the graph, this will raise an error.
        - station_name: the name of the station to be added."""

        if station_name not in self.graph_nodes:
            self.graph.add_node(station_name)
            self.graph_nodes.append(station_name)

        else:
            raise ValueError(f"Station {station_name} already existing in the network graph.")        


        