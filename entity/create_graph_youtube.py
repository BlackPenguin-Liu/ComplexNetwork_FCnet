import networkx as nx

class CreateGraph():
    def __init__(self, networkUtil):
        self.networkUtil = networkUtil

    def create_graph(self):
        nodes = nx.path_graph(self.networkUtil.number_nodes)
        self.networkUtil.add_nodes_from(nodes)

        with open("./entity/youtube_dataset/youtube_edgelist.txt") as f:
            for line in f:
                a, b = line.split()
                self.add_edge_between_two_nodes(a, b)

    def add_edge_between_two_nodes(self, a, b):
        '''
        这三个节点之间连边
        :param a: 需要连接的一个节点a
        :param b: 需要连接的另一个节点b
        '''
        a, b = int(a), int(b)
        if b not in self.networkUtil.graph.neighbors(a):  # a，b之间连边
            self.networkUtil.graph.add_edge(a, b)