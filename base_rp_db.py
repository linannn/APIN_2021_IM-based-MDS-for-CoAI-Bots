#!/usr/bin/env python
# encoding: utf-8

'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/14 16:26
# @Author  : junruit
# @File    : base_rp_db.py
# @desc: PyCharm
'''

import requests
import json
import heapq
from datetime import datetime
import os
import logging
from intent_recognition import *
from base_content_and_service_kg import *
import random


extra_child_node = {
                "id": 1842,
                "goal": {
                    "goalId": 1842,
                    "content": "餐馆",
                    "parentId": 1840,
                    "requireId": 194,
                    "restricts": [],
                    "optTargets": [],
                    "hasMatched": "false",
                    "rpId": -1
                },
                "children": []
            }


class StackUnderflow(ValueError):
    # 栈下溢(空栈访问)
    pass


class Stack(object):
    """栈"""
    def __init__(self):
        self.items = []

    def is_empty(self):
        """判断是否为空"""
        return self.items == []

    def push(self, item):
        """加入元素"""
        self.items.append(item)

    def pop(self):
        """弹出元素"""
        return self.items.pop()

    def peek(self):
        """返回栈顶元素"""
        return self.items[len(self.items)-1]

    def size(self):
        """返回栈的大小"""
        return len(self.items)


def communicate_of_new_restricts(arraylist):
    # todo 与前端交互
    if (arraylist[0] == 1) or (arraylist[0] == 3) or (arraylist[0] == 4):
        if arraylist[1] is None:
            print("请重复您的约束内容：")
            pick = input()
            # 出现循环互相调用communicate_of_new_restricts和deal_bert_result_into_extra_restricts
            arraylist = deal_bert_result_into_extra_restricts(pick)
        elif arraylist[5] is None:
            print("请重复您对"+arraylist[1]+"的约束值")
            pick = input()
            arraylist[5] = pick
    elif arraylist[0] == 2:
        if arraylist[1] is None:
            print("请重复您的约束内容")
            pick = input()
            arraylist = deal_bert_result_into_extra_restricts(pick)
        elif arraylist[2] is None:
            print("请重复您对"+arraylist[1]+"的最小值要求")
            pick = input()
            arraylist[2] = pick
        elif arraylist[3] is None:
            print("请重复您对"+arraylist[1]+"的最大值要求")
            pick = input()
            arraylist[3] = pick
        elif arraylist[4] is None:
            print("请重复您对"+arraylist[1]+"的（数值）单位要求")
            pick = input()
            arraylist[4] = pick
    else:
        pass
    return arraylist


def add_restricts(restrict, content):
    # 对额外的用户约束进行询问,新增多轮对话
    str_1 = "请问对于"+content+"还有什么其他的约束吗？"
    print(str_1)
    pick = input()

    # mode 1 for 大服务平台
    # temp_content = deal_bert_result_into_extra_restricts(pick)

    # mode 2 for testing
    # function_res = [-1, -1, -1, -1, -1, -1]
    # [0]:标签位，约束的类型；[1]:约束的名字；[2]:minvalue; [3]:maxvalue; [4]:unit 单位； [5]:value;
    if pick == "没了":
        temp_content = [0, -1, -1, -1, -1, -1]
    else:
        temp_content = pick.split(" ")

    while temp_content[0] != 0:
        if temp_content[0] == 1:
            add_res = {
              "key": temp_content[1],
              "valueType": "enum",
              "minValue": 0.0,
              "maxValue": 9999.0,
              "unit": "0",
              "value": temp_content[5]
            }
            restrict.append(add_res)
        elif temp_content[0] == 2:
            add_res = {
              "key": temp_content[1],
              "valueType": "region",
              "minValue": temp_content[2],
              "maxValue": temp_content[3],
              "unit": temp_content[4],
              "value": ""
            }
            restrict.append(add_res)
        elif temp_content[0] == 3:
            add_res = {
              "key": temp_content[1],
              "valueType": "service-provider",
              "minValue": 0.0,
              "maxValue": 9999.0,
              "unit": "0",
              "value": temp_content[5]
            }
            restrict.append(add_res)
        elif temp_content[0] == 4:
            add_res = {
              "key": temp_content[1],
              "valueType": "after",
              "minValue": 0.0,
              "maxValue": 9999.0,
              "unit": "0",
              "value": temp_content[5]
            }
            restrict.append(add_res)

        str_1 = "请问对于" + content + "还有什么其他的约束吗？"
        print(str_1)
        pick = input()

        # mode 1 for 大服务平台
        # temp_content = deal_bert_result_into_extra_restricts(pick)

        # mode 2 for testing
        if pick == "没了":
            temp_content = [0, -1, -1, -1, -1, -1]
        else:
            temp_content = pick.split(" ")

    return restrict


def random_db(rparr):
    length = len(rparr)
    if length < 1:
        return []
    if length == 1:
        return rparr[0]
    randomNumber = random.randint(0, length-1)
    return rparr[randomNumber]


# 找到含有content为节点的子树
def get_rptree_baseline(content, mode, support, test_id):
    # todo the switch of two mode

    # mode of based on 大服务平台
    # solve the problem of one to more rp
    # url = "http://require-linan.192.168.42.159.nip.io/require/api/search-rp?detail=" + content
    # response = requests.get(url)
    # respon_json = json.loads(response.content)
    # find the shallowest content in trees
    # rp_base_tree = []
    # for respon in respon_json:
    #     rp = respon['data'][0]
    #     depth = calculate_content_depth(rp, content)
    #     rp_base_tree.append(depth)
    # # Python查找列表 first 数组最小元素索引
    # result = rp_base_tree.index(min(rp_base_tree))
    # rp = respon_json[result]
    # # rp = respon_json[result]['data'][0]
    # return rp

    # mode of json_test
    file_path = "./data/rps_supp_" + str(support) + ".json"
    with open(file_path, 'r', encoding='utf-8') as fj:
        rpdb = json.load(fj)
    including_content_rp_tree = []
    rp_base_tree = []
    rp_res = []
    # including_content_rp_tree 是包含所有含有content的rp-tree
    for rp in rpdb:
        if calculate_content_depth(rp, content) > 0:
            including_content_rp_tree.append(rp)
    # find the shallowest content in trees in rpdb
    for rp_tree in including_content_rp_tree:
        depth = calculate_content_depth(rp_tree, content)
        rp_base_tree.append(depth)
    min_depth = min(rp_base_tree)
    for index_num in range(0, len(rp_base_tree)):
        if rp_base_tree[index_num] == min_depth:
            rp_res.append(including_content_rp_tree[index_num])
    # 1-con-kg 2-mod-rpdb 3-ran-rpdb 4-mod-rpdb+kg 5-ran-rpdb+kg
    if (mode == 2) or (mode == 4):
        i = rp_res[(test_id - 1) % len(rp_res)]
    elif (mode == 3) or (mode == 5):
        i = random_db(rp_res)
    else:
        print("-----------选择rps模板树mode出错-----------------\n")
        logging.warning("-----------选择rps模板树mode出错-----------------\n")
        pass
    q = i['data'][0]
    return q


# num = 0: not existing; num = 1: root node; num > 1: the depth of content in the tree
def calculate_content_depth(rp_tree, content):
    # calculate the depth of content in the tree
    num = 1
    rp_t = rp_tree['data'][0]
    tree_set = [rp_t]
    while traversal_rp_tree_content(tree_set, content) == 0:
        new_tree_set = []
        num = num + 1
        for child_tree in tree_set:
            children_nodes = child_tree['children']
            new_tree_set.extend(children_nodes)
        tree_set = new_tree_set
        if len(tree_set) == 0:
            # avoid endless loop, content not existing, wrong in api
            num = 0
            # print("系统返回结果出错！")
            # logging.warning("系统返回结果出错！")
            break
    return num


# judge content existing or not
def traversal_rp_tree_content(set_tree, content):
    # could not find content in this flour
    res = 0
    for tree in set_tree:
        # find in this depth
        if tree["goal"]["content"] == content:
            res = 1
            break
    return res


with open("./data/test_rptree_499.json", 'r', encoding='utf-8') as fr:
    # type = list, len = 200
    test_499 = json.load(fr)

with open("./data/test_rptree_5008.json", 'r', encoding='utf-8') as fq:
    test_5008 = json.load(fq)


def get_rptree_test(test_id):
    num = 0
    for i in test_499:
        num = num + 1
        if num == test_id:
            return i
    for j in test_5008:
        num = num + 1
        if num == test_id:
            return j


def write_in_file(passage, mode):

    if mode == "model":
        file_path = './out/model_' + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
        with open(file_path, 'w', encoding='utf-8') as fw:
            json.dump(passage, fw, ensure_ascii=False)
    elif mode == "generate":
        file_path = './out/generate_' + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
        with open(file_path, 'w', encoding='utf-8') as fw:
            json.dump(passage, fw, ensure_ascii=False)


# 基于rp库/rp+kg的单独对话策略,以函数为最小单位
def rptree_setup_based_rpdb(content, mode, support, round, test_id, hit_content):
    record_test = get_rptree_test(test_id)
    if (mode == 1) or (mode == 0):

        initial_node = setup_extra_node(content)
        initial_node['id'] = 999999
        core_tree = initial_node
        construction_queue = [initial_node]
    else:
        record = get_rptree_baseline(content, mode, support, test_id)

        # 保持最大树结构
        core_tree = record
        # define 可修改的rp-tree
        modifiable_rp_tree = record

        # define Queue about node of the tree
        construction_queue = [modifiable_rp_tree]

    # print("Model:")
    logging.info("Model:" + str(core_tree))
    # print(core_tree)
    # write_in_file(core_tree, "model")

    test_record_queue = [record_test]
    initial = 1
    while (len(construction_queue)) and (len(test_record_queue)) > 0:
        # 处理父节点的约束,initial 用来判断是否为root-node(non-root-node allow deny)
        construction_queue, test_record_queue, round, hit_content, initial = confirm_node_restricts(construction_queue, test_record_queue, initial, support, round, hit_content, mode, record_test)
        # todo add service-kg to support prune

    # requirement_pattern_setup(content)
    # 在子节点和约束条件都修改状态后，将整个需求树更新
    # remove restricts为delete的子树,模拟删除节点及子树操作
    # core_tree = remove_children_tree(core_tree)

    # # mode 1 for 大服务平台
    # TODO 最终（在不考虑森林）的情况下处理，默认requirement_pattern['data']只有一项
    # response = get_rptree_baseline(content)
    # # 多意图在模块入口被分开处理
    # response['data'][0] = core_tree
    # return response
    # print("Generate Result:")
    logging.info("Generate Result:" + str(record_test))
    # print(record_test)
    # write_in_file(record_test, "generate")
    # mode 2 for testing
    return core_tree, record_test, round, hit_content


# 交互函数
def communicate(con):
    extra = ""
    extra_children_node = []
    while extra != 0:
        # 定义临时字典
        temp_point = {}
        # TODO 用户交互
        str_1 = "请问您对于"+con+"还有什么细节的需求吗？"
        print(str_1)
        pick = input()
        # define extra == children_point
        if pick == "没有了":
            extra = 0
            break
        # TODO 意图理解
        # 样例 司仪
        content_pick = "每个环节时间"
        str_1 = "您对" + content_pick + "的约束是什么？"
        print(str_1)
        # TODO 用户交互
        pick = input()
        restricts_pick = "每个环节时间不多于20分钟"
        restricts_temp = {
            "key2": "每个环节时间",
            "valueType": "region",
            "minValue": 0.0,
            "maxValue": 20,
            "unit": "0",
            "value": ""
        }
        content = content_pick
        goal = {}
        goal["content"] = content
        goal["restricts"] = restricts_temp
        temp_point["goal"] = goal
        temp_point["children"] = []
        extra_children_node.append(temp_point)
    return extra_children_node
    # 1状态代表没有子节点的新定义空点


# 将父节点father_node出栈,同时将其子节点从右到左压入栈
def stack_tree(stack_example):
    temp_father = stack_example.peek()[0]
    # 若干children， 数组结构
    children_nodes = temp_father['children']
    father_content = temp_father['goal']['content']
    # 此时father_node在栈中，不需要再添加
    depth = stack_example.peek()[1] + 1
    # 移除栈顶元素
    stack_example.pop()
    # children_nodes 有可能为空
    new_children_nodes = ask_for_add_new_node(father_content, children_nodes)
    # 返回的new_children_nodes 为 原有的children_nodes 和可选的子意图中用户需要的部分
    # 从右到左，倒着压入栈
    if len(new_children_nodes) != 0:
        for children_node in range(0, new_children_nodes.__len__())[::-1]:
            temp = [new_children_nodes[children_node], depth, 0]
            stack_example.push(temp)
    # if new_children_nodes == null: father content doesn't have child content
    return stack_example


# 一次性取对应需求模式库中所有需求和对应约束
def get_res_con_set_for_one_time(support):
    file_path = "./data/rps_supp_" + str(support) + ".json"
    with open(file_path, 'r', encoding='utf-8') as fo:
        rps_db = json.load(fo)
    child_set = {}
    restricts_set = {}
    for i in rps_db:
        q = i['data'][0]
        queue = [q]
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


# 一次性取对应测试需求树中所有需求和对应约束
def get_test_con_set_for_one_time(rps_db):
    child_set = {}
    restricts_set = {}
    str_out = "rps_db length: " + str(len(rps_db))
    logging.info(str_out)
    # print(rps_db)
    while len(rps_db) > 0:
        children_nodes_set = []
        for j in rps_db:
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
        rps_db = children_nodes_set
    return restricts_set, child_set


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


# judge content exist in content-kg or not
def judge_content_in_kg(content):
    with open("./rp_db_content_set/kg_content_set.txt", 'r', encoding='utf-8') as f:
        content_set = f.read()
    if content in content_set:
        return 1
    else:
        return 0


# 1:模式库中能匹配到;2:模式库中匹配不到但是需求知识图谱中能匹配到;3:全匹配不到
def hit_cover(mode, hit, content, rt_set):
    # 模式库中能匹配到
    if (mode == 2) or (mode == 3):
        for k, v in rt_set.items():
            if content in k:
                hit = hit + 1
                return hit, 1, k
        else:
            return hit, 3, content
    # 模式库中匹配不到但是需求知识图谱中能匹配到
    elif (mode == 4) or (mode == 5):
        for k, v in rt_set.items():
            if content in k:
                hit = hit + 1
                return hit, 1, k
        else:
            if judge_content_in_kg(content) > 0:
                hit = hit + 1
                return hit, 2, content
            else:
                return hit, 3, content
    elif mode == 1:
        if judge_content_in_kg(content) > 0:
            hit = hit + 1
            return hit, 2, content
        else:
            return hit, 3, content
    elif mode == 0:
        return hit, 3, content


def get_father(content, dict_content, dict_content_2):
    for k, v in dict_content.items():
        if content in dict_content[k]:
            return k
    for k, v in dict_content_2.items():
        if content in dict_content_2[k]:
            return k
    return 0


# 创建一个以content为意图的空点，注入需求模式格式
def setup_extra_node(content):
    res = {'id': 999999, 'goal': {}, 'children': []}
    res['goal']['goalId'] = random.randint(0, 9999)
    res['goal']['content'] = str(content)
    res['goal']['restricts'] = []
    res['goal']['rpId'] = -1
    res['goal']['hasMatched'] = "false"
    res['goal']['optTargets'] = []
    res['goal']['requireId'] = random.randint(0, 9999)
    res['goal']['parentId'] = random.randint(0, 9999)
    return res


URL_SP = "http://sp-algorithm-linan.192.168.42.159.nip.io"
URL_STATE = "http://service-registry-linan.192.168.42.159.nip.io/"
URL_BASE = "http://require-linan.192.168.42.159.nip.io/require"


def kg_prediction(intent):
    if 1 < 0:
        search_url = URL_BASE + "/api/kg-predict?detail=" + intent
        data = requests.get(search_url)
        data = json.loads(data.text)
        data_res = data[0]["data"]
        if len(data) != 0:
            return data
    else:
        return []


def no_child_add(round, mode, test_child_set, new_node, children_nodes_set):
    round = round + 1
    str_out = "----------Round:" + str(round) + "----------\n"
    # print(str_out)
    logging.debug(str_out)
    if (mode == 2) or (mode == 3) or (mode == 0):
        str_out = "To User: ---------检测到当前" + str(new_node) + "下无子节点，请问对于该意图有什么其他的子需求吗-----\n"
    else:
        # todo
        prediction_content = kg_prediction(new_node)
        round = round - 1
        str_out = "To User: ---------检测到当前" + str(
            new_node) + "下无子节点，请问对于该意图有什么其他的子需求吗,需求知识图谱为您推荐" + str(prediction_content) + "-----\n"
    # print(str_out)
    logging.debug(str_out)
    if len(test_child_set[new_node]) == 0:
        str_out = "----USER: 没了-----\n"
        # print(str_out)
        logging.debug(str_out)
    else:
        if len([val for val in prediction_content if val in test_child_set[new_node]]) != 0:
            round = round - 1
        for t_child in test_child_set[new_node]:
            str_out = "USER: 我还需要" + str(t_child) + "\n"
            # print(str_out)
            logging.debug(str_out)
            extra_node = setup_extra_node(t_child)
            children_nodes_set.append(extra_node)
            round = round + 1
            str_out = "----------Round:" + str(round) + "----------\n"
            # print(str_out)
            logging.debug(str_out)
            if (mode == 2) or (mode == 3) or (mode == 0):
                str_out = "To User: 请问对于" + str(new_node) + "意图有什么其他的子需求吗-----\n"
            else:
                str_out = "To User: 请问对于" + str(new_node) + "意图有什么其他的子需求吗,需求知识图谱为您推荐...-----\n"
            # print(str_out)
            logging.debug(str_out)
        str_out = "----USER: 没了-----\n"
        # print(str_out)
        logging.debug(str_out)
    return round, children_nodes_set


def extra_new_node(round, mode, test_child_set, c_set, hit_content, rest_set, content_ask, restricts, test_rest_set, children_nodes_set):
    round = round + 1
    str_out = "----------Round:" + str(round) + "----------\n"
    # print(str_out)
    logging.debug(str_out)
    prediction_content = []
    if (mode == 2) or (mode == 3) or (mode == 0):
        str_out = "To User: 你对" + str(content_ask) + "还有什么新需求吗？\n"
    else:
        content_prediction = kg_prediction(content_ask)
        str_out = "To User: 你对" + str(content_ask) + "还有什么新需求吗？需求知识图谱为您推荐...\n"
        round = round - 1
    # print(str_out)
    logging.debug(str_out)
    for new_node in test_child_set[content_ask]:
        if new_node not in c_set:
            str_out = "USER: 我要加入" + str(new_node) + "\n"
            # print(str_out)
            logging.debug(str_out)
            hit_content, cover_mode, new_node_in_rp = hit_cover(mode, hit_content, new_node, rest_set)
            restricts_actual, round = confirm_restricts(new_node, new_node_in_rp, restricts, rest_set,
                                                        test_rest_set, round, cover_mode)
            round, children_node_set = no_child_add(round, mode, test_child_set, new_node, children_nodes_set)


            round = round + 1
            str_out = "----------Round:" + str(round) + "----------\n"
            # print(str_out)
            logging.debug(str_out)
            if (mode == 2) or (mode == 3) or (mode == 0):
                str_out = "To User: 你对" + str(content_ask) + "还有什么新需求吗？\n"
            else:
                str_out = "To User: 你对" + str(content_ask) + "还有什么新需求吗？需求知识图谱为您推荐...\n"
            # print(str_out)
            logging.debug(str_out)
    str_out = "USER: 没有了\n"
    # print(str_out)
    logging.debug(str_out)
    return round, children_nodes_set, hit_content


def need_or_not(content, result, round):
    if result == 1:
        round = round + 1
        str_out = "----------Round:" + str(round) + "----------\n"
        # print(str_out)
        logging.debug(str_out)
        str_out = "请问您对于" + content + "是否需要？\n"
        # print(str_out)
        logging.debug(str_out)
        str_out = "USER: " + "需要\n"
        # print(str_out)
        logging.debug(str_out)
    else:
        round = round + 1
        str_out = "----------Round:" + str(round) + "----------\n"
        # print(str_out)
        logging.debug(str_out)
        str_out = "请问您对于" + content + "是否需要？\n"
        # print(str_out)
        logging.debug(str_out)
        str_out = "USER: " + "不需要\n"
        # print(str_out)
        logging.debug(str_out)

    return round


# define restricts confirmation of communication
# step: fetch the stack top and fill in the blank
# ask for a whole layer
def confirm_node_restricts(c_queue, t_queue, initial, support, round, hit_content, mode, test_tree):
    # 对于需求模式库/需求知识图谱的信息构建
    rest_set, child_set = get_res_con_set_for_one_time(support)
    # 对于当前测试层的信息构建
    test_rest_set, test_child_set = get_test_con_set_for_one_time(t_queue)
    # 对于当前模板层的信息构建
    c_rest_set, c_child_set = get_test_con_set_for_one_time(c_queue)
    # 对于整个测试用户需求模式树的信息构建
    test_tree_rest_set, test_tree_child_set = test_tree_con_set_for_one_time(test_tree)
    # 当前层下层的子节点集合构建/替换下一轮的c_queue
    children_nodes_set = []
    # 赋予初始值父节点initial
    father_content_old = get_father(c_queue[0]['goal']['content'], child_set, test_tree_child_set)
    content_id_old = c_queue[0]['id']
    for id_q in range(0, len(c_queue)):
        c_temp = c_queue[id_q]
        # 存储记录需求树的content 和约束restricts
        content = c_temp['goal']['content']
        father_content_new = get_father(content, child_set, test_tree_child_set)
        content_id = c_temp['id']
        restricts = c_temp['goal']['restricts']
        if initial == 1:
            hit_content, cover_mode, content_in_rp = hit_cover(mode, hit_content, content, rest_set)
            restricts_actual, round = confirm_restricts(content, content_in_rp, restricts, rest_set, test_rest_set, round, cover_mode)
            c_temp['goal']['restricts'] = restricts_actual
            children_nodes = c_temp['children']
            if len(children_nodes) == 0:
                round, children_node_set = no_child_add(round, mode, test_child_set, content, children_nodes_set)
            children_nodes_set.extend(children_nodes)
        else:
            if father_content_new == father_content_old:
                if content_id == 999999:
                    str_out = "-----当前指针点为" + str(content) + "\n"
                    # print(str_out)
                    logging.info(str_out)
                    # calculate cover
                    # 1:模式库中能匹配到;2:模式库中匹配不到但是需求知识图谱中能匹配到;3:全匹配不到
                    hit_content, cover_mode, content_in_rp = hit_cover(mode, hit_content, content, rest_set)
                    # no matter what cover_mode is:
                    restricts_actual, round = confirm_restricts(content, content_in_rp, restricts, rest_set,
                                                                test_rest_set, round, cover_mode)
                    c_temp['goal']['restricts'] = restricts_actual
                    children_nodes = c_temp['children']
                    if len(children_nodes) == 0:
                        round, children_node_set = no_child_add(round, mode, test_child_set, content,
                                                                children_nodes_set)
                    children_nodes_set.extend(children_nodes)
                else:
                    if content in test_child_set:
                        round = need_or_not(content, 1, round)
                        # 1:模式库中能匹配到;2:模式库中匹配不到但是需求知识图谱中能匹配到;3:全匹配不到
                        hit_content, cover_mode, content_in_rp = hit_cover(mode, hit_content, content, rest_set)
                        # no matter what cover_mode is:
                        restricts_actual, round = confirm_restricts(content, content_in_rp, restricts, rest_set, test_rest_set, round,
                                                                    cover_mode)
                        c_temp['goal']['restricts'] = restricts_actual
                        children_nodes = c_temp['children']
                        if len(children_nodes) == 0:
                            round, children_node_set = no_child_add(round, mode, test_child_set, content,
                                                                    children_nodes_set)
                        children_nodes_set.extend(children_nodes)

                    elif content not in test_child_set:
                        round = need_or_not(content, 0, round)

                    if id_q == len(c_queue) - 1:
                        round = round + 1
                        str_out = "----------Round:" + str(round) + "----------\n"
                        # print(str_out)
                        logging.debug(str_out)
                        if (mode == 2) or (mode == 3) or (mode == 0):
                            str_out = "To User: 你对" + str(father_content_new) + "还有什么新需求吗？\n"
                        else:
                            content_prediction = kg_prediction(father_content_new)
                            str_out = "To User: 你对" + str(father_content_new) + "还有什么新需求吗？需求知识图谱预测您需要\n"
                            round = round - 1
                        # print(str_out)
                        logging.debug(str_out)
                        for new_node in test_tree_child_set[father_content_new]:
                            if new_node not in c_rest_set:
                                str_out = "USER: 我要加入" + str(new_node) + "\n"
                                # print(str_out)
                                logging.debug(str_out)

                                hit_content, cover_mode, new_node_in_rp = hit_cover(mode, hit_content, new_node,
                                                                                    rest_set)
                                restricts_actual, round = confirm_restricts(new_node, new_node_in_rp, restricts,
                                                                            rest_set, test_rest_set, round,
                                                                            cover_mode)

                                round, children_node_set = no_child_add(round, mode, test_child_set, new_node,
                                                                        children_nodes_set)

                                round = round + 1
                                str_out = "----------Round:" + str(round) + "----------\n"
                                # print(str_out)
                                logging.debug(str_out)
                                if (mode == 2) or (mode == 3) or (mode == 0):
                                    str_out = "To User: 你对" + str(father_content_new) + "还有什么新需求吗？\n"
                                else:
                                    str_out = "To User: 你对" + str(father_content_new) + "还有什么新需求吗？需求知识图谱为您推荐...\n"
                                # print(str_out)
                                logging.debug(str_out)
                        str_out = "USER: 没有了\n"
                        # print(str_out)
                        logging.debug(str_out)

            else:
                # 当前层面判定前后两点父节点不一致/当前层最后一个点 触发：对于old父节点的额外询问
                if content_id != 999999:
                    if content_id_old != 999999:
                        round, children_nodes_set, hit_content = extra_new_node(round, mode, test_tree_child_set,
                                                                                c_child_set, hit_content, rest_set,
                                       father_content_old, restricts,
                                       test_rest_set, children_nodes_set)
                    if content in test_child_set:
                        round = need_or_not(content, 1, round)
                        # 1:模式库中能匹配到;2:模式库中匹配不到但是需求知识图谱中能匹配到;3:全匹配不到
                        hit_content, cover_mode, content_in_rp = hit_cover(mode, hit_content, content, rest_set)
                        # no matter what cover_mode is:
                        restricts_actual, round = confirm_restricts(content, content_in_rp, restricts, rest_set, test_rest_set, round,
                                                                    cover_mode)
                        c_temp['goal']['restricts'] = restricts_actual
                        children_nodes = c_temp['children']
                        if len(children_nodes) == 0:
                            round, children_node_set = no_child_add(round, mode, test_child_set, content,
                                                                    children_nodes_set)
                        children_nodes_set.extend(children_nodes)

                    elif content not in test_child_set:
                        round = need_or_not(content, 0, round)

                    if id_q == len(c_queue) - 1:
                        round, children_nodes_set, hit_content = extra_new_node(round, mode, test_tree_child_set,
                                                                                c_child_set, hit_content, rest_set,
                                                                                father_content_new, restricts,
                                                                                test_rest_set, children_nodes_set)

                else:
                    if content_id_old != 999999:
                        round, children_nodes_set, hit_content = extra_new_node(round, mode, test_tree_child_set, c_child_set, hit_content, rest_set,
                                       father_content_old, restricts,
                                       test_rest_set, children_nodes_set)
                    hit_content, cover_mode, content_in_rp = hit_cover(mode, hit_content, content, rest_set)
                    # no matter what cover_mode is:
                    restricts_actual, round = confirm_restricts(content, content_in_rp, restricts, rest_set,
                                                                test_rest_set, round,
                                                                cover_mode)
                    c_temp['goal']['restricts'] = restricts_actual
                    children_nodes = c_temp['children']
                    if len(children_nodes) == 0:
                        round, children_node_set = no_child_add(round, mode, test_child_set, content,
                                                                children_nodes_set)
                    children_nodes_set.extend(children_nodes)

        father_content_old = father_content_new
        content_id_old = content_id
        initial = 0
    c_queue = children_nodes_set

    children_nodes_test_set = []
    for variable in t_queue:
        children_node_test = variable['children']
        children_nodes_test_set.extend(children_node_test)
    t_queue = children_nodes_test_set

    return c_queue, t_queue, round, hit_content, initial


# 需求模式库中对应需求约束去重key
def remove_duplication(array_restricts):
    key_set = []
    res_restricts = []
    for i in array_restricts:
        key = i['key']
        if key not in key_set:
            key_set.append(key)
            res_restricts.append(i)
    return res_restricts


def confirm_restricts(content, content_in_rp, restricts, r_set, test_rest_set, round, mode):
    if mode == 1:
        if len(restricts) == 0:
            str_out = "---模板树中对应" + str(content) + "意图无约束----\n"
            # print(str_out)
            logging.info(str_out)
            str_out = "----正在需求模式库中查找所有对应" + str(content) + "的模式或子模式约束...----\n"
            # print(str_out)
            logging.info(str_out)
            if len(r_set[content_in_rp]) == 0:
                round = round + 1
                str_out = "----------Round:" + str(round) + "----------\n"
                # print(str_out)
                logging.debug(str_out)
                str_out = "----需求模式库中" + str(content) + "的约束为空.----\n"
                # print(str_out)
                logging.info(str_out)
                # print("content:")
                # print(content)
                logging.info("content" + str(content))
                # print("restricts:")
                # print(restricts)
                logging.info("restricts:" + str(restricts))
                str_out = "To user:对于" + str(content) + "部分是否满意?\n"
                # print(str_out)
                logging.debug(str_out)
            else:
                round = round + 1
                str_out = "----------Round:" + str(round) + "----------\n"
                # print(str_out)
                logging.info(str_out)
                str_out = "To User:对于" + str(content) + "的约束这样如何:\n"
                # print(str_out)
                logging.debug(str_out)
                e_res_set = remove_duplication(r_set[content_in_rp])
                for e_res in e_res_set:
                    valuetype = e_res['valueType']
                    if valuetype == "region":
                        minValue = int(e_res['minValue'])
                        maxValue = int(e_res['maxValue'])
                        key = e_res['key']
                        unit = e_res['unit']
                        str_1 = content + "的" + key + "范围, " + str(minValue) + "到" + str(maxValue) + unit + "\n"
                        # print(str_1)
                        logging.debug(str_1)
                        # pick = input()
                        # temp_content = deal_bert_result_into_nature_language_restricts(pick, valuetype)
                        # # 更新子约束
                        # if temp_content == "random":
                        #     e_res['minValue'] = "random"
                        #     e_res['maxValue'] = "random"
                        # # 对于约束来说，只会出现特殊情况“我无所谓”而不会出现“我不需要”
                        # else:
                        #     mediate = temp_content.split("-")
                        #     e_res['minValue'] = mediate[0]
                        #     e_res['maxValue'] = mediate[1]
                    elif (valuetype == "service-provider") or (valuetype == "enum") or (valuetype == "after"):
                        value = e_res['value']
                        key = e_res['key']
                        str_1 = content + "的" + key + "：" + value + "\n"
                        # print(str_1)
                        logging.debug(str_1)
                        # pick = input()
                        # temp_content = deal_bert_result_into_nature_language_restricts(pick, valuetype)
                        # if temp_content == "random":
                        #     e_res['value'] = "random"
                        # else:
                        #     e_res['value'] = temp_content
                str_out = "To user:对于" + str(content) + "部分是否满意?\n"
                # print(str_out)
                logging.debug(str_out)
        else:
            round = round + 1
            str_out = "----------Round:" + str(round) + "----------\n"
            # print(str_out)
            logging.info(str_out)
            str_out = "在需求模式库中对" + str(content) + "进行查找..."
            # print(str_out)
            logging.debug(str_out)
            str_out = "对于" + str(content) + "的约束这样如何:\n"
            # print(str_out)
            logging.debug(str_out)
            e_res_set = remove_duplication(r_set[content_in_rp])
            for e_res in e_res_set:
                valuetype = e_res['valueType']
                if valuetype == "region":
                    minValue = int(e_res['minValue'])
                    maxValue = int(e_res['maxValue'])
                    key = e_res['key']
                    unit = e_res['unit']
                    str_1 = content + "的" + key + "范围, " + str(minValue) + "到" + str(maxValue) + unit + "\n"
                    # print(str_1)
                    logging.debug(str_1)
                    # pick = input()
                    # temp_content = deal_bert_result_into_nature_language_restricts(pick, valuetype)
                    # # 更新子约束
                    # if temp_content == "random":
                    #     e_res['minValue'] = "random"
                    #     e_res['maxValue'] = "random"
                    # # 对于约束来说，只会出现特殊情况“我无所谓”而不会出现“我不需要”
                    # else:
                    #     mediate = temp_content.split("-")
                    #     e_res['minValue'] = mediate[0]
                    #     e_res['maxValue'] = mediate[1]
                elif (valuetype == "service-provider") or (valuetype == "enum") or (valuetype == "after"):
                    value = e_res['value']
                    key = e_res['key']
                    str_1 = content + "的" + key + "：" + value + "\n"
                    # print(str_1)
                    logging.debug(str_1)
                    # pick = input()
                    # temp_content = deal_bert_result_into_nature_language_restricts(pick, valuetype)
                    # if temp_content == "random":
                    #     e_res['value'] = "random"
                    # else:
                    #     e_res['value'] = temp_content
            str_out = "To user:对于" + str(content) + "部分是否满意?\n"
            # print(str_out)
            logging.debug(str_out)
        str_out = "USER: 我觉得应该有如下修改：\n"
        # print(str_out)
        logging.debug(str_out)
        restricts_test = test_rest_set[content]
        for e_res in restricts_test:
            valuetype = e_res['valueType']
            if valuetype == "region":
                minValue = int(e_res['minValue'])
                maxValue = int(e_res['maxValue'])
                key = e_res['key']
                unit = e_res['unit']
                str_1 = content + "的" + key + "范围, " + str(minValue) + "到" + str(maxValue) + unit + "\n"
                # print(str_1)
                logging.debug(str_1)
            elif (valuetype == "service-provider") or (valuetype == "enum") or (valuetype == "after"):
                value = e_res['value']
                key = e_res['key']
                str_1 = content + "的" + key + "：" + value + "\n"
                # print(str_1)
                logging.debug(str_1)
        str_out = "--------Round End---------\n"
        # print(str_out)
        logging.info(str_out)

    elif mode == 2:
        str_out = "---未使用模式库或模式库中无" + str(content) + "意图----\n"
        # print(str_out)
        logging.info(str_out)
        str_out = "---需求知识图谱中存在" + str(content) + "意图----\n"
        # print(str_out)
        logging.info(str_out)
        round = round + 1
        str_out = "----------Round:" + str(round) + "----------\n"
        # print(str_out)
        logging.info(str_out)
        str_out = "To User: 你对" + str(content) + "的约束是什么？\n"
        # print(str_out)
        logging.debug(str_out)

        restricts_test = test_rest_set[content]
        if len(restricts_test) > 0:
            for e_res in range(0, len(restricts_test)):
                valuetype = restricts_test[e_res]['valueType']

                if valuetype == "region":
                    minValue = int(restricts_test[e_res]['minValue'])
                    maxValue = int(restricts_test[e_res]['maxValue'])
                    key = restricts_test[e_res]['key']
                    unit = restricts_test[e_res]['unit']
                    str_1 = content + "的" + key + "范围, " + str(minValue) + "到" + str(maxValue) + unit + "\n"
                    # print(str_1)
                    logging.debug(str_1)
                elif (valuetype == "service-provider") or (valuetype == "enum") or (valuetype == "after"):
                    value = restricts_test[e_res]['value']
                    key = restricts_test[e_res]['key']
                    str_1 = content + "的" + key + "：" + value + "\n"
                    # print(str_1)
                    logging.debug(str_1)

                round = round + 1
                str_out = "----------Round:" + str(round) + "----------\n"
                # print(str_out)
                logging.info(str_out)
                str_out = "To User: 你对" + str(content) + "还有其他约束吗？\n"
                # print(str_out)
                logging.debug(str_out)

            str_out = "没有了\n"
            # print(str_out)
            logging.debug(str_out)
        else:
            str_out = "USER:我都无所谓\n"
            # print(str_out)
            logging.debug(str_out)

    elif mode == 3:
        # 匹配不到
        str_out = "---未使用模式库或模式库或需求知识图谱中无" + str(content) + "意图----\n"
        # print(str_out)
        logging.info(str_out)
        round = round + 1
        str_out = "----------Round:" + str(round) + "----------\n"
        # print(str_out)
        logging.info(str_out)
        str_out = "To User: 无法匹配" + str(content) + "\n"
        # print(str_out)
        logging.debug(str_out)

        str_out = "To User: 你对" + str(content) + "的约束是什么？\n"
        # print(str_out)
        logging.debug(str_out)
        restricts_test = test_rest_set[content]
        if len(restricts_test) > 0:
            for e_res in range(0, len(restricts_test)):
                valuetype = restricts_test[e_res]['valueType']

                if valuetype == "region":
                    minValue = int(restricts_test[e_res]['minValue'])
                    maxValue = int(restricts_test[e_res]['maxValue'])
                    key = restricts_test[e_res]['key']
                    unit = restricts_test[e_res]['unit']
                    str_1 = content + "的" + key + "范围, " + str(minValue) + "到" + str(maxValue) + unit + "\n"
                    # print(str_1)
                    logging.debug(str_1)
                elif (valuetype == "service-provider") or (valuetype == "enum") or (valuetype == "after"):
                    value = restricts_test[e_res]['value']
                    key = restricts_test[e_res]['key']
                    str_1 = content + "的" + key + "：" + value + "\n"
                    # print(str_1)
                    logging.debug(str_1)

                round = round + 1
                str_out = "----------Round:" + str(round) + "----------\n"
                # print(str_out)
                logging.info(str_out)
                str_out = "To User: 你对" + str(content) + "还有其他约束吗？\n"
                # print(str_out)
                logging.debug(str_out)

            str_out = "USER: 没有了\n"
            # print(str_out)
            logging.debug(str_out)
        else:
            str_out = "USER: 我都无所谓\n"
            # print(str_out)
            logging.debug(str_out)

    return restricts_test, round


# remove restricts为delete的子树,模拟删除节点及子树操作
def remove_children_tree(tree):
    child_content = tree['children']
    if len(child_content) > 0:
        remove_temp = []
        for child in range(0, len(child_content)):
            if child_content[child]['goal']['restricts'] == "delete":
                remove_temp.append(child_content[child])
            else:
                child_content[child] = remove_children_tree(child_content[child])
        for i in remove_temp:
            if i in child_content:
                child_content.remove(i)
        tree['children'] = child_content
        return tree
    else:
        return tree


# input ：
# base_tree 中的children_nodes ;
# return ：
# 原有的children_nodes 和可选的子意图中用户需要的部分
def ask_for_add_new_node(content, children_nodes):
    children = []
    # search_new_nodes 与 children_nodes 结构相同,为推荐的新点全集,可为空
    search_new_nodes = recommendation_new_nodes(content, children_nodes)
    # 后续对话内容 include multi-QA of new nodes, until answer is “no need”
    if (len(search_new_nodes) > 0) and (len(children_nodes) != 0):
        # output sentence
        for children_node in range(0, len(children_nodes)):
            children.append(children_nodes[children_node]['goal']['content'])
        str_temp = "你对于"+content+"除了"
        print(str_temp)
        if len(children) > 1:
            for i in range(0, len(children) - 1):
                print(children[i])
                print("和")
            print(children[len(children) - 1])
        else:
            print(children[len(children) - 1])
        print("，还需要其他的需求吗，例如")
        if len(search_new_nodes) > 1:
            for j in range(0, len(search_new_nodes) - 1):
                print(search_new_nodes[j]['goal']['content'])
                print("和")
            print(search_new_nodes[len(search_new_nodes) - 1]['goal']['content'])
        else:
            print(search_new_nodes[len(search_new_nodes) - 1]['goal']['content'])

        # accept用户输入, new_nodes 接受多轮输入
        pick = input()
        while refuse_or_negative(pick) != "没有了":
            child_node = get_content(pick)
            flag = 0
            for i in search_new_nodes:
                if i['goal']['content'] == child_node:
                    children_nodes.append(i)
                    search_new_nodes.remove(i)
                    flag = 1
                    break
            if flag == 0:
                print("无法识别您的新需求，请重新输入")
                pick = input()
                continue
            else:
                if len(search_new_nodes) == 0:
                    print("已添加所有可供选择的子需求")
                    break
                for children_node in range(0, children_nodes.__len__()):
                    children.append(children_nodes[children_node]['goal']['content'])
                str_temp = "你对于" + content + "除了"
                print(str_temp)
                if len(children) > 1:
                    for i in range(0, len(children) - 1):
                        print(children[i])
                        print("和")
                    print(children[len(children) - 1])
                else:
                    print(children[len(children) - 1])
                print("，还需要其他的需求吗，例如")
                if len(search_new_nodes) > 1:
                    for j in range(0, len(search_new_nodes) - 1):
                        print(search_new_nodes[j]['goal']['content'])
                        print("和")
                    print(search_new_nodes[len(search_new_nodes) - 1]['goal']['content'])
                else:
                    print(search_new_nodes[len(search_new_nodes) - 1]['goal']['content'])
                pick = input()
        return children_nodes
    elif (len(search_new_nodes) > 0) and (len(children_nodes) == 0):
        # output sentence
        str_temp = "你对于" + content + "还需要其他的需求吗，例如"
        print(str_temp)
        if len(search_new_nodes) > 1:
            for j in range(0, len(search_new_nodes) - 1):
                print(search_new_nodes[j]['goal']['content'])
                print("和")
            print(search_new_nodes[len(search_new_nodes) - 1]['goal']['content'])
            print("?")
        else:
            print(search_new_nodes[len(search_new_nodes) - 1]['goal']['content'])
            print("?")

        # accept用户输入,new_nodes 接受多轮输入
        pick = input()
        while refuse_or_negative(pick) != "没有了":
            child_node = get_content(pick)
            flag = 0
            for i in search_new_nodes:
                if i['goal']['content'] == child_node:
                    children_nodes.append(i)
                    search_new_nodes.remove(i)
                    flag = 1
                    break
            if flag == 0:
                print("无法识别您的新需求，请重新输入")
                pick = input()
                continue
            else:
                if len(search_new_nodes) == 0:
                    print("已添加所有可供选择的子需求")
                    break
                for children_node in range(0, children_nodes.__len__()):
                    children.append(children_nodes[children_node]['goal']['content'])
                str_temp = "你对于" + content + "除了"
                print(str_temp)
                # 边界测试
                if len(children) > 1:
                    for i in range(0, len(children) - 1):
                        print(children[i])
                        print("和")
                    print(children[len(children) - 1])
                else:
                    print(children[len(children) - 1])
                print("，还需要其他的需求吗，例如")
                if len(search_new_nodes) > 1:
                    for j in range(0, len(search_new_nodes) - 1):
                        print(search_new_nodes[j]['goal']['content'])
                        print("和")
                    print(search_new_nodes[len(search_new_nodes) - 1]['goal']['content'])
                else:
                    print(search_new_nodes[len(search_new_nodes) - 1]['goal']['content'])
                pick = input()
        return children_nodes

    elif (len(search_new_nodes) == 0) and (len(children_nodes) > 0):
        print("注意：当前意图下不支持新增子意图")
        print(content)
        return children_nodes
    else:
        print("注意：当前意图下不支持新增子意图")
        print(content)
        return children_nodes


# return :与 children_nodes 结构相同,为推荐的新点,可为空
def recommendation_new_nodes(content, exist_nodes):
    res = []
    # 记录已有子节点(非推荐)下的子意图
    exist_res = []
    # 增加新结点
    # fetch all child_node of the content
    res_rpdb = new_node_search_in_rpdb(content)
    res.extend(res_rpdb)
    res_content_kg = new_node_search_in_content_kg(content)
    # todo add restricts for 0 restrict of content
    res.extend(res_content_kg)
    # service_kg == out support module
    # new_node_search_in_service_kg()

    # delete the replicated nodes;
    res = del_repeat_node(res)
    # before return , remove existing nodes in "exist_nodes"
    res_temp = []
    for exist_node in exist_nodes:
        exist_res.append(exist_node['goal']['content'])
    for node in res:
        if node['goal']['content'] not in exist_res:
            res_temp.append(node)

    # return the answer
    return res_temp


def new_node_search_in_rpdb(content):
    res = []

    # mode 1 Project for 大服务平台
    # fetch the rp-tree including content
    # url = "http://require-linan.192.168.42.159.nip.io/require/api/search-rp?detail=" + content
    # response = requests.get(url)
    # respon_json = json.loads(response.content)
    # for respon in respon_json:
    #     rp = respon['data'][0]
    #     # 取出对应rp中所有content的子意图
    #     children = fetch_child(rp, content)
    #     res.extend(children)

    # mode 2 Project for testing
    with open("rpdb.json", 'r', encoding='utf-8') as fr:
        rpdb = json.load(fr)
    for rp in rpdb:
        if calculate_content_depth(rp, content) > 0:
            children = fetch_child(rp, content)
            res.extend(children)

    return res


def fetch_child(rp, content):
    tree_set = [rp]
    while rp_children_content(tree_set, content) == 0:
        new_tree_set = []
        for child_tree in tree_set:
            children_nodes = child_tree['children']
            new_tree_set.extend(children_nodes)
        tree_set = new_tree_set
        if len(tree_set) == 0:
            # avoid endless loop, content not existing, wrong in api
            print("系统返回结果fetch_child出错！")
            break
    res = rp_children_content(tree_set, content)
    return res


# 返回content的子意图
def rp_children_content(set_tree, content):
    # could not find content in this flour
    res = 0
    for tree in set_tree:
        # find in this depth
        if tree["goal"]["content"] == content:
            res = tree['children']
            break
    return res


def del_repeat_node(s):
    s1 = []
    content = []
    for i in s:
        if i['goal']['content'] not in content:
            s1.append(i)
            content.append(i['goal']['content'])
        else:
            pass
    return s1



