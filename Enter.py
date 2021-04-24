from handler import graph_handler
from handler import circles_handler
from util.NetworkUtil import NetworkUtil
from handler.sir_handler import SIR
from handler import expirement_handler as expirement

from handler import graph_ego_handler
from handler import circles_ego_handler

from handler import graph_youtube_handler
from handler import circles_youtube_handler

# 网络参数，实验参数
networkUtil = NetworkUtil()

###################模拟的网络 begin

# 生成图，包括节点、边
# graph_handler.generate_network(networkUtil)
# # 生成好友圈（数据已经记录到文件里面）
# circles_handler.generate_circles()

# sir = SIR(networkUtil)

# 实验
# expirement.draw_plot_traditional_csir()
# expirement.draw_plot_max_degree_average_tau()
# expirement.draw_plot_interest_extent()
# expirement.draw_plot_average_beta()
###################模拟的网络 end

###################ego-facebook begin
# graph_ego_handler.generate_network(networkUtil)
# circles_ego_handler.generate_circles(networkUtil)
#
expirement.draw_plot_ego_sir_csir()
###################ego-facebook end

###################youtube begin
# graph_youtube_handler.generate_network(networkUtil)
# circles_youtube_handler.generate_circles(networkUtil)

expirement.draw_plot_ego_max_degree_average_tau()
###################youtube end