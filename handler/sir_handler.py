import random
import math
import numpy as np

from handler.spread_handler import spread

from Data.circlesData50 import circles
from Data.circlesData50 import node_in_circles
from Data.circlesData50 import node_inner_degree
from Data.circlesData50 import edges_betw_circles
from Data.circlesData50 import average_degree


class SIR(spread):
    def __init__(self, networkUtil):
        super().__init__(networkUtil)

    def traditional_spread_once(self, infect, recover):
        '''
        一轮传播
        :param infect: 这一轮传播开始前，上一轮的infect set
        :param recover: 同上 set
        :return: 这一轮传播之后的infect recover集合
        '''
        infect_copy = infect.copy()
        for node in infect_copy:
            var_infect_node_list = []
            for nei in self.networkUtil.graph.neighbors(node):
                # 如果nei为易感节点
                if self.nodes_state[nei] == 'S' and nei not in infect:
                    beta = self.networkUtil.infect_rate
                    g = random.random()
                    if g < beta:
                        var_infect_node_list.append(nei)
                        self.nodes_state[nei] = "I"
            infect.update(set(var_infect_node_list))

        var_recover_list = []
        for infect_node in infect_copy:
            g = random.random()
            if g < self.networkUtil.recover_rate and self.nodes_state[
                infect_node] == "I" and infect_node not in recover:
                self.nodes_state[infect_node] = "R"
                var_recover_list.append(infect_node)
        recover.update(var_recover_list)
        infect -= recover
        return infect, recover

    def traditional_spread_sir(self):
        '''
        传统sir传播
        :return:
        '''
        self.init_traditional_graph_states()  # 初始化图状态
        infect = self.beginning_traditional_infected_with_init_rate()  # 初始率感染
        recover = set()
        flag = 0
        while flag <= self.networkUtil.generate_time:
            infect, recover = self.traditional_spread_once(infect, recover)
            self.traditional_infect_num.append(len(infect))
            self.traditional_recover_num.append(len(recover))
            self.traditional_suspect_num.append(self.networkUtil.graph.number_of_nodes() - len(infect) - len(recover))
            flag += 1
        # self.traditional_infect_num 为传播感染变化的数据

    def spread_csir_once(self, infect, recover):
        infect_copy = infect.copy()

        for node in infect_copy:
            # 计算感染节点的综合圈内影响力
            tau = self.calculate_synthesized_effect(node)
            var_infect_node_list = []
            for nei in self.networkUtil.graph.neighbors(node):
                # 如果nei为易感节点
                if self.nodes_state[nei] == 'S' and nei not in infect:
                    # 计算易感节点感兴趣度
                    P, radis = self.calculate_interests(nei)
                    # 计算感染节点影响力度
                    delta = self.calculate_imminent_connection_between_circles(node, nei)
                    impact_of_nodes = delta * tau
                    beta = self.sigmoid(self.networkUtil.infect_rate + impact_of_nodes * P)

                    if beta < 0:
                        beta = 0
                    g = random.random()
                    if g < beta:
                        var_infect_node_list.append(nei)
                        self.nodes_state[nei] = "I"

            infect.update(set(var_infect_node_list))

        var_recover_list = []
        for infect_node in infect_copy:
            gamma = self.calculate_recovery_peer_association(infect_node)
            g = random.random()
            if g < gamma and self.nodes_state[infect_node] == "I" and infect_node not in recover:
                self.nodes_state[infect_node] = "R"
                var_recover_list.append(infect_node)

        recover.update(var_recover_list)
        infect -= recover

        return infect, recover

    def spread_csir(self):
        '''
        基于FCnet的SIR传播
        '''
        self.init_graph_states()  # 初始化图状态
        infect = self.beginning_infected_with_init_rate()  # 初始率感染
        recover = set()
        flag = 0
        while flag <= self.networkUtil.generate_time:
            infect, recover = self.spread_csir_once(infect, recover)
            self.infect_num.append(len(infect))
            self.recover_num.append(len(recover))
            self.suspect_num.append(self.networkUtil.graph.number_of_nodes() - len(infect) - len(recover))
            flag += 1
        # self.infect_num 是感染数量变化的数据

    def calculate_synthesized_effect(self, node):
        '''
        计算node节点同圈综合影响力
        :param node: 节点node
        :return: tau 同圈综合影响力
        '''
        tau = 0
        if node in node_in_circles:
            # 获取节点node所在圈列表
            for cir in node_in_circles[node]:
                degree = 0
                max_degree = 0
                for node_degree in node_inner_degree[cir]:
                    if node in node_degree:
                        degree = node_degree[1]  # 获取node节点的圈内度
                        max_degree = node_inner_degree[cir][-1][1]
                        break
                if max_degree == 0:
                    tau += 0
                else:
                    tau += degree / max_degree

        else:  # 节点node为孤立点
            if self.networkUtil.graph.degree(node) == 0:
                tau = 0
            else:
                tau = 1 / (self.networkUtil.graph.degree(node))
        return tau

    def calculate_imminent_connection_between_circles(self, node, nei):
        '''
        计算两圈的紧密程度
        :param node: 感染节点
        :param nei:  感染节点的邻居节点
        :return:
        '''
        delta = 0
        same_circle = []
        if node not in node_in_circles and nei in node_in_circles:  # 感染节点为孤立节点
            var_list = []
            E = 0
            for nei_cir in node_in_circles[nei]:
                var_list.extend(circles[nei_cir])
            for var_nei in self.networkUtil.graph.neighbors(node):
                if var_nei in var_list:
                    E += 1
            delta = 2 / math.pi * math.atan(E)
        elif node in node_in_circles and nei not in node_in_circles:  # 易感节点为孤立节点
            var_list = []
            E = 0
            for node_cir in node_in_circles[node]:
                var_list.extend(circles[node_cir])
            for var_nei in self.networkUtil.graph.neighbors(node):
                if var_nei in var_list:
                    E += 1
            delta = 2 / math.pi * math.atan(E)
        elif node not in node_in_circles and nei not in node_in_circles:  # 易感节点 感染节点 为孤立节点
            delta = 2 / math.pi * math.atan(1)
        else:
            node_cir_list = node_in_circles[node].copy()
            nei_cir_list = node_in_circles[nei].copy()
            # 求有没有同圈
            for var_cir in node_cir_list:
                if var_cir in nei_cir_list:
                    same_circle.append(var_cir)
                    node_cir_list.remove(var_cir)
                    nei_cir_list.remove(var_cir)
                    break  # 只要有同圈 就按1算
            # 计算圈联系紧密程度
            if len(same_circle) != 0:  # 有同圈
                delta = 1
            else:  # 皆为异圈
                # 求圈的连边数
                E = self.get_E(node_cir_list, nei_cir_list)
                delta = 2 / math.pi * math.atan(E)
        return delta

    def get_E(self, node_cir_list, nei_cir_list):
        '''
        从记录中获取连边数E
        :param node_cir_list:   好友圈列表
        :param nei_cir_list:    好友圈列表
        :return: 连边数E
        '''
        E = 0
        for noc in node_cir_list:
            for nec in nei_cir_list:
                a, b = noc, nec
                if a > b:
                    a, b = b, a
                for e in edges_betw_circles[a]:
                    if b in e:
                        E += e[1]
        return E

    def calculate_interests(self, nei):
        '''
        计算易感节点感兴趣度
        :param nei: nei为易感节点
        :return: 返回nei节点的感兴趣度，nei节点感兴趣度矩阵的谱半径
        '''
        P = 0
        radis = 0
        if nei not in node_in_circles:  # 易感节点为孤立节点
            var_up = 0
            for nei_nei in self.networkUtil.graph.neighbors(nei):
                if self.nodes_state[nei_nei] == 'I':
                    var_up += 1
            P = math.log(var_up / self.networkUtil.graph.degree(nei) + 1, 10)
        else:
            # 获取nei的圈列表
            nei_cir = node_in_circles[nei]
            avde_list = []  # 易感节点好友圈的圈内平均度
            peer_association = []  # 易感节点的好友关联
            for nc in nei_cir:
                avde_list.append(average_degree[nc])  # 圈内平均度
                nei_infect = 0
                nei_recover = 0
                degree_nei = 0
                for n in node_inner_degree[nc]:
                    if nei in n:
                        degree_nei = n[1]
                        break
                if degree_nei != 0:
                    var_temp = dict()
                    for nei_cir_node in circles[nc]:
                        var_temp[nei_cir_node] = 0
                    for neinei in self.networkUtil.graph.neighbors(nei):
                        if neinei in circles[nc] and self.nodes_state[neinei] == 'I' and var_temp[neinei] == 0:
                            nei_infect += 1
                            var_temp[neinei] = 1
                        elif neinei in circles[nc] and self.nodes_state[neinei] == 'R' and var_temp[neinei] == 0:
                            nei_recover += 1
                            var_temp[neinei] = 1
                    a = (nei_infect - nei_recover) / degree_nei
                else:
                    a = 0
                peer_association.append(a)  # 节点圈内好友关联
            np_avde_list = np.array(avde_list)
            np_peer_association = np.array(peer_association)

            np_peer_association = np_peer_association.reshape((len(np_peer_association), 1))
            np_avde_list = np_avde_list.reshape((1, len(np_avde_list)))
            matrix_P = np.dot(np_peer_association, np_avde_list)

            var_lambda = np.linalg.eig(matrix_P)[0]
            var_lambda = [abs(tzz) for tzz in var_lambda]
            radis = max(var_lambda)  # 谱半径

            first = 0
            for r in range(len(node_in_circles[nei])):
                first += matrix_P[r][r]  # 对角线元素之和
            second = 0
            for r in range(len(node_in_circles[nei])):
                for c in range(len(node_in_circles[nei])):
                    if r != c:
                        second += matrix_P[r][c]  # 非对角线元素和
            second /= 10  # 权值
            P = first + second
        return P, radis

    def calculate_recovery_peer_association(self, infect_node):
        '''
        计算恢复率
        :param infect_node: 感染节点
        :return: 返回动态恢复率
        '''
        kappa_r = 0
        if infect_node not in node_in_circles:  # 节点为孤立节点
            var_num = 0
            for nei_here in self.networkUtil.graph.neighbors(infect_node):
                if self.nodes_state[nei_here] == 'R':
                    var_num += 1
            if self.networkUtil.graph.degree(infect_node) == 0:
                kappa_r = 0
            else:
                kappa_r = var_num / self.networkUtil.graph.degree(infect_node)
            gamma = math.log(0.08 * (kappa_r + self.networkUtil.recover_rate) + 1)
        else:
            degree_re = 0
            for infect_cir in node_in_circles[infect_node]:
                recovery_num = 0
                for neinei in self.networkUtil.graph.neighbors(infect_node):
                    if neinei in circles[infect_cir] and self.nodes_state[neinei] == "R":
                        recovery_num += 1

                for no_list in node_inner_degree[infect_cir]:
                    if infect_node in no_list:
                        degree_re = no_list[1]
                        break
                if degree_re == 0:
                    kappa_r += 0
                else:
                    kappa_r = +recovery_num / degree_re
            gamma = math.log(0.2 * (kappa_r + self.networkUtil.recover_rate) + 1)
        return gamma

    def sigmoid(self, x):
        s = 1.5 / (1 + np.exp(-x)) - 0.5
        return s
