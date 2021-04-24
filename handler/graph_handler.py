'''
生成网络
'''
from entity.create_graph import CreateGraph


def generate_network(networkUtil):
    createGraph = CreateGraph(networkUtil)
    createGraph.create_graph()