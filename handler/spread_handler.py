import random




class spread():
    def __init__(self, networkUtil):
        self.networkUtil = networkUtil

        self.suspect_num = list()
        self.infect_num = list()
        self.recover_num = list()
        self.nodes_state = dict()

        self.traditional_suspect_num = list()  # 传统的sir 做对比用
        self.traditional_infect_num = list()
        self.traditional_recover_num = list()

    def init_graph_states(self):
        '''
        初始化图
        '''
        self.nodes_state.update(dict().fromkeys(self.networkUtil.graph.nodes, "S"))  # 所有节点初始化为'S'状态
        self.suspect_num = []
        self.infect_num = []
        self.recover_num = []

        self.suspect_num.append(self.networkUtil.graph.number_of_nodes())
        self.infect_num.append(0)
        self.recover_num.append(0)

    def init_traditional_graph_states(self):
        '''
        初始化图 传统的sir
        '''
        self.nodes_state.update(dict().fromkeys(self.networkUtil.graph.nodes, "S"))
        self.traditional_suspect_num = []
        self.traditional_infect_num = []
        self.traditional_recover_num = []

        self.traditional_suspect_num.append(self.networkUtil.graph.number_of_nodes())
        self.traditional_infect_num.append(0)
        self.traditional_recover_num.append(0)

    def beginning_infected_with_init_rate(self):
        '''
        以初始感染率 感染图中节点
        :return: 初始率感染的感染节点列表
        '''
        infected_node_list = self.change_node_state_by_rate(self.networkUtil.graph.nodes, "I", self.networkUtil.init_rate)  # 初始感染率随机感染节点

        infect_num = len(infected_node_list)
        self.suspect_num.append(self.networkUtil.graph.number_of_nodes() - infect_num)
        self.infect_num.append(infect_num)
        self.recover_num.append(0)

        return infected_node_list

    def beginning_traditional_infected_with_init_rate(self):
        '''
        以初始感染率 感染图中节点 传统的sir
        :return: 初始率感染的感染节点列表
        '''
        infected_node_list = self.change_node_state_by_rate(self.networkUtil.graph.nodes, "I", self.networkUtil.init_rate)  # 初始感染率随机感染节点

        infect_num = len(infected_node_list)
        self.traditional_suspect_num.append(self.networkUtil.graph.number_of_nodes() - infect_num)
        self.traditional_infect_num.append(infect_num)
        self.traditional_recover_num.append(0)

        return infected_node_list

    def change_node_state_by_rate(self, source, to_state, rate):
        '''
        修改source列表中的节点的状态为to_state，变化的率为rate
        更新节点的状态
        :param source: 源 需要改变的列表
        :param to_state: 改成to_state状态
        :param rate: 以rate的概率
        :return: 修改之后的列表
        '''
        nodes_list = random.sample(source, int(len(source) * rate))
        self.nodes_state.update(dict().fromkeys(nodes_list, to_state))
        return set(nodes_list)

    # def calculate_density_in_circle(self, cir):  # 计算该圈子的感染密度
    #     sum_infect = 0
    #     for node in self.circle_nodes[cir]:  # 对于圈子cir中的节点
    #         if self.nodes_state[node] == 'I':  # 统计cir圈子中的感染节点个数
    #             sum_infect += 1
    #     den_cir = sum_infect / len(self.circle_nodes[cir])  # 计算该圈子内的感染密度
    #     return den_cir
