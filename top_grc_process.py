#!/usr/bin/env python
# coding: utf-8
# encoding: utf-8
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/13 11:07
# @Author  : junruit
# @File    : top_grc_process.py
# @desc: PyCharm
'''
from base_content_and_service_kg import get_rptree_test
from base_content_and_service_kg import test_tree_con_set_for_one_time
from base_content_and_service_kg import ask_for_layer_2
from base_content_and_service_kg import fetch_class
from base_content_and_service_kg import layer_2_cluster
from base_content_and_service_kg import calculate_rps_length
import json
import random
import logging
from Grc_requirement_pattern import children_node_calculate


def calculate_feature(rp_data):
    content_set = []
    content_layer_2 = ['出租', '景点', '酒店', '餐馆', '地铁']
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
    if (len(content_set) == 0) or (
            (content_layer_2[1] not in content_set) and (content_layer_2[2] not in content_set) and (
            content_layer_2[3] not in content_set)):
        rp_time_min = 0
        rp_time_max = 99
        rp_price_min = 0
        rp_price_max = 999999
        rp_star_min = 0
        rp_star_max = 5
    else:
        for node in rp_second:
            rp_time_min, rp_time_max, rp_price_min, rp_price_max, rp_star_min, rp_star_max = children_node_calculate(
                node, rp_time_min, rp_time_max, rp_price_min, rp_price_max, rp_star_min, rp_star_max)

    return rp_time_min, rp_time_max, rp_price_min, rp_price_max, rp_star_min, rp_star_max


def ask_top(round, rp_test, hit_content):
    round = round + 1
    str_out = "---------------------Round:" + str(round) + "-----------\n"
    # print(str_out)
    logging.info(str_out)

    str_out = "----To User:你对整个旅行的花费要求是多少？高档>20000; 中档1-2w; 低档<1w------\n"
    # print(str_out)
    logging.debug(str_out)
    # hit_content = hit_content + 1

    rp_time_min, rp_time_max, rp_price_min, rp_price_max, rp_star_min, rp_star_max = calculate_feature(rp_test)
    rp_star_min = 5 * rp_star_min / rp_star_max
    str_out = "----USER:" + str(rp_price_min) + "到" + str(rp_price_max) + "之间吧------\n"
    logging.debug(str_out)

    round = round + 1
    str_out = "---------------------Round:" + str(round) + "-----------\n"
    # print(str_out)
    logging.info(str_out)

    str_out = "----To User:你对整个旅行的档次要求是多少？高5-5 中4.5-5 低4.0-4.5------\n"
    # print(str_out)
    logging.info(str_out)

    str_out = "----USER:" + str(rp_star_min) + "吧------\n"
    logging.debug(str_out)
    # hit_content = hit_content + 1

    if rp_time_max > 0:
        round = round + 1
        str_out = "---------------------Round:" + str(round) + "-----------\n"
        # print(str_out)
        logging.info(str_out)

        str_out = "----To User:你对整个旅行景点游玩时长的要求？高6 中2-4 低<2------\n"
        # print(str_out)
        logging.info(str_out)
        # hit_content = hit_content + 1
        str_out = "----USER:" + str(rp_time_min) + "到" + str(rp_time_max) + "之间吧------\n"
        logging.debug(str_out)

    return round, hit_content


def granule_tree(tree):
    layer_3 = 0
    queue = [tree]
    # print(queue)
    layer = 0
    while len(queue) > 0:
        layer_3 = len(queue)
        layer = layer + 1
        children_nodes_set = []
        for j in queue:
            children_nodes = j['children']
            children_nodes_set.extend(children_nodes)
        queue = children_nodes_set
        # print(queue)
    # print("layer:")
    # print(layer)
    # print("layer_3:")
    # print(layer_3)
    return layer, layer_3


def rptree_setup_top_grc(content, mode, support, round, test_id, hit_content):
    record_test = get_rptree_test(test_id)
    test_tree_rest_set, test_tree_child_set = test_tree_con_set_for_one_time(record_test)
    content_layer_2 = ['出租', '景点', '酒店', '餐馆', '地铁']
    test_layer_2 = [-1, -1, -1, -1, -1]
    round, hit_content = ask_top(round, record_test, hit_content)
    fine_tune_turn, fine_tune_turn_layer_3 = granule_tree(record_test)
    # find the generated result
    if (mode == 4) or ((mode == 6) and (support == 2)):
        # array_content, array_test, begin, end, round, tree_rest_set
        round, test_layer_2, hit_content = ask_for_layer_2(content_layer_2, test_layer_2, 1, 4, round, test_tree_rest_set, hit_content)

        class_cluster = fetch_class(test_layer_2, support)
        logging.info("class_cluser:" + str(class_cluster))
        round_no, hit_content_no, rps_list = layer_2_cluster(5, support, class_cluster, test_tree_rest_set, round,
                                                       hit_content)

    logging.info("记录路径选取合适的需求树...-----")
    round = round + 1
    str_out = "---------------------Round:" + str(round) + "-----------\n"
    # print(str_out)
    logging.info(str_out)
    logging.info("输出对应路径符合要求的rp...XXXXXXXXXXXXXXX-----")
    str_out = "To User: 请根据上述对话搜索相应的需求树，请进行对应的修改-----\n"
    # print(str_out)
    logging.debug(str_out)

    str_out = "----USER: 我对的微调是XXXXXXX-----\n"
    logging.debug(str_out)
    logging.info("将用户意图与所示意图树的区别作为答案反馈给系统...----")
    if len(rps_list) == 0:
        file_path_2 = "./k" + str(support) + "_Grc/k" + str(support) + "_content_layer2_旅行_clu" + str(
            class_cluster) + ".json"
        with open(file_path_2, 'r', encoding='utf-8') as fr0:
            rps_list = json.load(fr0)
    model_tree = rps_list[random.randint(0, len(rps_list)-1)]
    recall = calculate_rps_length(model_tree)
    round = round + fine_tune_turn
    recall = recall + fine_tune_turn
    hit_content = hit_content + fine_tune_turn

    # layer-1, layer-2 make sure; layer-3 waiting for fine-tune
    if fine_tune_turn > 2:
        hit_content = hit_content + fine_tune_turn_layer_3
    if hit_content > recall:
        hit_content = recall

    # print(fine_tune_turn)
    # print(fine_tune_turn_layer_3)
    # print(hit_content)
    # print(recall)
    return round, hit_content, recall

