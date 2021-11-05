import os

import experiment


# 返回结果 规模，轮数，精确度，召回率
def f1(arr):
    pre = arr[2]
    rec = arr[3]
    return 200 * pre * rec / (pre + rec)


# 后面减前面
def plot_delta_cover_and_delta_round(cmp_from, cmp_to):
    options = {
        0: {
            'l': 'Unlimited Slot Filling Dialogue Strategy',
            'c': 'r'
        },
        2: {
            'l': 'Strategy Based on RP Repository',
            'c': 'b',
        },
        3: {
            'l': 'Dialogue Strategy Based on RP+KGR',
            'c': 'y'
        },
        4: {
            'l': 'Strategy Based on Top-down Pruning',
            'c': 'black'
        },
        5: {
            'l': 'Strategy Based on Bottom-up Pruning',
            'c': 'coral'
        },
        6: {
            'l': 'Strategy Based on RP Holistic Analysis Pruning',
            'c': 'm'

        },
        'new_3': {
            'l': 'Dialogue based on KGR & RP repository',
            'c': 'y'
        },
    }

    from collections import Counter
    import matplotlib.pyplot as plt
    import numpy as np
    # style.use('ggplot')
    x_width = 0.4
    y_width = 0.4

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # ax = Axes3D(fig)

    ori_data = experiment.get_data(cmp_from)

    # 绘制
    start_idx = 500 if cmp_to == 6 or cmp_from == 6 else 0

    def draw_3d(e_num):
        cmp_data = experiment.get_data(e_num)
        y_1 = [cmp_data[i - start_idx][1] - ori_data[i][1] for i in range(start_idx, len(ori_data))]
        # y_1 = [cmp_data[i][2] - ori_data[i][2] for i in range(len(cmp_data))]
        x_1 = [f1(cmp_data[i - start_idx]) - f1(ori_data[i]) for i in range(start_idx, len(ori_data))]
        # x_1 = [f1(cmp_data[i]) - f1(ori_data[i]) for i in range(len(cmp_data))]
        point_counter = Counter(list(zip(x_1, y_1)))
        print(point_counter)
        x3 = list(map(lambda x: x[0], point_counter.keys()))
        y3 = list(map(lambda x: x[1], point_counter.keys()))
        z3 = np.zeros(len(x3))

        dx = [x_width for i in range(len(x3))]
        dy = [y_width for i in range(len(x3))]
        dz = list(point_counter.values())
        ax.bar3d(x3, y3, z3, dx, dy, dz, color=options[e_num]['c'], alpha=0.45)

    draw_3d(cmp_to)
    # draw_3d(cmp_from)

    # 图例
    # from_proxy = plt.Rectangle((0, 0), 1, 1, fc=options[cmp_from]['c'])
    to_proxy = plt.Rectangle((0, 0), 1, 1, fc=options[cmp_to]['c'])
    ax.legend([to_proxy], [options[cmp_to]['l']])

    # if cmp_to == 5 and cmp_from == 2:
    # plt.gca().invert_yaxis() # y轴反向
    # ax.invert_xaxis()
    ax.set_ylabel('$\Delta$ Dialogue Turns')
    ax.set_xlabel('$\Delta$ Micro F1-score')
    ax.set_zlabel('Frequency')

    import os.path
    if not os.path.exists(PATH_PREFIX):
        os.mkdir(PATH_PREFIX)
    if SAVE_FIG:
        plt.savefig('{}/lab_{}_3d.pdf'.format(PATH_PREFIX, cmp_to), bbox_inches='tight')
    plt.show()


PATH_PREFIX = './pic/pdfs'
if not os.path.exists(PATH_PREFIX):
    os.mkdir(PATH_PREFIX)
SAVE_FIG = True
if __name__ == '__main__':
    # 4-0 2-0
    # 5-0 2-0
    # 6-0 2-0
    # 3-0 2-0
    plot_delta_cover_and_delta_round(2, 6)
    plot_delta_cover_and_delta_round(2, 4)
    plot_delta_cover_and_delta_round(2, 5)
    plot_delta_cover_and_delta_round(2, 3)
