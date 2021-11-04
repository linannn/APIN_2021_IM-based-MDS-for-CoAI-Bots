#!/usr/bin/env python

# encoding: utf-8
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/14 16:27
# @Author  : junruit
# @File    : base_service_kg.py
# @desc: PyCharm
'''
import json
import logging
import random


def choose_top_k():
    # choose top k to recommendation
    return


# define recommendation in step 3
def rptree_setup_based_kg(content):

    choose_top_k()
    return


def new_node_search_in_content_kg(content):
    res = []

    return res


# 一次性取对应测试需求树中所有需求和对应约束
def test_tree_con_set_for_one_time(tree):
    child_set = {}
    restricts_set = {}

    queue = [tree]
    # children_nodes = test_sample['children']
    # children_content = []
    while len(queue) > 0:
        children_nodes_set = []
        for j in queue:
            content = j['goal']['content']
            restricts = j['goal']['restricts']
            if content not in child_set:
                # content_set[content]  [0]children [1]father
                child_set[content] = []
                restricts_set[content] = []
            restricts_set[content].extend(restricts)
            children_nodes = j['children']
            child_content = []
            for w in children_nodes:
                if w['goal']['content'] not in child_content:
                    child_content.append(w['goal']['content'])
            child_set[content].extend(child_content)
            children_nodes_set.extend(children_nodes)
        queue = children_nodes_set
    return restricts_set, child_set


def get_rptree_test(test_id):
    with open("./data/test_rptree_499.json", 'r', encoding='utf-8') as fr:
        # type = list, len = 200
        test_499 = json.load(fr)

    with open("./data/test_rptree_5008.json", 'r', encoding='utf-8') as fq:
        test_5008 = json.load(fq)

    num = 0
    for i in test_499:
        num = num + 1
        if num == test_id:
            return i
    for j in test_5008:
        num = num + 1
        if num == test_id:
            return j


def ask_for_layer_2(array_content, array_test, begin, end, round, tree_rest_set, hit_content):

    for i in range(begin, end):
        round = round + 1
        str_out = "---------------------Round:" + str(round) + "-----------\n"
        # print(str_out)
        logging.info(str_out)

        str_out = "----To User:你对" + str(array_content[i]) + "是否需要？------\n"
        # print(str_out)
        logging.debug(str_out)
        if array_content[i] in tree_rest_set:
            str_out = "----USER:需要------\n"
            # print(str_out)
            logging.debug(str_out)
            array_test[i] = 1
            hit_content = hit_content + 1
        else:
            str_out = "----USER:不需要------\n"
            # print(str_out)
            logging.debug(str_out)
            array_test[i] = 0

    return round, array_test, hit_content


def subset(list_a, list_b):
    flag = 0
    for i in list_a:
        if i in list_b:
            flag = flag + 1
        else:
            flag = flag - 1
    if flag == len(list_a):
        return 1
    elif flag == -len(list_a):
        return 2
    else:
        # print("有的在类，有的不在；一定出错\n")
        logging.warning("some in, some not, bug!")
        return -1


def sblist(list_a, list_b):
    in_set = []
    for i in range(0, len(list_b)):
        if list_b[i] == 1:
            in_set.append(i)
    for j in range(0, len(list_a)):
        if (list_a[j] == 1) and (j not in in_set):
            return 0
    return 1


def hit_subset(list_a, list_b):
    res = 0
    for i in list_a:
        if i in list_b:
            res = res + 1
    return res


# 找到符合测试树第二层状态的需求模式库对应cluster_id(k=2, 1-12)(k=3456,1-8)
def fetch_class(test_list, support):
    file_path = "./grc_epoch_" + str(support) + ".txt"
    rp_id_list = []
    order_id_list = []
    with open(file_path, 'r', encoding='utf-8') as fr:
        sentence = fr.readline()
        sentence = fr.readline()
        while sentence:
            temp_array = sentence.split("\t")
            temp_array[2] = eval(temp_array[2])
            if temp_array[2] == test_list:
                order_id_list.append(eval(temp_array[0]) - 1)
                rp_id_list.append(eval(temp_array[1]))
            sentence = fr.readline()
    if (len(order_id_list) == 0) and (len(rp_id_list) == 0):
        with open(file_path, 'r', encoding='utf-8') as fr:
            sentence = fr.readline()
            sentence = fr.readline()
            while sentence:
                temp_array = sentence.split("\t")
                temp_array[2] = eval(temp_array[2])
                if sblist(temp_array[2], test_list):
                    order_id_list.append(eval(temp_array[0]) - 1)
                    rp_id_list.append(eval(temp_array[1]))
                sentence = fr.readline()
        file_path_2 = "./k" + str(support) + "_Grc/divide_res_旅行" + str(support) + ".txt"
        cluster_hit = [0]
        with open(file_path_2, 'r', encoding='utf-8') as fr:
            sentence = fr.readline()
            cluster_id = 1
            while sentence:
                temp_array_class = eval(sentence)
                cluster_hit.append(hit_subset(order_id_list, temp_array_class))
                sentence = fr.readline()
                cluster_id = cluster_id + 1
        cluster_id = cluster_hit.index(max(cluster_hit))
        return cluster_id
    else:
        file_path_2 = "./k" + str(support) + "_Grc/divide_res_旅行" + str(support) + ".txt"
        with open(file_path_2, 'r', encoding='utf-8') as fr:
            sentence = fr.readline()
            cluster_id = 1
            while sentence:
                temp_array_class = eval(sentence)
                if subset(order_id_list, temp_array_class) == 1:
                    return cluster_id
                sentence = fr.readline()
                cluster_id = cluster_id + 1
            # print("-----cluster分类找不到出现错误-----\n")
            logging.warning("-----cluster分类找不到出现错误-----")
            return 0


def judge_content(t_child, hit_content, support):
    file_path = "./rp_db_content_set/k" + str(support) + "_content0.txt"
    with open(file_path, 'r', encoding='utf-8') as fr:
        passage = fr.read()
    if t_child in passage:
        hit_content = hit_content + 1
    return hit_content


def judge_in_restricts_key(content, key, rest_set):
    if content in rest_set:
        for i in rest_set[content]:
            if i['key'] == key:
                return i
        return 0
    # print("-------该layer2意图本身不被接受------\n")
    logging.warning("-------该layer2意图本身不被接受------")
    return -1


def restricts_filter_2(rps_list, restrict, content):
    # print("length rps:")
    # print(len(rps_list))
    logging.info("length rps:" + str(len(rps_list)))
    valuetype = restrict['valueType']
    key = restrict['key']
    minValue = restrict['minValue']
    maxValue = restrict['maxValue']
    value = restrict['value']
    res_list = []
    for i in rps_list:
        q = i['data'][0]
        rest_set, child_set = test_tree_con_set_for_one_time(q)
        key_set = []
        for j in rest_set[content]:
            if j['key'] not in key_set:
                key_set.append(j['key'])

            if j['valueType'] == "region":
                if (j['key'] == key) and (j['minValue'] == minValue) and (j['maxValue'] == maxValue):
                    res_list.append(i)
                    str_out = "---------filter" + str(content) + "/" + str(key) + "----筛选成功--\n"
                    # print(str_out)
                    logging.info(str_out)
                    break
            elif (j['valueType'] == "service-provider") or (j['valueType'] == "enum") or (j['valueType'] == "after"):
                if (j['key'] == key) and (j['value'] == value):
                    res_list.append(i)
                    str_out = "---------filter" + str(content) + "/" + str(key) + "----筛选成功--\n"
                    # print(str_out)
                    logging.info(str_out)
                    break

        if key not in key_set:
            res_list.append(i)
    # print(len(res_list))
    logging.info("length rps:" + str(len(res_list)))
    return res_list


def restricts_filter_3(rps_list, content, support):
    file_path = "./rp_db_content_set/k" + str(support) + "_content0.txt"
    with open(file_path, 'r', encoding='utf-8') as fr:
        passage = fr.read()
    if content in passage:
        # print("length rps:")
        # print(len(rps_list))
        logging.info("length rps:" + str(len(rps_list)))
        res_list = []
        for i in rps_list:
            q = i['data'][0]
            rest_set, child_set = test_tree_con_set_for_one_time(q)
            if content in rest_set:
                res_list.append(i)
                str_out = "---------filter" + str(content) + "----筛选成功--\n"
                # print(str_out)
                logging.info(str_out)
                break
        return res_list
    else:
        return rps_list


# todo 详细grc路径划分
def layer_2_cluster(mode, support, cluster_id, test_rest_set, round, hit_content):
    file_path = "./k" + str(support) + "_rule/" + str(mode) + "/cluster_" + str(cluster_id) + ".txt"
    file_path_2 = "./k" + str(support) + "_Grc/k" + str(support) + "_content_layer2_旅行_clu" + str(cluster_id) + ".json"
    with open(file_path_2, 'r', encoding='utf-8') as fr0:
        rps_list = json.load(fr0)
    with open(file_path, 'r', encoding='utf-8') as fr:
        sentence = fr.readline()
        while sentence:
            divide_list = sentence.split("\t")
            restricts_sentence = divide_list[2].replace(" ", "/")
            round = round + 1
            str_out = "----------Round:" + str(round) + "----------\n"
            # print(str_out)
            logging.info(str_out)
            str_out = "To User: 对于" + divide_list[0] + "的" + str(divide_list[1]) + ",您有什么选择" + str(restricts_sentence) +"\n"
            # print(str_out)
            logging.debug(str_out)
            if judge_in_restricts_key(divide_list[0], divide_list[1], test_rest_set) == 0:
                str_out = "USER: 我无所谓\n"
                # print(str_out)
                logging.debug(str_out)
            elif (judge_in_restricts_key(divide_list[0], divide_list[1], test_rest_set) != -1) and (judge_in_restricts_key(divide_list[0], divide_list[1], test_rest_set) != 0):
                e_res = judge_in_restricts_key(divide_list[0], divide_list[1], test_rest_set)
                rps_list = restricts_filter_2(rps_list, e_res, divide_list[0])
                valuetype = e_res['valueType']
                if valuetype == "region":
                    minValue = int(e_res['minValue'])
                    maxValue = int(e_res['maxValue'])
                    key = e_res['key']
                    unit = e_res['unit']
                    str_1 = divide_list[0] + "的" + key + "范围, " + str(minValue) + "到" + str(maxValue) + unit + "\n"
                    # print(str_1)
                    logging.debug(str_out)
                elif (valuetype == "service-provider") or (valuetype == "enum") or (valuetype == "after"):
                    value = e_res['value']
                    key = e_res['key']
                    str_1 = divide_list[0] + "的" + key + "：" + value + "\n"
                    # print(str_1)
                    logging.debug(str_out)
            sentence = fr.readline()
    # print("--------layer2--restricts询问结束------------")
    str_out = "----------layer2--restricts询问结束----------"
    logging.info(str_out)
    return round, hit_content, rps_list


def calculate_rps_length(rp):
    length = len(str(rp).split("content")) - 1
    return length


# 4-grc-bottom-to-top 5-grc-top-to-bottom
# content, mode, support, round, test_id, hit_content
def rptree_setup_based_grc(content, mode, support, round, test_id, hit_content):
    record_test = get_rptree_test(test_id)
    test_tree_rest_set, test_tree_child_set = test_tree_con_set_for_one_time(record_test)
    content_layer_2 = ['出租', '景点', '酒店', '餐馆', '地铁']
    test_layer_2 = [-1, -1, -1, -1, -1]
    if (mode == 4) or ((mode == 5) and (support == 2)):
        # array_content, array_test, begin, end, round, tree_rest_set
        round, test_layer_2, hit_content = ask_for_layer_2(content_layer_2, test_layer_2, 0, len(content_layer_2), round, test_tree_rest_set, hit_content)

    elif (mode == 5) and (support != 2):
        test_layer_2[0] = 0
        test_layer_2[4] = 0
        round, test_layer_2, hit_content = ask_for_layer_2(content_layer_2, test_layer_2, 1, 4, round, test_tree_rest_set, hit_content)

    # print("layer_2:")
    # print(test_layer_2)
    logging.info("layer_2:" + str(test_layer_2))

    # class_cluster type = arraylist
    class_cluster = fetch_class(test_layer_2, support)
    # print("class_cluster")
    # print(class_cluster)
    # ==============================================
    logging.info("class_cluser:" + str(class_cluster))

    round, hit_content, rps_list = layer_2_cluster(mode, support, class_cluster, test_tree_rest_set, round, hit_content)

    # print(len(rps_list))
    logging.info("rps_list:" + str(len(rps_list)))
    # layer3部分
    # 酒店的子需求
    if test_layer_2[2] == 1:
        round = round + 1
        str_out = "----------Round:" + str(round) + "----------\n"
        # print(str_out)
        logging.info(str_out)
        str_out = "To User: 对于酒店,您有什么子需求？\n"
        # print(str_out)
        logging.debug(str_out)
        child_content = test_tree_child_set['酒店']
        if len(child_content) == 0:
            str_out = "----USER: 我不需要-----\n"
            # print(str_out)
            logging.debug(str_out)
        else:
            for t_child in child_content:
                str_out = "----User:我还需要" + str(t_child) + "\n"
                # print(str_out)
                logging.debug(str_out)
                hit_content = judge_content(t_child, hit_content, support)
                rps_list = restricts_filter_3(rps_list, t_child, support)
                # extra_node = setup_extra_node(t_child)
                # children_nodes.append(extra_node)
                round = round + 1
                str_out = "----------Round:" + str(round) + "----------\n"
                # print(str_out)
                logging.info(str_out)
                str_out = "To User: 请问对于" + str(content) + "意图有什么其他的子需求吗,需求知识图谱为您推荐...-----\n"
                # print(str_out)
                logging.debug(str_out)
            str_out = "----USER: 没了-----\n"
            # print(str_out)
            logging.debug(str_out)
    if support == 2:
        if test_layer_2[3] == 1:
            round = round + 1
            str_out = "----------Round:" + str(round) + "----------\n"
            # print(str_out)
            logging.info(str_out)
            str_out = "To User: 对于餐馆,您有什么子需求？\n"
            # print(str_out)
            logging.debug(str_out)
            child_content = test_tree_child_set['餐馆']
            if len(child_content) == 0:
                str_out = "----USER: 没了-----\n"
                # print(str_out)
                logging.debug(str_out)
            else:
                for t_child in child_content:
                    str_out = "我还需要" + str(t_child) + "\n"
                    # print(str_out)
                    logging.debug(str_out)
                    hit_content = judge_content(t_child, hit_content, support)
                    rps_list = restricts_filter_3(rps_list, t_child, support)
                    # extra_node = setup_extra_node(t_child)
                    # children_nodes.append(extra_node)
                    round = round + 1
                    str_out = "----------Round:" + str(round) + "----------\n"
                    # print(str_out)
                    logging.info(str_out)
                    str_out = "To User: 请问对于" + str(content) + "意图有什么其他的子需求吗,需求知识图谱为您推荐...-----\n"
                    # print(str_out)
                    logging.debug(str_out)
                str_out = "----USER: 没了-----\n"
                # print(str_out)
                logging.debug(str_out)

    # print("--------layer3询问结束---------\n")
    logging.info("--------layer3询问结束---------")
    # print("记录路径选取合适的需求树...-----\n")
    logging.info("记录路径选取合适的需求树...-----")
    round = round + 1
    str_out = "----------Round:" + str(round) + "----------\n"
    # print(str_out)
    logging.info(str_out)
    str_out = "To User: 根据上述对话搜索相应的需求树，请进行对应的修改-----\n"
    # print(str_out)
    logging.debug(str_out)
    if len(rps_list) == 0:
        file_path_2 = "./k" + str(support) + "_Grc/k" + str(support) + "_content_layer2_旅行_clu" + str(
            class_cluster) + ".json"
        with open(file_path_2, 'r', encoding='utf-8') as fr0:
            rps_list = json.load(fr0)
    for m in rps_list:
        recall = calculate_rps_length(m)

        pass
    logging.info("rps_list length:" + str(len(rps_list)))
    str_out = "User: 我的修改意见是....\n"
    # print(str_out)
    logging.debug(str_out)

    model_tree = rps_list[random.randint(0, len(rps_list)-1)]
    recall = calculate_rps_length(model_tree)
    print("recall")
    print(recall)
    generate_tree = record_test
    return model_tree, generate_tree, round, hit_content, recall
