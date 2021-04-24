import matplotlib.pyplot as plt
import numpy as np

from entity.partition_circles import PartitionCircles
from Data import circlesData50



def generate_circles(networkUtil):
    partitionCircles = PartitionCircles(networkUtil)




def draw_plot_number_nodes():
    '''
    画图：圈内节点数
    :return:
    '''
    plt.xlabel("Circles", fontdict={'family': 'Times New Roman', 'size': 16})
    plt.ylabel("Number of Nodes", fontdict={'family': 'Times New Roman', 'size': 16})
    plt.xticks(fontproperties='Times New Roman', size=14)
    plt.yticks(fontproperties='Times New Roman', size=14)

    ad = [len(cir) for cir in circlesData50.circles]

    ad = sorted(ad, reverse=True)
    p2, = plt.plot(range(len(ad)), ad, '->', color='tomato')

    plt.savefig("./figures/circles-number_nodes.png", dpi=600)
    plt.show()

def draw_plot_average_degree():
    '''
    画图：圈内平均度
    :return:
    '''
    plt.xlabel("Circles", fontdict={'family': 'Times New Roman', 'size': 16})
    plt.ylabel("Average Degree of Circles", fontdict={'family': 'Times New Roman', 'size': 16})
    plt.xticks(fontproperties='Times New Roman', size=14)
    plt.yticks(fontproperties='Times New Roman', size=14)

    ad = sorted(circlesData50.average_degree, reverse=True)
    p2, = plt.plot(range(len(ad)), ad, '->', color='tomato')

    plt.savefig("./figures/circles-average_degree.png", dpi=600)
    plt.show()

def draw_polar_number_nodes_inner_degree():
    '''
    画图：极坐标，内圈是圈内节点数、外圈为圈内平均度。按照圈内节点数排序
    '''
    # 圈内节点数量、圈内平均度。且圈内节点数量取对数，10为底，从小到大排序
    aa = [[0.0, 0.30102999566398114, 0.47712125471966244, 0.9542425094393249, 1.0, 1.0, 1.0791812460476247,
           1.1139433523068367, 1.1760912590556811, 1.2552725051033058, 1.2552725051033058, 1.301029995663981,
           1.322219294733919, 1.3617278360175928, 1.3979400086720375, 1.3979400086720375, 1.414973347970818,
           1.4313637641589871, 1.462397997898956, 1.6901960800285134, 1.7781512503836434, 1.8061799739838869,
           1.8808135922807911, 1.9138138523837167, 2.1003705451175625, 2.1139433523068365, 2.170261715394957,
           2.187520720836463, 2.217483944213906, 2.2329961103921536, 2.2695129442179165, 2.3138672203691533,
           2.4578818967339924, 2.4899584794248346, 2.5198279937757184, 2.638489256954637, 2.747411807886423,
           2.7481880270062002, 2.9827233876685453, 3.0362295440862943, 3.050766311233042, 3.107549129744686,
           3.1306553490220304, 3.2049335223541444, 3.2933625547114453, 3.445915413951123, 3.470851324526117,
           3.4974825373673695, 3.544688022302677, 3.565965817446666],
          [1.9649122807017543, 0.6666666666666666, 1.2, 2.187311178247734, 3.2106017191977076, 0.0, 0.0, 0.0,
           1.0476190476190477, 0.0, 0.0, 0.0, 0.0, 3.233682786608049, 3.2729007633587788, 2.37567084078712,
           1.3846153846153846, 0.0, 2.8131672597864767, 3.3637598478674273, 0.0, 1.6333333333333333,
           1.903030303030303, 3.04529262086514, 0.0, 3.3477888730385166, 2.367816091954023, 1.3846153846153846,
           2.129032258064516, 2.7650273224043715, 1.3877551020408163, 1.375, 0.0, 2.220064724919094,
           1.4473684210526316, 2.142857142857143, 2.813474734872115, 2.0675675675675675, 1.5609756097560976, 0.0,
           2.299651567944251, 2.772760917838638, 2.5535714285714284, 0.0, 2.737810487580497, 1.7777777777777777,
           2.1941747572815533, 1.873015873015873, 1.7692307692307692, 2.6867845993756503]]

    theta = np.linspace(0.0, 2 * np.pi, 50, endpoint=False)  # 是分为了num_circle个角度的值
    angles = np.linspace(0.0, 2 * np.pi, 1)  # 分割极坐标为6个轴
    feature = [0]  # 设置各轴指标名称

    ax = plt.subplot(111, projection='polar')
    ax.set_thetagrids(angles * 180 / np.pi, feature)  # 添加每个特征的标签

    # ax.bar 需要的参数
    width = 0.15  # 表示每一个格子的宽度
    minlabel = 130
    maxlabel = 230
    p = (maxlabel - minlabel) / 50
    colorbb = []
    for i in range(minlabel, maxlabel, int(p)):
        colorbb.append(i)
    ax.spines['polar'].set_visible(False)  # 不显示极坐标最外的圆形
    ax.set_theta_zero_location('N')  # 设置极坐标的起点（即0度）在正上方向
    ax.set_yticks([])  # 不显示坐标间隔

    for i in range(len(aa)):
        if i == 0:
            colors = plt.cm.magma(colorbb)
            ax.bar(theta, aa[i], width=width, bottom=0.0, color=colors, alpha=0.8)  # alpha 是透明度
        else:
            colors = plt.cm.plasma(colorbb)
            ax.bar(theta, aa[i], width=width, bottom=aa[i - 1], color=colors, alpha=0.5)
    plt.savefig("./figures/polar-numberNode_innerDegree.png", dpi=600)
    plt.show()
