#!/usr/bin/env python

# encoding: utf-8
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/2 7:32
# @Author  : junruit
# @File    : res_test.py
# @desc: PyCharm
'''
import json
import random
from rp_tree_v_2_0.base_rp_db import *


def initial_divide():
    with open("../requirement_tree/hehehe.json", 'r', encoding='utf-8') as fr:
        test_with_db = json.load(fr)
        print(type(test_with_db), len(test_with_db))
    random.shuffle(test_with_db)
    rpdb = []
    test_rp_tree = []
    for i in range(0, len(test_with_db)):
        if i < 200:
            test_rp_tree.append(test_with_db[i])
        else:
            rpdb.append(test_with_db[i])
    with open('rpdb.json', 'w', encoding='utf-8') as f:
        json.dump(rpdb, f, ensure_ascii=False)
    with open('test_rp_tree.json', 'w', encoding='utf-8') as f:
        json.dump(test_rp_tree, f, ensure_ascii=False)

    return


# initial_divide()
with open("rpdb.json", 'r', encoding='utf-8') as fr:
    rpdb = json.load(fr)
    # type = list, len = 299

with open("test_rp_tree.json", 'r', encoding='utf-8') as fr:
    # type = list, len = 200
    test_sample = json.load(fr)

with open("test_rp_tree_sample.json", 'r', encoding='utf-8') as fr:
    # type = list, len = 200
    test_rp_sample = json.load(fr)

# for test_tree in test_sample:
#     print(test_tree)
# 测试样例1
# print(test_sample[0])
# print(rpdb[0])
# with open("测试样例1.txt", 'w', encoding='utf-8') as ft:
#     ft.write("目标需求树")
#     ft.write(str(test_sample[0]))
#     ft.write("\n\n")
#     ft.write("base-tree")
#     ft.write(str(rpdb[0]))
# 对于空约束 ：没了
# paper ：1.我先做rpdb的，然后发现rpdb有可优化的地方，然后分别加入content和service 的支持
# ！忽略重复确认的过程


def judge_information(content):
    flag = 0
    for rp in rpdb:
        if calculate_content_depth(rp, content) > 0:
            flag = 1
            break
    return flag


def judge_information_from_big_service(content):
    url = "http://10.147.18.111:8080/api/search-rp?detail="+content
    response = requests.get(url)
    respon_json = json.loads(response.content)
    # print(respon_json)
    # print(respon_json[0])
    # print(respon_json[1])
    # print(respon_json[2])
    if respon_json:
        return 1
    else:
        return 0


def test_cover():
    # content 覆盖度的测试
    # single_test_sample = test_sample[0]
    num_of_content_set = []
    lack_set = []
    counter = 0
    # for single_test_sample in test_sample:
    for single_test_sample in test_rp_sample:
        counter = counter + 1
        if (counter > 0) and (counter < 66):
            num_of_content = 0
            lack = 0
            stack = Stack()
            # 1 = right; 0 means not exist
            array_test = [single_test_sample, 1]
            stack.push(array_test)
            while stack.size() > 0:
                exist = -1
                temp_father = stack.peek()[0]
                exist_judge = stack.peek()[1]
                children_nodes = temp_father['children']
                father_content = temp_father['goal']['content']
                if exist_judge == 0:
                    exist = 0
                    num_of_content = num_of_content + 1
                    lack = lack + 1
                    stack.pop()
                    if len(children_nodes) != 0:
                        for children_node in range(0, children_nodes.__len__())[::-1]:
                            temp_content = [children_nodes[children_node], exist]
                            stack.push(temp_content)

                else:
                    # if judge_information(father_content) > 0:
                    if judge_information_from_big_service(father_content) > 0:
                        num_of_content = num_of_content + 1
                        exist = 1
                    else:
                        num_of_content = num_of_content + 1
                        exist = 0
                        lack = lack + 1
                    stack.pop()
                    if len(children_nodes) != 0:
                        for children_node in range(0, children_nodes.__len__())[::-1]:
                            temp_content = [children_nodes[children_node], exist]
                            stack.push(temp_content)
            num_of_content_set.append(num_of_content)
            lack_set.append(lack)
            with open("cover_res_3_1_65.txt", 'a', encoding='utf-8') as fc:
                str_1 = "No." + str(counter) + " 总意图树：" + str(num_of_content) + "  lack content:" + str(lack) + "  覆盖度:" + str((num_of_content-lack)/num_of_content) + "\n"
                print(str_1)
                fc.write(str_1)
    return num_of_content_set, lack_set


# 覆盖度
# test_cover()
# final res 3 0521
test_cover()


# calculate number of round
def calculate_num_round(single_test_sample):
    # content 覆盖度的测试
    # single_test_sample = test_sample[0]
    # for single_test_sample in test_sample:
    #     num_of_round = 1
    #     stack = Stack()
    #     stack_db = Stack()
    #     # 1 = right; 0 means not exist
    #     array_test = [single_test_sample, 1]
    #     array_db = [rpdb[0], 1]
    #     stack.push(array_test)
    #     stack_db.push(array_db)
    #     while stack.size() > 0:
    #         exist = -1
    #         temp_father = stack.peek()[0]
    #         temp_father_db = stack_db.peek()[0]
    #         exist_judge = stack.peek()[1]
    #         children_nodes = temp_father['children']
    #         father_content = temp_father['goal']['content']
    #         # 你对content 需要吗？---需要/我不需要
    #         num_of_round = num_of_round + 1
    #
    #         restricts = temp_father['goal']['restricts']
    #         restricts_db = temp_father_db['goal']['restricts']
    #         # rp-tree-db----约束/我无所谓
    #         num_of_round = num_of_round + len(restricts_db)
    #         # 额外多余的约束
    #         goal_restricts = []
    #         base_restricts = []
    #         for i in restricts:
    #             goal_restricts.append(i['key'])
    #         for i in restricts_db:
    #             base_restricts.append(i['key'])
    #         all_difference = list(set(goal_restricts).difference(set(base_restricts)))
    #         # 对额外的约束的对话轮数
    #         num_of_round = num_of_round + len(all_difference)
    #         # 额外的约束？--没了
    #         num_of_round = num_of_round + 1
    #         # 你对於father-content还有什么其他的需求如XXX/ 本轮不支持新增子意图
    num_of_round = 1
    goal_restricts = single_test_sample['goal']['restricts']
    num_of_round = num_of_round + len(goal_restricts)
    # 还有什么额外约束吗？--没了
    num_of_round = num_of_round + 1
    # 子意图除了XX还有什么，例如XXX？
    children_nodes = single_test_sample['children']
    children_content = []
    if children_nodes != 0:
        for i in children_nodes:
            children_content.append(i['goal']['content'])
    base_content_one = ['酒店', '餐馆', '地铁', '景点']
    # for j in base_content_one:
    #     if j not in children_content:
    #         # 你对base_content是否需要？我不需要
    #         num_of_round = num_of_round + 1
    # jiudian_restricts = rpdb[0]['children'][0]
    # canguan_restricts = rpdb[0]['children'][1]
    # ditie_restricts = rpdb[0]['children'][2]
    # jingdian_restricts = rpdb[0]['children'][3]
    stack = Stack()
    for i in children_nodes:
        array_test = [i, 1]
        stack.push(array_test)
    while stack.size() > 0:
        exist = -1
        temp_father = stack.peek()[0]
        exist_judge = stack.peek()[1]
        children_nodes = temp_father['children']
        father_content = temp_father['goal']['content']
        if father_content in base_content_one:
            index = base_content_one.index(father_content)
            restricts = temp_father['goal']['restricts']
            # todo
            restricts_db = rpdb[0]['children'][index]['goal']['restricts']
        else:
            restricts_db = fetch_restricts(father_content)
            restricts = temp_father['goal']['restricts']
            if type(restricts_db) == int:
                restricts_db = []
        # rp-tree-db----约束/我无所谓
        num_of_round = num_of_round + len(restricts_db)
        # 额外多余的约束
        goal_restricts = []
        base_restricts = []
        for i in restricts:
            goal_restricts.append(i['key'])
        for i in restricts_db:
            base_restricts.append(i['key'])
        all_difference = list(set(goal_restricts).difference(set(base_restricts)))
        # 对额外的约束的对话轮数
        num_of_round = num_of_round + len(all_difference)
        # 额外的约束？--没了
        num_of_round = num_of_round + 1
        stack.pop()
        # 你对於father-content还有什么其他的需求如XXX/ 本轮不支持新增子意图
        if len(children_nodes) != 0:
            for children_node in range(0, children_nodes.__len__())[::-1]:
                temp_content = [children_nodes[children_node], exist]
                num_of_round = num_of_round + 1
                if judge_information(children_nodes[children_node]['goal']['content']) > 0:
                    stack.push(temp_content)
                num_of_round = num_of_round + 1

        # 你对於father-content还有什么其他的需求如XXX/ --没了/本轮不支持新增子意图
        num_of_round = num_of_round + 1

    return num_of_round


def fetch_restricts(content):
    for i in rpdb:
        tree_set = [i]
        while traversal_rp_tree_restricts(tree_set, content) == 0:
            new_tree_set = []
            # num = num + 1
            for child_tree in tree_set:
                children_nodes = child_tree['children']
                new_tree_set.extend(children_nodes)
            tree_set = new_tree_set
            if len(tree_set) == 0:
                # avoid endless loop, content not existing, wrong in api
                # num = 0
                # print("系统返回结果出错！")
                break
        if traversal_rp_tree_restricts(tree_set, content) != 0:
            break
    return traversal_rp_tree_restricts(tree_set, content)


def traversal_rp_tree_restricts(set_tree, content):
    # could not find content in this flour
    res = 0
    for tree in set_tree:
        # find in this depth
        if tree["goal"]["content"] == content:
            res = tree["goal"]["restricts"]
            break
    return res

# final res 2:
# re_num = 0
# round = []
# # for i in test_sample:
# for i in test_rp_sample:
#     re_num = re_num + 1
#     res = calculate_num_round(i)
#     round.append(res)
#     # print(str(re_num) + "round:" + str(res) + "\n")
# # with open("round_res.txt", 'w', encoding='utf-8') as fww:
# #     for j in range(0, len(round)):
# #         str_w = "No." + str(j + 1) + "   Round: " + str(round[j]) + "\n"
# #         fww.write(str_w)
# with open("final_res_2.txt", 'w', encoding='utf-8') as fww:
#     with open("cover_res_2_final.txt", 'r', encoding='utf-8') as frr:
#         content = frr.readline()
#         array_t = content.split()
#         counter = 0
#         str_r = "Round: " + str(round[counter])
#         array_t.insert(1, str_r)
#         str_w = ""
#         for j in array_t:
#             str_w = str_w + str(j) + "\t"
#         fww.write(str_w + "\n")
#         # print(array_t)
#         content = frr.readline()
#         while content:
#             counter = counter + 1
#             array_t = content.split()
#             str_r = "Round: " + str(round[counter])
#             array_t.insert(1, str_r)
#             str_w = ""
#             for j in array_t:
#                 str_w = str_w + str(j) + "\t"
#             fww.write(str_w + "\n")
#             content = frr.readline()

# str_res = "No." + str(n) + "  Round:" + str(round[i] + content_num[i]) + ";
# Total Content:" + str(content_num[i]) + ";
# Lack Content:" + str(lack_num[i]) + ";
# Hit rate:" + str((content_num[i]-lack_num[i])/content_num[i]) + "\n"


# 您好，很高兴为您服务
# 我想去旅行
# <class 'list'>
# 请问对于旅行还有什么其他的约束吗？
# 没了
# 你对于旅行除了酒店和餐馆和地铁和景点，还需要其他的需求吗，例如出租
# 没有了

# 请问您对于酒店是否需要？
# 需要
# 请定义酒店的名称,例如：北京望京华彩智选假日酒店
# 北京万斯酒店
# 请定义酒店的评分范围,例如4到9999分
# ！！！我无所谓
# 请定义酒店的酒店类型,例如：舒适型
# ！！！我无所谓
# 请问对于酒店还有什么其他的约束吗？
# 没了
# { 你对于酒店还需要其他的需求吗，例如SPA和行李寄存和无烟房和室内游泳池和接机服务和宽带上网
#   和接待外宾和吹风机和会议室和叫醒服务和国际长途电话和公共区域和部分房间提供wifi和中式餐厅和
#   酒店各处提供wifi和健身房和残疾人设施和洗衣服务和免费市内电话和24小时热水和早餐服务和
#   免费国内长途电话和酒吧和公共区域提供wifi和所有房间提供wifi和部分房间提供wifi和
#   棋牌室和租车和桑拿和接站服务和暖气和商务中心和西式餐厅和收费停车位和早餐服务免费}
# 没有了
# 请问您对于餐馆是否需要？
# 我不需要
# 请问您对于地铁是否需要？
# 我不需要
# 请问您对于景点是否需要？
# 需要
# 请定义景点的名称,例如：卧龙公园
# 我无所谓
# 请定义景点的评分,例如：5分
# 4
# 请问对于景点还有什么其他的约束吗？
# 2 游玩时间 2 3 h -1
# 请问对于景点还有什么其他的约束吗？
# 2 门票 0 0 元 -1
# 请问对于景点还有什么其他的约束吗？
# 没了
# !!!注意：景点意图下不支持新增子意图
# 1轮round
# 对话结束


def initial_divide_heheh():
    with open("../requirement_tree/hehehe.json", 'r', encoding='utf-8') as fr:
        test_with_db = json.load(fr)
        print(type(test_with_db), len(test_with_db))
    random.shuffle(test_with_db)
    test_rp_tree = []
    for i in range(0, len(test_with_db)):
        test_rp_tree.append(test_with_db[i])
    with open('test_rp_tree_sample.json', 'w', encoding='utf-8') as f:
        json.dump(test_rp_tree, f, ensure_ascii=False)

    return


# initial_divide_heheh()

# test_cover()

# res = judge_information_from_big_service("旅行")
# print(res)

# counter = 0
# for single_test_sample in test_rp_sample:
#     counter = counter + 1
#     if counter == 227:
#         print(single_test_sample)
#         break


# {
#     'info': {
#         'name': '旅行',
#         'rpId': 51,
#         'frequency': 43,
#         'description': '旅行 新生成',
#         'domain': 'new',
#         'timestamp': '2020-05-05T10:52:50.000+0800',
#         'fresh': '2020-05-05T10:52:35.000+0800', 'support': 43, 'md5': '26118633'},
#     'data': [{
#         'id': 3364,
#         'goal': {
#             'goalId': 3364,
#             'content': '旅行',
#             'parentId': -1,
#             'requireId': -1,
#             'restricts': [],
#             'optTargets': None,
#             'hasMatched': False,
#             'rpId': 51},
#         'children': []
#     }],
#     'goalNum': 1
# }


def write_cover():
    with open("cover_res_2_final.txt", 'w', encoding='utf-8')as fw:
        with open("cover_res_2_1_65.txt", 'r', encoding='utf-8') as fc:
            content = fc.read()
            fw.write(content)
        with open("cover_res_2_65_100.txt", 'r', encoding='utf-8') as fc:
            content = fc.read()
            fw.write(content)
        with open("cover_res_2_101_150.txt", 'r', encoding='utf-8') as fc:
            content = fc.read()
            fw.write(content)
        with open("cover_res_2_151_200.txt", 'r', encoding='utf-8') as fc:
            content = fc.read()
            fw.write(content)
        with open("cover_res_2_201_250.txt", 'r', encoding='utf-8') as fc:
            content = fc.read()
            fw.write(content)
        with open("cover_res_2_251_300.txt", 'r', encoding='utf-8') as fc:
            content = fc.read()
            fw.write(content)
        with open("cover_res_2_301_350.txt", 'r', encoding='utf-8') as fc:
            content = fc.read()
            fw.write(content)
        with open("cover_res_2_351_400.txt", 'r', encoding='utf-8') as fc:
            content = fc.read()
            fw.write(content)
        with open("cover_res_2_401_450.txt", 'r', encoding='utf-8') as fc:
            content = fc.read()
            fw.write(content)
        with open("cover_res_2_451_500.txt", 'r', encoding='utf-8') as fc:
            content = fc.read()
            fw.write(content)
    return 0

# write_cover()


# single_test_sample = {'id': 3364, 'goal': {'goalId': 3364, 'content': '旅行', 'parentId': -1, 'requireId': -1, 'restricts': [], 'optTargets': None, 'hasMatched': False, 'rpId': 51}, 'children': []}


