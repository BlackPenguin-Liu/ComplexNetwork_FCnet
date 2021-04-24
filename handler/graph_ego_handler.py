'''
生成网络
'''
import networkx as nx
from entity.create_graph_ego import CreateGraph


def generate_network(networkUtil):
    graph = nx.Graph()
    networkUtil.set_graph(graph)
    networkUtil.set_number_nodes(4039)
    createGraph = CreateGraph(networkUtil)
    createGraph.create_graph()