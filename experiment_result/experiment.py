import os

import numpy as np
from matplotlib import pyplot as plt
# import warnings
#
# warnings.filterwarnings('ignore')
from scipy.interpolate import make_interp_spline, BSpline


# 返回结果 规模，轮数，精确度，召回率
def get_data(key):
    res = []
    info = info_map[key]
    with open(info['filepath'], encoding='utf-8') as f:
        f.readline()
        line = f.readline()
        count = 0
        while line:
            arr = line.split()
            arr = [float(item) for item in arr]
            if arr[3] < 0:
                arr[3] = 0
            if arr[3] < 0:
                count += 1
            value_set = list(info['round'](arr))
            value_set.extend([info['pre'](arr), info['recall'](arr)])
            res.append(value_set)
            line = f.readline()
    return res


# 返回结果 规模，轮数，精确度，召回率
#     No    Content_num  Round     cover
def precision0(arr):
    return 1


def recall0(arr):
    return 1


def precision2(arr):
    return 1


def recall2(arr):
    return (arr[2] - arr[3]) / arr[2]


def precision4(arr):
    return (arr[2] - arr[3]) / arr[-1]


def recall4(arr):
    return (arr[2] - arr[3]) / arr[2]


def recall5(arr):
    return arr[-1] / arr[2]


def precision6_1(arr):
    return precision4(arr)


def precision6_2(arr):
    return arr[-1] + 1


def round0(arr):
    return arr[1], arr[2]


def round1(arr):
    return arr[2], arr[1]


info_map = {
    1: {
        'filepath': 'k2/e0_without_rp_res_5508_1_5508.txt',
        'pre': precision0,
        'recall': recall0,
        'round': round0,
        'label': 'Unlimited Slot Filling Dialogue Strategy',
        'color': 'r',
    },
    2: {
        'filepath': 'k2/e2_mod_rpdb_1_5508.txt',
        'pre': precision2,
        'recall': recall2,
        'round': round1,
        'label': 'Strategy Based on RP Repository',
        'color': 'b'
    },
    3: {
        'filepath': 'k2/e3_mod_rp_kg_1_5508_update.txt',
        'pre': precision2,
        'recall': recall2,
        'round': round1,
        'label': 'Dialogue Strategy Based on RP+KGR',
        'color': 'y'
    },
    4: {
        'filepath': 'new_exp/e5_grc_bt_1_5508_update.txt',
        'pre': precision4,
        'recall': recall4,
        'round': round1,
        'label': 'Strategy Based on Top-down Pruning',
        'color': 'black'
    },
    5: {
        'filepath': 'new_exp/e4_grc_tb_1_5508_update.txt',
        'pre': precision4,
        'recall': recall4,
        'round': round1,
        'label': 'Strategy Based on Bottom-up Pruning',
        'color': 'coral'
    },
    6: {
        'filepath': 'e6/e6_top_grc_500_5508(1).txt',
        'pre': precision6_1,
        'recall': recall4,
        'round': round1,
        'label': 'Strategy Based on RP Holistic Analysis Pruning',
        'color': 'm'
    }}


def plot_graph_ori_cover(item, dates, draw_list):
    def get_precision(_data, par):
        if par == 1:
            return [100 for i in range(11)]
        from collections import defaultdict
        d = defaultdict(list)
        for _item in _data:
            d[_item[0]].append(_item[2])
        b = [0 for i in range(11)]
        for k in d.keys():
            avg = sum(d[k]) / len(d[k])
            b[int(k)] = avg * 100
        return b

    def get_recall(_data, par):
        if par == 1:
            return [100 for i in range(11)]
        from collections import defaultdict
        d = defaultdict(list)
        for _item in _data:
            d[_item[0]].append(_item[3])
        b = [0 for i in range(11)]
        for k in d.keys():
            avg = sum(d[k]) / len(d[k])
            b[int(k)] = avg * 100
        return b

    def get_f1(_data, par):
        from collections import defaultdict
        pres = [arr[2] for arr in _data]
        recalls = [arr[3] for arr in _data]
        d = defaultdict(list)
        for idx_in, _item in enumerate(_data):
            d[_item[0]].append(2 * pres[idx_in] * recalls[idx_in] / (pres[idx_in] + recalls[idx_in]))
        b = [0 for i in range(11)]
        for k in d.keys():
            avg = sum(d[k]) / len(d[k])
            b[int(k)] = avg * 100
        return b

    # 原来的racall.ylim是[70, 240]
    fig_ctrl = {
        'precision': {
            'label': 'Precision Rate (%)',
            'func': get_precision,
            'ylim': [40, 105]
        },
        'recall': {
            'label': 'Recall Rate (%)',
            'func': get_recall,
            'ylim': [60, 105]
        },
        'f1': {
            'label': 'Micro F1-score',
            'func': get_f1,
            'ylim': [60, 105],
        }
    }
    fig = plt.figure()
    ax = fig.add_subplot(111)
    for idx, date in enumerate(dates):
        # TODO 控制精确度怎么显示
        if len(dates) >= 4 and len(dates) - idx <= 3 and item == 'precision':
            continue
        b = fig_ctrl[item]['func'](date, draw_list[idx])
        x = [2, 3, 4, 5, 6, 7, 8, 9, 10]
        x = np.array(x)
        x_new = np.linspace(x.min(), x.max(), 300)
        # power_smooth = spline(x, b[2:], x_new)
        spl = make_interp_spline(x, b[2:], k=3)  # type: BSpline
        power_smooth = spl(x_new)
        if all([i == 100 for i in b[2:]]):
            power_smooth = [100 for i in range(300)]
        # ax.scatter(x, b[2:], color=colors[idx])
        # ax.plot(x_new, power_smooth, color=colors[idx], label=labels[idx])
        ax.scatter(x, b[2:], color=info_map[draw_list[idx]]['color'])
        ax.plot(x_new, power_smooth, color=info_map[draw_list[idx]]['color'], label=info_map[draw_list[idx]]['label'])
    ax.legend(loc='best')
    ax.set_ylabel(fig_ctrl[item]['label'], fontdict={'size': 15, 'color': 'black'})
    ax.set_xlabel('Scale of Requirement', fontdict={
        'size': 15, 'color': 'black'})
    # ax.set_ylim(ymin=fig_ctrl[item]['ylim'])
    # ax.set_ylim(fig_ctrl[item]['ylim'])
    # 展示
    plt.show()
    print(fig_ctrl[item]['ylim'])
    file_name = '{}/lab_{}_{}.pdf'.format(PATH_PREFIX, draw_list[0], item)
    if SAVE_FIGURE:
        fig.savefig(file_name, bbox_inches='tight', pad_inches=0.05)


def plot_graph_ori_round(dates, draw_list):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    for idx, data in enumerate(dates):
        # data = np.array(get_data(0, 0, 0))
        x1 = data[:, 0]  # [ 0  3  6  9 12 15 18 21]
        y1 = data[:, 1]  # [ 1  4  7 10 13 16 19 22]
        plot_line = {}
        line_1 = {}
        from collections import defaultdict
        d = defaultdict(list)
        for _item in data:
            d[_item[0]].append(_item[1])
        b = [0 for i in range(11)]
        for k in d.keys():
            avg = sum(d[k]) / len(d[k])
            b[int(k)] = avg
        # print(b)
        x = [2, 3, 4, 5, 6, 7, 8, 9, 10]
        ax.scatter(x, b[2:], color=info_map[draw_list[idx]]['color'])
        ax.plot(x, b[2:], color=info_map[draw_list[idx]]['color'], label=info_map[draw_list[idx]]['label'])
        ax.legend(loc='best')
        ax.set_ylabel('Average Dialogue Turns', fontdict={'size': 15, 'color': 'black'})
        ax.set_xlabel('Scale of Requirement', fontdict={
            'size': 15, 'color': 'black'})

    # 展示
    ax.legend(loc='best')
    plt.show()

    file_name = '{}/lab_{}_dialogue_round.pdf'.format(PATH_PREFIX, draw_list[0])
    if SAVE_FIGURE:
        fig.savefig(file_name, bbox_inches='tight', pad_inches=0.05)


def plot_graph(draw_list):
    datas = [np.array(get_data(key)) for key in draw_list]
    pic_str_list = ['precision', 'recall', 'f1']
    # pic_str_list = ['precision', 'f1']
    for item in pic_str_list:
        plot_graph_ori_cover(item, datas, draw_list)
    plot_graph_ori_round(datas, draw_list)


PATH_PREFIX = './pic/pdfs'
if not os.path.exists(PATH_PREFIX):
    os.mkdir(PATH_PREFIX)
SAVE_FIGURE = True

if __name__ == '__main__':
    # 实验1
    plot_graph([1])
    # 实验2
    plot_graph([2, 1])

    # 实验3
    plot_graph([3, 2, 1])

    # new_实验四
    plot_graph([4, 3, 2, 1])

    # new_实验5
    plot_graph([5, 4, 3, 2, 1])
    #
    # # new_实验6
    plot_graph([6, 5, 4, 3, 2, 1])
