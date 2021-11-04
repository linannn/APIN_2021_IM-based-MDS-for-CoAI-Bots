#!/usr/bin/env python
# coding:utf-8
# encoding: utf-8
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/11 20:57
# @Author  : junruit
# @File    : Grc_requirement_pattern.py
# @desc: PyCharm
'''
import json


def calculate_grc_top(support):
    file_path = "./k" + str(support) + "_Grc/k" + str(support) + "_content_旅行.json"
    with open(file_path, 'r', encoding='utf-8') as fr:
        rps_db = json.load(fr)
    cluster_record = {}
    for rp in rps_db:
        rpid, rp_t_min, rp_t_max, rp_p_min, rp_p_max, rp_s_min, rp_s_max = calculate_rp_feature(rp)
        rp_s_min = 5 * rp_s_min / rp_s_max
        cluster_record[rpid] = [rp_t_min, rp_t_max, rp_p_min, rp_p_max, rp_s_min, 5]

    return cluster_record


def calculate_rp_feature(rp):
    content_set = []
    content_layer_2 = ['出租', '景点', '酒店', '餐馆', '地铁']
    rp_data = rp['data'][0]
    rp_id = rp['info']['rpId']
    rp_second = rp_data['children']
    rp_time_min = 0
    rp_time_max = 0
    rp_price_min = 0
    rp_price_max = 0
    rp_star_min = 0
    rp_star_max = 0
    for node in rp_second:
        content = node['goal']['content']
        content_set.append(content)
    if (len(content_set) == 0) or ((content_layer_2[1] not in content_set) and (content_layer_2[2] not in content_set) and (content_layer_2[3] not in content_set)):
        rp_time_min = 0
        rp_time_max = 99
        rp_price_min = 0
        rp_price_max = 999999
        rp_star_min = 0
        rp_star_max = 5
    else:
        for node in rp_second:
            rp_time_min, rp_time_max, rp_price_min, rp_price_max, rp_star_min, rp_star_max = children_node_calculate(node, rp_time_min, rp_time_max, rp_price_min, rp_price_max, rp_star_min, rp_star_max)

    return rp_id, rp_time_min, rp_time_max, rp_price_min, rp_price_max, rp_star_min, rp_star_max


def find_restrict(restricts_set, key):
    for i in restricts_set:
        if i['key'] == key:
            return i


def is_chinese(uchar):
    """判断一个unicode是否是汉字"""
    if (uchar >= u'\u4e00') and (uchar <= u'\u9fa5'):
        return True
    else:
        return False


def remove_chinese(str_in):
    str_out = ""
    for i in str_in:
        if is_chinese(i):
            pass
        else:
            str_out = str_out + i

    return str_out


def translate(object):
    if type(object) == str:
        object = remove_chinese(object)
        if len(object) > 0:
            return eval(object)
        else:
            return ""
    else:
        return object


def children_node_calculate(rp_child, rp_time_min, rp_time_max, rp_price_min, rp_price_max, rp_star_min, rp_star_max):
    content_layer_2 = ['出租', '景点', '酒店', '餐馆', '地铁']
    content = rp_child['goal']['content']
    restricts = rp_child['goal']['restricts']
    key_set = []
    for restrict in restricts:
        if restrict['key'] not in key_set:
            key_set.append(restrict['key'])
    if content == content_layer_2[1]:

        if "游玩时间" in key_set:
            key_restrict = find_restrict(restricts, "游玩时间")
            if key_restrict['valueType'] == "region":
                rp_time_min = rp_time_min + translate(key_restrict['minValue'])
                rp_time_max = rp_time_max + translate(key_restrict['maxValue'])
            elif key_restrict['valueType'] == "enum":
                rp_time_min = rp_time_min + translate(remove_chinese(key_restrict['value']))
                rp_time_max = rp_time_max + translate(remove_chinese(key_restrict['value']))
        else:
            rp_time_min = rp_time_min + 0
            # 基于数据的结论
            rp_time_max = rp_time_max + 6

        if "门票" in key_set:
            key_restrict = find_restrict(restricts, "门票")
            if key_restrict['valueType'] == "region":
                rp_price_min = rp_price_min + translate(key_restrict['minValue'])
                rp_price_max = rp_price_max + translate(key_restrict['maxValue'])
            else:
                print(key_restrict)
                rp_price_min = rp_price_min + 0
                # 基于数据的结论
                rp_price_max = rp_price_max + 9999
        else:
            rp_price_min = rp_price_min + 0
            # 基于数据的结论
            rp_price_max = rp_price_max + 9999

        if '评分' in key_set:
            key_restrict = find_restrict(restricts, '评分')
            if key_restrict['valueType'] == "region":
                rp_star_min = rp_star_min + translate(key_restrict['minValue'])
                # rp_star_max = rp_star_max + key_restrict['maxValue']
                rp_star_max = rp_star_max + 5
            elif key_restrict['valueType'] == "enum":
                rp_star_min = rp_star_min + translate(remove_chinese(key_restrict['value']))
                rp_star_max = rp_star_max + translate(remove_chinese(key_restrict['value']))
        else:
            rp_star_min = rp_star_min + 4
            # 基于数据的结论
            rp_star_max = rp_star_max + 5

    elif content == content_layer_2[2]:
        if "价格" in key_set:
            key_restrict = find_restrict(restricts, "价格")
            if key_restrict['valueType'] == "region":
                rp_price_min = rp_price_min + translate(key_restrict['minValue'])
                rp_price_max = rp_price_max + translate(key_restrict['maxValue'])
            elif key_restrict['valueType'] == "enum":
                rp_price_min = rp_price_min + translate(remove_chinese(key_restrict['value']))
                rp_price_max = rp_price_max + translate(remove_chinese(key_restrict['value']))
        else:
            rp_price_min = rp_price_min + 0
            # 基于数据的结论
            rp_price_max = rp_price_max + 9999

        if '评分' in key_set:
            key_restrict = find_restrict(restricts, '评分')
            if key_restrict['valueType'] == "region":
                rp_star_min = rp_star_min + translate(key_restrict['minValue'])
                # rp_star_max = rp_star_max + key_restrict['maxValue']
                rp_star_max = rp_star_max + 5
            elif key_restrict['valueType'] == "enum":
                rp_star_min = rp_star_min + translate(remove_chinese(key_restrict['value']))
                rp_star_max = rp_star_max + translate(remove_chinese(key_restrict['value']))
        else:
            rp_star_min = rp_star_min + 4
            # 基于数据的结论
            rp_star_max = rp_star_max + 5

    elif content == content_layer_2[3]:
        if '人均消费' in key_set:
            key_restrict = find_restrict(restricts, '人均消费')
            if key_restrict['valueType'] == "region":
                rp_price_min = rp_price_min + translate(key_restrict['minValue'])
                rp_price_max = rp_price_max + translate(key_restrict['maxValue'])
            elif key_restrict['valueType'] == "enum":
                rp_price_min = rp_price_min + translate(remove_chinese(key_restrict['value']))
                rp_price_max = rp_price_max + translate(remove_chinese(key_restrict['value']))
        else:
            rp_price_min = rp_price_min + 50
            # 基于数据的结论
            rp_price_max = rp_price_max + 150

        if '评分' in key_set:
            key_restrict = find_restrict(restricts, '评分')
            if key_restrict['valueType'] == "region":
                rp_star_min = rp_star_min + translate(key_restrict['minValue'])
                # rp_star_max = rp_star_max + key_restrict['maxValue']
                rp_star_max = rp_star_max + 5
            elif key_restrict['valueType'] == "enum":
                print(key_restrict['value'])
                if type(translate(remove_chinese(key_restrict['value']))) != str:
                    rp_star_min = rp_star_min + translate(remove_chinese(key_restrict['value']))
                    rp_star_max = rp_star_max + translate(remove_chinese(key_restrict['value']))
                else:
                    rp_star_min = rp_star_min + 0
                    rp_star_max = rp_star_max + 5
        else:
            rp_star_min = rp_star_min + 4
            # 基于数据的结论
            rp_star_max = rp_star_max + 5

    return rp_time_min, rp_time_max, rp_price_min, rp_price_max, rp_star_min, rp_star_max


def top_grc_write():
    result_record = calculate_grc_top(2)
    file_path = "./top_grc/top_grc_result_k2.json"
    file_path_fcm = "./top_grc/top_grc_fcm_k2.txt"
    file_path_record = "./top_grc/record_top_grc_k2.txt"
    with open(file_path, 'w', encoding='utf-8') as fw:
        json.dump(result_record, fw)
    with open(file_path_fcm, 'w', encoding='utf-8') as fw2:
        for k in result_record:
            for v in result_record[k]:
                fw2.write(str(v))
                fw2.write(" ")
            fw2.write("\n")
    with open(file_path_record, 'w', encoding='utf-8') as fw3:
        fw3.write("No\tID\tGrc time_min time_max price_min price_max star_min star_max\n")
        num = 0
        for k in result_record:
            num = num + 1
            fw3.write(str(num))
            fw3.write("\t")
            fw3.write(str(k))
            fw3.write("\t")
            for v in result_record[k]:
                fw3.write(str(v))
                fw3.write(" ")
            fw3.write("\n")


def fetch_res(id_t):
    with open("./top_grc/record_top_grc_k2.txt", 'r', encoding='utf-8') as fr1:
        sentence = fr1.readline()

        sentence = fr1.readline()
        num = 0
        while sentence:
            if num == id_t:
                list_divide = sentence.split("\t")
                return list_divide[2]
            sentence = fr1.readline()
            num = num + 1


def grc_res_show():
    file_path = "./top_grc/divide_top_k_2.txt"
    with open("./top_grc/record_top_grc_show_k2_whole.txt", 'w', encoding='utf-8') as fw:
        with open(file_path, 'r', encoding='utf-8') as fr:
            num = 0
            sentence = fr.readline()
            while sentence:
                num = num + 1
                res_set = []
                id_list = eval(sentence)
                for i in id_list:
                    res_line = fetch_res(i)
                    if res_line not in res_set:
                        res_set.append(res_line)
                for j in res_set:
                    fw.write(j)
                    fw.write("\n")
                fw.write(str(len(id_list)))
                fw.write("\t")
                fw.write(str(len(res_set)))
                fw.write("\n\n")
                file_write = "./top_grc/record_top_grc_show_k2_" + str(num) + ".txt"
                with open(file_write, 'w', encoding='utf-8') as fww:
                    for j in res_set:
                        fww.write(j)
                sentence = fr.readline()


def grc_res_show_child(mode):
    file_path = "./top_grc/divide_top_k2_" + str(mode) + ".txt"
    with open(file_path, 'r', encoding='utf-8') as fr:
        num = 0
        sentence = fr.readline()
        while sentence:
            num = num + 1
            res_set = []
            id_list = eval(sentence)
            for i in id_list:
                res_line = fetch_res(i)
                if res_line not in res_set:
                    res_set.append(res_line)
            file_write = "./top_grc/record_top_grc_show_k2_" + str(mode) + "_" + str(num) + ".txt"
            with open(file_write, 'w', encoding='utf-8') as fww:
                for j in res_set:
                    fww.write(j)
            sentence = fr.readline()


# top_grc_write()
# grc_res_show()
for i in range(2, 5):
    grc_res_show_child(i)
