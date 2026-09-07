"""networks.py provides a Network class representing a metro graph."""
import networkx



class Network(networkx.Graph):
    def __init__(self):

        # Initialize the parent Graph object
        super().__init__()

        print("Instantiated new metro network")