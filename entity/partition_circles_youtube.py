import logging
from collections import defaultdict

class PartitionCircles():
    def __init__(self, networkUtil):
        self.networkUtil = networkUtil
        self.circles = []
        self.node_in_circles = defaultdict()

    def create_circles(self):
        circle_name = 0
        with open("./entity/youtube_dataset/youtube_community.txt") as f:
            for line in f:  # 对于文件里的每一行
                self.circles.append(line.split())
                circle_name += 1

        self.circles = list(set([tuple(t) for t in self.circles]))  # 去除重复的圈子
        # 因为set的对象不能是列表中的列表，所以要将列表里的列表转化为元组形式
        self.circles = [list(t) for t in self.circles]  # 二维列表化，将里面的元组改为列表
        self.circles = [[int(node) for node in no] for no in self.circles]  # 节点int化
        self.networkUtil.set_number_circles(len(self.circles))  # 14870

    def calculate_average_degree_in_circles(self):
        '''
        圈内平均度
        '''
        average_degree = []
        for i in range(len(self.circles)):
            degree = 0
            for node in self.circles[i]:
                for nei in self.networkUtil.graph.neighbors(node):
                    if nei in self.node_in_circles and i in self.node_in_circles[nei]:
                        degree += 1
            average_degree.append(degree / len(self.circles[i]))

    def calculate_node_inner_degree(self):
        '''
        计算节点圈内度
        '''
        node_inner_degree = defaultdict()
        for i in range(len(self.circles)):
            for node in self.circles[i]:
                sum_degree = 0
                for nei in self.networkUtil.graph.neighbors(node):
                    if nei in self.circles[i]:
                        sum_degree += 1  # 获取圈内度
                if sum_degree != 0:
                    node_inner_degree[i].append([node, sum_degree])  # key为圈i，value为[节点node，圈内度]
                else:
                    node_inner_degree[i].append([node, 0])  # 圈内度为0
        for i in range(len(node_inner_degree)):
            node_inner_degree[i].sort(key=lambda x: x[1])  # 按照圈内度排序

        log_file = "./Data/basic_logger_node_inner_degree.log"
        logging.basicConfig(filename=log_file, level=logging.DEBUG)
        logging.info(node_inner_degree)

    def find_node_in_which_circle(self):
        '''
        节点的圈子列表
        '''
        log_file = "./Data/basic_logger_node_in_circles.log"
        for cir_line in range(len(self.circles)):  # 对于circles里的所有圈子
            for i in range(len(self.circles[cir_line])):  # 对每个圈子里的节点们
                node = int(self.circles[cir_line][i])  # 圈子里的节点
                self.node_in_circles[node].append(cir_line)  # 将圈子划定到一个节点中
        logging.basicConfig(filename=log_file, level=logging.DEBUG)
        logging.info(self.node_in_circles)

    def edges(self):
        '''
        计算圈之间连边数
        '''
        edges_betw_circles = defaultdict(list)
        var_len = len(self.circles)
        for i in range(var_len):
            print("i "+str(i) + "*************" + str(var_len))
            for j in range(i + 1, var_len):
                # 交叠部分的节点列表
                overlapping_nodes = [node for node in self.circles[i] if node in self.circles[j]]
                # 不是交叠部分的节点列表
                normal_nodes = [node for node in self.circles[i] if node not in self.circles[j]]
                normal_nodes += [node for node in self.circles[j] if node not in self.circles[i]]
                edge = 0
                edge_state = []
                # 对于交叠部分节点 edge最后乘2
                for node in overlapping_nodes:
                    for nei in self.networkUtil.graph.neighbors(node):
                        a, b = nei, node
                        if a > b:
                            a, b = b, a
                        if nei in self.circles[i] and [a, b] not in edge_state:
                            edge += 1
                            edge_state.append([a, b])
                        if nei in self.circles[j] and [a, b] not in edge_state:
                            edge += 1
                            edge_state.append([a, b])
                edge = edge * 2

                # 对于非交叠部分的节点 统计连边的数量
                for node in normal_nodes:
                    for nei in self.networkUtil.graph.neighbors(node):
                        a, b = nei, node
                        if a > b:
                            a, b = b, a
                        if (nei in self.circles[i] or nei in self.circles[j]) and [a, b] not in edge_state:
                            edge += 1
                            edge_state.append([a, b])
                edges_betw_circles[i].append([j, edge])
        log_file = "./basic_logger_edge_betw_circles.log"
        logging.basicConfig(filename=log_file, level=logging.DEBUG)
        logging.info(edges_betw_circles)