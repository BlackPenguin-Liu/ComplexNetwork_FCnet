'''
网络中的参数
'''

import networkx as nx

class NetworkUtil():
    def __init__(self):
        self.number_nodes = 10000
        self.graph = nx.barabasi_albert_graph(self.number_nodes, 2)
        self.number_circles = 50
        self.generate_time = 40

        self.init_rate = 0.04
        self.infect_rate = 0.25
        self.recover_rate = 0.25

    def set_number_nodes(self, number_nodes):
        self.number_nodes = number_nodes

    def set_graph(self, graph):
        self.graph = graph

    def set_number_circles(self, number_circles):
        self.number_circles = number_circles