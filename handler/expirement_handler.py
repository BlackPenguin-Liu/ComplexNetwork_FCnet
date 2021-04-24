import matplotlib.pyplot as plt

from Data import expirement_data
from Data import dataset_data

def draw_plot_traditional_csir():
    '''
    比较传统sir与c-sir模型
    '''
    plt.figure(figsize=(15, 9.5))
    plt.xlabel("Time", fontdict={'family': 'Times New Roman', 'size': 23})
    plt.ylabel("Infect Num", fontdict={'family': 'Times New Roman', 'size': 23})

    plt.xticks(fontproperties='Times New Roman', size=20)
    plt.yticks(fontproperties='Times New Roman', size=20)

    p3, = plt.plot(range(len(expirement_data.infect_num_traditional[0])),
                   expirement_data.infect_num_traditional[0], 'p',
                   linestyle=":", color='orange')
    p4, = plt.plot(range(len(expirement_data.infect_num_traditional[0])),
                   expirement_data.infect_num_traditional[1], '>',
                   linestyle=":", color='cornflowerblue')
    p5, = plt.plot(range(len(expirement_data.infect_num_traditional[0])),
                   expirement_data.infect_num_traditional[2], '*',
                   linestyle=":", color='grey')

    p0, = plt.plot(range(len(expirement_data.infect_num_csir[0])),
                   expirement_data.infect_num_csir[0], '-p',
                   color='tomato')
    p1, = plt.plot(range(len(expirement_data.infect_num_csir[0])),
                   expirement_data.infect_num_csir[1], '-d',
                   color='mediumvioletred')
    p2, = plt.plot(range(len(expirement_data.infect_num_csir[0])),
                   expirement_data.infect_num_csir[2], '-s',
                   color='mediumaquamarine')

    plt.grid()
    plt.legend([p3, p4, p5, p0, p1, p2],
               ['β0=0.25,γ0=0.25 in SIR', 'β0=0.25,γ0=0.1 in SIR', 'β0=0.1,γ0=0.25 in SIR', 'β0=0.25,γ0=0.25 in C-SIR',
                'β0=0.25,γ0=0.1 in C-SIR', 'β0=0.1,γ0=0.25 in C-SIR'],
               prop={'family': 'Times New Roman', 'size': 20})
    plt.savefig("./figures/compare_traditional_csir", dpi=600)
    plt.show()

def draw_plot_max_degree_average_tau():
    '''
    max degree 对average tau的影响
    '''
    plt.figure(figsize=(15, 9.5))
    plt.xlabel("Max Degree in Circles", fontdict={'family': 'Times New Roman', 'size': 23})
    plt.ylabel("Average τ", fontdict={'family': 'Times New Roman', 'size': 23})

    plt.xticks(fontproperties='Times New Roman', size=20)
    plt.yticks(fontproperties='Times New Roman', size=20)

    p1, = plt.loglog(expirement_data.max_degree_average_tau[1], expirement_data.max_degree_average_tau[0], 'p',
                     color='orange')
    p2, = plt.loglog(expirement_data.max_degree_average_tau[3], expirement_data.max_degree_average_tau[2], 's',
                     color='cornflowerblue')
    p3, = plt.loglog(expirement_data.max_degree_average_tau[5], expirement_data.max_degree_average_tau[4], '^',
                     color='mediumaquamarine')
    p4, = plt.loglog(expirement_data.max_degree_average_tau[7], expirement_data.max_degree_average_tau[6], '<',
                     color='tomato')

    plt.grid()
    plt.legend([p1, p2, p3, p4],
               ['40 circles', '50 circles', '60 circles', '70 circles'],
               prop={'family': 'Times New Roman', 'size': 20})
    plt.savefig("./figures/max_degree-average_tau.png", dpi=600)
    plt.show()

def draw_plot_interest_extent():
    '''
    average interest extent的变化
    '''
    plt.figure(figsize=(15, 9.5))
    plt.xlabel("Time", fontdict={'family': 'Times New Roman', 'size': 23})
    plt.ylabel("Average Interest Extent", fontdict={'family': 'Times New Roman', 'size': 23})

    plt.xticks(fontproperties='Times New Roman', size=20)
    plt.yticks(fontproperties='Times New Roman', size=20)

    p0, = plt.plot(range(len(expirement_data.average_interest_extent[0])),
                   expirement_data.average_interest_extent[4], 'p',
                   linestyle="-", color='orange')
    p1, = plt.plot(range(len(expirement_data.average_interest_extent[0])),
                   expirement_data.average_interest_extent[5], 's',
                   linestyle="--", color='cornflowerblue')
    p2, = plt.plot(range(len(expirement_data.average_interest_extent[0])),
                   expirement_data.average_interest_extent[6], '>',
                   linestyle="--", color='tomato')

    plt.grid()
    plt.legend([p0, p1, p2],
                ['β0=0.25,γ0=0.25', 'β0=0.25,γ0=0.1', 'β0=0.1,γ0=0.25'],
               prop={'family': 'Times New Roman', 'size': 20})
    plt.savefig("./figures/interest_extent_50.png", dpi=600)
    plt.show()

def draw_plot_average_beta():
    '''
    average beta的变化
    '''
    plt.figure(figsize=(10, 9.5))
    plt.xlabel("Time", fontdict={'family': 'Times New Roman', 'size': 23})
    plt.ylabel("Average β", fontdict={'family': 'Times New Roman', 'size': 23})

    plt.xticks(fontproperties='Times New Roman', size=20)
    plt.yticks(fontproperties='Times New Roman', size=20)

    p0, = plt.plot(range(len(expirement_data.average_beta[3])),
                   expirement_data.average_beta[3], 'p',
                   linestyle="--", color='orange')
    p1, = plt.plot(range(len(expirement_data.average_beta[3])),
                   expirement_data.average_beta[4], 's',
                   linestyle="--", color='mediumaquamarine')
    p2, = plt.plot(range(len(expirement_data.average_beta[3])),
                   expirement_data.average_beta[5], '>',
                   linestyle="--", color='tomato')

    plt.grid()
    plt.legend([p0, p1, p2],
               ['β0=0.25,γ0=0.25', 'β0=0.25,γ0=0.1', 'β0=0.1,γ0=0.25'],
               prop={'family': 'Times New Roman', 'size': 20})
    plt.savefig("./figures/average_beta-50", dpi=600)
    plt.show()

def draw_plot_ego_sir_csir():
    '''
    对比sir与csir模型，ego-facebook数据集
    '''
    plt.figure(figsize=(15, 9.5))

    plt.xlabel('Time', fontdict={'family': 'Times New Roman', 'size': 23})
    plt.ylabel('Infect Num', fontdict={'family': 'Times New Roman', 'size': 23})

    p1, = plt.plot(range(len(dataset_data.ego_infect_num[0])), dataset_data.ego_infect_num[3], 'H',
                   linestyle=":", color='orange')
    p2, = plt.plot(range(len(dataset_data.ego_infect_num[0])), dataset_data.ego_infect_num[4], '>',
                   linestyle=":", color='cornflowerblue')
    p3, = plt.plot(range(len(dataset_data.ego_infect_num[0])), dataset_data.ego_infect_num[5], '*',
                   linestyle=":", color='grey')

    p4, = plt.plot(range(len(dataset_data.ego_infect_num[0])), dataset_data.ego_infect_num[0], '-p',
                   color='tomato')
    p5, = plt.plot(range(len(dataset_data.ego_infect_num[0])), dataset_data.ego_infect_num[1], '-d',
                   color='mediumvioletred')
    p6, = plt.plot(range(len(dataset_data.ego_infect_num[0])), dataset_data.ego_infect_num[2], '-s',
                   color='mediumaquamarine')

    plt.yticks(fontproperties='Times New Roman', size=20)
    plt.xticks(fontproperties='Times New Roman', size=20)
    plt.grid()  # 在背景中加上方格
    plt.legend([p1, p2, p3, p4, p5, p6],
               ['β0=0.25, γ0=0.25 in SIR', 'β0=0.25, γ0=0.1 in SIR', 'β0=0.1, γ0=0.25 in SIR',
                'β0=0.25, γ0=0.25 in C-SIR', 'β0=0.25, γ0=0.1 in C-SIR', 'β0=0.1, γ0=0.25 in C-SIR'],
               prop={'family': 'Times New Roman', 'size': 20})
    plt.savefig("./figures/compare_ego_sir_csir.png", dpi=600)
    plt.show()

def draw_plot_ego_max_degree_average_tau():
    plt.figure(figsize=(15, 9.5))

    plt.xlabel('Max Degree in Circles', fontdict={'family': 'Times New Roman', 'size': 23})
    plt.ylabel('Average τ', fontdict={'family': 'Times New Roman', 'size': 23})

    # 最大度与 average tau的关系-------------------------
    p5, = plt.loglog(dataset_data.ego_tau_circles_nodes[1], dataset_data.ego_tau_circles_nodes[0], 'p',
                     linestyle="", color='cornflowerblue')
    # 最大度与 average tau的关系 END----------------------

    # # 圈内节点数量与 average tau的关系---------------------
    # p5, = plt.loglog(dataset_data.ego_tau_circles_nodes[5], dataset_data.ego_tau_circles_nodes[4], 'p',
    #                  linestyle="", color='cornflowerblue')
    # # 圈内节点数量与 average tau的关系 END-----------------

    plt.yticks(fontproperties='Times New Roman', size=20)
    plt.xticks(fontproperties='Times New Roman', size=20)
    plt.grid()  # 在背景中加上方格
    plt.savefig("./figures/ego-max_degree-average_tau.png", dpi=600)
    plt.show()

def draw_plot_youtube_sir_csir():
    '''
    youtube数据集上sir与csir对比
    '''
    plt.figure(figsize=(15, 9.5))

    plt.xlabel('Time', fontdict={'family': 'Times New Roman', 'size': 23})
    plt.ylabel('Infect Num', fontdict={'family': 'Times New Roman', 'size': 23})

    p5, = plt.plot(range(len(dataset_data.youtube_infect_num[0])), dataset_data.youtube_infect_num[0], '-p',
                   color='tomato')
    p6, = plt.plot(range(len(dataset_data.youtube_infect_num[0])), dataset_data.youtube_infect_num[1], '-d',
                   color='mediumvioletred')
    p7, = plt.plot(range(len(dataset_data.youtube_infect_num[0])), dataset_data.youtube_infect_num[2], '-s',
                   color='mediumaquamarine')

    p1, = plt.plot(range(len(dataset_data.youtube_infect_num[0])), dataset_data.youtube_infect_num[3], 's',
                   linestyle=":", color='orange')
    p2, = plt.plot(range(len(dataset_data.youtube_infect_num[0])), dataset_data.youtube_infect_num[4], '>',
                   linestyle=":", color='cornflowerblue')
    p3, = plt.plot(range(len(dataset_data.youtube_infect_num[0])), dataset_data.youtube_infect_num[5], '*',
                   linestyle=":", color='grey')

    plt.yticks(fontproperties='Times New Roman', size=20)
    plt.xticks(fontproperties='Times New Roman', size=20)
    plt.grid()  # 在背景中加上方格
    plt.legend([p1, p2, p3, p5, p6, p7],
               ['β0=0.25,γ0=0.25 in SIR', 'β0=0.25,γ0=0.1 in SIR', 'β0=0.1,γ0=0.25 in SIR',
                'β0=0.25,γ0=0.25 in C-SIR', 'β0=0.25,γ0=0.1 in C-SIR', 'β0=0.1,γ0=0.25 in C-SIR'],
               prop={'family': 'Times New Roman', 'size': 20})
    plt.savefig("./figures/compare_youtube_sir_csir.png", dpi=600)
    plt.show()

def draw_plot_youtube_sum_nodes_average_tau():
    '''
        画youtube数据集上average tau与圈内最大度、节点数量的关系
    '''
    plt.figure(figsize=(15, 9.5))

    plt.xlabel('Sum of Nodes in Circles', fontdict={'family': 'Times New Roman', 'size': 23})
    plt.ylabel('Average τ', fontdict={'family': 'Times New Roman', 'size': 23})

    # # 与最大度-----------------------------------
    # p5, = plt.loglog(dataset_data.youtube_tau_circle_nodes[1], dataset_data.youtube_tau_circle_nodes[0], 'p',
    #                  linestyle="", color='mediumaquamarine')
    # # 与最大度 END-------------------------------

    # 与圈内节点数量-----------------------------------
    p5, = plt.loglog(dataset_data.youtube_tau_circle_nodes[5], dataset_data.youtube_tau_circle_nodes[4], 'p',
                     linestyle="", color='mediumaquamarine')
    # 与圈内节点数量 END-------------------------------

    plt.yticks(fontproperties='Times New Roman', size=20)
    plt.xticks(fontproperties='Times New Roman', size=20)
    plt.grid()  # 在背景中加上方格
    plt.savefig("./figures/youtube-sum_nodes-average_tau.png", dpi=600)
    plt.show()