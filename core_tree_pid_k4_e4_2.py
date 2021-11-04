#!/usr/bin/env python

# encoding: utf-8
from base_rp_db import *
from base_content_and_service_kg import *
import requests
import json
import logging
import sys
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/14 16:25
# @Author  : junruit
# @File    : core_tree.py
# @desc: PyCharm
'''
# todo print+"\n"


def calculate_depth_of_the_baseline():
    depth = 0
    # todo
    return depth


def calculate_width_of_the_baseline():
    width = 0

    return width


# TODO finish the combination of amounts of rp-tree s
def content_rp_tree_combine():

    return


# dict = {{'pro':{'housekeeper'},'price':{'low'},'gender':{'woman'},'age':{'young'}},{'org':{'abc'}}}
# extract core intent of user from the result of NLU module
# [housekeeper,abc]
def core_extract(dict):
    core_group = []
    for each_intent in dict:
        core = []
        if 'pro' in each_intent.keys():
            for pro in each_intent['pro']:
                core.append(pro)
        if 'org' in each_intent.keys():
            for org in each_intent['org']:
                core.append(org)
        if len(core) > 0:
            # core_group.append(core)
            core_group.extend(core)
    return core_group


# define whether can found the requirement pattern in rp_database for baseline on rp_tree setting up
def find_rp(content, support):
    # todo switch of two mode
    # base on 大服务平台
    # url = "http://require-linan.192.168.42.159.nip.io/require/api/search-rp?detail="+content
    # response = requests.get(url)
    # respon_json = json.loads(response.content)
    # if respon_json:
    #     return True
    # else:
    #     return False

    rest_set, child_set = get_res_con_set_for_one_time(support)
    # base on client test
    if content in rest_set:
        return True
    else:
        return False


def print_in_file(content, grc, support, mode, test_id):
    print(sys._getframe().f_code.co_filename)  # 当前文件名，可以通过__file__获得
    # print(sys._getframe(0).f_code.co_name)  # 当前函数名
    print(sys._getframe(1).f_code.co_name)  # 调用该函数的函数名字，如果没有被调用，则返回<module>
    # print(sys._getframe(0).f_lineno)  # 当前函数的行号
    print(sys._getframe(1).f_lineno)  # 调用该函数的行号
    if grc == 0:
        file_name = "./out_dia_process/k" + str(support) + "/" + mode_file[mode] + "_" + str(test_id) + ".txt"
    else:
        file_name = "./out_dia_process/k" + str(support) + "/e" + str(mode) + "/grc_" + str(test_id) + ".txt"
    with open(file_name, 'a+', encoding='utf-8') as fw:
        fw.write("-----------------------------------")
        fw.write(content)


def copy_file(a, b):
    with open(a, 'rb') as fr:
        sentence = fr.read()
    with open(b, 'wb') as fw:
        fw.write(sentence)

    return 0


def start_program(grc, support, mode, test_id):
    if grc == 0:
        file_name = "./out_dia_process/k" + str(support) + "/" + mode_file[mode] + "_" + str(test_id) + ".log"
    else:
        file_name = "./out_dia_process/k" + str(support) + "/e" + str(mode) + "/e" + str(mode) + "_grc_" + str(test_id) + ".log"

    logger = logging.getLogger()  # 实例化一个logger对象
    logger.setLevel(logging.DEBUG)  # 设置初始显示级别

    # 创建一个文件句柄
    file_handle = logging.FileHandler(file_name, encoding="utf-8-sig", mode='w')

    # 创建一个流句柄
    # stream_handle = logging.StreamHandler()

    # 创建一个输出格式
    fmt = logging.Formatter(f"{'-' * 40}\n"
                            "> %(asctime)s - %(levelname)s - %(filename)s - "
                            "[line:%(lineno)d] -"
                            "  %(message)s\n",
                            datefmt="%a, %d %b %Y"
                                    "%H:%M:%S"
                            )

    file_handle.setFormatter(fmt)  # 文件句柄设置格式
    # stream_handle.setFormatter(fmt)  # 流句柄设置格式

    logger.addHandler(file_handle)  # logger对象绑定文件句柄
    # logger.addHandler(stream_handle)  # logger对象绑定流句柄

    # logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s', filename=file_name,
    #                     filemode='w', encoding='utf-8')
    logging.info('Start of program')

    print("test_id:\n")
    print(test_id)
    logging.info("test_id:\n")
    logging.info(test_id)

    str_out = "------Round:1---------\n"
    print(str_out)
    logging.info(str_out)
    # print("您好，很高兴为您服务\n")
    logging.debug("您好，很高兴为您服务")
    # First round user intention
    # user_input = input()
    user_input = ""
    # print("USER: 我要去旅行\n")
    logging.debug("USER: 我要去旅行")
    # change the user input into intention Array

    intent_list = intent_bert(user_input)
    # extract the core intent as root-baseline
    core_intent = core_extract(intent_list)
    # print(core_intent)
    rp_tree_set = []
    for ci in core_intent:
        # 开局需求模式库中存在对于意图树
        # (content, support)
        if (find_rp(ci, support)) and (grc == 0):
            # mode 0-no-rp; 1-con-kg; 2-mod-rpdb; 3-ran-rpdb; 4-mod-rpdb+kg; 5-ran-rpdb+kg;
            # content, mode, support, round, test_id, hit_content
            model_tree, generate_tree, round, hit_content = rptree_setup_based_rpdb(ci, mode, support, 1, test_id, 0)
            rp_tree_set.append(model_tree)
            # print("round:")
            # print(round)
            # print("hit_content:")
            # print(hit_content)
            logging.info(test_id)
        # 在无法匹配的条件下直接执行free_qa
        else:
            # mode 4-grc-bt 5-grc-tb
            # content, mode, support, round, test_id, hit_content
            model_tree, generate_tree, round, hit_content = rptree_setup_based_grc(ci, mode, support, 1, test_id, 1)
            rp_tree_set.append(model_tree)
            logging.info(test_id)

    # print("--------对话已结束------------\n")
    logging.info("--------对话已结束------------")
    # rp_tree_result = content_rp_tree_combine()
    # msg = rp_tree_result
    msg = rp_tree_set
    # for generate_tree in rp_tree_set:
    #     print("Model Result:")
    #     print(generate_tree)
    logging.shutdown()
    if grc == 0:
        file_name_copy = "./out_dia_process/k" + str(support) + "/" + mode_file[mode] + "_" + str(test_id) + "_final.log"
    else:
        file_name_copy = "./out_dia_process/k" + str(support) + "/e" + str(mode) + "/e" + str(mode) + "_grc_" + str(test_id) + "_final.log"
    copy_file(file_name, file_name_copy)
    return round, hit_content


def e0_write(support, grc, mode, a, b):
    with open("./experiment_result/e0_without_rp_res_5508_" + str(a) + "_" + str(b) + ".txt", 'w', encoding='utf-8') as f1:
        str_tab_1 = "No"
        str_tab_2 = "Content_num"
        str_tab_3 = "Round"
        str_tab_4 = "cover"
        f1.write('{:^10}{:^10}{:^10}{:^10}'.format(str_tab_1, str_tab_2, str_tab_3, str_tab_4))
        f1.write("\n")
        for test_id in range(a, b):
            round, hit_content = start_program(grc, support, mode, test_id)
            ori_content = record[test_id - 1]
            f1.write('{:^10}{:^10}{:^10}{:^10}'.format(str(test_id), str(ori_content), str(round), "1.0"))
            f1.write("\n")

    return 0


def e1_write(support, grc, mode, a, b):
    with open("./experiment_result/e1_with_kg_res_5508_" + str(a) + "_" + str(b) + ".txt", 'w', encoding='utf-8') as f1:
        f1.write('{:^10}{:^10}{:^15}{:^15}{:^15}{:^15}'.format("NO.", "Round", "Ori_Content", "Lack_Content",
                                                               "Extra_Content", "Final_Cover"))
        f1.write("\n")
        for test_id in range(a, b):
            round, hit_content = start_program(grc, support, mode, test_id)
            ori_content = record[test_id - 1]
            # f1.write(str_e1)
            f1.write('{:^10}{:^10}{:^15}{:^15}{:^15}{:^15}'.format(str(test_id), str(round), str(ori_content),
                                                                   str(ori_content - hit_content),
                                                                   str(0),
                                                                   str(hit_content / ori_content)))
            f1.write("\n")

    return 0


def e2_write(support, grc, mode, a, b):
    with open("./experiment_result/k" + str(support) + "/" + str(mode_file[mode]) + "_" + str(a) + "_" + str(b) + ".txt", 'w', encoding='utf-8') as f1:
        f1.write('{:^10}{:^10}{:^15}{:^15}{:^15}{:^15}'.format("NO.", "Round", "Ori_Content", "Lack_Content",
                                                               "Extra_Content", "Final_Cover"))
        f1.write("\n")
        for test_id in range(a, b):
            round, hit_content = start_program(grc, support, mode, test_id)
            ori_content = record[test_id - 1]
            # f1.write(str_e1)
            f1.write('{:^10}{:^10}{:^15}{:^15}{:^15}{:^15}'.format(str(test_id), str(round), str(ori_content),
                                                                   str(ori_content - hit_content),
                                                                   str(0),
                                                                   str(hit_content / ori_content)))
            f1.write("\n")

    return 0


def e4_e5_write(support, grc, mode, a, b):
    if mode == 4:
        path = "e4/e4_grc_tb"
    elif mode == 5:
        path = "e5/e5_grc_bt"
    with open("./experiment_result/k" + str(support) + "/" + str(path) + "_" + str(a) + "_" + str(b) + ".txt", 'w', encoding='utf-8') as f1:
        f1.write('{:^10}{:^10}{:^15}{:^15}{:^15}{:^15}'.format("NO.", "Round", "Ori_Content", "Lack_Content",
                                                               "Extra_Content", "Final_Cover"))
        f1.write("\n")
        for test_id in range(a, b):
            print(test_id)
            round, hit_content = start_program(grc, support, mode, test_id)
            ori_content = record[test_id - 1]
            # f1.write(str_e1)
            f1.write('{:^10}{:^10}{:^15}{:^15}{:^15}{:^15}'.format(str(test_id), str(round), str(ori_content),
                                                                   str(ori_content - hit_content),
                                                                   str(0),
                                                                   str(hit_content / ori_content)))
            f1.write("\n")

    return 0


with open("e0_content_num_record.txt", 'r', encoding='utf-8') as ff:
    record = eval(ff.read())
# mode 0-no-rp; 1-con-kg; 2-mod-rpdb; 3-ran-rpdb; 4-mod-rpdb+kg; 5-ran-rpdb+kg;
mode_file = ["e0/e0_no_rp", "e1/e1_con_kg", "e2/e2_mod_rpdb", "e2/e2_ran_rpdb", "e3/e3_mod_rp_kg", "e3/e3_ran_rp_kg"]
# mode = 0
# test_id from 1 to 5507
# test_id = 1
# support k = 2; 3; 4; 5; 6
# support = 2
# use grc mode or not ; mode 4-grc-bt; 5-grc-tb
# grc = 0
for support in range(4, 5):
    for grc in range(1, 2):
            # a = [1, 1001, 2001, 3001, 4001, 5001]
            # b = [1001, 2001, 3001, 4001, 5001, 5508]
            begin_id = 1
            end_id = 5508
            # e0_write(support, grc, 0, begin_id, end_id)
            # e1_write(support, grc, 1, a[5], b[5])
            # e2_write(support, grc, 4, begin_id, end_id)
            # e1_write(support, grc, 1, begin_id, end_id)
            e4_e5_write(support, grc, 4, 3001, end_id)
            # e4_e5_write(support, grc, 5, begin_id, end_id)

