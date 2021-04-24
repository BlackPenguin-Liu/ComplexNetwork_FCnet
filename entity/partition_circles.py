'''
好友圈划分
'''

import random
import csv
import codecs
from collections import defaultdict


class PartitionCircles():
    def __init__(self, networkUtil):
        self.networkUtil = networkUtil
        self.node_state = dict()  # 节点的状态 是否已经加入好友圈中
        self.circles = []
        self.circles_dict = defaultdict()

        self.create_circles()

    def create_one_circle(self):
        generate= random.randint(1,5)# 迭代次数
        queue_list = []  # 临时列队列表 记录当前需要加入好友圈的节点队列
        # 随机挑选的节点列表
        node_pick_list = random.sample(self.networkUtil.graph.nodes, random.randint(1, 30))
        self.node_state.update(dict().fromkeys(self.networkUtil.graph.nodes, 0))

        for node in node_pick_list:
            queue_list.append(node)  # 把每一个节点放入队列
            self.node_state[node] = 1

        circle_list = []  # 临时队列，记录这个好友圈内的节点
        for gene in range(generate):
            for i in range(len(queue_list)):
                node = queue_list.pop(0)
                circle_list.append(node)
                for nei in self.networkUtil.graph.neighbors(node):
                    g = random.random()
                    if g > 0.5 and self.node_state[nei] == 0:  # 具有一定概率 使其成为一个好友圈
                        queue_list.append(nei)
                        self.node_state[nei] = 1
        circle_list = list(set(circle_list))
        return circle_list


    def create_circles(self):
        for i in range(self.networkUtil.number_circles):
            li = self.create_one_circle()  # 生成一个好友圈
            self.circles.append(li)  # 将这个好友圈存入二维列表中

        for i in range(len(self.circles)):  # 将圈子-节点的列表转换为dict字典
            self.circles_dict[i] = self.circles[i]

    def calculate_nodes_degree_in_circles(self):
        '''
        计算节点的圈内度、圈内平均度
        '''
        average_degree = []  # 圈内平均度
        node_inner_degree = defaultdict()  # 节点圈内度

        for circle, nodes_list in self.circles_dict:
            sum_degree = 0
            for node in nodes_list:
                for nei in self.networkUtil.graph.neighbors(node):
                    if nei in nodes_list:
                        sum_degree += 1
                node_inner_degree[circle].append([node, sum_degree])
            average_degree.append(sum_degree / len(nodes_list))

    def find_node_in_which_circles(self):
        node_in_circles = defaultdict()
        for node in range(self.networkUtil.number_nodes):
            for cir in range(len(self.circles)):
                if node in self.circles[cir]:
                    node_in_circles[node].append(cir)  # 节点都在哪些圈子


    def write_list_into_files(self, variable, path):
        '''
        将二维列表写入csv
        :param variable: 要写入的数据
        :param path: 文件路径
        '''
        file_csv = codecs.open(path, 'w+', 'utf-8')
        writer = csv.writer(file_csv, delimiter=' ', quotechar=' ',quoting=csv.QUOTE_MINIMAL)
        for line in variable:
            writer.writerow(line)

    def reader_from_file(self, path):
        '''
        从csv中读取
        :param path:
        :return: 从文件中读取后生成的列表
        '''
        list = []
        with open(path, 'r') as f:
            reader = csv.reader(f)
            for line in reader:
                tl = [int(q) for q in line[0].split(" ")]
                list.append(tl)

        return list

