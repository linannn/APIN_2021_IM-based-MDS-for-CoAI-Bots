#!/usr/bin/env python

# encoding: utf-8
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/7 15:10
# @Author  : junruit
# @File    : deal_plot.py
# @desc: PyCharm
'''
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 4., 1.06 * height, '%s' % int(height))


# mode * 4  1-mod 2-mod_fill 3-ran 4-ran_fill
def get_data(e_num, k, mode):
    res_set = []
    if e_num == 0:
        file_name = "e0_without_rp_res_5508.txt"
        with open(file_name, 'r', encoding='utf-8') as fr:
            value = fr.readline()
            value = fr.readline()
            while value:
                value = ' '.join(value.split())
                array_record = value.split()
                value_set = [array_record[1], array_record[2]]
                cover = [array_record[3]]
                cover = list(map(float, cover))
                # print(cover)
                value_set = list(map(int, value_set))
                value_set[1] = value_set[1] + 1
                value_set.extend(cover)
                res_set.append(value_set)
                value = fr.readline()
    elif e_num == 1:
        file_name = "e1_with_kg_res_5508.txt"
        with open(file_name, 'r', encoding='utf-8') as fr:
            value = fr.readline()
            value = fr.readline()
            while value:
                value = ' '.join(value.split())
                array_record = value.split()
                value_set = [array_record[2], array_record[1]]
                cover = [array_record[5]]
                cover = list(map(float, cover))
                value_set = list(map(int, value_set))
                value_set[1] = value_set[1] + 1
                value_set.extend(cover)
                res_set.append(value_set)
                value = fr.readline()
    elif e_num == 2:
        file_name_ran = "./random_e2/e2_with_rpdb_" + str(k) + "_ran_5508.txt"
        file_name_ran_fill = "./random_e2/e2_rpdb_fill_" + str(k) + "_ran_5508.txt"
        file_name_mod = "./mod_e2/e2_with_rpdb_" + str(k) + "_mod_5508.txt"
        file_name_mod_fill = "./mod_e2/e2_rpdb_fill_" + str(k) + "_mod_5508.txt"
        if mode == 1:
            file_name = file_name_mod
        elif mode == 2:
            file_name = file_name_mod_fill
        elif mode == 3:
            file_name = file_name_ran
        elif mode == 4:
            file_name = file_name_ran_fill
        with open(file_name, 'r', encoding='utf-8') as fr:
            value = fr.readline()
            value = fr.readline()
            while value:
                value = ' '.join(value.split())
                array_record = value.split()
                value_set = [array_record[2], array_record[1]]
                cover = [array_record[5]]
                cover = list(map(float, cover))
                value_set = list(map(int, value_set))
                value_set.extend(cover)
                res_set.append(value_set)
                value = fr.readline()
    elif e_num == 3:
        file_name_ran = "./random_e3/e3_rpdb_kg_" + str(k) + "_ran_5508.txt"
        file_name_ran_fill = "./random_e3/e3_rpdb_kg_fill_" + str(k) + "_ran_5508.txt"
        file_name_mod = "./mod_e3/e3_rpdb_kg_" + str(k) + "_mod_5508.txt"
        file_name_mod_fill = "./mod_e3/e3_rpdb_kg_fill_" + str(k) + "_mod_5508.txt"
        if mode == 1:
            file_name = file_name_mod
        elif mode == 2:
            file_name = file_name_mod_fill
        elif mode == 3:
            file_name = file_name_ran
        elif mode == 4:
            file_name = file_name_ran_fill
        with open(file_name, 'r', encoding='utf-8') as fr:
            value = fr.readline()
            value = fr.readline()
            while value:
                value = ' '.join(value.split())
                array_record = value.split()
                value_set = [array_record[2], array_record[1]]
                cover = [array_record[5]]
                cover = list(map(float, cover))
                value_set = list(map(int, value_set))
                value_set.extend(cover)
                res_set.append(value_set)
                value = fr.readline()
    elif e_num == 4:
        file_name_grc = "./e4_bottom_to_top/e4_grc_bottom_to_top_" + str(k) + "_5508.txt"
        file_name_grc_fill = "./e4_bottom_to_top/e4_grc_fill_bottom_to_top_" + str(k) + "_5508.txt"
        if mode == 1:
            file_name = file_name_grc
        elif mode == 2:
            file_name = file_name_grc_fill
        with open(file_name, 'r', encoding='utf-8') as fr:
            value = fr.readline()
            value = fr.readline()
            while value:
                value = ' '.join(value.split())
                array_record = value.split()
                value_set = [array_record[2], array_record[1]]
                cover = [array_record[5]]
                cover = list(map(float, cover))
                value_set = list(map(int, value_set))
                value_set.extend(cover)
                res_set.append(value_set)
                value = fr.readline()
    elif e_num == 5:
        file_name_grc = "./e5_top_to_bottom/e5_grc_top_to_bottom_" + str(k) + "_5508.txt"
        file_name_grc_fill = "./e5_top_to_bottom/e5_grc_top_to_bottom_fill" + str(k) + "_5508.txt"
        if mode == 1:
            file_name = file_name_grc
        elif mode == 2:
            file_name = file_name_grc_fill
        with open(file_name, 'r', encoding='utf-8') as fr:
            value = fr.readline()
            value = fr.readline()
            while value:
                value = ' '.join(value.split())
                array_record = value.split()
                value_set = [array_record[2], array_record[1]]
                cover = [array_record[5]]
                cover = list(map(float, cover))
                value_set = list(map(int, value_set))
                value_set.extend(cover)
                res_set.append(value_set)
                value = fr.readline()
    return res_set


# 数据
# x:ori_content y:round z:cover
# 数据１
# data1 = np.arange(24).reshape((8, 3))
data1 = get_data(0, 0, 0)
data1 = np.array(data1)
# data的值如下：
# [[ 0  1  2]
#  [ 3  4  5]
#  [ 6  7  8]
#  [ 9 10 11]
#  [12 13 14]
#  [15 16 17]
#  [18 19 20]
#  [21 22 23]]
x1 = data1[:, 0]  # [ 0  3  6  9 12 15 18 21]
y1 = data1[:, 1]  # [ 1  4  7 10 13 16 19 22]
z1 = data1[:, 2]  # [ 2  5  8 11 14 17 20 23]

# 数据２
data2 = get_data(1, 0, 0)
data2 = np.array(data2)
x2 = data2[:, 0]
y2 = data2[:, 1]
z2 = data2[:, 2]

# mode * 4  1-mod 2-mod_fill 3-ran 4-ran_fill
data3_1 = get_data(2, 6, 1)
data3_1 = np.array(data3_1)
x3_1 = data3_1[:, 0]
y3_1 = data3_1[:, 1]
z3_1 = data3_1[:, 2]

data3_2 = get_data(2, 6, 2)
data3_2 = np.array(data3_2)
x3_2 = data3_2[:, 0]
y3_2 = data3_2[:, 1]
z3_2 = data3_2[:, 2]

data3_3 = get_data(2, 6, 3)
data3_3 = np.array(data3_3)
x3_3 = data3_3[:, 0]
y3_3 = data3_3[:, 1]
z3_3 = data3_3[:, 2]

data3_4 = get_data(2, 6, 4)
data3_4 = np.array(data3_4)
x3_4 = data3_4[:, 0]
y3_4 = data3_4[:, 1]
z3_4 = data3_4[:, 2]

data4_1 = get_data(3, 6, 1)
data4_1 = np.array(data4_1)
x4_1 = data4_1[:, 0]
y4_1 = data4_1[:, 1]
z4_1 = data4_1[:, 2]

data4_2 = get_data(3, 6, 2)
data4_2 = np.array(data4_2)
x4_2 = data4_2[:, 0]
y4_2 = data4_2[:, 1]
z4_2 = data4_2[:, 2]

data4_3 = get_data(3, 6, 3)
data4_3 = np.array(data4_3)
x4_3 = data4_3[:, 0]
y4_3 = data4_3[:, 1]
z4_3 = data4_3[:, 2]

data4_4 = get_data(3, 6, 4)
data4_4 = np.array(data4_4)
x4_4 = data4_4[:, 0]
y4_4 = data4_4[:, 1]
z4_4 = data4_4[:, 2]

# grc-bottom_to_top
data5_1 = get_data(4, 6, 1)
data5_1 = np.array(data5_1)
x5_1 = data5_1[:, 0]
y5_1 = data5_1[:, 1]
z5_1 = data5_1[:, 2]

# grc-fill-bottom_to_top
data5_2 = get_data(4, 6, 2)
data5_2 = np.array(data5_2)
x5_2 = data5_2[:, 0]
y5_2 = data5_2[:, 1]
z5_2 = data5_2[:, 2]

# grc-top_to_bottom
data6_1 = get_data(5, 6, 1)
data6_1 = np.array(data6_1)
x6_1 = data6_1[:, 0]
y6_1 = data6_1[:, 1]
z6_1 = data6_1[:, 2]

# grc-fill-top_to_bottom
data6_2 = get_data(5, 6, 2)
data6_2 = np.array(data6_2)
x6_2 = data6_2[:, 0]
y6_2 = data6_2[:, 1]
z6_2 = data6_2[:, 2]


# def plot_graph_3(switch):
#     # 绘制散点图
#     fig = plt.figure()
#     ax = Axes3D(fig)
#
#     if switch == 1:
#         ax.scatter(x1, y1, z1, color='r', label='2')
#         ax.scatter(x2, y2, z2, color='g', label='3')
#         ax.scatter(x3, y3, z3, color='b', label='4')
#         ax.scatter(x4, y4, z4, color='cyan', label='5')
#         ax.scatter(x5, y5, z5, color='y', label='6')
#     elif switch == 2:
#         ax.scatter(x1, y1, z1, color='r', label='2')
#     elif switch == 3:
#         ax.scatter(x2, y2, z2, color='g', label='3')
#     elif switch == 4:
#         ax.scatter(x3, y3, z3, color='b', label='4')
#     elif switch == 5:
#         ax.scatter(x4, y4, z4, color='cyan', label='5')
#     elif switch == 6:
#         ax.scatter(x5, y5, z5, color='y', label='6')
#
#     # 绘制图例
#     ax.legend(loc='best')
#
#     # 添加坐标轴(顺序是Z, Y, X)
#     ax.set_zlabel('Round', fontdict={'size': 15, 'color': 'red'})
#     ax.set_ylabel('Lack_content', fontdict={'size': 15, 'color': 'red'})
#     ax.set_xlabel('Origin_content', fontdict={'size': 15, 'color': 'red'})
#
#     # 展示
#     plt.show()
#     file_name = "../plot_res/三维_e2_" + str(switch) + "_random.png"
#     fig.savefig(file_name)


def plot_graph_2_ori_round(support):
    # 绘制散点图
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(x1, y1, color='r', label='e0')
    ax.scatter(x2, y2, color='g', label='e1')
    ax.scatter(x3_2, y3_2, color='b', label='e2-1mod-fill')
    ax.scatter(x3_4, y3_4, color='cyan', label='e2-2ran-fill')
    ax.scatter(x4_2, y4_2, color='y', label='e3-1mod-fill')
    ax.scatter(x4_4, y4_4, color='black', label='e3-2ran-fill')
    ax.scatter(x5_2, y5_2, color='m', label='e4-grc-fill-bottom-top')
    ax.scatter(x6_2, y6_2, color='coral', label='e5-grc-fill-top-bottom')

    # 绘制图例
    ax.legend(loc='best')

    # 添加坐标轴(顺序是Z, Y, X)
    # ax.set_zlabel('Round', fontdict={'size': 15, 'color': 'red'})
    ax.set_ylabel('Round', fontdict={'size': 15, 'color': 'black'})
    ax.set_xlabel('Origin_content', fontdict={'size': 15, 'color': 'black'})

    # 展示
    plt.show()
    # file_name = "../plot_res/二维_e2_" + str(switch) + "_random.png"
    file_name = "../plot_res/二维_k" + str(support) + "_compare_fill.png"
    fig.savefig(file_name)


def plot_graph_2_ori_cover(support):
    # 绘制散点图
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(x1, z1, color='r', label='e0')
    ax.scatter(x2, z2, color='g', label='e1')
    ax.scatter(x3_1, z3_1, color='b', label='e2-1mod')
    ax.scatter(x3_3, z3_3, color='cyan', label='e2-2ran')
    ax.scatter(x4_1, z4_1, color='y', label='e3-1mod')
    ax.scatter(x4_3, z4_3, color='black', label='e3-2ran')
    ax.scatter(x5_1, z5_1, color='m', label='e4-grc')
    ax.scatter(x6_1, z6_1, color='coral', label='e5-grc')

    # 绘制图例
    ax.legend(loc='best')

    # 添加坐标轴(顺序是Z, Y, X)
    # ax.set_zlabel('Round', fontdict={'size': 15, 'color': 'red'})
    ax.set_ylabel('Cover', fontdict={'size': 15, 'color': 'black'})
    ax.set_xlabel('Origin_content', fontdict={'size': 15, 'color': 'black'})

    # 展示
    plt.show()
    # file_name = "../plot_res/二维_e2_" + str(switch) + "_random.png"
    file_name = "../plot_res/二维_k" + str(support) + "_cover_compare.png"
    fig.savefig(file_name)


def plot_average_2_ori_round(switch, support):
    # 绘制散点图
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plot_line = {}
    line_1 = {}
    # i0: ori_content i1: round i2: cover
    for i in data1:
        if i[0] not in plot_line:
            plot_line[i[0]] = [i[1]]
        else:
            plot_line[i[0]].append(i[1])
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num

    b = [0] * 11
    for k, v in line_1.items():
        b[int(k)] = v

    plot_line = {}
    line_1 = {}
    for i in data2:
        if i[0] not in plot_line:
            plot_line[i[0]] = [i[1]]
        else:
            plot_line[i[0]].append(i[1])
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    c = [0] * 11
    for k, v in line_1.items():
        c[int(k)] = v

    plot_line = {}
    line_1 = {}
    for i in data3_2:
        if i[0] not in plot_line:
            plot_line[i[0]] = [i[1]]
        else:
            plot_line[i[0]].append(i[1])
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    d = [0] * 11
    for k, v in line_1.items():
        d[int(k)] = v

    plot_line = {}
    line_1 = {}
    for i in data3_4:
        if i[0] not in plot_line:
            plot_line[i[0]] = [i[1]]
        else:
            plot_line[i[0]].append(i[1])
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    e = [0] * 11
    for k, v in line_1.items():
        e[int(k)] = v

    plot_line = {}
    line_1 = {}
    for i in data4_2:
        if i[0] not in plot_line:
            plot_line[i[0]] = [i[1]]
        else:
            plot_line[i[0]].append(i[1])
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    f = [0] * 11
    for k, v in line_1.items():
        f[int(k)] = v

    plot_line = {}
    line_1 = {}
    for i in data4_4:
        if i[0] not in plot_line:
            plot_line[i[0]] = [i[1]]
        else:
            plot_line[i[0]].append(i[1])
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    g = [0] * 11
    for k, v in line_1.items():
        g[int(k)] = v

    plot_line = {}
    line_1 = {}
    for i in data5_2:
        if i[0] not in plot_line:
            plot_line[i[0]] = [i[1]]
        else:
            plot_line[i[0]].append(i[1])
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    h = [0] * 11
    for k, v in line_1.items():
        h[int(k)] = v

    plot_line = {}
    line_1 = {}
    for i in data3_1:
        if i[0] not in plot_line:
            plot_line[i[0]] = [i[1]]
        else:
            plot_line[i[0]].append(i[1])
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    u = [0] * 11
    for k, v in line_1.items():
        u[int(k)] = v

    plot_line = {}
    line_1 = {}
    for i in data4_1:
        if i[0] not in plot_line:
            plot_line[i[0]] = [i[1]]
        else:
            plot_line[i[0]].append(i[1])
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    u_41 = [0] * 11
    for k, v in line_1.items():
        u_41[int(k)] = v

    plot_line = {}
    line_1 = {}
    for i in data5_1:
        if i[0] not in plot_line:
            plot_line[i[0]] = [i[1]]
        else:
            plot_line[i[0]].append(i[1])
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    u_51 = [0] * 11
    for k, v in line_1.items():
        u_51[int(k)] = v

    plot_line = {}
    line_1 = {}
    for i in data6_2:
        if i[0] not in plot_line:
            plot_line[i[0]] = [i[1]]
        else:
            plot_line[i[0]].append(i[1])
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    u_62 = [0] * 11
    for k, v in line_1.items():
        u_62[int(k)] = v

    plot_line = {}
    line_1 = {}
    for i in data6_1:
        if i[0] not in plot_line:
            plot_line[i[0]] = [i[1]]
        else:
            plot_line[i[0]].append(i[1])
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    u_61 = [0] * 11
    for k, v in line_1.items():
        u_61[int(k)] = v

    x = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    z1 = b[2:]
    z2 = c[2:]
    z3 = d[2:]
    z4 = e[2:]
    z5 = f[2:]
    z6 = g[2:]
    z7 = h[2:]
    z12 = u_62[2:]

    # un-fill
    z8 = u[2:]  # e2-mod
    z9 = u_41[2:]  # e3-mod
    z10 = u_51[2:]  # e4
    z11 = u_61[2:]  # e5

    if switch == 0:
        ax.plot(x, z1, color='r')
        ax.scatter(x, z1, color='r', label='e0')
    if switch == 1:
        ax.plot(x, z2, color='g')
        ax.scatter(x, z2, color='g', label='e1')
    if switch == 2:
        ax.plot(x, z3, color='b')
        ax.plot(x, z4, color='cyan')
        ax.scatter(x, z3, color='b', label='e2-1mod-fill')
        ax.scatter(x, z4, color='cyan', label='e2-2ran-fill')
    if switch == 3:
        ax.plot(x, z5, color='y')
        ax.plot(x, z6, color='black')
        ax.scatter(x, z5, color='y', label='e3-1mod-fill')
        ax.scatter(x, z6, color='black', label='e3-2ran-fill')
    if switch == 4:
        ax.plot(x, z1, color='r')
        ax.plot(x, z2, color='g')
        ax.scatter(x, z1, color='r', label='e0')
        ax.scatter(x, z2, color='g', label='e1')
    if switch == 5:
        ax.plot(x, z1, color='r')
        ax.plot(x, z3, color='b')
        ax.plot(x, z4, color='cyan')
        ax.scatter(x, z1, color='r', label='e0')
        ax.scatter(x, z3, color='b', label='e2-1mod-fill')
        ax.scatter(x, z4, color='cyan', label='e2-2ran-fill')
    if switch == 6:
        ax.plot(x, z3, color='b')
        ax.plot(x, z4, color='cyan')
        ax.plot(x, z5, color='y')
        ax.plot(x, z6, color='black')
        ax.scatter(x, z3, color='b', label='e2-1mod-fill')
        ax.scatter(x, z4, color='cyan', label='e2-2ran-fill')
        ax.scatter(x, z5, color='y', label='e3-1mod-fill')
        ax.scatter(x, z6, color='black', label='e3-2ran-fill')
    if switch == -1:
        ax.plot(x, z1, color='r')
        ax.plot(x, z2, color='g')
        ax.plot(x, z3, color='b')
        ax.plot(x, z4, color='cyan')
        ax.plot(x, z5, color='y')
        ax.plot(x, z6, color='black')
        ax.plot(x, z7, color='m')
        ax.plot(x, z12, color='coral')
        ax.scatter(x, z1, color='r', label='e0')
        ax.scatter(x, z2, color='g', label='e1')
        ax.scatter(x, z3, color='b', label='e2-1mod-fill')
        ax.scatter(x, z4, color='cyan', label='e2-2ran-fill')
        ax.scatter(x, z5, color='y', label='e3-1mod-fill')
        ax.scatter(x, z6, color='black', label='e3-2ran-fill')
        ax.scatter(x, z7, color='m', label='e4-grc-bt-fill')
        ax.scatter(x, z12, color='coral', label='e5-grc-tb-fill')
    if switch == 7:  # un-fill
        ax.plot(x, z1, color='r')
        ax.plot(x, z2, color='g')
        ax.plot(x, z8, color='b')
        ax.plot(x, z9, color='cyan')
        ax.plot(x, z10, color='m')
        ax.plot(x, z11, color='coral')
        ax.scatter(x, z1, color='r', label='e0')
        ax.scatter(x, z2, color='g', label='e1')
        ax.scatter(x, z8, color='b', label='e2-mod')
        ax.scatter(x, z9, color='cyan', label='e3-mod')
        ax.scatter(x, z10, color='m', label='e4-grc-bt')
        ax.scatter(x, z11, color='coral', label='e5-grc-tb')
    if switch == 8:
        ax.plot(x, z7, color='m')
        ax.plot(x, z12, color='coral')
        ax.scatter(x, z7, color='m', label='e4-grc-bt-fill')
        ax.scatter(x, z12, color='coral', label='e5-grc-tb-fill')

    # 绘制图例
    ax.legend(loc='best')

    # 添加坐标轴(顺序是Z, Y, X)
    # ax.set_zlabel('Round', fontdict={'size': 15, 'color': 'red'})
    ax.set_ylabel('Round', fontdict={'size': 15, 'color': 'black'})
    ax.set_xlabel('Origin_content', fontdict={'size': 15, 'color': 'black'})

    # 展示
    plt.show()
    file_name = "../plot_res/k" + str(support) + "_compare_round_line_subgraph" + str(switch) + ".png"
    fig.savefig(file_name)


def plot_average_2_ori_cover(switch, support):
    # 绘制散点图
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plot_line = {}
    line_1 = {}
    # i0: ori_content i1: round i2: cover
    for i in data1:
        if i[0] not in plot_line:
            plot_line[i[0]] = [i[2]]
        else:
            plot_line[i[0]].append(i[2])

    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    b = [0] * 11
    for k, v in line_1.items():
        b[int(k)] = v
    # print(b)

    plot_line = {}
    line_1 = {}
    for i in data2:
        if i[0] not in plot_line:
            plot_line[i[0]] = [i[2]]
        else:
            plot_line[i[0]].append(i[2])
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    c = [0] * 11
    for k, v in line_1.items():
        c[int(k)] = v

    plot_line = {}
    line_1 = {}
    for i in data3_1:
        if i[0] not in plot_line:
            plot_line[i[0]] = [i[2]]
        else:
            plot_line[i[0]].append(i[2])
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    d = [0] * 11
    for k, v in line_1.items():
        d[int(k)] = v

    plot_line = {}
    line_1 = {}
    for i in data3_3:
        if i[0] not in plot_line:
            plot_line[i[0]] = [i[2]]
        else:
            plot_line[i[0]].append(i[2])
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    e = [0] * 11
    for k, v in line_1.items():
        e[int(k)] = v

    plot_line = {}
    line_1 = {}
    for i in data4_1:
        if i[0] not in plot_line:
            plot_line[i[0]] = [i[2]]
        else:
            plot_line[i[0]].append(i[2])
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    f = [0] * 11
    for k, v in line_1.items():
        f[int(k)] = v

    plot_line = {}
    line_1 = {}
    for i in data4_3:
        if i[0] not in plot_line:
            plot_line[i[0]] = [i[2]]
        else:
            plot_line[i[0]].append(i[2])
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    g = [0] * 11
    for k, v in line_1.items():
        g[int(k)] = v

    plot_line = {}
    line_1 = {}
    for i in data5_1:
        if i[0] not in plot_line:
            plot_line[i[0]] = [i[2]]
        else:
            plot_line[i[0]].append(i[2])
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    h = [0] * 11
    for k, v in line_1.items():
        h[int(k)] = v

    plot_line = {}
    line_1 = {}
    for i in data6_1:
        if i[0] not in plot_line:
            plot_line[i[0]] = [i[2]]
        else:
            plot_line[i[0]].append(i[2])
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    h_61 = [0] * 11
    for k, v in line_1.items():
        h_61[int(k)] = v

    x = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    z1 = b[2:]
    z2 = c[2:]
    z3 = d[2:]
    z4 = e[2:]
    z5 = f[2:]
    z6 = g[2:]
    z7 = h[2:]
    z8 = h_61[2:]

    if switch == 0:
        ax.plot(x, z1, color='r')
        ax.scatter(x, z1, color='r', label='e0')
    if switch == 1:
        ax.plot(x, z2, color='g')
        ax.scatter(x, z2, color='g', label='e1')
    if switch == 2:
        ax.plot(x, z3, color='b')
        ax.plot(x, z4, color='cyan')
        ax.scatter(x, z3, color='b', label='e2-1mod')
        ax.scatter(x, z4, color='cyan', label='e2-2ran')
    if switch == 3:
        ax.plot(x, z5, color='y')
        ax.plot(x, z6, color='black')
        ax.scatter(x, z5, color='y', label='e3-1mod')
        ax.scatter(x, z6, color='black', label='e3-2ran')
    if switch == 4:
        ax.plot(x, z7, color='m')
        ax.scatter(x, z7, color='m', label='e4-grc')
    if switch == 6:
        ax.plot(x, z8, color='m')
        ax.scatter(x, z8, color='m', label='e5-grc')
    if switch == -1:
        ax.plot(x, z1, color='r')
        ax.plot(x, z2, color='g')
        ax.plot(x, z3, color='b')
        ax.plot(x, z4, color='cyan')
        ax.plot(x, z5, color='y')
        ax.plot(x, z6, color='black')
        ax.plot(x, z7, color='m')
        ax.plot(x, z8, color='coral')
        ax.scatter(x, z1, color='r', label='e0')
        ax.scatter(x, z2, color='g', label='e1')
        ax.scatter(x, z3, color='b', label='e2-1mod')
        ax.scatter(x, z4, color='cyan', label='e2-2ran')
        ax.scatter(x, z5, color='y', label='e3-1mod')
        ax.scatter(x, z6, color='black', label='e3-2ran')
        ax.scatter(x, z7, color='m', label='e4-grc')
        ax.scatter(x, z8, color='coral', label='e5-grc')
    if switch == 5:
        ax.plot(x, z1, color='r')
        ax.plot(x, z7, color='m')
        ax.plot(x, z8, color='coral')
        ax.scatter(x, z1, color='r', label='e0')
        ax.scatter(x, z7, color='m', label='e4-grc')
        ax.scatter(x, z8, color='coral', label='e5-grc')

    # 绘制图例
    ax.legend(loc='best')

    # 添加坐标轴(顺序是Z, Y, X)
    # ax.set_zlabel('Round', fontdict={'size': 15, 'color': 'red'})
    ax.set_ylabel('Cover', fontdict={'size': 15, 'color': 'black'})
    ax.set_xlabel('Origin_content', fontdict={'size': 15, 'color': 'black'})

    # 展示
    plt.show()
    file_name = "../plot_res/k" + str(support) + "_compare_cover_line_subgraph" + str(switch) + ".png"
    fig.savefig(file_name)


def plot_delta_2_ori_cover(switch, support):
    # 绘制散点图
    fig = plt.figure()
    ax = fig.add_subplot(111)
    x_stand = [2, 3, 4, 5, 6, 7, 8, 9, 10]

    # data1 和 data2,data3_1,data4_1,
    plot_line = {}
    line_1 = {}
    statistics_1 = []
    statistics_2 = []
    statistics_3 = []
    statistics_4 = []
    statistics_5 = []
    for i in range(0, len(data1)):
        if data1[i][0] not in plot_line:
            # ori_content
            plot_line[data1[i][0]] = [data1[i][2] - data2[i][2]]
        else:
            plot_line[data1[i][0]].append(data1[i][2] - data2[i][2])
        statistics_1.append(data1[i][2] - data2[i][2])
    res_1 = []
    for j in x_stand:
        for m in plot_line[j]:
            temp = [j, m]
            res_1.append(temp)
    res_1 = np.array(res_1)
    x1 = res_1[:, 0]
    z1 = res_1[:, 1]
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    a = [0] * 11
    for k, v in line_1.items():
        a[int(k)] = v

    plot_line = {}
    for i in range(0, len(data1)):
        if data1[i][0] not in plot_line:
            # ori_content
            plot_line[data1[i][0]] = [data1[i][2] - data3_1[i][2]]
        else:
            plot_line[data1[i][0]].append(data1[i][2] - data3_1[i][2])
        statistics_2.append(data1[i][2] - data3_1[i][2])
    res_2 = []
    for j in x_stand:
        for m in plot_line[j]:
            temp = [j, m]
            res_2.append(temp)
    res_2 = np.array(res_2)
    x2 = res_2[:, 0]
    z2 = res_2[:, 1]
    line_1 = {}
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    b = [0] * 11
    for k, v in line_1.items():
        b[int(k)] = v

    plot_line = {}
    for i in range(0, len(data1)):
        if data1[i][0] not in plot_line:
            # ori_content
            plot_line[data1[i][0]] = [data1[i][2] - data4_1[i][2]]
        else:
            plot_line[data1[i][0]].append(data1[i][2] - data4_1[i][2])
        statistics_3.append(data1[i][2] - data4_1[i][2])
    res_3 = []
    for j in x_stand:
        for m in plot_line[j]:
            temp = [j, m]
            res_3.append(temp)
    res_3 = np.array(res_3)
    x3 = res_3[:, 0]
    z3 = res_3[:, 1]
    line_1 = {}
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    c = [0] * 11
    for k, v in line_1.items():
        c[int(k)] = v

    plot_line = {}
    for i in range(0, len(data1)):
        if data1[i][0] not in plot_line:
            # ori_content
            plot_line[data1[i][0]] = [data1[i][2] - data5_1[i][2]]
        else:
            plot_line[data1[i][0]].append(data1[i][2] - data5_1[i][2])
        statistics_4.append(data1[i][2] - data5_1[i][2])
    res_4 = []
    for j in x_stand:
        for m in plot_line[j]:
            temp = [j, m]
            res_4.append(temp)
    res_4 = np.array(res_4)
    x4 = res_4[:, 0]
    z4 = res_4[:, 1]
    line_1 = {}
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    d = [0] * 11
    for k, v in line_1.items():
        d[int(k)] = v

    plot_line = {}
    for i in range(0, len(data1)):
        if data1[i][0] not in plot_line:
            # ori_content
            plot_line[data1[i][0]] = [data1[i][2] - data6_1[i][2]]
        else:
            plot_line[data1[i][0]].append(data1[i][2] - data6_1[i][2])
        statistics_5.append(data1[i][2] - data6_1[i][2])
    res_5 = []
    for j in x_stand:
        for m in plot_line[j]:
            temp = [j, m]
            res_5.append(temp)
    res_5 = np.array(res_5)
    x5 = res_5[:, 0]
    z5 = res_5[:, 1]
    line_1 = {}
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    e = [0] * 11
    for k, v in line_1.items():
        e[int(k)] = v

    za = a[2:]
    zb = b[2:]
    zc = c[2:]
    zd = d[2:]
    ze = e[2:]

    p_x_1 = []
    p_y_1 = []
    p_x_2 = []
    p_y_2 = []
    p_x_3 = []
    p_y_3 = []
    p_x_4 = []
    p_y_4 = []

    for p in statistics_1:
        p = round(p, 2)
        if p not in p_x_1:
            p_x_1.append(p)
            p_y_1.append(1)
        else:
            p_y_1[p_x_1.index(p)] = p_y_1[p_x_1.index(p)] + 1
    for i in range(0, len(p_x_1)):
        for j in range(0, len(p_x_1) - i - 1):
            if p_x_1[j] > p_x_1[j + 1]:
                p_x_1[j], p_x_1[j + 1] = p_x_1[j + 1], p_x_1[j]
                p_y_1[j], p_y_1[j + 1] = p_y_1[j + 1], p_y_1[j]
    print(p_x_1)
    for p in statistics_2:
        p = round(p, 2)
        if p not in p_x_2:
            p_x_2.append(p)
            p_y_2.append(1)
        else:
            p_y_2[p_x_2.index(p)] = p_y_2[p_x_2.index(p)] + 1
    for i in range(0, len(p_x_2)):
        for j in range(0, len(p_x_2) - i - 1):
            if p_x_2[j] > p_x_2[j + 1]:
                p_x_2[j], p_x_2[j + 1] = p_x_2[j + 1], p_x_2[j]
                p_y_2[j], p_y_2[j + 1] = p_y_2[j + 1], p_y_2[j]
    for p in statistics_3:
        p = round(p, 2)
        if p not in p_x_3:
            p_x_3.append(p)
            p_y_3.append(1)
        else:
            p_y_3[p_x_3.index(p)] = p_y_3[p_x_3.index(p)] + 1
    for i in range(0, len(p_x_3)):
        for j in range(0, len(p_x_3) - i - 1):
            if p_x_3[j] > p_x_3[j + 1]:
                p_x_3[j], p_x_3[j + 1] = p_x_3[j + 1], p_x_3[j]
                p_y_3[j], p_y_3[j + 1] = p_y_3[j + 1], p_y_3[j]
    for p in statistics_4:
        p = round(p, 2)
        if p not in p_x_4:
            p_x_4.append(p)
            p_y_4.append(1)
        else:
            p_y_4[p_x_4.index(p)] = p_y_4[p_x_4.index(p)] + 1
    for i in range(0, len(p_x_4)):
        for j in range(0, len(p_x_4) - i - 1):
            if p_x_4[j] > p_x_4[j + 1]:
                p_x_4[j], p_x_4[j + 1] = p_x_4[j + 1], p_x_4[j]
                p_y_4[j], p_y_4[j + 1] = p_y_4[j + 1], p_y_4[j]
    p_x = ['0.0', '0.1', '0.11', '0.12', '0.14', '0.17', '0.2', '0.25', '0.29', '0.33']
    X = np.arange(10) + 1
    if switch == 0:
        ax.scatter(x1, z1, color='r', label=r'$\Delta e0-e1$')
        ax.scatter(x2, z2, color='g', label=r'$\Delta e0-e2$')
        ax.scatter(x3, z3, color='b', label=r'$\Delta e0-e3$')
        ax.scatter(x4, z4, color='cyan', label=r'$\Delta e0-e4$')
        ax.scatter(x5, z5, color='coral', label=r'$\Delta e0-e5$')
    elif switch == 1:
        ax.plot(x_stand, za, color='r')
        ax.plot(x_stand, zb, color='g')
        ax.plot(x_stand, zc, color='b')
        ax.plot(x_stand, zd, color='cyan')
        ax.plot(x_stand, ze, color='coral')
        ax.scatter(x_stand, za, color='r', label=r'$\Delta e0-e1$')
        ax.scatter(x_stand, zb, color='g', label=r'$\Delta e0-e2$')
        ax.scatter(x_stand, zc, color='b', label=r'$\Delta e0-e3$')
        ax.scatter(x_stand, zd, color='cyan', label=r'$\Delta e0-e4$')
        ax.scatter(x_stand, ze, color='coral', label=r'$\Delta e0-e5$')
    elif switch == 2:
        wid = 0.15
        # rects1 = plt.bar(X, p_y_1, color='r', label=r'$\Delta e0-e1$', width=wid)
        rects2 = plt.bar(X, p_y_2, color='g', label=r'$\Delta e0-e2$', width=wid)
        # rects3 = plt.bar(X+wid*2, p_y_3, color='b', label=r'$\Delta e0-e3$', width=wid)
        rects4 = plt.bar(X + wid, p_y_4, color='cyan', label=r'$\Delta e0-e4$', width=wid)
        # autolabel(rects1)
        autolabel(rects2)
        # autolabel(rects3)
        autolabel(rects4)
        plt.xticks(X, p_x)
        ax.set_ylabel("k", fontdict={'size': 15, 'color': 'black'})

    # 绘制图例
    ax.legend(loc='best')

    # 添加坐标轴(顺序是Z, Y, X)
    # ax.set_zlabel('Round', fontdict={'size': 15, 'color': 'red'})
    # ax.set_ylabel(r'$\Delta_{Cover}$', fontdict={'size': 15, 'color': 'black'})
    # ax.set_xlabel('Origin_content', fontdict={'size': 15, 'color': 'black'})

    # 展示
    plt.show()
    file_name = "../plot_res/k" + str(support) + "_compare_delta_cover_subgraph" + str(switch) + ".png"
    fig.savefig(file_name)


def plot_delta_2_ori_round(switch, support):
    # 绘制散点图
    fig = plt.figure()
    ax = fig.add_subplot(111)
    x_stand = [2, 3, 4, 5, 6, 7, 8, 9, 10]

    # data1 和 data2,data3_2,data4_2,5-2
    plot_line = {}
    line_1 = {}
    statistics_1 = []
    statistics_2 = []
    statistics_3 = []
    statistics_4 = []
    statistics_5 = []
    for i in range(0, len(data1)):
        if data1[i][0] not in plot_line:
            # ori_content
            plot_line[data1[i][0]] = [data1[i][1] - data2[i][1]]
        else:
            plot_line[data1[i][0]].append(data1[i][1] - data2[i][1])
        statistics_1.append(data1[i][1] - data2[i][1])
    res_1 = []
    for j in x_stand:
        for m in plot_line[j]:
            temp = [j, m]
            res_1.append(temp)
    res_1 = np.array(res_1)
    x1 = res_1[:, 0]
    z1 = res_1[:, 1]
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    a = [0] * 11
    for k, v in line_1.items():
        a[int(k)] = v

    plot_line = {}
    for i in range(0, len(data1)):
        if data1[i][0] not in plot_line:
            # ori_content
            plot_line[data1[i][0]] = [data1[i][1] - data3_2[i][1]]
        else:
            plot_line[data1[i][0]].append(data1[i][1] - data3_2[i][1])
        statistics_2.append(data1[i][1] - data3_2[i][1])
    res_2 = []
    for j in x_stand:
        for m in plot_line[j]:
            temp = [j, m]
            res_2.append(temp)
    res_2 = np.array(res_2)
    x2 = res_2[:, 0]
    z2 = res_2[:, 1]
    line_1 = {}
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    b = [0] * 11
    for k, v in line_1.items():
        b[int(k)] = v

    plot_line = {}
    for i in range(0, len(data1)):
        if data1[i][0] not in plot_line:
            # ori_content
            plot_line[data1[i][0]] = [data1[i][1] - data4_2[i][1]]
        else:
            plot_line[data1[i][0]].append(data1[i][1] - data4_2[i][1])
        statistics_3.append(data1[i][1] - data4_2[i][1])
    res_3 = []
    for j in x_stand:
        for m in plot_line[j]:
            temp = [j, m]
            res_3.append(temp)
    res_3 = np.array(res_3)
    x3 = res_3[:, 0]
    z3 = res_3[:, 1]
    line_1 = {}
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    c = [0] * 11
    for k, v in line_1.items():
        c[int(k)] = v

    plot_line = {}
    for i in range(0, len(data1)):
        if data1[i][0] not in plot_line:
            # ori_content
            plot_line[data1[i][0]] = [data1[i][1] - data5_2[i][1]]
        else:
            plot_line[data1[i][0]].append(data1[i][1] - data5_2[i][1])
        statistics_4.append(data1[i][1] - data5_2[i][1])
    res_4 = []
    for j in x_stand:
        for m in plot_line[j]:
            temp = [j, m]
            res_4.append(temp)
    res_4 = np.array(res_4)
    x4 = res_4[:, 0]
    z4 = res_4[:, 1]
    line_1 = {}
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    d = [0] * 11
    for k, v in line_1.items():
        d[int(k)] = v

    plot_line = {}
    for i in range(0, len(data1)):
        if data1[i][0] not in plot_line:
            # ori_content
            plot_line[data1[i][0]] = [data1[i][1] - data6_2[i][1]]
        else:
            plot_line[data1[i][0]].append(data1[i][1] - data6_2[i][1])
        statistics_5.append(data1[i][1] - data6_2[i][1])
    res_5 = []
    for j in x_stand:
        for m in plot_line[j]:
            temp = [j, m]
            res_5.append(temp)
    res_5 = np.array(res_5)
    x5 = res_5[:, 0]
    z5 = res_5[:, 1]
    line_1 = {}
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    e = [0] * 11
    for k, v in line_1.items():
        e[int(k)] = v

    za = a[2:]
    zb = b[2:]
    zc = c[2:]
    zd = d[2:]
    ze = e[2:]

    p_x_1 = []
    p_y_1 = []
    p_x_2 = []
    p_y_2 = []
    p_x_3 = []
    p_y_3 = []
    p_x_4 = []
    p_y_4 = []

    for p in statistics_1:
        if p not in p_x_1:
            p_x_1.append(p)
            p_y_1.append(1)
        else:
            p_y_1[p_x_1.index(p)] = p_y_1[p_x_1.index(p)] + 1
    for i in range(0, len(p_x_1)):
        for j in range(0, len(p_x_1) - i - 1):
            if p_x_1[j] > p_x_1[j + 1]:
                p_x_1[j], p_x_1[j + 1] = p_x_1[j + 1], p_x_1[j]
                p_y_1[j], p_y_1[j + 1] = p_y_1[j + 1], p_y_1[j]
    print(p_x_1)
    for p in statistics_2:

        if p not in p_x_2:
            p_x_2.append(p)
            p_y_2.append(1)
        else:
            p_y_2[p_x_2.index(p)] = p_y_2[p_x_2.index(p)] + 1
    for i in range(0, len(p_x_2)):
        for j in range(0, len(p_x_2) - i - 1):
            if p_x_2[j] > p_x_2[j + 1]:
                p_x_2[j], p_x_2[j + 1] = p_x_2[j + 1], p_x_2[j]
                p_y_2[j], p_y_2[j + 1] = p_y_2[j + 1], p_y_2[j]
    for p in statistics_3:

        if p not in p_x_3:
            p_x_3.append(p)
            p_y_3.append(1)
        else:
            p_y_3[p_x_3.index(p)] = p_y_3[p_x_3.index(p)] + 1
    for i in range(0, len(p_x_3)):
        for j in range(0, len(p_x_3) - i - 1):
            if p_x_3[j] > p_x_3[j + 1]:
                p_x_3[j], p_x_3[j + 1] = p_x_3[j + 1], p_x_3[j]
                p_y_3[j], p_y_3[j + 1] = p_y_3[j + 1], p_y_3[j]
    for p in statistics_4:
        if p not in p_x_4:
            p_x_4.append(p)
            p_y_4.append(1)
        else:
            p_y_4[p_x_4.index(p)] = p_y_4[p_x_4.index(p)] + 1
    for i in range(0, len(p_x_4)):
        for j in range(0, len(p_x_4) - i - 1):
            if p_x_4[j] > p_x_4[j + 1]:
                p_x_4[j], p_x_4[j + 1] = p_x_4[j + 1], p_x_4[j]
                p_y_4[j], p_y_4[j + 1] = p_y_4[j + 1], p_y_4[j]
    print(p_x_2)
    print(p_x_3)
    print(p_x_4)
    p_x = ['-8.0', '1.0', '2.0']
    X = np.arange(30) + 1
    if switch == 0:
        ax.scatter(x1, z1, color='r', label=r'$\Delta e0-e1$')
        ax.scatter(x2, z2, color='g', label=r'$\Delta e0-e2$')
        ax.scatter(x3, z3, color='b', label=r'$\Delta e0-e3$')
        ax.scatter(x4, z4, color='cyan', label=r'$\Delta e0-e4$')
        ax.scatter(x5, z5, color='coral', label=r'$\Delta e0-e5$')
    elif switch == 1:
        ax.plot(x_stand, za, color='r')
        ax.plot(x_stand, zb, color='g')
        ax.plot(x_stand, zc, color='b')
        ax.plot(x_stand, zd, color='cyan')
        ax.plot(x_stand, ze, color='coral')
        ax.scatter(x_stand, za, color='r', label=r'$\Delta e0-e1$')
        ax.scatter(x_stand, zb, color='g', label=r'$\Delta e0-e2$')
        ax.scatter(x_stand, zc, color='b', label=r'$\Delta e0-e3$')
        ax.scatter(x_stand, zd, color='cyan', label=r'$\Delta e0-e4$')
        ax.scatter(x_stand, ze, color='coral', label=r'$\Delta e0-e5$')
    elif switch == 2:
        wid = 0.15
        rects1 = plt.bar(X, p_y_1, color='r', label=r'$\Delta e0-e1$', width=wid)
        rects2 = plt.bar(X + wid, p_y_2, color='g', label=r'$\Delta e0-e2$', width=wid)
        rects3 = plt.bar(X + wid * 2, p_y_3, color='b', label=r'$\Delta e0-e3$', width=wid)
        rects4 = plt.bar(X + wid * 3, p_y_4, color='cyan', label=r'$\Delta e0-e4$', width=wid)
        # autolabel(rects1)
        # autolabel(rects2)
        # autolabel(rects3)
        # autolabel(rects4)
        ax.set_xlabel(r'$\Delta_{round}$', fontdict={'size': 15, 'color': 'black'})
        ax.set_ylabel("k", fontdict={'size': 15, 'color': 'black'})

    # 绘制图例
    ax.legend(loc='best')

    # 添加坐标轴(顺序是Z, Y, X)
    # ax.set_zlabel('Round', fontdict={'size': 15, 'color': 'red'})
    ax.set_ylabel(r'$\Delta_{round}$', fontdict={'size': 15, 'color': 'black'})
    ax.set_xlabel('Origin_content', fontdict={'size': 15, 'color': 'black'})

    # 展示
    plt.show()
    file_name = "../plot_res/k" + str(support) + "_compare_delta_round_subgraph" + str(switch) + ".png"
    fig.savefig(file_name)


def sort_order(array_a, array_b):
    for i in range(len(array_a) - 1):
        for j in range(len(array_a) - i - 1):
            if array_a[j] > array_a[j + 1]:
                array_a[j], array_a[j + 1] = array_a[j + 1], array_a[j]
                array_b[j], array_b[j + 1] = array_b[j + 1], array_b[j]

    return array_a, array_b


def plot_delta_ycover_xround(switch, support):
    # 绘制散点图
    fig = plt.figure()
    ax = fig.add_subplot(111)
    x_stand = [2, 3, 4, 5, 6, 7, 8, 9, 10]

    # data1 和 data2,data3_2,data4_2,5-2,6-2
    plot_line = {}
    line_1 = {}

    for i in range(0, len(data1)):
        if (data1[i][1] - data2[i][1]) not in plot_line:
            # ori_content
            plot_line[data1[i][1] - data2[i][1]] = [data1[i][2] - data2[i][2]]
        else:
            plot_line[data1[i][1] - data2[i][1]].append(data1[i][2] - data2[i][2])
    res_1 = []
    for j in plot_line:
        for m in plot_line[j]:
            temp = [j, m]
            res_1.append(temp)
    res_1 = np.array(res_1)
    x1 = res_1[:, 0]
    z1 = res_1[:, 1]
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    x_c = []
    y_c = []
    for p, q in line_1.items():
        x_c.append(p)
        y_c.append(q)

    plot_line = {}
    line_1 = {}
    for i in range(0, len(data1)):
        if (data1[i][1] - data3_2[i][1]) not in plot_line:
            plot_line[data1[i][1] - data3_2[i][1]] = [data1[i][2] - data3_1[i][2]]
        else:
            plot_line[data1[i][1] - data3_2[i][1]].append(data1[i][2] - data3_1[i][2])
    res_1 = []
    for j in plot_line:
        for m in plot_line[j]:
            temp = [j, m]
            res_1.append(temp)
    res_1 = np.array(res_1)
    x2_1 = res_1[:, 0]
    z2_1 = res_1[:, 1]
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    x_d = []
    y_d = []
    for p, q in line_1.items():
        x_d.append(p)
        y_d.append(q)

    plot_line = {}
    line_1 = {}
    for i in range(0, len(data1)):
        if (data1[i][1] - data4_2[i][1]) not in plot_line:
            plot_line[data1[i][1] - data4_2[i][1]] = [data1[i][2] - data4_1[i][2]]
        else:
            plot_line[data1[i][1] - data4_2[i][1]].append(data1[i][2] - data4_1[i][2])
    res_1 = []
    for j in plot_line:
        for m in plot_line[j]:
            temp = [j, m]
            res_1.append(temp)
    res_1 = np.array(res_1)
    r3_1 = res_1[:, 0]
    c3_1 = res_1[:, 1]
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    x_e = []
    y_e = []
    for p, q in line_1.items():
        x_e.append(p)
        y_e.append(q)

    plot_line = {}
    line_1 = {}
    for i in range(0, len(data1)):
        if (data1[i][1] - data5_2[i][1]) not in plot_line:
            plot_line[data1[i][1] - data5_2[i][1]] = [data1[i][2] - data5_1[i][2]]
        else:
            plot_line[data1[i][1] - data5_2[i][1]].append(data1[i][2] - data5_1[i][2])
    res_1 = []
    for j in plot_line:
        for m in plot_line[j]:
            temp = [j, m]
            res_1.append(temp)
    res_1 = np.array(res_1)
    r4_1 = res_1[:, 0]
    c4_1 = res_1[:, 1]
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    x_f = []
    y_f = []
    for p, q in line_1.items():
        x_f.append(p)
        y_f.append(q)

    plot_line = {}
    line_1 = {}
    for i in range(0, len(data1)):
        if (data1[i][1] - data6_2[i][1]) not in plot_line:
            plot_line[data1[i][1] - data6_2[i][1]] = [data1[i][2] - data6_1[i][2]]
        else:
            plot_line[data1[i][1] - data6_2[i][1]].append(data1[i][2] - data6_1[i][2])
    res_1 = []
    for j in plot_line:
        for m in plot_line[j]:
            temp = [j, m]
            res_1.append(temp)
    res_1 = np.array(res_1)
    r5_1 = res_1[:, 0]
    c5_1 = res_1[:, 1]
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    x_g = []
    y_g = []
    for p, q in line_1.items():
        x_g.append(p)
        y_g.append(q)

    x_c, y_c = sort_order(x_c, y_c)
    x_d, y_d = sort_order(x_d, y_d)
    x_e, y_e = sort_order(x_e, y_e)
    x_f, y_f = sort_order(x_f, y_f)
    x_g, y_g = sort_order(x_g, y_g)

    if switch == 0:
        ax.scatter(x1, z1, color='r', label=r'$\Delta e0-e1$')
        ax.scatter(x2_1, z2_1, color='g', label=r'$\Delta e0-e2$')
        ax.scatter(r3_1, c3_1, color='b', label=r'$\Delta e0-e3$')
        ax.scatter(r4_1, c4_1, color='cyan', label=r'$\Delta e0-e4$')
        ax.scatter(r5_1, c5_1, color='coral', label=r'$\Delta e0-e5$')
    elif switch == 1:
        ax.plot(x_c, y_c, color='r')
        ax.plot(x_d, y_d, color='g')
        ax.plot(x_e, y_e, color='b')
        ax.plot(x_f, y_f, color='cyan')
        ax.plot(x_g, y_g, color='coral')
        ax.scatter(x_c, y_c, color='r', label=r'$\Delta e0-e1$')
        ax.scatter(x_d, y_d, color='g', label=r'$\Delta e0-e2$')
        ax.scatter(x_e, y_e, color='b', label=r'$\Delta e0-e3$')
        ax.scatter(x_f, y_f, color='cyan', label=r'$\Delta e0-e4$')
        ax.scatter(x_g, y_g, color='coral', label=r'$\Delta e0-e5$')

    # 绘制图例
    ax.legend(loc='best')

    # 添加坐标轴(顺序是Z, Y, X)
    # ax.set_zlabel('Round', fontdict={'size': 15, 'color': 'red'})
    ax.set_ylabel(r'$\Delta_{cover}$', fontdict={'size': 15, 'color': 'black'})
    ax.set_xlabel(r'$\Delta_{round}$', fontdict={'size': 15, 'color': 'black'})

    # 展示
    plt.show()
    file_name = "../plot_res/k" + str(support) + "_delta_ycover_xround_" + str(switch) + ".png"
    fig.savefig(file_name)


def plot_delta_yround_xcover(switch, support):
    # 绘制散点图
    fig = plt.figure()
    ax = fig.add_subplot(111)
    x_stand = [2, 3, 4, 5, 6, 7, 8, 9, 10]

    # data1 和 data2,data3_2,data4_2,5-2,6-2
    plot_line = {}
    line_1 = {}

    for i in range(0, len(data1)):
        if (data1[i][2] - data2[i][2]) not in plot_line:
            # ori_content
            plot_line[data1[i][2] - data2[i][2]] = [data1[i][1] - data2[i][1]]
        else:
            plot_line[data1[i][2] - data2[i][2]].append(data1[i][1] - data2[i][1])
    res_1 = []
    for j in plot_line:
        for m in plot_line[j]:
            temp = [j, m]
            res_1.append(temp)
    res_1 = np.array(res_1)
    x1 = res_1[:, 0]
    z1 = res_1[:, 1]
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    x_c = []
    y_c = []
    for p, q in line_1.items():
        x_c.append(p)
        y_c.append(q)

    plot_line = {}
    line_1 = {}
    for i in range(0, len(data1)):
        if (data1[i][2] - data3_1[i][2]) not in plot_line:
            plot_line[data1[i][2] - data3_1[i][2]] = [data1[i][1] - data3_2[i][1]]
        else:
            plot_line[data1[i][2] - data3_1[i][2]].append(data1[i][1] - data3_2[i][1])
    res_1 = []
    for j in plot_line:
        for m in plot_line[j]:
            temp = [j, m]
            res_1.append(temp)
    res_1 = np.array(res_1)
    x2_1 = res_1[:, 0]
    z2_1 = res_1[:, 1]
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    x_d = []
    y_d = []
    for p, q in line_1.items():
        x_d.append(p)
        y_d.append(q)

    plot_line = {}
    line_1 = {}
    for i in range(0, len(data1)):
        if (data1[i][2] - data4_1[i][2]) not in plot_line:
            plot_line[data1[i][2] - data4_1[i][2]] = [data1[i][1] - data4_2[i][1]]
        else:
            plot_line[data1[i][2] - data4_1[i][2]].append(data1[i][1] - data4_2[i][1])
    res_1 = []
    for j in plot_line:
        for m in plot_line[j]:
            temp = [j, m]
            res_1.append(temp)
    res_1 = np.array(res_1)
    r3_1 = res_1[:, 0]
    c3_1 = res_1[:, 1]
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    x_e = []
    y_e = []
    for p, q in line_1.items():
        x_e.append(p)
        y_e.append(q)

    plot_line = {}
    line_1 = {}
    for i in range(0, len(data1)):
        if (data1[i][2] - data5_1[i][2]) not in plot_line:
            plot_line[data1[i][2] - data5_1[i][2]] = [data1[i][1] - data5_2[i][1]]
        else:
            plot_line[data1[i][2] - data5_1[i][2]].append(data1[i][1] - data5_2[i][1])
    res_1 = []
    for j in plot_line:
        for m in plot_line[j]:
            temp = [j, m]
            res_1.append(temp)
    res_1 = np.array(res_1)
    r4_1 = res_1[:, 0]
    c4_1 = res_1[:, 1]
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    x_f = []
    y_f = []
    for p, q in line_1.items():
        x_f.append(p)
        y_f.append(q)

    plot_line = {}
    line_1 = {}
    for i in range(0, len(data1)):
        if (data1[i][2] - data6_2[i][2]) not in plot_line:
            plot_line[data1[i][2] - data6_1[i][2]] = [data1[i][1] - data6_2[i][1]]
        else:
            plot_line[data1[i][2] - data6_1[i][2]].append(data1[i][1] - data6_2[i][1])
    res_1 = []
    for j in plot_line:
        for m in plot_line[j]:
            temp = [j, m]
            res_1.append(temp)
    res_1 = np.array(res_1)
    r5_1 = res_1[:, 0]
    c5_1 = res_1[:, 1]
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    x_g = []
    y_g = []
    for p, q in line_1.items():
        x_g.append(p)
        y_g.append(q)

    x_c, y_c = sort_order(x_c, y_c)
    x_d, y_d = sort_order(x_d, y_d)
    x_e, y_e = sort_order(x_e, y_e)
    x_f, y_f = sort_order(x_f, y_f)
    x_g, y_g = sort_order(x_g, y_g)

    if switch == 0:
        ax.scatter(x1, z1, color='r', label=r'$\Delta e0-e1$')
        ax.scatter(x2_1, z2_1, color='g', label=r'$\Delta e0-e2$')
        ax.scatter(r3_1, c3_1, color='b', label=r'$\Delta e0-e3$')
        ax.scatter(r4_1, c4_1, color='cyan', label=r'$\Delta e0-e4$')
        ax.scatter(r5_1, c5_1, color='coral', label=r'$\Delta e0-e5$')
    elif switch == 1:
        ax.plot(x_c, y_c, color='r')
        ax.plot(x_d, y_d, color='g')
        ax.plot(x_e, y_e, color='b')
        ax.plot(x_f, y_f, color='cyan')
        ax.plot(x_g, y_g, color='coral')
        ax.scatter(x_c, y_c, color='r', label=r'$\Delta e0-e1$')
        ax.scatter(x_d, y_d, color='g', label=r'$\Delta e0-e2$')
        ax.scatter(x_e, y_e, color='b', label=r'$\Delta e0-e3$')
        ax.scatter(x_f, y_f, color='cyan', label=r'$\Delta e0-e4$')
        ax.scatter(x_g, y_g, color='coral', label=r'$\Delta e0-e5$')

    # 绘制图例
    ax.legend(loc='best')

    # 添加坐标轴(顺序是Z, Y, X)
    # ax.set_zlabel('Round', fontdict={'size': 15, 'color': 'red'})
    ax.set_ylabel(r'$\Delta_{round}$', fontdict={'size': 15, 'color': 'black'})
    ax.set_xlabel(r'$\Delta_{cover}$', fontdict={'size': 15, 'color': 'black'})

    # 展示
    plt.show()
    file_name = "../plot_res/k" + str(support) + "_delta_yround_xcover" + str(switch) + ".png"
    fig.savefig(file_name)

# for i in range(1, 7):
#     plot_graph_2_ori_round(i)
#     plot_graph_3(i)
# plot_average_2_ori_round(1)
# plot_average_2_ori_cover(1)


variable = 2
# plot_graph_2_ori_cover(variable)
# plot_average_2_ori_cover(-1, variable)
plot_average_2_ori_cover(0, variable)
# plot_average_2_ori_cover(1, variable)
# plot_average_2_ori_cover(2, variable)
# plot_average_2_ori_cover(3, variable)
# plot_average_2_ori_cover(4, variable)
# plot_average_2_ori_cover(5, variable)
# plot_average_2_ori_cover(6, variable)
#
# plot_graph_2_ori_round(variable)
# plot_average_2_ori_round(0, variable)
# plot_average_2_ori_round(1, variable)
# plot_average_2_ori_round(2, variable)
# plot_average_2_ori_round(3, variable)
# plot_average_2_ori_round(4, variable)
# plot_average_2_ori_round(5, variable)
# plot_average_2_ori_round(6, variable)
# plot_average_2_ori_round(-1, variable)
# plot_average_2_ori_round(7, variable)
# plot_average_2_ori_round(8, variable)
#
# plot_delta_2_ori_cover(0, variable)
# plot_delta_2_ori_cover(1, variable)
# # plot_delta_2_ori_cover(2)
#
# plot_delta_2_ori_round(0, variable)
# plot_delta_2_ori_round(1, variable)
# # # plot_delta_2_ori_round(2)
#
# plot_delta_ycover_xround(0, variable)
# plot_delta_ycover_xround(1, variable)
# plot_delta_yround_xcover(0, variable)
# plot_delta_yround_xcover(1, variable)


def plot_average_k_ori_round(switch, experiment):
    # 绘制散点图
    fig = plt.figure()
    ax = fig.add_subplot(111)

    # mode * 4  1-mod 2-mod_fill 3-ran 4-ran_fill
    datae2_2 = get_data(experiment, 2, 2)
    datae2_2 = np.array(datae2_2)
    xe2_2 = datae2_2[:, 0]
    ye2_2 = datae2_2[:, 1]
    ze2_2 = datae2_2[:, 2]

    # mode * 4  1-mod 2-mod_fill 3-ran 4-ran_fill
    datae2_3 = get_data(experiment, 3, 2)
    datae2_3 = np.array(datae2_3)
    xe2_3 = datae2_3[:, 0]
    ye2_3 = datae2_3[:, 1]
    ze2_3 = datae2_3[:, 2]

    # mode * 4  1-mod 2-mod_fill 3-ran 4-ran_fill
    datae2_4 = get_data(experiment, 4, 2)
    datae2_4 = np.array(datae2_4)
    xe2_4 = datae2_4[:, 0]
    ye2_4 = datae2_4[:, 1]
    ze2_4 = datae2_4[:, 2]

    # mode * 4  1-mod 2-mod_fill 3-ran 4-ran_fill
    datae2_5 = get_data(experiment, 5, 2)
    datae2_5 = np.array(datae2_5)
    xe2_5 = datae2_5[:, 0]
    ye2_5 = datae2_5[:, 1]
    ze2_5 = datae2_5[:, 2]

    # mode * 4  1-mod 2-mod_fill 3-ran 4-ran_fill
    datae2_6 = get_data(experiment, 6, 2)
    datae2_6 = np.array(datae2_6)
    xe2_6 = datae2_6[:, 0]
    ye2_6 = datae2_6[:, 1]
    ze2_6 = datae2_6[:, 2]

    plot_line = {}
    line_1 = {}
    # i0: ori_content i1: round i2: cover
    for i in data1:
        if i[0] not in plot_line:
            plot_line[i[0]] = [i[1]]
        else:
            plot_line[i[0]].append(i[1])
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num

    b = [0] * 11
    for k, v in line_1.items():
        b[int(k)] = v

    plot_line = {}
    line_1 = {}
    for i in data2:
        if i[0] not in plot_line:
            plot_line[i[0]] = [i[1]]
        else:
            plot_line[i[0]].append(i[1])
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    c = [0] * 11
    for k, v in line_1.items():
        c[int(k)] = v

    plot_line = {}
    line_1 = {}
    for i in datae2_2:
        if i[0] not in plot_line:
            plot_line[i[0]] = [i[1]]
        else:
            plot_line[i[0]].append(i[1])
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    d = [0] * 11
    for k, v in line_1.items():
        d[int(k)] = v

    plot_line = {}
    line_1 = {}
    for i in datae2_3:
        if i[0] not in plot_line:
            plot_line[i[0]] = [i[1]]
        else:
            plot_line[i[0]].append(i[1])
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    e = [0] * 11
    for k, v in line_1.items():
        e[int(k)] = v

    plot_line = {}
    line_1 = {}
    for i in datae2_4:
        if i[0] not in plot_line:
            plot_line[i[0]] = [i[1]]
        else:
            plot_line[i[0]].append(i[1])
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    f = [0] * 11
    for k, v in line_1.items():
        f[int(k)] = v

    plot_line = {}
    line_1 = {}
    for i in datae2_5:
        if i[0] not in plot_line:
            plot_line[i[0]] = [i[1]]
        else:
            plot_line[i[0]].append(i[1])
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    g = [0] * 11
    for k, v in line_1.items():
        g[int(k)] = v

    plot_line = {}
    line_1 = {}
    for i in datae2_6:
        if i[0] not in plot_line:
            plot_line[i[0]] = [i[1]]
        else:
            plot_line[i[0]].append(i[1])
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    h = [0] * 11
    for k, v in line_1.items():
        h[int(k)] = v

    x = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    z1 = b[2:]
    z2 = c[2:]
    z3 = d[2:]
    z4 = e[2:]
    z5 = f[2:]
    z6 = g[2:]
    z7 = h[2:]

    if switch == 0:
        ax.plot(x, z1, color='r')
        ax.scatter(x, z1, color='r', label='e0')
        ax.plot(x, z2, color='g')
        ax.scatter(x, z2, color='g', label='e1')
        ax.plot(x, z3, color='b')
        ax.plot(x, z4, color='cyan')
        ax.scatter(x, z3, color='b', label='k2')
        ax.scatter(x, z4, color='cyan', label='k3')
        ax.plot(x, z5, color='y')
        ax.plot(x, z6, color='black')
        ax.scatter(x, z5, color='y', label='k4')
        ax.scatter(x, z6, color='black', label='k5')
        ax.plot(x, z7, color='m')
        ax.scatter(x, z7, color='m', label='k6')
    if switch == 1:
        ax.plot(x, z3, color='b')
        ax.plot(x, z4, color='cyan')
        ax.scatter(x, z3, color='b', label='k2')
        ax.scatter(x, z4, color='cyan', label='k3')
        ax.plot(x, z5, color='y')
        ax.plot(x, z6, color='black')
        ax.scatter(x, z5, color='y', label='k4')
        ax.scatter(x, z6, color='black', label='k5')
        ax.plot(x, z7, color='m')
        ax.scatter(x, z7, color='m', label='k6')


    # 绘制图例
    ax.legend(loc='best')

    # 添加坐标轴(顺序是Z, Y, X)
    # ax.set_zlabel('Round', fontdict={'size': 15, 'color': 'red'})
    ax.set_ylabel('Round', fontdict={'size': 15, 'color': 'black'})
    ax.set_xlabel('Origin_content', fontdict={'size': 15, 'color': 'black'})

    # 展示
    plt.show()
    file_name = "../plot_res/e" + str(experiment) + "_round_subgraph" + str(switch) + ".png"
    fig.savefig(file_name)


def plot_average_k_ori_cover(switch, experiment):
    # 绘制散点图
    fig = plt.figure()
    ax = fig.add_subplot(111)

    # mode * 4  1-mod 2-mod_fill 3-ran 4-ran_fill
    datae2_2 = get_data(experiment, 2, 1)
    datae2_2 = np.array(datae2_2)
    xe2_2 = datae2_2[:, 0]
    ye2_2 = datae2_2[:, 1]
    ze2_2 = datae2_2[:, 2]

    # mode * 4  1-mod 2-mod_fill 3-ran 4-ran_fill
    datae2_3 = get_data(experiment, 3, 1)
    datae2_3 = np.array(datae2_3)
    xe2_3 = datae2_3[:, 0]
    ye2_3 = datae2_3[:, 1]
    ze2_3 = datae2_3[:, 2]

    # mode * 4  1-mod 2-mod_fill 3-ran 4-ran_fill
    datae2_4 = get_data(experiment, 4, 1)
    datae2_4 = np.array(datae2_4)
    xe2_4 = datae2_4[:, 0]
    ye2_4 = datae2_4[:, 1]
    ze2_4 = datae2_4[:, 2]

    # mode * 4  1-mod 2-mod_fill 3-ran 4-ran_fill
    datae2_5 = get_data(experiment, 5, 1)
    datae2_5 = np.array(datae2_5)
    xe2_5 = datae2_5[:, 0]
    ye2_5 = datae2_5[:, 1]
    ze2_5 = datae2_5[:, 2]

    # mode * 4  1-mod 2-mod_fill 3-ran 4-ran_fill
    datae2_6 = get_data(experiment, 6, 1)
    datae2_6 = np.array(datae2_6)
    xe2_6 = datae2_6[:, 0]
    ye2_6 = datae2_6[:, 1]
    ze2_6 = datae2_6[:, 2]

    plot_line = {}
    line_1 = {}
    # i0: ori_content i1: round i2: cover
    for i in data1:
        if i[0] not in plot_line:
            plot_line[i[0]] = [i[2]]
        else:
            plot_line[i[0]].append(i[2])
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num

    b = [0] * 11
    for k, v in line_1.items():
        b[int(k)] = v

    plot_line = {}
    line_1 = {}
    for i in data2:
        if i[0] not in plot_line:
            plot_line[i[0]] = [i[2]]
        else:
            plot_line[i[0]].append(i[2])
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    c = [0] * 11
    for k, v in line_1.items():
        c[int(k)] = v

    plot_line = {}
    line_1 = {}
    for i in datae2_2:
        if i[0] not in plot_line:
            plot_line[i[0]] = [i[2]]
        else:
            plot_line[i[0]].append(i[2])
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    d = [0] * 11
    for k, v in line_1.items():
        d[int(k)] = v

    plot_line = {}
    line_1 = {}
    for i in datae2_3:
        if i[0] not in plot_line:
            plot_line[i[0]] = [i[2]]
        else:
            plot_line[i[0]].append(i[2])
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    e = [0] * 11
    for k, v in line_1.items():
        e[int(k)] = v

    plot_line = {}
    line_1 = {}
    for i in datae2_4:
        if i[0] not in plot_line:
            plot_line[i[0]] = [i[2]]
        else:
            plot_line[i[0]].append(i[2])
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    f = [0] * 11
    for k, v in line_1.items():
        f[int(k)] = v

    plot_line = {}
    line_1 = {}
    for i in datae2_5:
        if i[0] not in plot_line:
            plot_line[i[0]] = [i[2]]
        else:
            plot_line[i[0]].append(i[2])
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    g = [0] * 11
    for k, v in line_1.items():
        g[int(k)] = v

    plot_line = {}
    line_1 = {}
    for i in datae2_6:
        if i[0] not in plot_line:
            plot_line[i[0]] = [i[2]]
        else:
            plot_line[i[0]].append(i[2])
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    h = [0] * 11
    for k, v in line_1.items():
        h[int(k)] = v

    x = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    z1 = b[2:]
    z2 = c[2:]
    z3 = d[2:]
    z4 = e[2:]
    z5 = f[2:]
    z6 = g[2:]
    z7 = h[2:]

    if switch == 0:
        ax.plot(x, z1, color='r')
        ax.scatter(x, z1, color='r', label='e0')
        ax.plot(x, z2, color='g')
        ax.scatter(x, z2, color='g', label='e1')
        ax.plot(x, z3, color='b')
        ax.plot(x, z4, color='cyan')
        ax.scatter(x, z3, color='b', label='k2')
        ax.scatter(x, z4, color='cyan', label='k3')
        ax.plot(x, z5, color='y')
        ax.plot(x, z6, color='black')
        ax.scatter(x, z5, color='y', label='k4')
        ax.scatter(x, z6, color='black', label='k5')
        ax.plot(x, z7, color='m')
        ax.scatter(x, z7, color='m', label='k6')
    if switch == 1:
        ax.plot(x, z3, color='b')
        ax.plot(x, z4, color='cyan')
        ax.scatter(x, z3, color='b', label='k2')
        ax.scatter(x, z4, color='cyan', label='k3')
        ax.plot(x, z5, color='y')
        ax.plot(x, z6, color='black')
        ax.scatter(x, z5, color='y', label='k4')
        ax.scatter(x, z6, color='black', label='k5')
        ax.plot(x, z7, color='m')
        ax.scatter(x, z7, color='m', label='k6')


    # 绘制图例
    ax.legend(loc='best')

    # 添加坐标轴(顺序是Z, Y, X)
    # ax.set_zlabel('Round', fontdict={'size': 15, 'color': 'red'})
    ax.set_ylabel('Cover', fontdict={'size': 15, 'color': 'black'})
    ax.set_xlabel('Origin_content', fontdict={'size': 15, 'color': 'black'})

    # 展示
    plt.show()
    file_name = "../plot_res/e" + str(experiment) + "_cover_subgraph" + str(switch) + ".png"
    fig.savefig(file_name)


def plot_delta_k_ori_round(switch, experiment):
    # 绘制散点图
    fig = plt.figure()
    ax = fig.add_subplot(111)
    x_stand = [2, 3, 4, 5, 6, 7, 8, 9, 10]

    # mode * 4  1-mod 2-mod_fill 3-ran 4-ran_fill
    datae2_2 = get_data(experiment, 2, 2)
    datae2_2 = np.array(datae2_2)
    xe2_2 = datae2_2[:, 0]
    ye2_2 = datae2_2[:, 1]
    ze2_2 = datae2_2[:, 2]

    # mode * 4  1-mod 2-mod_fill 3-ran 4-ran_fill
    datae2_3 = get_data(experiment, 3, 2)
    datae2_3 = np.array(datae2_3)
    xe2_3 = datae2_3[:, 0]
    ye2_3 = datae2_3[:, 1]
    ze2_3 = datae2_3[:, 2]

    # mode * 4  1-mod 2-mod_fill 3-ran 4-ran_fill
    datae2_4 = get_data(experiment, 4, 2)
    datae2_4 = np.array(datae2_4)
    xe2_4 = datae2_4[:, 0]
    ye2_4 = datae2_4[:, 1]
    ze2_4 = datae2_4[:, 2]

    # mode * 4  1-mod 2-mod_fill 3-ran 4-ran_fill
    datae2_5 = get_data(experiment, 5, 2)
    datae2_5 = np.array(datae2_5)
    xe2_5 = datae2_5[:, 0]
    ye2_5 = datae2_5[:, 1]
    ze2_5 = datae2_5[:, 2]

    # mode * 4  1-mod 2-mod_fill 3-ran 4-ran_fill
    datae2_6 = get_data(experiment, 6, 2)
    datae2_6 = np.array(datae2_6)
    xe2_6 = datae2_6[:, 0]
    ye2_6 = datae2_6[:, 1]
    ze2_6 = datae2_6[:, 2]

    # data1 和 data2,data3_2,data4_2,5-2
    plot_line = {}
    line_1 = {}

    for i in range(0, len(data1)):
        if data1[i][0] not in plot_line:
            # ori_content
            plot_line[data1[i][0]] = [data1[i][1] - data2[i][1]]
        else:
            plot_line[data1[i][0]].append(data1[i][1] - data2[i][1])
    res_1 = []
    for j in x_stand:
        for m in plot_line[j]:
            temp = [j, m]
            res_1.append(temp)
    res_1 = np.array(res_1)
    x1 = res_1[:, 0]
    z1 = res_1[:, 1]
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    a = [0] * 11
    for k, v in line_1.items():
        a[int(k)] = v

    plot_line = {}
    for i in range(0, len(data1)):
        if data1[i][0] not in plot_line:
            # ori_content
            plot_line[data1[i][0]] = [data1[i][1] - datae2_2[i][1]]
        else:
            plot_line[data1[i][0]].append(data1[i][1] - datae2_2[i][1])
    res_2 = []
    for j in x_stand:
        for m in plot_line[j]:
            temp = [j, m]
            res_2.append(temp)
    res_2 = np.array(res_2)
    x2 = res_2[:, 0]
    z2 = res_2[:, 1]
    line_1 = {}
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    b = [0] * 11
    for k, v in line_1.items():
        b[int(k)] = v

    plot_line = {}
    for i in range(0, len(data1)):
        if data1[i][0] not in plot_line:
            # ori_content
            plot_line[data1[i][0]] = [data1[i][1] - datae2_3[i][1]]
        else:
            plot_line[data1[i][0]].append(data1[i][1] - datae2_3[i][1])
    res_3 = []
    for j in x_stand:
        for m in plot_line[j]:
            temp = [j, m]
            res_3.append(temp)
    res_3 = np.array(res_3)
    x3 = res_3[:, 0]
    z3 = res_3[:, 1]
    line_1 = {}
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    c = [0] * 11
    for k, v in line_1.items():
        c[int(k)] = v

    plot_line = {}
    for i in range(0, len(data1)):
        if data1[i][0] not in plot_line:
            # ori_content
            plot_line[data1[i][0]] = [data1[i][1] - datae2_4[i][1]]
        else:
            plot_line[data1[i][0]].append(data1[i][1] - datae2_4[i][1])
    res_4 = []
    for j in x_stand:
        for m in plot_line[j]:
            temp = [j, m]
            res_4.append(temp)
    res_4 = np.array(res_4)
    x4 = res_4[:, 0]
    z4 = res_4[:, 1]
    line_1 = {}
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    d = [0] * 11
    for k, v in line_1.items():
        d[int(k)] = v

    plot_line = {}
    for i in range(0, len(data1)):
        if data1[i][0] not in plot_line:
            # ori_content
            plot_line[data1[i][0]] = [data1[i][1] - datae2_5[i][1]]
        else:
            plot_line[data1[i][0]].append(data1[i][1] - datae2_5[i][1])
    res_5 = []
    for j in x_stand:
        for m in plot_line[j]:
            temp = [j, m]
            res_5.append(temp)
    res_5 = np.array(res_5)
    x5 = res_5[:, 0]
    z5 = res_5[:, 1]
    line_1 = {}
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    e = [0] * 11
    for k, v in line_1.items():
        e[int(k)] = v

    plot_line = {}
    for i in range(0, len(data1)):
        if data1[i][0] not in plot_line:
            # ori_content
            plot_line[data1[i][0]] = [data1[i][1] - datae2_6[i][1]]
        else:
            plot_line[data1[i][0]].append(data1[i][1] - datae2_6[i][1])
    res_6 = []
    for j in x_stand:
        for m in plot_line[j]:
            temp = [j, m]
            res_6.append(temp)
    res_6 = np.array(res_5)
    x6 = res_6[:, 0]
    z6 = res_6[:, 1]
    line_1 = {}
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    f = [0] * 11
    for k, v in line_1.items():
        f[int(k)] = v

    za = a[2:]
    zb = b[2:]
    zc = c[2:]
    zd = d[2:]
    ze = e[2:]
    zf = f[2:]

    if switch == 0:
        # ax.scatter(x1, z1, color='r', label=r'$\Delta e0-e1$')
        ax.scatter(x2, z2, color='g', label=r'$\Delta K2$')
        ax.scatter(x3, z3, color='b', label=r'$\Delta K3$')
        ax.scatter(x4, z4, color='cyan', label=r'$\Delta K4$')
        ax.scatter(x5, z5, color='coral', label=r'$\Delta K5$')
        ax.scatter(x6, z6, color='m', label=r'$\Delta K5$')
    elif switch == 1:
        # ax.plot(x_stand, za, color='r')
        ax.plot(x_stand, zb, color='g')
        ax.plot(x_stand, zc, color='b')
        ax.plot(x_stand, zd, color='cyan')
        ax.plot(x_stand, ze, color='coral')
        ax.plot(x_stand, zf, color='m')
        # ax.scatter(x_stand, za, color='r', label=r'$\Delta e0-e1$')
        ax.scatter(x_stand, zb, color='g', label=r'$\Delta K2$')
        ax.scatter(x_stand, zc, color='b', label=r'$\Delta K3$')
        ax.scatter(x_stand, zd, color='cyan', label=r'$\Delta K4$')
        ax.scatter(x_stand, ze, color='coral', label=r'$\Delta K5$')
        ax.scatter(x_stand, zf, color='m', label=r'$\Delta K6$')


    # 绘制图例
    ax.legend(loc='best')

    # 添加坐标轴(顺序是Z, Y, X)
    # ax.set_zlabel('Round', fontdict={'size': 15, 'color': 'red'})
    ax.set_ylabel(r'$\Delta_{round}$', fontdict={'size': 15, 'color': 'black'})
    ax.set_xlabel('Origin_content', fontdict={'size': 15, 'color': 'black'})

    # 展示
    plt.show()
    file_name = "../plot_res/e" + str(experiment) + "_delta_round_subgraph" + str(switch) + ".png"
    fig.savefig(file_name)


def plot_delta_k_ori_cover(switch, experiment):
    # 绘制散点图
    fig = plt.figure()
    ax = fig.add_subplot(111)
    x_stand = [2, 3, 4, 5, 6, 7, 8, 9, 10]

    # mode * 4  1-mod 2-mod_fill 3-ran 4-ran_fill
    datae2_2 = get_data(experiment, 2, 1)
    datae2_2 = np.array(datae2_2)
    xe2_2 = datae2_2[:, 0]
    ye2_2 = datae2_2[:, 1]
    ze2_2 = datae2_2[:, 2]

    # mode * 4  1-mod 2-mod_fill 3-ran 4-ran_fill
    datae2_3 = get_data(experiment, 3, 1)
    datae2_3 = np.array(datae2_3)
    xe2_3 = datae2_3[:, 0]
    ye2_3 = datae2_3[:, 1]
    ze2_3 = datae2_3[:, 2]

    # mode * 4  1-mod 2-mod_fill 3-ran 4-ran_fill
    datae2_4 = get_data(experiment, 4, 1)
    datae2_4 = np.array(datae2_4)
    xe2_4 = datae2_4[:, 0]
    ye2_4 = datae2_4[:, 1]
    ze2_4 = datae2_4[:, 2]

    # mode * 4  1-mod 2-mod_fill 3-ran 4-ran_fill
    datae2_5 = get_data(experiment, 5, 1)
    datae2_5 = np.array(datae2_5)
    xe2_5 = datae2_5[:, 0]
    ye2_5 = datae2_5[:, 1]
    ze2_5 = datae2_5[:, 2]

    # mode * 4  1-mod 2-mod_fill 3-ran 4-ran_fill
    datae2_6 = get_data(experiment, 6, 1)
    datae2_6 = np.array(datae2_6)
    xe2_6 = datae2_6[:, 0]
    ye2_6 = datae2_6[:, 1]
    ze2_6 = datae2_6[:, 2]

    # data1 和 data2,data3_2,data4_2,5-2
    plot_line = {}
    line_1 = {}

    for i in range(0, len(data1)):
        if data1[i][0] not in plot_line:
            # ori_content
            plot_line[data1[i][0]] = [data1[i][2] - data2[i][2]]
        else:
            plot_line[data1[i][0]].append(data1[i][2] - data2[i][2])
    res_1 = []
    for j in x_stand:
        for m in plot_line[j]:
            temp = [j, m]
            res_1.append(temp)
    res_1 = np.array(res_1)
    x1 = res_1[:, 0]
    z1 = res_1[:, 1]
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    a = [0] * 11
    for k, v in line_1.items():
        a[int(k)] = v

    plot_line = {}
    for i in range(0, len(data1)):
        if data1[i][0] not in plot_line:
            # ori_content
            plot_line[data1[i][0]] = [data1[i][2] - datae2_2[i][2]]
        else:
            plot_line[data1[i][0]].append(data1[i][2] - datae2_2[i][2])
    res_2 = []
    for j in x_stand:
        for m in plot_line[j]:
            temp = [j, m]
            res_2.append(temp)
    res_2 = np.array(res_2)
    x2 = res_2[:, 0]
    z2 = res_2[:, 1]
    line_1 = {}
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    b = [0] * 11
    for k, v in line_1.items():
        b[int(k)] = v

    plot_line = {}
    for i in range(0, len(data1)):
        if data1[i][0] not in plot_line:
            # ori_content
            plot_line[data1[i][0]] = [data1[i][2] - datae2_3[i][2]]
        else:
            plot_line[data1[i][0]].append(data1[i][2] - datae2_3[i][2])
    res_3 = []
    for j in x_stand:
        for m in plot_line[j]:
            temp = [j, m]
            res_3.append(temp)
    res_3 = np.array(res_3)
    x3 = res_3[:, 0]
    z3 = res_3[:, 1]
    line_1 = {}
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    c = [0] * 11
    for k, v in line_1.items():
        c[int(k)] = v

    plot_line = {}
    for i in range(0, len(data1)):
        if data1[i][0] not in plot_line:
            # ori_content
            plot_line[data1[i][0]] = [data1[i][2] - datae2_4[i][2]]
        else:
            plot_line[data1[i][0]].append(data1[i][2] - datae2_4[i][2])
    res_4 = []
    for j in x_stand:
        for m in plot_line[j]:
            temp = [j, m]
            res_4.append(temp)
    res_4 = np.array(res_4)
    x4 = res_4[:, 0]
    z4 = res_4[:, 1]
    line_1 = {}
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    d = [0] * 11
    for k, v in line_1.items():
        d[int(k)] = v

    plot_line = {}
    for i in range(0, len(data1)):
        if data1[i][0] not in plot_line:
            # ori_content
            plot_line[data1[i][0]] = [data1[i][2] - datae2_5[i][2]]
        else:
            plot_line[data1[i][0]].append(data1[i][2] - datae2_5[i][2])
    res_5 = []
    for j in x_stand:
        for m in plot_line[j]:
            temp = [j, m]
            res_5.append(temp)
    res_5 = np.array(res_5)
    x5 = res_5[:, 0]
    z5 = res_5[:, 1]
    line_1 = {}
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    e = [0] * 11
    for k, v in line_1.items():
        e[int(k)] = v

    plot_line = {}
    for i in range(0, len(data1)):
        if data1[i][0] not in plot_line:
            # ori_content
            plot_line[data1[i][0]] = [data1[i][2] - datae2_6[i][2]]
        else:
            plot_line[data1[i][0]].append(data1[i][2] - datae2_6[i][2])
    res_6 = []
    for j in x_stand:
        for m in plot_line[j]:
            temp = [j, m]
            res_6.append(temp)
    res_6 = np.array(res_5)
    x6 = res_6[:, 0]
    z6 = res_6[:, 1]
    line_1 = {}
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    f = [0] * 11
    for k, v in line_1.items():
        f[int(k)] = v

    za = a[2:]
    zb = b[2:]
    zc = c[2:]
    zd = d[2:]
    ze = e[2:]
    zf = f[2:]

    if switch == 0:
        # ax.scatter(x1, z1, color='r', label=r'$\Delta e0-e1$')
        ax.scatter(x2, z2, color='g', label=r'$\Delta K2$')
        ax.scatter(x3, z3, color='b', label=r'$\Delta K3$')
        ax.scatter(x4, z4, color='cyan', label=r'$\Delta K4$')
        ax.scatter(x5, z5, color='coral', label=r'$\Delta K5$')
        ax.scatter(x6, z6, color='m', label=r'$\Delta K5$')
    elif switch == 1:
        # ax.plot(x_stand, za, color='r')
        ax.plot(x_stand, zb, color='g')
        ax.plot(x_stand, zc, color='b')
        ax.plot(x_stand, zd, color='cyan')
        ax.plot(x_stand, ze, color='coral')
        ax.plot(x_stand, zf, color='m')
        # ax.scatter(x_stand, za, color='r', label=r'$\Delta e0-e1$')
        ax.scatter(x_stand, zb, color='g', label=r'$\Delta K2$')
        ax.scatter(x_stand, zc, color='b', label=r'$\Delta K3$')
        ax.scatter(x_stand, zd, color='cyan', label=r'$\Delta K4$')
        ax.scatter(x_stand, ze, color='coral', label=r'$\Delta K5$')
        ax.scatter(x_stand, zf, color='m', label=r'$\Delta K6$')


    # 绘制图例
    ax.legend(loc='best')

    # 添加坐标轴(顺序是Z, Y, X)
    # ax.set_zlabel('Round', fontdict={'size': 15, 'color': 'red'})
    ax.set_ylabel(r'$\Delta_{cover}$', fontdict={'size': 15, 'color': 'black'})
    ax.set_xlabel('Origin_content', fontdict={'size': 15, 'color': 'black'})

    # 展示
    plt.show()
    file_name = "../plot_res/e" + str(experiment) + "_delta_cover_subgraph" + str(switch) + ".png"
    fig.savefig(file_name)


def plot_delta_k_yround_xcover(switch, experiment):
    # 绘制散点图
    fig = plt.figure()
    ax = fig.add_subplot(111)

    # mode * 4  1-mod 2-mod_fill 3-ran 4-ran_fill
    datae2_2 = get_data(experiment, 2, 2)
    datae2_2 = np.array(datae2_2)
    xe2_2 = datae2_2[:, 0]
    ye2_2 = datae2_2[:, 1]
    ze2_2 = datae2_2[:, 2]

    # mode * 4  1-mod 2-mod_fill 3-ran 4-ran_fill
    datae2_3 = get_data(experiment, 3, 2)
    datae2_3 = np.array(datae2_3)
    xe2_3 = datae2_3[:, 0]
    ye2_3 = datae2_3[:, 1]
    ze2_3 = datae2_3[:, 2]

    # mode * 4  1-mod 2-mod_fill 3-ran 4-ran_fill
    datae2_4 = get_data(experiment, 4, 2)
    datae2_4 = np.array(datae2_4)
    xe2_4 = datae2_4[:, 0]
    ye2_4 = datae2_4[:, 1]
    ze2_4 = datae2_4[:, 2]

    # mode * 4  1-mod 2-mod_fill 3-ran 4-ran_fill
    datae2_5 = get_data(experiment, 5, 2)
    datae2_5 = np.array(datae2_5)
    xe2_5 = datae2_5[:, 0]
    ye2_5 = datae2_5[:, 1]
    ze2_5 = datae2_5[:, 2]

    # mode * 4  1-mod 2-mod_fill 3-ran 4-ran_fill
    datae2_6 = get_data(experiment, 6, 2)
    datae2_6 = np.array(datae2_6)
    xe2_6 = datae2_6[:, 0]
    ye2_6 = datae2_6[:, 1]
    ze2_6 = datae2_6[:, 2]

    # mode * 4  1-mod 2-mod_fill 3-ran 4-ran_fill
    datae1_2 = get_data(experiment, 2, 1)
    datae1_2 = np.array(datae1_2)
    xe1_2 = datae1_2[:, 0]
    ye1_2 = datae1_2[:, 1]
    ze1_2 = datae1_2[:, 2]

    # mode * 4  1-mod 2-mod_fill 3-ran 4-ran_fill
    datae1_3 = get_data(experiment, 3, 1)
    datae1_3 = np.array(datae1_3)
    xe1_3 = datae1_3[:, 0]
    ye1_3 = datae1_3[:, 1]
    ze1_3 = datae1_3[:, 2]

    # mode * 4  1-mod 2-mod_fill 3-ran 4-ran_fill
    datae1_4 = get_data(experiment, 4, 1)
    datae1_4 = np.array(datae1_4)
    xe1_4 = datae1_4[:, 0]
    ye1_4 = datae1_4[:, 1]
    ze1_4 = datae1_4[:, 2]

    # mode * 4  1-mod 2-mod_fill 3-ran 4-ran_fill
    datae1_5 = get_data(experiment, 5, 1)
    datae1_5 = np.array(datae1_5)
    xe1_5 = datae1_5[:, 0]
    ye1_5 = datae1_5[:, 1]
    ze1_5 = datae1_5[:, 2]

    # mode * 4  1-mod 2-mod_fill 3-ran 4-ran_fill
    datae1_6 = get_data(experiment, 6, 1)
    datae1_6 = np.array(datae1_6)
    xe1_6 = datae1_6[:, 0]
    ye1_6 = datae1_6[:, 1]
    ze1_6 = datae1_6[:, 2]

    # data1 和 data2,data3_2,data4_2,5-2,6-2
    plot_line = {}
    line_1 = {}

    for i in range(0, len(data1)):
        if (data1[i][2] - data2[i][2]) not in plot_line:
            # ori_content
            plot_line[data1[i][2] - data2[i][2]] = [data1[i][1] - data2[i][1]]
        else:
            plot_line[data1[i][2] - data2[i][2]].append(data1[i][1] - data2[i][1])
    res_1 = []
    for j in plot_line:
        for m in plot_line[j]:
            temp = [j, m]
            res_1.append(temp)
    res_1 = np.array(res_1)
    x1 = res_1[:, 0]
    z1 = res_1[:, 1]
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    x_c = []
    y_c = []
    for p, q in line_1.items():
        x_c.append(p)
        y_c.append(q)

    plot_line = {}
    line_1 = {}
    for i in range(0, len(data1)):
        if (data1[i][2] - datae1_2[i][2]) not in plot_line:
            plot_line[data1[i][2] - datae1_2[i][2]] = [data1[i][1] - datae2_2[i][1]]
        else:
            plot_line[data1[i][2] - datae1_2[i][2]].append(data1[i][1] - datae2_2[i][1])
    res_1 = []
    for j in plot_line:
        for m in plot_line[j]:
            temp = [j, m]
            res_1.append(temp)
    res_1 = np.array(res_1)
    x2_1 = res_1[:, 0]
    z2_1 = res_1[:, 1]
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    x_d = []
    y_d = []
    for p, q in line_1.items():
        x_d.append(p)
        y_d.append(q)

    plot_line = {}
    line_1 = {}
    for i in range(0, len(data1)):
        if (data1[i][2] - datae1_3[i][2]) not in plot_line:
            plot_line[data1[i][2] - datae1_3[i][2]] = [data1[i][1] - datae2_3[i][1]]
        else:
            plot_line[data1[i][2] - datae1_3[i][2]].append(data1[i][1] - datae2_3[i][1])
    res_1 = []
    for j in plot_line:
        for m in plot_line[j]:
            temp = [j, m]
            res_1.append(temp)
    res_1 = np.array(res_1)
    r3_1 = res_1[:, 0]
    c3_1 = res_1[:, 1]
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    x_e = []
    y_e = []
    for p, q in line_1.items():
        x_e.append(p)
        y_e.append(q)

    plot_line = {}
    line_1 = {}
    for i in range(0, len(data1)):
        if (data1[i][2] - datae1_4[i][2]) not in plot_line:
            plot_line[data1[i][2] - datae1_4[i][2]] = [data1[i][1] - datae2_4[i][1]]
        else:
            plot_line[data1[i][2] - datae1_4[i][2]].append(data1[i][1] - datae2_4[i][1])
    res_1 = []
    for j in plot_line:
        for m in plot_line[j]:
            temp = [j, m]
            res_1.append(temp)
    res_1 = np.array(res_1)
    r4_1 = res_1[:, 0]
    c4_1 = res_1[:, 1]
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    x_f = []
    y_f = []
    for p, q in line_1.items():
        x_f.append(p)
        y_f.append(q)

    plot_line = {}
    line_1 = {}
    for i in range(0, len(data1)):
        if (data1[i][2] - datae1_5[i][2]) not in plot_line:
            plot_line[data1[i][2] - datae1_5[i][2]] = [data1[i][1] - datae2_5[i][1]]
        else:
            plot_line[data1[i][2] - datae1_5[i][2]].append(data1[i][1] - datae2_5[i][1])
    res_1 = []
    for j in plot_line:
        for m in plot_line[j]:
            temp = [j, m]
            res_1.append(temp)
    res_1 = np.array(res_1)
    r5_1 = res_1[:, 0]
    c5_1 = res_1[:, 1]
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    x_g = []
    y_g = []
    for p, q in line_1.items():
        x_g.append(p)
        y_g.append(q)

    plot_line = {}
    line_1 = {}
    for i in range(0, len(data1)):
        if (data1[i][2] - datae1_6[i][2]) not in plot_line:
            plot_line[data1[i][2] - datae1_6[i][2]] = [data1[i][1] - datae2_6[i][1]]
        else:
            plot_line[data1[i][2] - datae1_6[i][2]].append(data1[i][1] - datae2_6[i][1])
    res_1 = []
    for j in plot_line:
        for m in plot_line[j]:
            temp = [j, m]
            res_1.append(temp)
    res_1 = np.array(res_1)
    r6_1 = res_1[:, 0]
    c6_1 = res_1[:, 1]
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    x_h = []
    y_h = []
    for p, q in line_1.items():
        x_h.append(p)
        y_h.append(q)

    x_c, y_c = sort_order(x_c, y_c)
    x_d, y_d = sort_order(x_d, y_d)
    x_e, y_e = sort_order(x_e, y_e)
    x_f, y_f = sort_order(x_f, y_f)
    x_g, y_g = sort_order(x_g, y_g)
    x_h, y_h = sort_order(x_h, y_h)

    if switch == 0:
        # ax.scatter(x1, z1, color='r', label=r'$\Delta K1$')
        ax.scatter(x2_1, z2_1, color='g', label=r'$\Delta K2$')
        ax.scatter(r3_1, c3_1, color='b', label=r'$\Delta K3$')
        ax.scatter(r4_1, c4_1, color='cyan', label=r'$\Delta K4$')
        ax.scatter(r5_1, c5_1, color='coral', label=r'$\Delta K5$')
        ax.scatter(r6_1, c6_1, color='m', label=r'$\Delta K6$')
    elif switch == 1:
        # ax.plot(x_c, y_c, color='r')
        ax.plot(x_d, y_d, color='g')
        ax.plot(x_e, y_e, color='b')
        ax.plot(x_f, y_f, color='cyan')
        ax.plot(x_g, y_g, color='coral')
        ax.plot(x_h, y_h, color='m')
        # ax.scatter(x_c, y_c, color='r', label=r'$\Delta e0-e1$')
        ax.scatter(x_d, y_d, color='g', label=r'$\Delta K2$')
        ax.scatter(x_e, y_e, color='b', label=r'$\Delta K3$')
        ax.scatter(x_f, y_f, color='cyan', label=r'$\Delta K4$')
        ax.scatter(x_g, y_g, color='coral', label=r'$\Delta K5$')
        ax.scatter(x_h, y_h, color='m', label=r'$\Delta K6$')

    # 绘制图例
    ax.legend(loc='best')

    # 添加坐标轴(顺序是Z, Y, X)
    # ax.set_zlabel('Round', fontdict={'size': 15, 'color': 'red'})
    ax.set_ylabel(r'$\Delta_{round}$', fontdict={'size': 15, 'color': 'black'})
    ax.set_xlabel(r'$\Delta_{cover}$', fontdict={'size': 15, 'color': 'black'})

    # 展示
    plt.show()
    file_name = "../plot_res/k" + str(experiment) + "_delta_yround_xcover" + str(switch) + ".png"
    fig.savefig(file_name)


def plot_delta_k_xround_ycover(switch, experiment):
    # 绘制散点图
    fig = plt.figure()
    ax = fig.add_subplot(111)

    # mode * 4  1-mod 2-mod_fill 3-ran 4-ran_fill
    datae2_2 = get_data(experiment, 2, 2)
    datae2_2 = np.array(datae2_2)
    xe2_2 = datae2_2[:, 0]
    ye2_2 = datae2_2[:, 1]
    ze2_2 = datae2_2[:, 2]

    # mode * 4  1-mod 2-mod_fill 3-ran 4-ran_fill
    datae2_3 = get_data(experiment, 3, 2)
    datae2_3 = np.array(datae2_3)
    xe2_3 = datae2_3[:, 0]
    ye2_3 = datae2_3[:, 1]
    ze2_3 = datae2_3[:, 2]

    # mode * 4  1-mod 2-mod_fill 3-ran 4-ran_fill
    datae2_4 = get_data(experiment, 4, 2)
    datae2_4 = np.array(datae2_4)
    xe2_4 = datae2_4[:, 0]
    ye2_4 = datae2_4[:, 1]
    ze2_4 = datae2_4[:, 2]

    # mode * 4  1-mod 2-mod_fill 3-ran 4-ran_fill
    datae2_5 = get_data(experiment, 5, 2)
    datae2_5 = np.array(datae2_5)
    xe2_5 = datae2_5[:, 0]
    ye2_5 = datae2_5[:, 1]
    ze2_5 = datae2_5[:, 2]

    # mode * 4  1-mod 2-mod_fill 3-ran 4-ran_fill
    datae2_6 = get_data(experiment, 6, 2)
    datae2_6 = np.array(datae2_6)
    xe2_6 = datae2_6[:, 0]
    ye2_6 = datae2_6[:, 1]
    ze2_6 = datae2_6[:, 2]

    # mode * 4  1-mod 2-mod_fill 3-ran 4-ran_fill
    datae1_2 = get_data(experiment, 2, 1)
    datae1_2 = np.array(datae1_2)
    xe1_2 = datae1_2[:, 0]
    ye1_2 = datae1_2[:, 1]
    ze1_2 = datae1_2[:, 2]

    # mode * 4  1-mod 2-mod_fill 3-ran 4-ran_fill
    datae1_3 = get_data(experiment, 3, 1)
    datae1_3 = np.array(datae1_3)
    xe1_3 = datae1_3[:, 0]
    ye1_3 = datae1_3[:, 1]
    ze1_3 = datae1_3[:, 2]

    # mode * 4  1-mod 2-mod_fill 3-ran 4-ran_fill
    datae1_4 = get_data(experiment, 4, 1)
    datae1_4 = np.array(datae1_4)
    xe1_4 = datae1_4[:, 0]
    ye1_4 = datae1_4[:, 1]
    ze1_4 = datae1_4[:, 2]

    # mode * 4  1-mod 2-mod_fill 3-ran 4-ran_fill
    datae1_5 = get_data(experiment, 5, 1)
    datae1_5 = np.array(datae1_5)
    xe1_5 = datae1_5[:, 0]
    ye1_5 = datae1_5[:, 1]
    ze1_5 = datae1_5[:, 2]

    # mode * 4  1-mod 2-mod_fill 3-ran 4-ran_fill
    datae1_6 = get_data(experiment, 6, 1)
    datae1_6 = np.array(datae1_6)
    xe1_6 = datae1_6[:, 0]
    ye1_6 = datae1_6[:, 1]
    ze1_6 = datae1_6[:, 2]

    # data1 和 data2,data3_2,data4_2,5-2,6-2
    plot_line = {}
    line_1 = {}

    for i in range(0, len(data1)):
        if (data1[i][1] - data2[i][1]) not in plot_line:
            # ori_content
            plot_line[data1[i][1] - data2[i][1]] = [data1[i][2] - data2[i][2]]
        else:
            plot_line[data1[i][1] - data2[i][1]].append(data1[i][2] - data2[i][2])
    res_1 = []
    for j in plot_line:
        for m in plot_line[j]:
            temp = [j, m]
            res_1.append(temp)
    res_1 = np.array(res_1)
    x1 = res_1[:, 0]
    z1 = res_1[:, 1]
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    x_c = []
    y_c = []
    for p, q in line_1.items():
        x_c.append(p)
        y_c.append(q)

    plot_line = {}
    line_1 = {}
    for i in range(0, len(data1)):
        if (data1[i][1] - datae2_2[i][1]) not in plot_line:
            plot_line[data1[i][1] - datae2_2[i][1]] = [data1[i][2] - datae1_2[i][2]]
        else:
            plot_line[data1[i][1] - datae2_2[i][1]].append(data1[i][2] - datae1_2[i][2])
    res_1 = []
    for j in plot_line:
        for m in plot_line[j]:
            temp = [j, m]
            res_1.append(temp)
    res_1 = np.array(res_1)
    x2_1 = res_1[:, 0]
    z2_1 = res_1[:, 1]
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    x_d = []
    y_d = []
    for p, q in line_1.items():
        x_d.append(p)
        y_d.append(q)

    plot_line = {}
    line_1 = {}
    for i in range(0, len(data1)):
        if (data1[i][1] - datae2_3[i][1]) not in plot_line:
            plot_line[data1[i][1] - datae2_3[i][1]] = [data1[i][2] - datae1_3[i][2]]
        else:
            plot_line[data1[i][1] - datae2_3[i][1]].append(data1[i][2] - datae1_3[i][2])
    res_1 = []
    for j in plot_line:
        for m in plot_line[j]:
            temp = [j, m]
            res_1.append(temp)
    res_1 = np.array(res_1)
    r3_1 = res_1[:, 0]
    c3_1 = res_1[:, 1]
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    x_e = []
    y_e = []
    for p, q in line_1.items():
        x_e.append(p)
        y_e.append(q)

    plot_line = {}
    line_1 = {}
    for i in range(0, len(data1)):
        if (data1[i][1] - datae2_4[i][1]) not in plot_line:
            plot_line[data1[i][1] - datae2_4[i][1]] = [data1[i][2] - datae1_4[i][2]]
        else:
            plot_line[data1[i][1] - datae2_4[i][1]].append(data1[i][2] - datae1_4[i][2])
    res_1 = []
    for j in plot_line:
        for m in plot_line[j]:
            temp = [j, m]
            res_1.append(temp)
    res_1 = np.array(res_1)
    r4_1 = res_1[:, 0]
    c4_1 = res_1[:, 1]
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    x_f = []
    y_f = []
    for p, q in line_1.items():
        x_f.append(p)
        y_f.append(q)

    plot_line = {}
    line_1 = {}
    for i in range(0, len(data1)):
        if (data1[i][1] - datae2_5[i][1]) not in plot_line:
            plot_line[data1[i][1] - datae2_5[i][1]] = [data1[i][2] - datae1_5[i][2]]
        else:
            plot_line[data1[i][1] - datae2_5[i][1]].append(data1[i][2] - datae1_5[i][2])
    res_1 = []
    for j in plot_line:
        for m in plot_line[j]:
            temp = [j, m]
            res_1.append(temp)
    res_1 = np.array(res_1)
    r5_1 = res_1[:, 0]
    c5_1 = res_1[:, 1]
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    x_g = []
    y_g = []
    for p, q in line_1.items():
        x_g.append(p)
        y_g.append(q)

    plot_line = {}
    line_1 = {}
    for i in range(0, len(data1)):
        if (data1[i][1] - datae2_6[i][1]) not in plot_line:
            plot_line[data1[i][1] - datae2_6[i][1]] = [data1[i][2] - datae1_6[i][2]]
        else:
            plot_line[data1[i][1] - datae2_6[i][1]].append(data1[i][2] - datae1_6[i][2])
    res_1 = []
    for j in plot_line:
        for m in plot_line[j]:
            temp = [j, m]
            res_1.append(temp)
    res_1 = np.array(res_1)
    r6_1 = res_1[:, 0]
    c6_1 = res_1[:, 1]
    for key, value in plot_line.items():
        num = len(plot_line[key])
        sum = 0
        for v in value:
            sum = sum + v
        line_1[key] = sum / num
    x_h = []
    y_h = []
    for p, q in line_1.items():
        x_h.append(p)
        y_h.append(q)

    x_c, y_c = sort_order(x_c, y_c)
    x_d, y_d = sort_order(x_d, y_d)
    x_e, y_e = sort_order(x_e, y_e)
    x_f, y_f = sort_order(x_f, y_f)
    x_g, y_g = sort_order(x_g, y_g)
    x_h, y_h = sort_order(x_h, y_h)

    if switch == 0:
        # ax.scatter(x1, z1, color='r', label=r'$\Delta K1$')
        ax.scatter(x2_1, z2_1, color='g', label=r'$\Delta K2$')
        ax.scatter(r3_1, c3_1, color='b', label=r'$\Delta K3$')
        ax.scatter(r4_1, c4_1, color='cyan', label=r'$\Delta K4$')
        ax.scatter(r5_1, c5_1, color='coral', label=r'$\Delta K5$')
        ax.scatter(r6_1, c6_1, color='m', label=r'$\Delta K6$')
    elif switch == 1:
        # ax.plot(x_c, y_c, color='r')
        ax.plot(x_d, y_d, color='g')
        ax.plot(x_e, y_e, color='b')
        ax.plot(x_f, y_f, color='cyan')
        ax.plot(x_g, y_g, color='coral')
        ax.plot(x_h, y_h, color='m')
        # ax.scatter(x_c, y_c, color='r', label=r'$\Delta e0-e1$')
        ax.scatter(x_d, y_d, color='g', label=r'$\Delta K2$')
        ax.scatter(x_e, y_e, color='b', label=r'$\Delta K3$')
        ax.scatter(x_f, y_f, color='cyan', label=r'$\Delta K4$')
        ax.scatter(x_g, y_g, color='coral', label=r'$\Delta K5$')
        ax.scatter(x_h, y_h, color='m', label=r'$\Delta K6$')

    # 绘制图例
    ax.legend(loc='best')

    # 添加坐标轴(顺序是Z, Y, X)
    # ax.set_zlabel('Round', fontdict={'size': 15, 'color': 'red'})
    ax.set_ylabel(r'$\Delta_{cover}$', fontdict={'size': 15, 'color': 'black'})
    ax.set_xlabel(r'$\Delta_{round}$', fontdict={'size': 15, 'color': 'black'})

    # 展示
    plt.show()
    file_name = "../plot_res/k" + str(experiment) + "_delta_xround_ycover" + str(switch) + ".png"
    fig.savefig(file_name)


# for t in range(2,6):
#     plot_average_k_ori_round(0, t)
#     plot_average_k_ori_round(1, t)
# for t in range(2, 6):
#     plot_average_k_ori_cover(0, t)
#     plot_average_k_ori_cover(1, t)
# for t in range(2, 6):
#     plot_delta_k_ori_round(0, t)
#     plot_delta_k_ori_round(1, t)
# for t in range(2, 6):
#     plot_delta_k_ori_cover(0, t)
#     plot_delta_k_ori_cover(1, t)
# for t in range(2, 6):
#     plot_delta_k_yround_xcover(0, t)
#     plot_delta_k_yround_xcover(1, t)
# for t in range(2, 6):
#     plot_delta_k_xround_ycover(0, t)
#     plot_delta_k_xround_ycover(1, t)


