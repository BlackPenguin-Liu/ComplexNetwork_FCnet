
import networkx as nx

class CreateGraph():
    def __init__(self, networkUtil):
        self.networkUtil = networkUtil
        self.edge_files = [0, 107, 348, 414, 686, 698, 1684, 1912, 3437, 3980]  # 文件名列表

    def create_graph(self):
        nodes = nx.path_graph(self.networkUtil.number_nodes)
        self.networkUtil.graph.add_nodes_from(nodes)

        # 把文件中的边整合到元组中，成为空图的边
        for i in range(len(self.edge_files)):
            with open("./entity/ego-facebook-dataset/" + str(self.edge_files[i]) + '.edges') as f:
                for line in f:
                    a, b = line.split()
                    self.add_edge_between_two_nodes(self.edge_files[i], a, b)

    def add_edge_between_two_nodes(self, node, a, b):
        '''
        这三个节点之间连边
        :param node: 文件名 edge_files列表里面的文件名，.edge文件中的所有点都和文件名代表的节点之间有连边
        :param a: 需要连接的一个节点a
        :param b: 需要连接的另一个节点b
        '''
        a, b = int(a), int(b)
        if b not in self.networkUtil.graph.neighbors(a):  # a，b之间连边
            self.networkUtil.graph.add_edge(a, b)
        if a not in self.networkUtil.graph.neighbors(node):  # a与node之间连边
            self.networkUtil.graph.add_edge(a, node)
        if b not in self.networkUtil.graph.neighbors(node):  # b与node之间连边
            self.networkUtil.graph.add_edge(node, b)