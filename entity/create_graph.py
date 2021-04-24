'''
创建网络的节点和边
'''

import networkx as nx
import re


class CreateGraph():
    def __init__(self, networkUtil):
        self.networkUtil = networkUtil

    def create_graph(self):
        # 加入节点
        nodes = nx.path_graph(self.networkUtil.number_nodes)
        self.networkUtil.graph.add_nodes_from(nodes)

        # 边文件
        # nx.write_edgelist(self.networkUtil.graph, "./Data/graph_edges_circles" + str(self.networkUtil.number_circles) + ".edgelist", delimiter=',', data=False)
        # 加入边
        with open("./Data/graph_edges_circles" + str(self.networkUtil.number_circles) + ".edgelist") as f:
            res = f.readlines()
        res = [each.strip() for each in res]  # 去掉'\n'换行符
        res = [re.split(',', each) for each in res]  # 去掉 ',' 分隔符
        edge = [(int(each[0]), int(each[1])) for each in res]  # 把数字int化
        self.networkUtil.graph.add_edges_from(edge)



