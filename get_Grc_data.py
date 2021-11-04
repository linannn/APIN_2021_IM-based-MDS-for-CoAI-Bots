#!/usr/bin/env python

# encoding: utf-8
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/21 10:14
# @Author  : junruit
# @File    : get_Grc_data.py
# @desc: PyCharm
'''
import json
import requests
import os
from res_test_2 import *
import re
import numpy as np


def fetch_information_from_content(c):
    url = "http://10.147.18.111:8080/api/search-rp?detail="+ c
    response = requests.get(url)
    respon_json = json.loads(response.content)
    return respon_json


def get_data(num, n_level, content_name):
    file_name = "./data/rps_supp_" + str(num) + ".json"
    with open(file_name, 'r', encoding='utf-8') as fr:
        rps_set = json.load(fr)
    content_set = []
    rp_set_1 = []
    restricts_set = {}
    for i in rps_set:
        rp = i['data'][0]
        # travel
        content = rp['goal']['content']
        if content != content_name:
            continue
        rp_set_1.append(i)
        if content not in content_set:
            content_set.append(content)
            restricts_set[content] = [0]
        restricts = rp['goal']['restricts']
        restricts_set[content].extend(restricts)
        tree_set = [rp]
        level = 1
        while len(tree_set) > 0:

            new_tree_set = []
            for child_tree in tree_set:
                content = child_tree['goal']['content']
                if content not in content_set:
                    content_set.append(content)
                    restricts_set[content] = []
                loc_level = [level]
                restricts_set[content].extend(loc_level)
                restricts = rp['goal']['restricts']
                restricts_set[content].extend(restricts)
                children_nodes = child_tree['children']
                new_tree_set.extend(children_nodes)
            tree_set = new_tree_set
            level = level + 1
            if level > n_level:
                break

    return content_set, restricts_set, rp_set_1


# K = 2, level = 1
# c_set, r_set, rp_set = get_data(2, 1)


def write_1():
    with open("grc_data_test.txt", 'w', encoding='utf-8') as fw:
        for k, v in r_set.items():
            if len(v) == 0:
                fw.write(str(k))
                fw.write("\t")
                fw.write(str(v))
                fw.write("\n")
            else:
                for s in v:
                    fw.write(str(k))
                    fw.write("\t")
                    fw.write(str(s))
                    fw.write("\n")


def write_content_0(k, c_set):
    file_name = "k" + str(k) + "_content0.txt"
    with open(file_name, 'w', encoding='utf-8') as fw:
        for i in c_set:
            fw.write(str(i))
            fw.write("\n")


def write_3(k):
    file_path = "k" + str(k) + "_content0.txt"
    with open(file_path, 'r', encoding='utf-8') as fr:
        content = fr.readline()
        while content:
            content = content.replace("\n", "")
            file_name = "./k" + str(k) + "_Grc/k" + str(k) + "_content_" + str(content) + ".json"
            c_set, r_set, rp_set = get_data(k, 5, content)
            with open(file_name, 'w', encoding='utf-8') as fw:
                json.dump(rp_set, fw, ensure_ascii=False)
            content = fr.readline()


# write_3()
def walk_file(k):
    rootdir = "./k" + str(k) + "_Grc"
    list = os.listdir(rootdir) # 列出文件夹下所有的目录与文件
    for i in list:
        path = os.path.join(rootdir, i)
        # if os.path.isfile(path):
        # 你想对文件的操作
        with open(path, 'r', encoding='utf-8') as fr:
            rps_set = json.load(fr)
        if len(rps_set) > 1:
            print(path)
            print(len(rps_set))

# # ./k2_Grc\k2_content_旅行.json
# # 1710
# # ./k2_Grc\k2_content_景点.json
# # 37
# # ./k2_Grc\k2_content_酒店.json
# # 67
# # ./k2_Grc\k2_content_餐馆.json
# # 25
# walk_file(3)
# # ./k3_Grc\k3_content_旅行.json
# # 549
# # ./k3_Grc\k3_content_景点.json
# # 23
# # ./k3_Grc\k3_content_酒店.json
# # 41
# # ./k3_Grc\k3_content_餐馆.json
# # 5
# walk_file(4)
# # ./k4_Grc\k4_content_旅行.json
# # 243
# # ./k4_Grc\k4_content_景点.json
# # 13
# # ./k4_Grc\k4_content_酒店.json
# # 32
# walk_file(5)
# # ./k5_Grc\k5_content_旅行.json
# # 101
# # ./k5_Grc\k5_content_景点.json
# # 10
# # ./k5_Grc\k5_content_酒店.json
# # 23
# walk_file(6)
# # ./k6_Grc\k6_content_旅行.json
# # 73
# # ./k6_Grc\k6_content_景点.json
# # 6
# # ./k6_Grc\k6_content_酒店.json
# # 22


def get_data_1(num, n_level):
    file_name = "./data/rps_supp_" + str(num) + ".json"
    with open(file_name, 'r', encoding='utf-8') as fr:
        rps_set = json.load(fr)
    content_set = []
    rp_set_1 = []
    restricts_set = {}
    for i in rps_set:
        rp = i['data'][0]
        # travel
        content = rp['goal']['content']
        # if content != content_name:
        #     continue
        rp_set_1.append(i)
        if content not in content_set:
            content_set.append(content)
            restricts_set[content] = [0]
        restricts = rp['goal']['restricts']
        restricts_set[content].extend(restricts)
        tree_set = [rp]
        level = 1
        while len(tree_set) > 0:
            new_tree_set = []
            for child_tree in tree_set:
                content = child_tree['goal']['content']
                if content not in content_set:
                    content_set.append(content)
                    restricts_set[content] = []
                loc_level = [level]
                restricts_set[content].extend(loc_level)
                restricts = rp['goal']['restricts']
                restricts_set[content].extend(restricts)
                children_nodes = child_tree['children']
                new_tree_set.extend(children_nodes)
            tree_set = new_tree_set
            level = level + 1
            if level > n_level:
                break

    return content_set, restricts_set, rp_set_1

# data initial fetch
# c_set, r_set, rp_set = get_data_1(3, 1)
# write_content_0(3, c_set)
# write_3(3)
# c_set, r_set, rp_set = get_data_1(4, 1)
# write_content_0(4, c_set)
# write_3(4)
# c_set, r_set, rp_set = get_data_1(5, 1)
# write_content_0(5, c_set)
# write_3(5)
# c_set, r_set, rp_set = get_data_1(6, 1)
# write_content_0(6, c_set)
# write_3(6)


def get_data_test(num, n_level, content_name):
    file_name = "./data/rps_supp_" + str(num) + ".json"
    with open(file_name, 'r', encoding='utf-8') as fr:
        rps_set = json.load(fr)
    content_set = []
    rp_set_1 = []
    restricts_set = {}
    rps_set = test_499 + test_5008
    for i in rps_set:
        rp = i
        # travel
        content = rp['goal']['content']
        # if content != content_name:
        #     continue
        rp_set_1.append(i)
        if content not in content_set:
            content_set.append(content)
            restricts_set[content] = [0]
        restricts = rp['goal']['restricts']
        restricts_set[content].extend(restricts)
        tree_set = [rp]
        level = 1
        while len(tree_set) > 0:
            new_tree_set = []
            for child_tree in tree_set:
                content = child_tree['goal']['content']
                if content not in content_set:
                    content_set.append(content)
                    restricts_set[content] = []
                loc_level = [level]
                restricts_set[content].extend(loc_level)
                restricts = rp['goal']['restricts']
                restricts_set[content].extend(restricts)
                children_nodes = child_tree['children']
                new_tree_set.extend(children_nodes)
            tree_set = new_tree_set
            level = level + 1
            if level > n_level:
                break

    return content_set, restricts_set, rp_set_1


# c_set, r_set, rp_set = get_data_test(2, 1, "")
# print(c_set)
# c_set, r_set, rp_set = get_data(2, 2, "旅行")
# print(c_set)
content_epoch_2 = ['出租', '景点', '酒店', '餐馆', '地铁']


def get_data_epoch(n_level, content_name, k):
    file_name = "./k" + str(k) + "_Grc/k" + str(k) + "_content_" + str(content_name) + ".json"
    with open(file_name, 'r', encoding='utf-8') as fr:
        rps_set = json.load(fr)
    rp_set_1 = []

    res = []
    restricts_set = {}
    for i in rps_set:
        res_set = [0, 0, 0, 0, 0]
        content_set = []
        rps_id = i['info']['rpId']
        rp = i['data'][0]
        # travel
        content = rp['goal']['content']
        if content != content_name:
            continue
        rp_set_1.append(i)
        if content not in content_set:
            content_set.append(content)
            restricts_set[content] = [0]
        restricts = rp['goal']['restricts']
        restricts_set[content].extend(restricts)
        tree_set = [rp]
        level = 1
        while len(tree_set) > 0:
            new_tree_set = []
            for child_tree in tree_set:
                content = child_tree['goal']['content']
                if content not in content_set:
                    content_set.append(content)
                    restricts_set[content] = []
                loc_level = [level]
                restricts_set[content].extend(loc_level)
                restricts = rp['goal']['restricts']
                restricts_set[content].extend(restricts)
                children_nodes = child_tree['children']
                new_tree_set.extend(children_nodes)
            tree_set = new_tree_set
            level = level + 1
            if level > n_level:
                break
        for i in range(0, len(content_epoch_2)):
            if content_epoch_2[i] in content_set:
                res_set[i] = 1
        res_temp = [rps_id, res_set]
        res.append(res_temp)

    return res


def write_fcm(k):
    set_res = get_data_epoch(2, "旅行", k)
    with open("grc_epoch_divide_" + str(k) + ".txt", 'w', encoding='utf-8') as fq:
        with open("grc_epoch_" + str(k) + ".txt", 'w', encoding='utf-8') as fw:
            num = 0
            fw.write("序号")
            fw.write("\t")
            fw.write("ID")
            fw.write("\t")
            fw.write("['出租', '景点', '酒店', '餐馆', '地铁']")
            fw.write("\n")
            for i in set_res:
                num = num + 1
                fw.write(str(num))
                fw.write("\t")
                fw.write(str(i[0]))
                fw.write("\t")
                fw.write(str(i[1]))
                for j in i[1]:
                    fq.write(str(j))
                    fq.write(" ")
                fw.write("\n")
                fq.write("\n")


# write_fcm(3)
# write_fcm(4)
# write_fcm(5)
# write_fcm(6)


def fetch_1_0(num_n, support):
    num = 0
    file = "grc_epoch_divide_" + str(support) + ".txt"
    with open(file, 'r', encoding='utf-8') as fr:
        content = fr.readline()
        while content:
            if num == num_n:
                break
            num = num + 1
            content = fr.readline()
    return content


def write_divide_2(support):
    file_write = "./k" + str(support) + "_Grc/divide_res_旅行_" + str(support) + "_分布.txt"
    file_read = "./k" + str(support) + "_Grc/divide_res_旅行" + str(support) + ".txt"
    with open(file_write, 'w', encoding='utf-8') as fw:
        with open(file_read, 'r', encoding='utf-8') as fr:
            content = fr.readline()
            while content:
                array_record = eval(content)
                temp_set = []
                for i in array_record:
                    str_res = fetch_1_0(i, support)
                    if str_res not in temp_set:
                        temp_set.append(str_res)
                        fw.write(str(str_res))
                fw.write(str(len(array_record)) + "\n")
                content = fr.readline()


# write_divide_2()
# write_divide_2(3)
# write_divide_2(4)
# write_divide_2(5)
# write_divide_2(6)


def fetch_rps(k, support):
    with open("./k" + str(support) + "_Grc/k" + str(support) + "_content_旅行.json", 'r', encoding='utf-8') as fr:
        rps_set = json.load(fr)
    rps = rps_set[k]

    return rps


def write_divide_3(support):
    temp_set = []
    file_read = "./k" + str(support) + "_Grc/divide_res_旅行" + str(support) + ".txt"
    with open(file_read, 'r', encoding='utf-8') as fr:
        content = fr.readline()
        while content:
            array_record = eval(content)
            temp_set.append(array_record)
            content = fr.readline()
    print(temp_set)
    num = 0
    for i in temp_set:
        num = num + 1
        file_path = "./k" + str(support) + "_Grc/k" + str(support) + "_content_layer2_旅行_clu" + str(num) + ".json"
        temp_write = []
        for j in i:
            rps = fetch_rps(j, support)
            temp_write.append(rps)
        with open(file_path, 'w', encoding='utf-8') as fw:
            json.dump(temp_write, fw, ensure_ascii=False)


# write_divide_3(3)
# write_divide_3(4)
# write_divide_3(5)
# write_divide_3(6)


def confirm_layer2_clu(k, n_level, support):
    file_path = "./k" + str(support) + "_Grc/k" + str(support) + "_content_layer2_旅行_clu" + str(k) + ".json"
    with open(file_path, 'r', encoding='utf-8') as fr:
        rps_set = json.load(fr)
    content_set = []
    restricts_set = {}
    restricts_set_all = {}
    for i in rps_set:
        rps_id = i['info']['rpId']
        temp_set = {}
        rp = i['data'][0]
        tree_set = [rp]
        level = 1
        while len(tree_set) > 0:
            if level > n_level:
                break
            new_tree_set = []
            for child_tree in tree_set:
                content = child_tree['goal']['content']
                if level == n_level:
                    if content not in content_set:
                        content_set.append(content)
                        restricts_set[content] = []
                    if content not in temp_set:
                        temp_set[content] = []
                    restricts = child_tree['goal']['restricts']
                    restricts_set[content].extend(restricts)
                    temp_set[content].extend(restricts)
                children_nodes = child_tree['children']
                new_tree_set.extend(children_nodes)
            tree_set = new_tree_set
            level = level + 1
        restricts_set_all[rps_id] = temp_set
    return restricts_set, content_set, restricts_set_all


def is_chinese(uchar):
    """判断一个unicode是否是汉字"""
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False


def adjust_in_similar(array_temp):
    # res = []
    # for i in array_temp:
    #     temp = eval(i)
    #     res.append(temp)
    res = array_temp
    for i in range(len(res) - 1):
        for j in range(len(res) - i - 1):
            if res[j]['key'][0] > res[j + 1]['key'][0]:
                res[j], res[j + 1] = res[j + 1], res[j]
    return res


def extra_deal(i):
    if 'maxValue' in i:
        if i['valueType'] == 'region':
            # maxvalue = i['maxValue']
            # minvalue = i['minValue']
            # unit = i['unit']
            # str_value = str(minvalue) + "--" + str(maxvalue)
            # i['value'] = str_value
            # del(i['maxValue'])
            # del(i['minValue'])
            pass
        elif i['valueType'] == 'enum':
            value = i['value']
            count = ""
            for m in range(0, len(value)):
                if is_chinese(value[m]):
                    break
                count = count + value[m]
            str_unit = value[m:]

            # i['value'] = str_value
            i['unit'] = str_unit
            if len(count) > 0:
                count = eval(count)
                i['maxValue'] = count
                i['minValue'] = count
            else:
                i['maxValue'] = 9999
                i['minValue'] = 0

    return i


def is_exist_by_double_list(target, element):
    """
        判断二维列表中是否存在某个元素
    :param target:目标列表
    :param element:需要判断的元素
    :return:bool类型，是否存在
    """
    for line in target:
        if element in line:
            return True
    return False


def write_layer_clu(clu_id, layer, support):
    rest_set_all, con_set, rest_set = confirm_layer2_clu(clu_id, layer, support)
    # print(con_set)
    # print(rest_set)
    file_path_1 = "k" + str(support) + "_analysize_record_旅行layer" + str(layer) + "clu" + str(clu_id) + ".txt"
    file_path_2 = "k" + str(support) + "_statistics_record_旅行layer" + str(layer) + "clu" + str(clu_id) + ".txt"

    with open(file_path_1, 'w', encoding='utf-8') as fw:
        for k, v in rest_set_all.items():
            fw.write(str(k))
            fw.write("\n")
            temp = []
            for d in v:
                del(d['goalId'])
                if d not in temp:
                    temp.append(d)
            temp = adjust_in_similar(temp)
            for order in temp:
                fw.write(str(order))
                fw.write("\n")
        for k, v in rest_set.items():
            fw.write(str(k))
            fw.write("\n")
            for key, value in v.items():
                fw.write(str(key))
                fw.write("\n")
                for s in value:
                    fw.write(str(s))
                    fw.write("\n")
    with open(file_path_2, 'w', encoding='utf-8') as fw:
        temp_id = {}
        for k, v in rest_set_all.items():
            fw.write(str(k))
            fw.write("\n")
            temp = []
            for d in v:
                if d not in temp:
                    temp.append(d)
            temp = adjust_in_similar(temp)
            for t in range(0, len(temp)):
                temp[t] = extra_deal(temp[t])
                fw.write(str(t))
                fw.write("\t")
                fw.write(str(temp[t]))
                fw.write("\n")
            temp_id[k] = temp
        record = {}
        for k, v in rest_set.items():
            fw.write("ID\t")
            fw.write(str(k))
            fw.write("\n")
            record[k] = {}
            record[k]['round'] = 0
            for key, value in v.items():
                fw.write(str(key))
                fw.write("\n")
                record[k][key] = []
                for s in value:
                    s = extra_deal(s)
                    num = temp_id[key].index(s)
                    fw.write(str(num))
                    fw.write("\t")
                    fw.write(str(s))
                    add_item = [num, s['minValue'], s['maxValue']]
                    record[k][key].append(add_item)
                    fw.write("\n")
                if len(record[k][key]) > 0:
                    w_temp = np.array(record[k][key])
                    idex = np.lexsort([w_temp[:, 0]])
                    sorted_data = w_temp[idex, :]
                    record[k][key] = sorted_data.tolist()
    print(record)

    return record


# res_record = write_layer_clu(6, 2)
# res_record = write_layer_clu(7, 2)
# res_record = write_layer_clu(8, 2)
# res_record = write_layer_clu(9, 2)
# res_record = write_layer_clu(11, 2)
# res_record = write_layer_clu(12, 2)

for j in range(3, 7):
    for i in range(1, 9):
        res_record = write_layer_clu(i, 2, j)



# for key, value in res_record.items():
#     res_record[key]['round'] = res_record[key]['round'] + 1
#     if '餐馆' in res_record[key]:
#         if len(res_record[key]['餐馆']) == 2:
#             res_record[key]['round'] = res_record[key]['round'] + 2
#         else:
#             res_record[key]['round'] = res_record[key]['round'] + 1
#     if '酒店' in res_record[key]:
#         res_record[key]['round'] = res_record[key]['round'] + len(res_record[key]['酒店'])
# with open("./k2_Grc/final_res_k2_旅行_clu12.txt", 'w', encoding='utf-8') as fw:
#     for key, value in res_record.items():
#         fw.write(str(key))
#         fw.write("\t")
#         fw.write(str(res_record[key]['round'] + 4))
#         fw.write("\n")

# with open("fcm_layer2_clu8.txt", 'w', encoding='utf-8') as fw:
#     for key, value in res_record.items():
#         if '出租' not in res_record[key] and (is_exist_by_double_list(res_record[key]['景点'], 12) == False) and (
#                 is_exist_by_double_list(res_record[key]['景点'], 13) == False):
#             res_record[key]['round'] = res_record[key]['round'] + 1
#             res_record[key]['round'] = res_record[key]['round'] + 1
#             fw.write(str(key))
#             fw.write("\n")
#             fw.write(str(res_record[key]['景点']))
#             fw.write("\n")
#     fw.write("\n\n\n")
#     for key, value in res_record.items():
#         if '出租' not in res_record[key]:
#             if is_exist_by_double_list(res_record[key]['景点'], 12):
#                 res_record[key]['round'] = res_record[key]['round'] + 1
#                 res_record[key]['round'] = res_record[key]['round'] + 1
#                 fw.write(str(key))
#                 fw.write("\n")
#                 fw.write(str(res_record[key]['景点']))
#                 fw.write("\n")
#                 res_record[key]['round'] = res_record[key]['round'] + 2
#     fw.write("\n\n\n")
#     for key, value in res_record.items():
#         if '出租' not in res_record[key]:
#             if is_exist_by_double_list(res_record[key]['景点'], 13):
#                 res_record[key]['round'] = res_record[key]['round'] + 1
#                 res_record[key]['round'] = res_record[key]['round'] + 1
#                 fw.write(str(key))
#                 fw.write("\n")
#                 fw.write(str(res_record[key]['景点']))
#                 fw.write("\n")
#                 if is_exist_by_double_list(res_record[key]['景点'], 20):
#                     res_record[key]['round'] = res_record[key]['round'] + 2
#                 else:
#                     res_record[key]['round'] = res_record[key]['round'] + 1
#     fw.write("\n\n\n")
#     for key, value in res_record.items():
#         if '出租' in res_record[key]:
#             fw.write(str(key))
#             fw.write("\n")
#             fw.write(str(res_record[key]['景点']))
#             fw.write("\n")
#             res_record[key]['round'] = res_record[key]['round'] + 1
#             if is_exist_by_double_list(res_record[key]['景点'], 12):
#                 res_record[key]['round'] = res_record[key]['round'] + 2
#             else:
#                 res_record[key]['round'] = res_record[key]['round'] + 1
#     for key, value in res_record.items():
#         if '酒店' in res_record[key]:
#             res_record[key]['round'] = res_record[key]['round'] + len(res_record[key]['酒店'])
#         if '餐馆' in res_record[key]:
#             res_record[key]['round'] = res_record[key]['round'] + 1
#
#     with open("./k2_Grc/final_res_k2_旅行_clu8.txt", 'w', encoding='utf-8') as fw:
#         for key, value in res_record.items():
#             fw.write(str(key))
#             fw.write("\t")
#             fw.write(str(res_record[key]['round'] + 4))
#             fw.write("\n")

def from_top_to_bottom():
    with open("./k2_Grc/k2_content_layer2_旅行_clu5.json", 'r', encoding='utf-8') as fr:
        rps_set = json.load(fr)
    with open("./k2_Grc/final_res_k2_旅行_clu5.txt", 'w', encoding='utf-8') as fw:
        for i in rps_set:
            rps_id = i['info']['rpId']
            fw.write(str(rps_id))
            fw.write("\t")
            fw.write("5")
            fw.write("\n")


# from_top_to_bottom()


def analysize_grc(clu_id, record):
    file_path_3 = "grc_旅行_clu" + str(clu_id) + ".txt"
    file_path_4 = "grc_divide_clu" + str(clu_id) + ".txt"
    with open(file_path_3, 'w', encoding='utf-8') as fw:
        for key, value in record.items():
            fw.write(str(key))
            fw.write("\t")
            if '出租' not in record[key]:
                fw.write("0 0 0 0 ")
            else:
                for i in record[key]['出租']:
                    fw.write(str(i[1]))
                    fw.write(" ")
                    fw.write(str(i[2]))
                    fw.write(" ")
            if '景点' not in record[key]:
                fw.write("0 0 0 0 0 0")
            else:
                flag = 0
                for j in range(0, len(record[key]['景点'])):
                    if record[key]['景点'][j][0] < 13:
                        fw.write(str(record[key]['景点'][j][1]))
                        fw.write(" ")
                        fw.write(str(record[key]['景点'][j][2]))
                        fw.write(" ")
                        flag = 1
                        break
                if flag == 0:
                    fw.write(str(0))
                    fw.write(" ")
                    fw.write(str(6))
                    fw.write(" ")

                flag = 0
                for j in range(0, len(record[key]['景点'])):
                    if (record[key]['景点'][j][0] < 15) and (record[key]['景点'][j][0] > 12):
                        fw.write(str(record[key]['景点'][j][1]))
                        fw.write(" ")
                        fw.write(str(record[key]['景点'][j][2]))
                        fw.write(" ")
                        flag = 1
                        break
                if flag == 0:
                    fw.write(str(0))
                    fw.write(" ")
                    fw.write(str(5))
                    fw.write(" ")

                flag = 0
                for j in range(0, len(record[key]['景点'])):
                    if record[key]['景点'][j][0] > 14:
                        fw.write(str(record[key]['景点'][j][1]))
                        fw.write(" ")
                        fw.write(str(record[key]['景点'][j][2]))
                        fw.write(" ")
                        flag = 1
                        break
                if flag == 0:
                    fw.write(str(0))
                    fw.write(" ")
                    fw.write(str(9999))
                    fw.write(" ")

            fw.write("\n")
    with open(file_path_4, 'w', encoding='utf-8') as fw:
        for key, value in record.items():
            if '出租' not in record[key]:
                fw.write("0 0 0 0 ")
            else:
                for i in record[key]['出租']:
                    fw.write(str(i[1]))
                    fw.write(" ")
                    fw.write(str(i[2]))
                    fw.write(" ")
            if '景点' not in record[key]:
                fw.write("0 0 0 0 0 0")
            else:
                flag = 0
                for j in range(0, len(record[key]['景点'])):
                    if record[key]['景点'][j][0] < 13:
                        fw.write(str(record[key]['景点'][j][1]))
                        fw.write(" ")
                        fw.write(str(record[key]['景点'][j][2]))
                        fw.write(" ")
                        flag = 1
                        break
                if flag == 0:
                    fw.write(str(0))
                    fw.write(" ")
                    fw.write(str(6))
                    fw.write(" ")

                flag = 0
                for j in range(0, len(record[key]['景点'])):
                    if (record[key]['景点'][j][0] < 15) and (record[key]['景点'][j][0] > 12):
                        fw.write(str(record[key]['景点'][j][1]))
                        fw.write(" ")
                        fw.write(str(record[key]['景点'][j][2]))
                        fw.write(" ")
                        flag = 1
                        break
                if flag == 0:
                    fw.write(str(0))
                    fw.write(" ")
                    fw.write(str(5))
                    fw.write(" ")

                flag = 0
                for j in range(0, len(record[key]['景点'])):
                    if record[key]['景点'][j][0] > 14:
                        fw.write(str(record[key]['景点'][j][1]))
                        fw.write(" ")
                        fw.write(str(record[key]['景点'][j][2]))
                        fw.write(" ")
                        flag = 1
                        break
                if flag == 0:
                    fw.write(str(0))
                    fw.write(" ")
                    fw.write(str(9999))
                    fw.write(" ")
            fw.write("\n")


# write_layer_clu(3, 2)
# write_layer_clu(4, 2)
# write_layer_clu(5, 2)
# res_record = write_layer_clu(6, 2)
# analysize_grc(6, res_record)

# res_record = write_layer_clu(7, 2)
# res_record = write_layer_clu(7, 2)
# res_record = write_layer_clu(8, 3)

# res_record = write_layer_clu(8, 2)
