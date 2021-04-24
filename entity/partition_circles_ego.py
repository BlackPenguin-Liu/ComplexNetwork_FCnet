from collections import defaultdict

class PartitionCircles():
    def __init__(self, networkUtil):
        self.networkUtil = networkUtil
        self.circle_file_names = [0, 107, 348, 414, 686, 698, 1684, 1912, 3437, 3980]  # 文件名列表
        self.circles = []
        self.node_in_circles = defaultdict()

        self.create_circles()

    def create_circles(self):
        '''
        从数据集中获取圈子里面的节点情况，生成circles列表
        该列表是指：圈子里面包含的节点，
        每一行代表一个圈子，每一行都是一个列表，列表元素是该圈子包含的节点
        '''
        for i in range(len(self.circle_file_names)):
            with open("./entity/ego-facebook-dataset/" + str(self.circle_file_names[i]) + '.circles') as f:
                for line in f:  # 对于文件里的每一行
                    line += ' ' + str(self.circle_file_names[i])  # 文件名也在这些圈子里面
                    # 文件名所指的节点是这些节点的中心节点
                    self.circles.append(line.split()[1:])  # circles是一个二维列表，当前圈子加入

        self.circles = list(set([tuple(t) for t in self.circles]))  # 去除重复的圈子
        # 因为set的对象不能是列表中的列表，所以要将列表里的列表转化为元组形式
        self.circles = [list(t) for t in self.circles]  # 二维列表化，将里面的元组改为列表
        self.circles = [[int(node) for node in no] for no in self.circles]  # 节点int化
        self.networkUtil.set_number_circles(len(self.circles)) # 192

    def calculate_average_degree_in_circles(self):
        '''
        计算圈内平均度
        '''
        average_degree = []
        for i in range(self.networkUtil.number_circles):
            degree = 0
            for node in self.circles[i]:
                for nei in self.networkUtil.graph.neighbors(node):
                    if i in self.node_in_circles[nei]:
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
            node_inner_degree[i].sort(key=lambda x: x[1])  # 按照圈内度排序。这个排序方法很有用



    def find_node_in_which_circles(self):
        '''
        节点的圈子列表
        '''
        for cir_line in range(len(self.circles)):  # 对于circles里的所有圈子
            for i in range(len(self.circles[cir_line])):  # 对每个圈子里的节点们
                node = int(self.circles[cir_line][i])  # 圈子里的节点
                self.node_in_circles[node].append(cir_line)  # 将圈子划定到一个节点中

    def calculate_interconnected_edges(self):
        '''
        计算圈之间连边数
        '''
        edges_betw_circles = defaultdict()
        for i in range(len(self.circles)):
            for j in range(i + 1, len(self.circles)):
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