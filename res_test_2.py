#!/usr/bin/env python

# encoding: utf-8
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/1 22:07
# @Author  : junruit
# @File    : res_test_2.py
# @desc: PyCharm
'''
import json
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


def calculate_e0_round(test_sample):
    counter = 0
    queue = [test_sample]
    content_num = 0
    # children_nodes = test_sample['children']
    # children_content = []
    while len(queue) > 0:
        children_nodes_set = []
        for j in queue:
            content = j['goal']['content']
            content_num = content_num + 1
            # 你需要什么 旅行
            counter = counter + 1
            restrict = j['goal']['restricts']
            # 额外的 "没有了"
            counter = counter + len(restrict) + 1
            children_nodes = j['children']
            children_nodes_set.extend(children_nodes)
            # another child content? --no
            counter = counter + 1
        queue = children_nodes_set
    counter = counter + 1
    return counter, content_num


def e0_write(test_rp_sample):
    with open("e0_without_rp_res_499.txt", 'w', encoding='utf-8') as f1:
        num = 0
        for i in test_rp_sample:
            num = num + 1
            res, content_num = calculate_e0_round(i)
            str_round_e0 = "No: " + str(num) + "\t" + "Content_num: " + str(content_num) + "\t" + "Round: " + str(res) + "\t" + "cover: 1\n"
            f1.write(str_round_e0)


def get_content_from_kg(file_name):
    with open(file_name, 'r', encoding='utf-8') as fo:
        rps_db = json.load(fo)
    content_set = []
    for i in rps_db:
        # q = i['data'][0]
        queue = [i]
        # children_nodes = test_sample['children']
        # children_content = []
        while len(queue) > 0:
            children_nodes_set = []
            for j in queue:
                content = j['goal']['content']
                if content not in content_set:
                    content_set.append(content)
                children_nodes = j['children']
                children_nodes_set.extend(children_nodes)
            queue = children_nodes_set
    return content_set


def get_content_from_rps(file_name):
    with open(file_name, 'r', encoding='utf-8') as fo:
        rps_db = json.load(fo)
    content_set = []
    for i in rps_db:
        q = i['data'][0]
        queue = [q]
        # children_nodes = test_sample['children']
        # children_content = []
        while len(queue) > 0:
            children_nodes_set = []
            for j in queue:
                content = j['goal']['content']
                if content not in content_set:
                    content_set.append(content)
                children_nodes = j['children']
                children_nodes_set.extend(children_nodes)
            queue = children_nodes_set
    return content_set


def get_restricts_from_rps(file_name):
    with open(file_name, 'r', encoding='utf-8') as fo:
        rps_db = json.load(fo)
    content_set = []
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
                if content not in content_set:
                    content_set.append(content)
                    restricts_set[content] = []
                    for k in restricts:
                        restricts_set[content].append(k)
                else:
                    for k in restricts:
                        restricts_set[content].append(k)
                children_nodes = j['children']
                children_nodes_set.extend(children_nodes)
            queue = children_nodes_set
    return restricts_set


def content_write(set_name, num):
    file_name = "k" + str(num) + "_content_set.txt"
    with open(file_name, 'w', encoding='utf-8') as fw:
        for t in set_name:
            fw.write(t)
            fw.write("\n")


def restricts_write(set_name, num):
    file_name = "k" + str(num) + "_restricts_set.txt"
    with open(file_name, 'w', encoding='utf-8') as fw:
        for key, value in set_name.items():
            if len(value) == 0:
                fw.write(str(key))
                fw.write("\t")
                fw.write(str(value))
                fw.write("\n")
            else:
                for s in value:
                    fw.write(str(key))
                    fw.write("\t")
                    fw.write(str(s))
                    fw.write("\n")


def judge_content_extra_kg():
    judge = random.random()
    if (judge > 0.7) and (judge < 0.9):
        return 1
    elif judge > 0.9:
        return 2
    else:
        return 0


def judge_content(content):
    with open("./rp_db_content_set/kg_content_set.txt", 'r', encoding='utf-8') as f:
        content_set = f.read()
    if content in content_set:
        return 1
    else:
        return 0


def judge_content_from_rpdb(content, num):
    file_path = "./rp_db_content_set/k" + str(num) + "_content_set.txt"
    with open(file_path, 'r', encoding='utf-8') as ff:
        content_set = ff.read()
    if content in content_set:
        return 1
    else:
        return 0


def summary_e4_res():
    final_res = {}
    with open("./k2_Grc/final_res_k2_旅行.json", 'w', encoding='utf-8') as fw:
        for i in range(1, 13):
            file_path = "./k2_Grc/final_res_k2_旅行_clu" + str(i) + ".txt"
            with open(file_path, 'r', encoding='utf-8') as fr:
                sentence = fr.readline()
                while sentence:
                    array = sentence.split("\t")
                    # print(sentence)
                    temp = eval(array[0])
                    final_res[temp] = int(array[1])
                    # print(type(array[0]))
                    sentence = fr.readline()
        # print(final_res)
        # final_res = sorted(final_res.items())
        # print(final_res)
        json.dump(final_res, fw, ensure_ascii=False)


# summary_e4_res()


def restricts_round(content, restrict, num):
    file_path = "./data/rps_supp_" + str(num) + ".json"
    restricts_dic = get_restricts_from_rps(file_path)
    restricts_set = restricts_dic[content]
    res = 0
    restrict_key = []
    for i in restricts_set:
        if i['key'] not in restrict_key:
            restrict_key.append(i['key'])
    for j in restrict:
        if j['key'] in restrict_key:
            pass
        else:
            res = res + 1

    return res


def calculate_e1_kg_round_cover(test_sample):
    counter = 0
    queue = [test_sample]
    content_num = 0
    extra_num = 0
    lack_num = 0
    while len(queue) > 0:
        children_nodes_set = []
        for j in queue:
            # 你需要什么 旅行
            counter = counter + 1
            content = j['goal']['content']
            if judge_content(content) != 1:
                lack_num = lack_num + 1
                # 你需要什么 旅行 -匹配不到 你还需要什么
                counter = counter + 1
            else:
                content_num = content_num + 1
                restrict = j['goal']['restricts']
                # 额外的约束 "没有了"
                counter = counter + len(restrict) + 1
                children_nodes = j['children']
                # if content != "旅行" and (judge_content_extra_kg() == 1):
                #     extra_num = extra_num + 1
                #     counter = counter + 1
                #     # children_nodes.append(extra_child_node)
                #     counter = counter + 1
                #     content_num = content_num + 1
                children_nodes_set.extend(children_nodes)
                # another child content? --no
                counter = counter + 1
        queue = children_nodes_set
    counter = counter + 1
    return counter, content_num, extra_num, lack_num


def random_db(rparr):
    length = len(rparr)
    if length < 1:
        return []
    if length == 1:
        return rparr[0]
    randomNumber = random.randint(0, length-1)
    return rparr[randomNumber]


def choose_rp_from_db(num, no, mode):
    file_name = "./k" + str(num) + "_Grc/k" + str(num) + "_content_旅行.json"
    with open(file_name, 'r', encoding='utf-8') as fo:
        rps_db = json.load(fo)
    content_set = {}
    restricts_set = {}
    # mode 1 random
    if mode == 1:
        i = random_db(rps_db)
    # mode 2 同余
    if mode == 2:
        i = rps_db[(no - 1) % len(rps_db)]
    q = i['data'][0]
    queue = [q]
    # children_nodes = test_sample['children']
    # children_content = []
    while len(queue) > 0:
        children_nodes_set = []
        for j in queue:
            content = j['goal']['content']
            restricts = j['goal']['restricts']
            # k_set = []
            # for k, v in content_set.items():
            #     if k not in k_set:
            #         k_set.append(k)
            if content not in content_set:
                # content_set[content]  [0]children [1]father
                content_set[content] = []
                restricts_set[content] = []
            restricts_set[content].extend(restricts)
            children_nodes = j['children']
            child_content = []
            for w in children_nodes:
                if w['goal']['content'] not in child_content:
                    child_content.append(w['goal']['content'])
            content_set[content].append(child_content)
            children_nodes_set.extend(children_nodes)
        queue = children_nodes_set
    return restricts_set, content_set


# num 是rpdb-支持度
def calculate_e2_rpdb_round_cover(test_sample, num, no, mode):
    counter = 0
    queue = [test_sample]
    r_set, c_set = choose_rp_from_db(num, no, mode)
    content_num = 0
    extra_num = 0
    content_test_sample_set = []
    lack_num = 0
    while len(queue) > 0:
        children_nodes_set = []
        for j in queue:
            # 你需要什么 旅行
            counter = counter + 1
            content = j['goal']['content']
            if content not in content_test_sample_set:
                content_test_sample_set.append(content)
            if judge_content_from_rpdb(content, num) != 1:
                lack_num = lack_num + 1
                # 你需要什么 旅行 -匹配不到 你还需要什么
                counter = counter + 1
            else:
                content_num = content_num + 1
                restrict = j['goal']['restricts']
                # 在模式中能匹配到的内容 作为一个整体返回给用户--- 符合我的要求/xx需要改动
                counter = counter + 1
                # if len(restrict) == 0:
                #     # 没什么约束。什么都行
                #     counter = counter + 1
                # else:
                #     # 对于现有的约束XXX你觉得如何
                #     # XXX要XX的
                #     len_restricts_round = restricts_round(content, restrict, num)
                #     if len_restricts_round == 0:
                #         # 没问题，我可以接受
                #         counter = counter + 1
                #     else:
                #         counter = counter + len_restricts_round
                # 额外的约束 "没有了"
                counter = counter + 1
                children_nodes = j['children']
                # if content != "旅行" and (judge_content_extra_kg() == 1):
                #     extra_num = extra_num + 1
                #     counter = counter + 1
                #     # children_nodes.append(extra_child_node)
                #     counter = counter + 1
                #     content_num = content_num + 1
                children_nodes_set.extend(children_nodes)
                # another child content? --no
                counter = counter + 1

        queue = children_nodes_set
    counter = counter + 1
    child_no_need = []
    for key, value in c_set.items():
        if (key not in content_test_sample_set) and (key not in child_no_need):
            child_no_need.extend(c_set[key][0])
            counter = counter + 1
    return counter, content_num, extra_num, lack_num


def calculate_e2_rpdb_round_cover_v2(test_sample, num, no):
    counter = 0
    queue = [test_sample]
    r_set, c_set = choose_rp_from_db(num, no)
    content_num = 0
    extra_num = 0
    lack_num = 0
    cal_c_set = []
    # 你需要什么 旅行
    counter = counter + 1
    while len(queue) > 0:
        children_nodes_set = []
        for j in queue:

            content = j['goal']['content']

            if judge_content_from_rpdb(content, num) != 1:
                lack_num = lack_num + 1
                # 你需要什么 旅行 -匹配不到 你还需要什么
                counter = counter + 1
            else:
                if content not in cal_c_set:
                    cal_c_set.append(content)
                content_num = content_num + 1
                # 这里会出现第一次未识别到找到最浅的content节点
                if content not in r_set:
                    restrict_rp = []
                else:
                    restrict_rp = r_set[content]
                restrict = j['goal']['restricts']
                # r_key replace 测试需求树中的约束 rp_key 需求模式约束集合
                r_key = []
                for key in restrict:
                    if key['key'] not in r_key:
                        r_key.append(key['key'])
                rp_key = []
                for key in restrict_rp:
                    if key['key'] not in rp_key:
                        rp_key.append(key['key'])
                if len(restrict) == 0:
                    # 没什么约束。什么都行
                    counter = counter + 1
                else:
                    for d in rp_key:
                        if d not in r_key:
                            counter = counter + 1
                    # 对于现有的约束XXX你觉得如何
                    # XXX要XX的
                    # len_restricts_round = restricts_round(content, restrict, num)
                    # if len_restricts_round == 0:
                    #     # 没问题，我可以接受
                    #     counter = counter + 1
                    # else:
                    #     counter = counter + len_restricts_round

                # 额外的约束 "没有了"
                counter = counter + 1
                children_nodes = j['children']
                # if content != "旅行" and (judge_content_extra_kg() == 1):
                #     extra_num = extra_num + 1
                #     counter = counter + 1
                #     # children_nodes.append(extra_child_node)
                #     counter = counter + 1
                #     content_num = content_num + 1
                children_nodes_set.extend(children_nodes)
                # another child content? --no
                counter = counter + 1

        queue = children_nodes_set
    counter = counter + 1
    for i in cal_c_set:
        if i not in c_set:
            counter = counter + 1
    ro = []
    for m, h in c_set.items():
        if m not in cal_c_set:
            ro.extend(c_set[m][0])
            ro.append(m)
    counter = counter + len(c_set) - len(ro)
    return counter, content_num, extra_num, lack_num


def calculate_e3_rpdb_round_cover(test_sample, num, no, mode):
    counter = 0
    queue = [test_sample]
    r_set, c_set = choose_rp_from_db(num, no, mode)
    content_num = 0
    extra_num = 0
    content_test_sample_set = []
    lack_num = 0
    while len(queue) > 0:
        children_nodes_set = []
        for j in queue:
            # 你需要什么 旅行
            counter = counter + 1
            content = j['goal']['content']
            if content not in content_test_sample_set:
                content_test_sample_set.append(content)
            if (judge_content_from_rpdb(content, num) != 1) and (judge_content(content) != 1):
                lack_num = lack_num + 1
                # 你需要什么 旅行 -匹配不到 你还需要什么
                counter = counter + 1
            # 模式库匹配不到 但是能在知识图谱中找到
            elif (judge_content_from_rpdb(content, num) != 1) and (judge_content(content) == 1):
                content_num = content_num + 1
                restrict = j['goal']['restricts']
                # 额外的约束 "没有了"
                counter = counter + len(restrict) + 1
                children_nodes = j['children']
                children_nodes_set.extend(children_nodes)
                # another child content? --no
                counter = counter + 1
            else:
                content_num = content_num + 1
                restrict = j['goal']['restricts']
                # 在模式中能匹配到的内容 作为一个整体返回给用户--- 符合我的要求/xx需要改动
                counter = counter + 1
                # if len(restrict) == 0:
                #     # 没什么约束。什么都行
                #     counter = counter + 1
                # else:
                #     # 对于现有的约束XXX你觉得如何
                #     # XXX要XX的
                #     len_restricts_round = restricts_round(content, restrict, num)
                #     if len_restricts_round == 0:
                #         # 没问题，我可以接受
                #         counter = counter + 1
                #     else:
                #         counter = counter + len_restricts_round
                # 额外的约束 "没有了"
                counter = counter + 1
                children_nodes = j['children']
                children_nodes_set.extend(children_nodes)
                # another child content? --no
                counter = counter + 1

        queue = children_nodes_set
    counter = counter + 1
    child_no_need = []
    for key, value in c_set.items():
        if (key not in content_test_sample_set) and (key not in child_no_need):
            child_no_need.extend(c_set[key][0])
            counter = counter + 1
    return counter, content_num, extra_num, lack_num


def calculate_e4_grc_fill_round_cover(test_sample, num):
    counter = 0
    queue = [test_sample]
    content_num = 0
    extra_num = 0
    # 你需要什么 旅行
    # counter = counter + 1
    lack_num = 0
    while len(queue) > 0:
        children_nodes_set = []
        for j in queue:
            content = j['goal']['content']
            if content in content_epoch_2:
                content_num = content_num + 1
                if content == '出租':
                    counter = counter + 1
                elif content == '景点':
                    counter = counter + 1
                    restrict = j['goal']['restricts']
                    if len(restrict) != 3:
                        counter = counter + 3 - len(restrict)
                    else:
                        counter = counter + 3
                elif content == '酒店':
                    counter = counter + 1
                    restrict = j['goal']['restricts']
                    if len(restrict) != 3:
                        counter = counter + 3 - len(restrict)
                    else:
                        counter = counter + 3
                    counter = counter + 1
                    t = judge_content_extra_kg()
                    if t > 1:
                        counter = counter + 2
                    elif t == 1:
                        counter = counter + 1

                elif content == '餐馆':
                    counter = counter + 1
                    restrict = j['goal']['restricts']
                    if len(restrict) != 3:
                        counter = counter + 3 - len(restrict)
                    else:
                        counter = counter + 3
                    counter = counter + 1
                    t = judge_content_extra_kg()
                    if t > 1:
                        counter = counter + 2
                    elif t == 1:
                        counter = counter + 1

                elif content == '地铁':
                    counter = counter + 1
                children_nodes = j['children']
                children_nodes_set.extend(children_nodes)
            else:
                counter = counter + 1
                if (judge_content_from_rpdb(content, num) != 1) and (judge_content(content) != 1):
                    lack_num = lack_num + 1
                    # 你需要什么 旅行 -匹配不到 你还需要什么
                    counter = counter + 1
                    restrict = j['goal']['restricts']
                    # 额外的 "没有了"
                    counter = counter + len(restrict) + 1
                    children_nodes = j['children']
                    children_nodes_set.extend(children_nodes)
                    # another child content? --no
                    counter = counter + 1
                # 模式库匹配不到 但是能在知识图谱中找到
                elif (judge_content_from_rpdb(content, num) != 1) and (judge_content(content) == 1):
                    content_num = content_num + 1
                    restrict = j['goal']['restricts']
                    # 额外的约束 "没有了"
                    counter = counter + len(restrict)
                    children_nodes = j['children']
                    children_nodes_set.extend(children_nodes)
                else:
                    content_num = content_num + 1
                    restrict = j['goal']['restricts']
                    # 在模式中能匹配到的内容 作为一个整体返回给用户--- 符合我的要求/xx需要改动
                    if content != '旅行':
                        counter = counter + 1 + len(restrict)
                    children_nodes = j['children']
                    children_nodes_set.extend(children_nodes)
        queue = children_nodes_set
        counter = counter + 1
    counter = counter + 1 + 1
    # for key, value in c_set.items():
    #     if key not in content_test_sample_set and key not in child_no_need:
    #         child_no_need.extend(c_set[key][0])
    #         counter = counter + 1
    return counter, content_num, extra_num, lack_num


content_epoch_2 = ['出租', '景点', '酒店', '餐馆', '地铁']


def calculate_e4_grc_bottom_to_top_round_cover(test_sample, num):
    counter = 0
    queue = [test_sample]
    content_num = 0
    extra_num = 0
    # 你需要什么 旅行
    # counter = counter + 1
    lack_num = 0
    while len(queue) > 0:
        children_nodes_set = []
        for j in queue:
            content = j['goal']['content']
            if content in content_epoch_2:
                content_num = content_num + 1
                if content == '出租':
                    counter = counter + 1
                elif content == '景点':
                    counter = counter + 1
                    restrict = j['goal']['restricts']
                    if len(restrict) != 3:
                        counter = counter + 3 - len(restrict)
                    else:
                        counter = counter + 3
                elif content == '酒店':
                    counter = counter + 1
                    restrict = j['goal']['restricts']
                    if len(restrict) != 3:
                        counter = counter + 3 - len(restrict)
                    else:
                        counter = counter + 3
                    counter = counter + 1
                    t = judge_content_extra_kg()
                    if t > 1:
                        counter = counter + 2
                    elif t == 1:
                        counter = counter + 1

                elif content == '餐馆':
                    counter = counter + 1
                    restrict = j['goal']['restricts']
                    if len(restrict) != 3:
                        counter = counter + 3 - len(restrict)
                    else:
                        counter = counter + 3
                    counter = counter + 1
                    t = judge_content_extra_kg()
                    if t > 1:
                        counter = counter + 2
                    elif t == 1:
                        counter = counter + 1

                elif content == '地铁':
                    counter = counter + 1
                children_nodes = j['children']
                children_nodes_set.extend(children_nodes)
            else:
                counter = counter + 1
                if (judge_content_from_rpdb(content, num) != 1) and (judge_content(content) != 1):
                    lack_num = lack_num + 1
                    # 你需要什么 旅行 -匹配不到 你还需要什么
                    counter = counter + 1
                # 模式库匹配不到 但是能在知识图谱中找到
                elif (judge_content_from_rpdb(content, num) != 1) and (judge_content(content) == 1):
                    content_num = content_num + 1
                    restrict = j['goal']['restricts']
                    # 额外的约束 "没有了"
                    counter = counter + len(restrict)
                    children_nodes = j['children']
                    children_nodes_set.extend(children_nodes)
                else:
                    content_num = content_num + 1
                    restrict = j['goal']['restricts']
                    # 在模式中能匹配到的内容 作为一个整体返回给用户--- 符合我的要求/xx需要改动
                    # counter = counter + 1 + len(restrict)
                    children_nodes = j['children']
                    children_nodes_set.extend(children_nodes)
        queue = children_nodes_set
        counter = counter + 1
    counter = counter + 1 + 1
    # for key, value in c_set.items():
    #     if key not in content_test_sample_set and key not in child_no_need:
    #         child_no_need.extend(c_set[key][0])
    #         counter = counter + 1
    return counter, content_num, extra_num, lack_num


def k3_calculate_e4_grc_fill_round_cover(test_sample, num):
    counter = 0
    queue = [test_sample]
    content_num = 0
    extra_num = 0
    # 你需要什么 旅行
    # counter = counter + 1
    lack_num = 0
    while len(queue) > 0:
        children_nodes_set = []
        for j in queue:
            content = j['goal']['content']
            if content in content_epoch_2:
                content_num = content_num + 1
                if content == '出租':
                    counter = counter + 1
                elif content == '景点':
                    counter = counter + 1
                    restrict = j['goal']['restricts']
                    if len(restrict) != 3:
                        counter = counter + 3 - len(restrict)
                    else:
                        counter = counter + 3
                elif content == '酒店':
                    counter = counter + 1
                    restrict = j['goal']['restricts']
                    if len(restrict) != 3:
                        counter = counter + 3 - len(restrict)
                    else:
                        counter = counter + 3
                    counter = counter + 1
                    t = judge_content_extra_kg()
                    if t > 1:
                        counter = counter + 2
                    elif t == 1:
                        counter = counter + 1

                elif content == '餐馆':
                    counter = counter + 1
                    restrict = j['goal']['restricts']

                elif content == '地铁':
                    counter = counter + 1
                children_nodes = j['children']
                children_nodes_set.extend(children_nodes)
            else:
                counter = counter + 1
                if (judge_content_from_rpdb(content, num) != 1) and (judge_content(content) != 1):
                    lack_num = lack_num + 1
                    # 你需要什么 旅行 -匹配不到 你还需要什么
                    counter = counter + 1
                    restrict = j['goal']['restricts']
                    # 额外的 "没有了"
                    counter = counter + len(restrict) + 1
                    children_nodes = j['children']
                    children_nodes_set.extend(children_nodes)
                    # another child content? --no
                    counter = counter + 1
                # 模式库匹配不到 但是能在知识图谱中找到
                elif (judge_content_from_rpdb(content, num) != 1) and (judge_content(content) == 1):
                    content_num = content_num + 1
                    restrict = j['goal']['restricts']
                    # 额外的约束 "没有了"
                    counter = counter + len(restrict)
                    children_nodes = j['children']
                    children_nodes_set.extend(children_nodes)
                else:
                    content_num = content_num + 1
                    restrict = j['goal']['restricts']
                    # 在模式中能匹配到的内容 作为一个整体返回给用户--- 符合我的要求/xx需要改动
                    if content != '旅行':
                        counter = counter + 1 + len(restrict)
                    children_nodes = j['children']
                    children_nodes_set.extend(children_nodes)
        queue = children_nodes_set
        counter = counter + 1
    counter = counter + 1 + 1
    # for key, value in c_set.items():
    #     if key not in content_test_sample_set and key not in child_no_need:
    #         child_no_need.extend(c_set[key][0])
    #         counter = counter + 1
    return counter, content_num, extra_num, lack_num


def k4_calculate_e4_grc_fill_round_cover(test_sample, num):
    counter = 0
    queue = [test_sample]
    content_num = 0
    extra_num = 0
    # 你需要什么 旅行
    # counter = counter + 1
    lack_num = 0
    while len(queue) > 0:
        children_nodes_set = []
        for j in queue:
            content = j['goal']['content']
            if content in content_epoch_2:
                content_num = content_num + 1
                if content == '出租':
                    counter = counter + 1
                elif content == '景点':
                    counter = counter + 1
                    restrict = j['goal']['restricts']
                    if len(restrict) <= 1:
                        counter = counter + 1  # 3条 中 一条无效 有1条/0条：1轮
                    else:
                        counter = counter + 2  # 2条/3条 2轮
                elif content == '酒店':
                    counter = counter + 1
                    restrict = j['goal']['restricts']
                    if len(restrict) != 3:
                        counter = counter + 3 - len(restrict)
                    else:
                        counter = counter + 3
                    counter = counter + 1
                    t = judge_content_extra_kg()
                    if t > 1:
                        counter = counter + 2
                    elif t == 1:
                        counter = counter + 1

                elif content == '餐馆':
                    counter = counter + 1
                    restrict = j['goal']['restricts']

                elif content == '地铁':
                    counter = counter + 1
                children_nodes = j['children']
                children_nodes_set.extend(children_nodes)
            else:
                counter = counter + 1
                if (judge_content_from_rpdb(content, num) != 1) and (judge_content(content) != 1):
                    lack_num = lack_num + 1
                    # 你需要什么 旅行 -匹配不到 你还需要什么
                    counter = counter + 1
                    restrict = j['goal']['restricts']
                    # 额外的 "没有了"
                    counter = counter + len(restrict) + 1
                    children_nodes = j['children']
                    children_nodes_set.extend(children_nodes)
                    # another child content? --no
                    counter = counter + 1
                # 模式库匹配不到 但是能在知识图谱中找到
                elif (judge_content_from_rpdb(content, num) != 1) and (judge_content(content) == 1):
                    content_num = content_num + 1
                    restrict = j['goal']['restricts']
                    # 额外的约束 "没有了"
                    counter = counter + len(restrict)
                    children_nodes = j['children']
                    children_nodes_set.extend(children_nodes)
                else:
                    content_num = content_num + 1
                    restrict = j['goal']['restricts']
                    # 在模式中能匹配到的内容 作为一个整体返回给用户--- 符合我的要求/xx需要改动
                    if content != '旅行':
                        counter = counter + 1 + len(restrict)
                    children_nodes = j['children']
                    children_nodes_set.extend(children_nodes)
        queue = children_nodes_set
        counter = counter + 1
    counter = counter + 1 + 1
    # for key, value in c_set.items():
    #     if key not in content_test_sample_set and key not in child_no_need:
    #         child_no_need.extend(c_set[key][0])
    #         counter = counter + 1
    return counter, content_num, extra_num, lack_num


def k5_calculate_e4_grc_fill_round_cover(test_sample, num):
    counter = 0
    queue = [test_sample]
    content_num = 0
    extra_num = 0
    # 你需要什么 旅行
    # counter = counter + 1
    lack_num = 0
    while len(queue) > 0:
        children_nodes_set = []
        for j in queue:
            content = j['goal']['content']
            if content in content_epoch_2:
                content_num = content_num + 1
                if content == '出租':
                    counter = counter + 1
                elif content == '景点':
                    counter = counter + 1
                    restrict = j['goal']['restricts']
                    if len(restrict) <= 1:
                        counter = counter + 1  # 3条 中 一条无效 有1条/0条：1轮
                    else:
                        counter = counter + 2  # 2条/3条 2轮
                elif content == '酒店':
                    counter = counter + 1
                    restrict = j['goal']['restricts']
                    counter = counter + 1
                    t = judge_content_extra_kg()
                    if t > 1:
                        counter = counter + 2
                    elif t == 1:
                        counter = counter + 1

                elif content == '餐馆':
                    counter = counter + 1
                    restrict = j['goal']['restricts']

                elif content == '地铁':
                    counter = counter + 1
                children_nodes = j['children']
                children_nodes_set.extend(children_nodes)
            else:
                counter = counter + 1
                if (judge_content_from_rpdb(content, num) != 1) and (judge_content(content) != 1):
                    lack_num = lack_num + 1
                    # 你需要什么 旅行 -匹配不到 你还需要什么
                    counter = counter + 1
                    restrict = j['goal']['restricts']
                    # 额外的 "没有了"
                    counter = counter + len(restrict) + 1
                    children_nodes = j['children']
                    children_nodes_set.extend(children_nodes)
                    # another child content? --no
                    counter = counter + 1
                # 模式库匹配不到 但是能在知识图谱中找到
                elif (judge_content_from_rpdb(content, num) != 1) and (judge_content(content) == 1):
                    content_num = content_num + 1
                    restrict = j['goal']['restricts']
                    # 额外的约束 "没有了"
                    counter = counter + len(restrict)
                    children_nodes = j['children']
                    children_nodes_set.extend(children_nodes)
                else:
                    content_num = content_num + 1
                    restrict = j['goal']['restricts']
                    # 在模式中能匹配到的内容 作为一个整体返回给用户--- 符合我的要求/xx需要改动
                    if content != '旅行':
                        counter = counter + 1 + len(restrict)
                    children_nodes = j['children']
                    children_nodes_set.extend(children_nodes)
        queue = children_nodes_set
        counter = counter + 1
    counter = counter + 1 + 1
    # for key, value in c_set.items():
    #     if key not in content_test_sample_set and key not in child_no_need:
    #         child_no_need.extend(c_set[key][0])
    #         counter = counter + 1
    return counter, content_num, extra_num, lack_num


def k6_calculate_e4_grc_fill_round_cover(test_sample, num):
    counter = 0
    queue = [test_sample]
    content_num = 0
    extra_num = 0
    # 你需要什么 旅行
    # counter = counter + 1
    lack_num = 0
    while len(queue) > 0:
        children_nodes_set = []
        for j in queue:
            content = j['goal']['content']
            if content in content_epoch_2:
                content_num = content_num + 1
                if content == '出租':
                    counter = counter + 1
                elif content == '景点':
                    counter = counter + 1
                    restrict = j['goal']['restricts']
                    if len(restrict) <= 1:
                        counter = counter + 1  # 3条 中 一条无效 有1条/0条：1轮
                    else:
                        counter = counter + 2  # 2条/3条 2轮
                elif content == '酒店':
                    counter = counter + 1
                    restrict = j['goal']['restricts']
                    ch = j['children']
                    # if len(ch) > 0:
                    # 一定要问一轮
                    counter = counter + 1

                elif content == '餐馆':
                    counter = counter + 1
                    restrict = j['goal']['restricts']

                elif content == '地铁':
                    counter = counter + 1
                children_nodes = j['children']
                children_nodes_set.extend(children_nodes)
            else:
                counter = counter + 1
                if (judge_content_from_rpdb(content, num) != 1) and (judge_content(content) != 1):
                    lack_num = lack_num + 1
                    # 你需要什么 旅行 -匹配不到 你还需要什么
                    counter = counter + 1
                    restrict = j['goal']['restricts']
                    # 额外的 "没有了"
                    counter = counter + len(restrict) + 1
                    children_nodes = j['children']
                    children_nodes_set.extend(children_nodes)
                    # another child content? --no
                    counter = counter + 1
                # 模式库匹配不到 但是能在知识图谱中找到
                elif (judge_content_from_rpdb(content, num) != 1) and (judge_content(content) == 1):
                    content_num = content_num + 1
                    restrict = j['goal']['restricts']
                    # 额外的约束 "没有了"
                    counter = counter + len(restrict)
                    children_nodes = j['children']
                    children_nodes_set.extend(children_nodes)
                else:
                    content_num = content_num + 1
                    restrict = j['goal']['restricts']
                    # 在模式中能匹配到的内容 作为一个整体返回给用户--- 符合我的要求/xx需要改动
                    if content != '旅行':
                        counter = counter + 1 + len(restrict)
                    children_nodes = j['children']
                    children_nodes_set.extend(children_nodes)
        queue = children_nodes_set
        counter = counter + 1
    counter = counter + 1 + 1
    # for key, value in c_set.items():
    #     if key not in content_test_sample_set and key not in child_no_need:
    #         child_no_need.extend(c_set[key][0])
    #         counter = counter + 1
    return counter, content_num, extra_num, lack_num


def k4_calculate_e4_grc_bottom_to_top_round_cover(test_sample, num):
    counter = 0
    queue = [test_sample]
    content_num = 0
    extra_num = 0
    # 你需要什么 旅行
    # counter = counter + 1
    lack_num = 0
    while len(queue) > 0:
        children_nodes_set = []
        for j in queue:
            content = j['goal']['content']
            if content in content_epoch_2:
                content_num = content_num + 1
                if content == '出租':
                    counter = counter + 1
                elif content == '景点':
                    counter = counter + 1
                    restrict = j['goal']['restricts']
                    if len(restrict) <= 1:
                        counter = counter + 1  # 3条 中 一条无效 有1条/0条：1轮
                    else:
                        counter = counter + 2  # 2条/3条 2轮

                elif content == '酒店':
                    counter = counter + 1
                    restrict = j['goal']['restricts']
                    if len(restrict) != 3:
                        counter = counter + 3 - len(restrict)
                    else:
                        counter = counter + 3
                    counter = counter + 1
                    t = judge_content_extra_kg()
                    if t > 1:
                        counter = counter + 2
                    elif t == 1:
                        counter = counter + 1

                elif content == '餐馆':
                    counter = counter + 1
                    restrict = j['goal']['restricts']

                elif content == '地铁':
                    counter = counter + 1

                children_nodes = j['children']
                children_nodes_set.extend(children_nodes)
            else:
                counter = counter + 1
                if (judge_content_from_rpdb(content, num) != 1) and (judge_content(content) != 1):
                    lack_num = lack_num + 1
                    # 你需要什么 旅行 -匹配不到 你还需要什么
                    counter = counter + 1
                # 模式库匹配不到 但是能在知识图谱中找到
                elif (judge_content_from_rpdb(content, num) != 1) and (judge_content(content) == 1):
                    content_num = content_num + 1
                    restrict = j['goal']['restricts']
                    # 额外的约束 "没有了"
                    counter = counter + len(restrict)
                    children_nodes = j['children']
                    children_nodes_set.extend(children_nodes)
                else:
                    content_num = content_num + 1
                    restrict = j['goal']['restricts']
                    # 在模式中能匹配到的内容 作为一个整体返回给用户--- 符合我的要求/xx需要改动
                    # counter = counter + 1 + len(restrict)
                    children_nodes = j['children']
                    children_nodes_set.extend(children_nodes)
        queue = children_nodes_set
        counter = counter + 1
    counter = counter + 1 + 1
    # for key, value in c_set.items():
    #     if key not in content_test_sample_set and key not in child_no_need:
    #         child_no_need.extend(c_set[key][0])
    #         counter = counter + 1
    return counter, content_num, extra_num, lack_num


def k5_calculate_e4_grc_bottom_to_top_round_cover(test_sample, num):
    counter = 0
    queue = [test_sample]
    content_num = 0
    extra_num = 0
    # 你需要什么 旅行
    # counter = counter + 1
    lack_num = 0
    while len(queue) > 0:
        children_nodes_set = []
        for j in queue:
            content = j['goal']['content']
            if content in content_epoch_2:
                content_num = content_num + 1
                if content == '出租':
                    counter = counter + 1
                elif content == '景点':
                    counter = counter + 1
                    restrict = j['goal']['restricts']
                    if len(restrict) <= 1:
                        counter = counter + 1  # 3条 中 一条无效 有1条/0条：1轮
                    else:
                        counter = counter + 2  # 2条/3条 2轮

                elif content == '酒店':
                    counter = counter + 1
                    restrict = j['goal']['restricts']
                    counter = counter + 1
                    t = judge_content_extra_kg()
                    if t > 1:
                        counter = counter + 2
                    elif t == 1:
                        counter = counter + 1

                elif content == '餐馆':
                    counter = counter + 1
                    restrict = j['goal']['restricts']

                elif content == '地铁':
                    counter = counter + 1

                children_nodes = j['children']
                children_nodes_set.extend(children_nodes)
            else:
                counter = counter + 1
                if (judge_content_from_rpdb(content, num) != 1) and (judge_content(content) != 1):
                    lack_num = lack_num + 1
                    # 你需要什么 旅行 -匹配不到 你还需要什么
                    counter = counter + 1
                # 模式库匹配不到 但是能在知识图谱中找到
                elif (judge_content_from_rpdb(content, num) != 1) and (judge_content(content) == 1):
                    content_num = content_num + 1
                    restrict = j['goal']['restricts']
                    # 额外的约束 "没有了"
                    counter = counter + len(restrict)
                    children_nodes = j['children']
                    children_nodes_set.extend(children_nodes)
                else:
                    content_num = content_num + 1
                    restrict = j['goal']['restricts']
                    # 在模式中能匹配到的内容 作为一个整体返回给用户--- 符合我的要求/xx需要改动
                    # counter = counter + 1 + len(restrict)
                    children_nodes = j['children']
                    children_nodes_set.extend(children_nodes)
        queue = children_nodes_set
        counter = counter + 1
    counter = counter + 1 + 1
    # for key, value in c_set.items():
    #     if key not in content_test_sample_set and key not in child_no_need:
    #         child_no_need.extend(c_set[key][0])
    #         counter = counter + 1
    return counter, content_num, extra_num, lack_num


def k6_calculate_e4_grc_bottom_to_top_round_cover(test_sample, num):
    counter = 0
    queue = [test_sample]
    content_num = 0
    extra_num = 0
    # 你需要什么 旅行
    # counter = counter + 1
    lack_num = 0
    while len(queue) > 0:
        children_nodes_set = []
        for j in queue:
            content = j['goal']['content']
            if content in content_epoch_2:
                content_num = content_num + 1
                if content == '出租':
                    counter = counter + 1
                elif content == '景点':
                    counter = counter + 1
                    restrict = j['goal']['restricts']
                    if len(restrict) <= 1:
                        counter = counter + 1  # 3条 中 一条无效 有1条/0条：1轮
                    else:
                        counter = counter + 2  # 2条/3条 2轮

                elif content == '酒店':
                    counter = counter + 1
                    restrict = j['goal']['restricts']
                    ch = j['children']
                    # if len(ch) > 0:
                    # 一定要问一轮
                    counter = counter + 1

                elif content == '餐馆':
                    counter = counter + 1
                    restrict = j['goal']['restricts']

                elif content == '地铁':
                    counter = counter + 1

                children_nodes = j['children']
                children_nodes_set.extend(children_nodes)
            else:
                counter = counter + 1
                if (judge_content_from_rpdb(content, num) != 1) and (judge_content(content) != 1):
                    lack_num = lack_num + 1
                    # 你需要什么 旅行 -匹配不到 你还需要什么
                    counter = counter + 1
                # 模式库匹配不到 但是能在知识图谱中找到
                elif (judge_content_from_rpdb(content, num) != 1) and (judge_content(content) == 1):
                    content_num = content_num + 1
                    restrict = j['goal']['restricts']
                    # 额外的约束 "没有了"
                    counter = counter + len(restrict)
                    children_nodes = j['children']
                    children_nodes_set.extend(children_nodes)
                else:
                    content_num = content_num + 1
                    restrict = j['goal']['restricts']
                    # 在模式中能匹配到的内容 作为一个整体返回给用户--- 符合我的要求/xx需要改动
                    # counter = counter + 1 + len(restrict)
                    children_nodes = j['children']
                    children_nodes_set.extend(children_nodes)
        queue = children_nodes_set
        counter = counter + 1
    counter = counter + 1 + 1
    # for key, value in c_set.items():
    #     if key not in content_test_sample_set and key not in child_no_need:
    #         child_no_need.extend(c_set[key][0])
    #         counter = counter + 1
    return counter, content_num, extra_num, lack_num


def k3_calculate_e4_grc_bottom_to_top_round_cover(test_sample, num):
    counter = 0
    queue = [test_sample]
    content_num = 0
    extra_num = 0
    # 你需要什么 旅行
    # counter = counter + 1
    lack_num = 0
    while len(queue) > 0:
        children_nodes_set = []
        for j in queue:
            content = j['goal']['content']
            if content in content_epoch_2:
                content_num = content_num + 1
                if content == '出租':
                    counter = counter + 1
                elif content == '景点':
                    counter = counter + 1
                    restrict = j['goal']['restricts']
                    if len(restrict) != 3:
                        counter = counter + 3 - len(restrict)
                    else:
                        counter = counter + 3

                elif content == '酒店':
                    counter = counter + 1
                    restrict = j['goal']['restricts']
                    if len(restrict) != 3:
                        counter = counter + 3 - len(restrict)
                    else:
                        counter = counter + 3
                    counter = counter + 1
                    t = judge_content_extra_kg()
                    if t > 1:
                        counter = counter + 2
                    elif t == 1:
                        counter = counter + 1

                elif content == '餐馆':
                    counter = counter + 1
                    restrict = j['goal']['restricts']

                elif content == '地铁':
                    counter = counter + 1

                children_nodes = j['children']
                children_nodes_set.extend(children_nodes)
            else:
                counter = counter + 1
                if (judge_content_from_rpdb(content, num) != 1) and (judge_content(content) != 1):
                    lack_num = lack_num + 1
                    # 你需要什么 旅行 -匹配不到 你还需要什么
                    counter = counter + 1
                # 模式库匹配不到 但是能在知识图谱中找到
                elif (judge_content_from_rpdb(content, num) != 1) and (judge_content(content) == 1):
                    content_num = content_num + 1
                    restrict = j['goal']['restricts']
                    # 额外的约束 "没有了"
                    counter = counter + len(restrict)
                    children_nodes = j['children']
                    children_nodes_set.extend(children_nodes)
                else:
                    content_num = content_num + 1
                    restrict = j['goal']['restricts']
                    # 在模式中能匹配到的内容 作为一个整体返回给用户--- 符合我的要求/xx需要改动
                    # counter = counter + 1 + len(restrict)
                    children_nodes = j['children']
                    children_nodes_set.extend(children_nodes)
        queue = children_nodes_set
        counter = counter + 1
    counter = counter + 1 + 1
    # for key, value in c_set.items():
    #     if key not in content_test_sample_set and key not in child_no_need:
    #         child_no_need.extend(c_set[key][0])
    #         counter = counter + 1
    return counter, content_num, extra_num, lack_num


def k3_calculate_e5_grc_top_to_bottom_round_cover(test_sample, num):
    counter = 0
    queue = [test_sample]
    content_num = 0
    extra_num = 0
    # 你需要什么 旅行
    # counter = counter + 1
    lack_num = 0
    while len(queue) > 0:
        children_nodes_set = []
        for j in queue:
            content = j['goal']['content']
            if content in content_epoch_2:
                content_num = content_num + 1
                if content == '出租':
                    counter = counter + 1
                elif content == '景点':
                    counter = counter + 1
                    restrict = j['goal']['restricts']
                    if len(restrict) != 3:
                        counter = counter + 3 - len(restrict)
                    else:
                        counter = counter + 3
                elif content == '酒店':
                    counter = counter + 1
                    restrict = j['goal']['restricts']
                    if len(restrict) != 3:
                        counter = counter + 3 - len(restrict)
                    else:
                        counter = counter + 3
                    ch = j['children']
                    p = judge_content_extra_kg()
                    if (len(ch) > 0) and (p == 1):
                        counter = counter + 2
                    if (len(ch) > 0) and (p == 2):
                        counter = counter + 3
                elif content == '餐馆':
                    counter = counter + 1
                    restrict = j['goal']['restricts']

                elif content == '地铁':
                    counter = counter + 1
                children_nodes = j['children']
                children_nodes_set.extend(children_nodes)
            else:
                counter = counter + 1
                if (judge_content_from_rpdb(content, num) != 1) and (judge_content(content) != 1):
                    lack_num = lack_num + 1
                    # 你需要什么 旅行 -匹配不到 你还需要什么
                    counter = counter + 1
                # 模式库匹配不到 但是能在知识图谱中找到
                elif (judge_content_from_rpdb(content, num) != 1) and (judge_content(content) == 1):
                    content_num = content_num + 1
                    restrict = j['goal']['restricts']
                    # 额外的约束 "没有了"
                    counter = counter + len(restrict)
                    children_nodes = j['children']
                    children_nodes_set.extend(children_nodes)
                else:
                    content_num = content_num + 1
                    restrict = j['goal']['restricts']
                    # 在模式中能匹配到的内容 作为一个整体返回给用户--- 符合我的要求/xx需要改动
                    # counter = counter + 1 + len(restrict)
                    children_nodes = j['children']
                    children_nodes_set.extend(children_nodes)
        queue = children_nodes_set
        counter = counter + 1
    counter = counter + 1 + 1
    return counter, content_num, extra_num, lack_num


def k4_calculate_e5_grc_top_to_bottom_round_cover(test_sample, num):
    counter = 0
    queue = [test_sample]
    content_num = 0
    extra_num = 0
    # 你需要什么 旅行
    # counter = counter + 1
    lack_num = 0
    while len(queue) > 0:
        children_nodes_set = []
        for j in queue:
            content = j['goal']['content']
            if content in content_epoch_2:
                content_num = content_num + 1
                if content == '出租':
                    counter = counter + 1
                elif content == '景点':
                    counter = counter + 1
                    restrict = j['goal']['restricts']
                    if len(restrict) <= 1:
                        counter = counter + 1  # 3条 中 一条无效 有1条/0条：1轮
                    else:
                        counter = counter + 2  # 2条/3条 2轮
                elif content == '酒店':
                    counter = counter + 1
                    restrict = j['goal']['restricts']
                    if len(restrict) != 3:
                        counter = counter + 3 - len(restrict)
                    else:
                        counter = counter + 3
                    ch = j['children']
                    p = judge_content_extra_kg()
                    if (len(ch) > 0) and (p == 1):
                        counter = counter + 2
                    if (len(ch) > 0) and (p == 2):
                        counter = counter + 3
                elif content == '餐馆':
                    counter = counter + 1
                    restrict = j['goal']['restricts']

                elif content == '地铁':
                    counter = counter + 1
                children_nodes = j['children']
                children_nodes_set.extend(children_nodes)
            else:
                counter = counter + 1
                if (judge_content_from_rpdb(content, num) != 1) and (judge_content(content) != 1):
                    lack_num = lack_num + 1
                    # 你需要什么 旅行 -匹配不到 你还需要什么
                    counter = counter + 1
                # 模式库匹配不到 但是能在知识图谱中找到
                elif (judge_content_from_rpdb(content, num) != 1) and (judge_content(content) == 1):
                    content_num = content_num + 1
                    restrict = j['goal']['restricts']
                    # 额外的约束 "没有了"
                    counter = counter + len(restrict)
                    children_nodes = j['children']
                    children_nodes_set.extend(children_nodes)
                else:
                    content_num = content_num + 1
                    restrict = j['goal']['restricts']
                    # 在模式中能匹配到的内容 作为一个整体返回给用户--- 符合我的要求/xx需要改动
                    # counter = counter + 1 + len(restrict)
                    children_nodes = j['children']
                    children_nodes_set.extend(children_nodes)
        queue = children_nodes_set
        counter = counter + 1
    counter = counter + 1 + 1
    return counter, content_num, extra_num, lack_num


def k5_calculate_e5_grc_top_to_bottom_round_cover(test_sample, num):
    counter = 0
    queue = [test_sample]
    content_num = 0
    extra_num = 0
    # 你需要什么 旅行
    # counter = counter + 1
    lack_num = 0
    while len(queue) > 0:
        children_nodes_set = []
        for j in queue:
            content = j['goal']['content']
            if content in content_epoch_2:
                content_num = content_num + 1
                if content == '出租':
                    counter = counter + 1
                elif content == '景点':
                    counter = counter + 1
                    restrict = j['goal']['restricts']
                    if len(restrict) <= 1:
                        counter = counter + 1  # 3条 中 一条无效 有1条/0条：1轮
                    else:
                        counter = counter + 2  # 2条/3条 2轮
                elif content == '酒店':
                    counter = counter + 1
                    restrict = j['goal']['restricts']
                    ch = j['children']
                    p = judge_content_extra_kg()
                    if (len(ch) > 0) and (p == 1):
                        counter = counter + 2
                    if (len(ch) > 0) and (p == 2):
                        counter = counter + 3
                elif content == '餐馆':
                    counter = counter + 1
                    restrict = j['goal']['restricts']

                elif content == '地铁':
                    counter = counter + 1
                children_nodes = j['children']
                children_nodes_set.extend(children_nodes)
            else:
                counter = counter + 1
                if (judge_content_from_rpdb(content, num) != 1) and (judge_content(content) != 1):
                    lack_num = lack_num + 1
                    # 你需要什么 旅行 -匹配不到 你还需要什么
                    counter = counter + 1
                # 模式库匹配不到 但是能在知识图谱中找到
                elif (judge_content_from_rpdb(content, num) != 1) and (judge_content(content) == 1):
                    content_num = content_num + 1
                    restrict = j['goal']['restricts']
                    # 额外的约束 "没有了"
                    counter = counter + len(restrict)
                    children_nodes = j['children']
                    children_nodes_set.extend(children_nodes)
                else:
                    content_num = content_num + 1
                    restrict = j['goal']['restricts']
                    # 在模式中能匹配到的内容 作为一个整体返回给用户--- 符合我的要求/xx需要改动
                    # counter = counter + 1 + len(restrict)
                    children_nodes = j['children']
                    children_nodes_set.extend(children_nodes)
        queue = children_nodes_set
        counter = counter + 1
    counter = counter + 1 + 1
    return counter, content_num, extra_num, lack_num


def k6_calculate_e5_grc_top_to_bottom_round_cover(test_sample, num):
    counter = 0
    queue = [test_sample]
    content_num = 0
    extra_num = 0
    # 你需要什么 旅行
    # counter = counter + 1
    lack_num = 0
    while len(queue) > 0:
        children_nodes_set = []
        for j in queue:
            content = j['goal']['content']
            if content in content_epoch_2:
                content_num = content_num + 1
                if content == '出租':
                    counter = counter + 1
                elif content == '景点':
                    counter = counter + 1
                    restrict = j['goal']['restricts']
                    if len(restrict) <= 1:
                        counter = counter + 1  # 3条 中 一条无效 有1条/0条：1轮
                    else:
                        counter = counter + 2  # 2条/3条 2轮
                elif content == '酒店':
                    counter = counter + 1
                    restrict = j['goal']['restricts']
                    ch = j['children']
                    if len(ch) > 0:
                        counter = counter + 1
                elif content == '餐馆':
                    counter = counter + 1
                    restrict = j['goal']['restricts']

                elif content == '地铁':
                    counter = counter + 1
                children_nodes = j['children']
                children_nodes_set.extend(children_nodes)
            else:
                counter = counter + 1
                if (judge_content_from_rpdb(content, num) != 1) and (judge_content(content) != 1):
                    lack_num = lack_num + 1
                    # 你需要什么 旅行 -匹配不到 你还需要什么
                    counter = counter + 1
                # 模式库匹配不到 但是能在知识图谱中找到
                elif (judge_content_from_rpdb(content, num) != 1) and (judge_content(content) == 1):
                    content_num = content_num + 1
                    restrict = j['goal']['restricts']
                    # 额外的约束 "没有了"
                    counter = counter + len(restrict)
                    children_nodes = j['children']
                    children_nodes_set.extend(children_nodes)
                else:
                    content_num = content_num + 1
                    restrict = j['goal']['restricts']
                    # 在模式中能匹配到的内容 作为一个整体返回给用户--- 符合我的要求/xx需要改动
                    # counter = counter + 1 + len(restrict)
                    children_nodes = j['children']
                    children_nodes_set.extend(children_nodes)
        queue = children_nodes_set
        counter = counter + 1
    counter = counter + 1 + 1
    return counter, content_num, extra_num, lack_num


def calculate_e5_grc_top_to_bottom_round_cover(test_sample, num):
    counter = 0
    queue = [test_sample]
    content_num = 0
    extra_num = 0
    # 你需要什么 旅行
    # counter = counter + 1
    lack_num = 0
    while len(queue) > 0:
        children_nodes_set = []
        for j in queue:
            content = j['goal']['content']
            if content in content_epoch_2:
                content_num = content_num + 1
                if content == '出租':
                    counter = counter + 1
                elif content == '景点':
                    counter = counter + 1
                    restrict = j['goal']['restricts']
                    if len(restrict) != 3:
                        counter = counter + 3 - len(restrict)
                    else:
                        counter = counter + 3
                elif content == '酒店':
                    counter = counter + 1
                    restrict = j['goal']['restricts']
                    if len(restrict) != 3:
                        counter = counter + 3 - len(restrict)
                    else:
                        counter = counter + 3
                    ch = j['children']
                    p = judge_content_extra_kg()
                    if (len(ch) > 0) and (p == 1):
                        counter = counter + 2
                    if (len(ch) > 0) and (p == 2):
                        counter = counter + 3
                elif content == '餐馆':
                    counter = counter + 1
                    restrict = j['goal']['restricts']
                    if len(restrict) != 3:
                        counter = counter + 3 - len(restrict)
                    else:
                        counter = counter + 3
                    ch = j['children']
                    p = judge_content_extra_kg()
                    if (len(ch) > 0) and (p == 1):
                        counter = counter + 2
                    if (len(ch) > 0) and (p == 2):
                        counter = counter + 3
                elif content == '地铁':
                    counter = counter + 1
                children_nodes = j['children']
                children_nodes_set.extend(children_nodes)
            else:
                counter = counter + 1
                if (judge_content_from_rpdb(content, num) != 1) and (judge_content(content) != 1):
                    lack_num = lack_num + 1
                    # 你需要什么 旅行 -匹配不到 你还需要什么
                    counter = counter + 1
                # 模式库匹配不到 但是能在知识图谱中找到
                elif (judge_content_from_rpdb(content, num) != 1) and (judge_content(content) == 1):
                    content_num = content_num + 1
                    restrict = j['goal']['restricts']
                    # 额外的约束 "没有了"
                    counter = counter + len(restrict)
                    children_nodes = j['children']
                    children_nodes_set.extend(children_nodes)
                else:
                    content_num = content_num + 1
                    restrict = j['goal']['restricts']
                    # 在模式中能匹配到的内容 作为一个整体返回给用户--- 符合我的要求/xx需要改动
                    # counter = counter + 1 + len(restrict)
                    children_nodes = j['children']
                    children_nodes_set.extend(children_nodes)
        queue = children_nodes_set
        counter = counter + 1
    counter = counter + 1 + 1
    return counter, content_num, extra_num, lack_num


def k3_calculate_e5_grc_top_to_bottom_round_cover_fill(test_sample, num):
    counter = 0
    queue = [test_sample]
    content_num = 0
    extra_num = 0
    # 你需要什么 旅行
    # counter = counter + 1
    lack_num = 0
    while len(queue) > 0:
        children_nodes_set = []
        for j in queue:
            content = j['goal']['content']
            if content in content_epoch_2:
                content_num = content_num + 1
                if content == '出租':
                    counter = counter + 1
                elif content == '景点':
                    counter = counter + 1
                    restrict = j['goal']['restricts']
                    if len(restrict) != 3:
                        counter = counter + 3 - len(restrict)
                    else:
                        counter = counter + 3
                elif content == '酒店':
                    counter = counter + 1
                    restrict = j['goal']['restricts']
                    if len(restrict) != 3:
                        counter = counter + 3 - len(restrict)
                    else:
                        counter = counter + 3
                    ch = j['children']
                    p = judge_content_extra_kg()
                    if (len(ch) > 0) and (p == 1):
                        counter = counter + 2
                    if (len(ch) > 0) and (p == 2):
                        counter = counter + 3
                elif content == '餐馆':
                    counter = counter + 1
                    restrict = j['goal']['restricts']

                elif content == '地铁':
                    counter = counter + 1
                children_nodes = j['children']
                children_nodes_set.extend(children_nodes)
            else:
                counter = counter + 1
                if (judge_content_from_rpdb(content, num) != 1) and (judge_content(content) != 1):
                    lack_num = lack_num + 1
                    # 你需要什么 旅行 -匹配不到 你还需要什么
                    counter = counter + 1
                    restrict = j['goal']['restricts']
                    # 额外的 "没有了"
                    counter = counter + len(restrict) + 1
                    children_nodes = j['children']
                    children_nodes_set.extend(children_nodes)
                    # another child content? --no
                    counter = counter + 1
                # 模式库匹配不到 但是能在知识图谱中找到
                elif (judge_content_from_rpdb(content, num) != 1) and (judge_content(content) == 1):
                    content_num = content_num + 1
                    restrict = j['goal']['restricts']
                    # 额外的约束 "没有了"
                    counter = counter + len(restrict)
                    children_nodes = j['children']
                    children_nodes_set.extend(children_nodes)
                else:
                    content_num = content_num + 1
                    restrict = j['goal']['restricts']
                    # 在模式中能匹配到的内容 作为一个整体返回给用户--- 符合我的要求/xx需要改动
                    if content != '旅行':
                        counter = counter + 1 + len(restrict)
                    children_nodes = j['children']
                    children_nodes_set.extend(children_nodes)
        queue = children_nodes_set
        counter = counter + 1
    counter = counter + 1 + 1
    return counter, content_num, extra_num, lack_num


def k4_calculate_e5_grc_top_to_bottom_round_cover_fill(test_sample, num):
    counter = 0
    queue = [test_sample]
    content_num = 0
    extra_num = 0
    # 你需要什么 旅行
    # counter = counter + 1
    lack_num = 0
    while len(queue) > 0:
        children_nodes_set = []
        for j in queue:
            content = j['goal']['content']
            if content in content_epoch_2:
                content_num = content_num + 1
                if content == '出租':
                    counter = counter + 1
                elif content == '景点':
                    counter = counter + 1
                    restrict = j['goal']['restricts']
                    if len(restrict) <= 1:
                        counter = counter + 1  # 3条 中 一条无效 有1条/0条：1轮
                    else:
                        counter = counter + 2  # 2条/3条 2轮
                elif content == '酒店':
                    counter = counter + 1
                    restrict = j['goal']['restricts']
                    if len(restrict) != 3:
                        counter = counter + 3 - len(restrict)
                    else:
                        counter = counter + 3
                    ch = j['children']
                    p = judge_content_extra_kg()
                    if (len(ch) > 0) and (p == 1):
                        counter = counter + 2
                    if (len(ch) > 0) and (p == 2):
                        counter = counter + 3
                elif content == '餐馆':
                    counter = counter + 1
                    restrict = j['goal']['restricts']

                elif content == '地铁':
                    counter = counter + 1
                children_nodes = j['children']
                children_nodes_set.extend(children_nodes)
            else:
                counter = counter + 1
                if (judge_content_from_rpdb(content, num) != 1) and (judge_content(content) != 1):
                    lack_num = lack_num + 1
                    # 你需要什么 旅行 -匹配不到 你还需要什么
                    counter = counter + 1
                    restrict = j['goal']['restricts']
                    # 额外的 "没有了"
                    counter = counter + len(restrict) + 1
                    children_nodes = j['children']
                    children_nodes_set.extend(children_nodes)
                    # another child content? --no
                    counter = counter + 1
                # 模式库匹配不到 但是能在知识图谱中找到
                elif (judge_content_from_rpdb(content, num) != 1) and (judge_content(content) == 1):
                    content_num = content_num + 1
                    restrict = j['goal']['restricts']
                    # 额外的约束 "没有了"
                    counter = counter + len(restrict)
                    children_nodes = j['children']
                    children_nodes_set.extend(children_nodes)
                else:
                    content_num = content_num + 1
                    restrict = j['goal']['restricts']
                    # 在模式中能匹配到的内容 作为一个整体返回给用户--- 符合我的要求/xx需要改动
                    if content != '旅行':
                        counter = counter + 1 + len(restrict)
                    children_nodes = j['children']
                    children_nodes_set.extend(children_nodes)
        queue = children_nodes_set
        counter = counter + 1
    counter = counter + 1 + 1
    return counter, content_num, extra_num, lack_num


def k5_calculate_e5_grc_top_to_bottom_round_cover_fill(test_sample, num):
    counter = 0
    queue = [test_sample]
    content_num = 0
    extra_num = 0
    # 你需要什么 旅行
    # counter = counter + 1
    lack_num = 0
    while len(queue) > 0:
        children_nodes_set = []
        for j in queue:
            content = j['goal']['content']
            if content in content_epoch_2:
                content_num = content_num + 1
                if content == '出租':
                    counter = counter + 1
                elif content == '景点':
                    counter = counter + 1
                    restrict = j['goal']['restricts']
                    if len(restrict) <= 1:
                        counter = counter + 1  # 3条 中 一条无效 有1条/0条：1轮
                    else:
                        counter = counter + 2  # 2条/3条 2轮
                elif content == '酒店':
                    counter = counter + 1
                    restrict = j['goal']['restricts']
                    ch = j['children']
                    p = judge_content_extra_kg()
                    if (len(ch) > 0) and (p == 1):
                        counter = counter + 2
                    if (len(ch) > 0) and (p == 2):
                        counter = counter + 3
                elif content == '餐馆':
                    counter = counter + 1
                    restrict = j['goal']['restricts']

                elif content == '地铁':
                    counter = counter + 1
                children_nodes = j['children']
                children_nodes_set.extend(children_nodes)
            else:
                counter = counter + 1
                if (judge_content_from_rpdb(content, num) != 1) and (judge_content(content) != 1):
                    lack_num = lack_num + 1
                    # 你需要什么 旅行 -匹配不到 你还需要什么
                    counter = counter + 1
                    restrict = j['goal']['restricts']
                    # 额外的 "没有了"
                    counter = counter + len(restrict) + 1
                    children_nodes = j['children']
                    children_nodes_set.extend(children_nodes)
                    # another child content? --no
                    counter = counter + 1
                # 模式库匹配不到 但是能在知识图谱中找到
                elif (judge_content_from_rpdb(content, num) != 1) and (judge_content(content) == 1):
                    content_num = content_num + 1
                    restrict = j['goal']['restricts']
                    # 额外的约束 "没有了"
                    counter = counter + len(restrict)
                    children_nodes = j['children']
                    children_nodes_set.extend(children_nodes)
                else:
                    content_num = content_num + 1
                    restrict = j['goal']['restricts']
                    # 在模式中能匹配到的内容 作为一个整体返回给用户--- 符合我的要求/xx需要改动
                    if content != '旅行':
                        counter = counter + 1 + len(restrict)
                    children_nodes = j['children']
                    children_nodes_set.extend(children_nodes)
        queue = children_nodes_set
        counter = counter + 1
    counter = counter + 1 + 1
    return counter, content_num, extra_num, lack_num


def k6_calculate_e5_grc_top_to_bottom_round_cover_fill(test_sample, num):
    counter = 0
    queue = [test_sample]
    content_num = 0
    extra_num = 0
    # 你需要什么 旅行
    # counter = counter + 1
    lack_num = 0
    while len(queue) > 0:
        children_nodes_set = []
        for j in queue:
            content = j['goal']['content']
            if content in content_epoch_2:
                content_num = content_num + 1
                if content == '出租':
                    counter = counter + 1
                elif content == '景点':
                    counter = counter + 1
                    restrict = j['goal']['restricts']
                    if len(restrict) <= 1:
                        counter = counter + 1  # 3条 中 一条无效 有1条/0条：1轮
                    else:
                        counter = counter + 2  # 2条/3条 2轮
                elif content == '酒店':
                    counter = counter + 1
                    restrict = j['goal']['restricts']
                    ch = j['children']
                    if len(ch) > 0:
                        counter = counter + 1
                elif content == '餐馆':
                    counter = counter + 1
                    restrict = j['goal']['restricts']

                elif content == '地铁':
                    counter = counter + 1
                children_nodes = j['children']
                children_nodes_set.extend(children_nodes)
            else:
                counter = counter + 1
                if (judge_content_from_rpdb(content, num) != 1) and (judge_content(content) != 1):
                    lack_num = lack_num + 1
                    # 你需要什么 旅行 -匹配不到 你还需要什么
                    counter = counter + 1
                    restrict = j['goal']['restricts']
                    # 额外的 "没有了"
                    counter = counter + len(restrict) + 1
                    children_nodes = j['children']
                    children_nodes_set.extend(children_nodes)
                    # another child content? --no
                    counter = counter + 1
                # 模式库匹配不到 但是能在知识图谱中找到
                elif (judge_content_from_rpdb(content, num) != 1) and (judge_content(content) == 1):
                    content_num = content_num + 1
                    restrict = j['goal']['restricts']
                    # 额外的约束 "没有了"
                    counter = counter + len(restrict)
                    children_nodes = j['children']
                    children_nodes_set.extend(children_nodes)
                else:
                    content_num = content_num + 1
                    restrict = j['goal']['restricts']
                    # 在模式中能匹配到的内容 作为一个整体返回给用户--- 符合我的要求/xx需要改动
                    if content != '旅行':
                        counter = counter + 1 + len(restrict)
                    children_nodes = j['children']
                    children_nodes_set.extend(children_nodes)
        queue = children_nodes_set
        counter = counter + 1
    counter = counter + 1 + 1
    return counter, content_num, extra_num, lack_num


def calculate_e5_grc_top_to_bottom_round_cover_fill(test_sample, num):
    counter = 0
    queue = [test_sample]
    content_num = 0
    extra_num = 0
    # 你需要什么 旅行
    # counter = counter + 1
    lack_num = 0
    while len(queue) > 0:
        children_nodes_set = []
        for j in queue:
            content = j['goal']['content']
            if content in content_epoch_2:
                content_num = content_num + 1
                if content == '出租':
                    counter = counter + 1
                elif content == '景点':
                    counter = counter + 1
                    restrict = j['goal']['restricts']
                    if len(restrict) != 3:
                        counter = counter + 3 - len(restrict)
                    else:
                        counter = counter + 3
                elif content == '酒店':
                    counter = counter + 1
                    restrict = j['goal']['restricts']
                    if len(restrict) != 3:
                        counter = counter + 3 - len(restrict)
                    else:
                        counter = counter + 3
                    ch = j['children']
                    p = judge_content_extra_kg()
                    if (len(ch) > 0) and (p == 1):
                        counter = counter + 2
                    if (len(ch) > 0) and (p == 2):
                        counter = counter + 3
                elif content == '餐馆':
                    counter = counter + 1
                    restrict = j['goal']['restricts']
                    if len(restrict) != 3:
                        counter = counter + 3 - len(restrict)
                    else:
                        counter = counter + 3
                    ch = j['children']
                    p = judge_content_extra_kg()
                    if (len(ch) > 0) and (p == 1):
                        counter = counter + 2
                    if (len(ch) > 0) and (p == 2):
                        counter = counter + 3
                elif content == '地铁':
                    counter = counter + 1
                children_nodes = j['children']
                children_nodes_set.extend(children_nodes)
            else:
                counter = counter + 1
                if (judge_content_from_rpdb(content, num) != 1) and (judge_content(content) != 1):
                    lack_num = lack_num + 1
                    # 你需要什么 旅行 -匹配不到 你还需要什么
                    counter = counter + 1
                    restrict = j['goal']['restricts']
                    # 额外的 "没有了"
                    counter = counter + len(restrict) + 1
                    children_nodes = j['children']
                    children_nodes_set.extend(children_nodes)
                    # another child content? --no
                    counter = counter + 1
                # 模式库匹配不到 但是能在知识图谱中找到
                elif (judge_content_from_rpdb(content, num) != 1) and (judge_content(content) == 1):
                    content_num = content_num + 1
                    restrict = j['goal']['restricts']
                    # 额外的约束 "没有了"
                    counter = counter + len(restrict)
                    children_nodes = j['children']
                    children_nodes_set.extend(children_nodes)
                else:
                    content_num = content_num + 1
                    restrict = j['goal']['restricts']
                    # 在模式中能匹配到的内容 作为一个整体返回给用户--- 符合我的要求/xx需要改动
                    if content != '旅行':
                        counter = counter + 1 + len(restrict)
                    children_nodes = j['children']
                    children_nodes_set.extend(children_nodes)
        queue = children_nodes_set
        counter = counter + 1
    counter = counter + 1 + 1
    return counter, content_num, extra_num, lack_num


def calculate_e2_rpdb_fill_v2(test_sample, num, no):
    counter = 0
    queue = [test_sample]
    r_set, c_set = choose_rp_from_db(num, no)
    content_num = 0
    extra_num = 0
    lack_num = 0
    cal_c_set = []
    # 你需要什么 旅行
    counter = counter + 1
    while len(queue) > 0:
        children_nodes_set = []
        for j in queue:

            content = j['goal']['content']

            if judge_content_from_rpdb(content, num) != 1:
                lack_num = lack_num + 1
                # 你需要什么 旅行 -匹配不到 你还需要什么
                counter = counter + 1
                # 约束记录
                restrict = j['goal']['restricts']
                counter = counter + len(restrict)
                # 额外的约束 "没有了"
                counter = counter + 1
                children_nodes = j['children']
                children_nodes_set.extend(children_nodes)
                # another child content? --no
                counter = counter + 1
            else:
                if content not in cal_c_set:
                    cal_c_set.append(content)
                content_num = content_num + 1
                # 这里会出现第一次未识别到找到最浅的content节点
                if content not in r_set:
                    restrict_rp = []
                else:
                    restrict_rp = r_set[content]
                restrict = j['goal']['restricts']
                # r_key replace 测试需求树中的约束 rp_key 需求模式约束集合
                r_key = []
                for key in restrict:
                    if key['key'] not in r_key:
                        r_key.append(key['key'])
                rp_key = []
                for key in restrict_rp:
                    if key['key'] not in rp_key:
                        rp_key.append(key['key'])
                if len(restrict) == 0:
                    # 没什么约束。什么都行
                    counter = counter + 1
                else:
                    for d in rp_key:
                        if d not in r_key:
                            counter = counter + 1
                    # 对于现有的约束XXX你觉得如何
                    # XXX要XX的
                    # len_restricts_round = restricts_round(content, restrict, num)
                    # if len_restricts_round == 0:
                    #     # 没问题，我可以接受
                    #     counter = counter + 1
                    # else:
                    #     counter = counter + len_restricts_round

                # 额外的约束 "没有了"
                counter = counter + 1
                children_nodes = j['children']
                # if content != "旅行" and (judge_content_extra_kg() == 1):
                #     extra_num = extra_num + 1
                #     counter = counter + 1
                #     # children_nodes.append(extra_child_node)
                #     counter = counter + 1
                #     content_num = content_num + 1
                children_nodes_set.extend(children_nodes)
                # another child content? --no
                counter = counter + 1

        queue = children_nodes_set
    counter = counter + 1
    for i in cal_c_set:
        if i not in c_set:
            counter = counter + 1
    ro = []
    for m, h in c_set.items():
        if m not in cal_c_set:
            ro.extend(c_set[m][0])
            ro.append(m)
    counter = counter + len(c_set) - len(ro)
    return counter, content_num, extra_num, lack_num


def calculate_e3_rpdb_kg_fill(test_sample, num, no, mode):
    counter = 0
    queue = [test_sample]
    r_set, c_set = choose_rp_from_db(num, no, mode)
    content_num = 0
    extra_num = 0
    content_test_sample_set = []
    lack_num = 0
    while len(queue) > 0:
        children_nodes_set = []
        for j in queue:
            # 你需要什么 旅行
            counter = counter + 1
            content = j['goal']['content']
            if content not in content_test_sample_set:
                content_test_sample_set.append(content)
            if (judge_content_from_rpdb(content, num) != 1) and (judge_content(content) != 1):
                lack_num = lack_num + 1
                # 你需要什么 旅行 -匹配不到 你还需要什么
                counter = counter + 1
                restrict = j['goal']['restricts']
                # 额外的 "没有了"
                counter = counter + len(restrict) + 1
                children_nodes = j['children']
                children_nodes_set.extend(children_nodes)
                # another child content? --no
                counter = counter + 1
            # 模式库匹配不到 但是能在知识图谱中找到
            elif (judge_content_from_rpdb(content, num) != 1) and (judge_content(content) == 1):
                content_num = content_num + 1
                restrict = j['goal']['restricts']
                # 额外的约束 "没有了"
                counter = counter + len(restrict) + 1
                children_nodes = j['children']
                children_nodes_set.extend(children_nodes)
                # another child content? --no
                counter = counter + 1
            else:
                content_num = content_num + 1
                restrict = j['goal']['restricts']
                # 在模式中能匹配到的内容 作为一个整体返回给用户--- 符合我的要求/xx需要改动
                counter = counter + 1
                # if len(restrict) == 0:
                #     # 没什么约束。什么都行
                #     counter = counter + 1
                # else:
                #     # 对于现有的约束XXX你觉得如何
                #     # XXX要XX的
                #     len_restricts_round = restricts_round(content, restrict, num)
                #     if len_restricts_round == 0:
                #         # 没问题，我可以接受
                #         counter = counter + 1
                #     else:
                #         counter = counter + len_restricts_round
                # 额外的约束 "没有了"
                counter = counter + 1
                children_nodes = j['children']
                children_nodes_set.extend(children_nodes)
                # another child content? --no
                counter = counter + 1

        queue = children_nodes_set
    counter = counter + 1
    child_no_need = []
    for key, value in c_set.items():
        if (key not in content_test_sample_set) and (key not in child_no_need):
            child_no_need.extend(c_set[key][0])
            counter = counter + 1
    return counter, content_num, extra_num, lack_num


def calculate_e2_rpdb_round_cover_fill(test_sample, num, no, mode):
    counter = 0
    queue = [test_sample]
    r_set, c_set = choose_rp_from_db(num, no, mode)
    content_num = 0
    extra_num = 0
    content_test_sample_set = []
    lack_num = 0
    while len(queue) > 0:
        children_nodes_set = []
        for j in queue:
            # 你需要什么 旅行
            counter = counter + 1
            content = j['goal']['content']
            if content not in content_test_sample_set:
                content_test_sample_set.append(content)
            if judge_content_from_rpdb(content, num) != 1:
                lack_num = lack_num + 1
                # 你需要什么 旅行 -匹配不到 你还需要什么
                counter = counter + 1
                restrict = j['goal']['restricts']
                # 额外的 "没有了"
                counter = counter + len(restrict) + 1
                children_nodes = j['children']
                children_nodes_set.extend(children_nodes)
                # another child content? --no
                counter = counter + 1
            else:
                content_num = content_num + 1
                restrict = j['goal']['restricts']
                # 在模式中能匹配到的内容 作为一个整体返回给用户--- 符合我的要求/xx需要改动
                counter = counter + 1
                # if len(restrict) == 0:
                #     # 没什么约束。什么都行
                #     counter = counter + 1
                # else:
                #     # 对于现有的约束XXX你觉得如何
                #     # XXX要XX的
                #     len_restricts_round = restricts_round(content, restrict, num)
                #     if len_restricts_round == 0:
                #         # 没问题，我可以接受
                #         counter = counter + 1
                #     else:
                #         counter = counter + len_restricts_round
                # 额外的约束 "没有了"
                counter = counter + 1
                children_nodes = j['children']
                # if content != "旅行" and (judge_content_extra_kg() == 1):
                #     extra_num = extra_num + 1
                #     counter = counter + 1
                #     # children_nodes.append(extra_child_node)
                #     counter = counter + 1
                #     content_num = content_num + 1
                children_nodes_set.extend(children_nodes)
                # another child content? --no
                counter = counter + 1

        queue = children_nodes_set
    counter = counter + 1
    child_no_need = []
    for key, value in c_set.items():
        if (key not in content_test_sample_set) and (key not in child_no_need):
            child_no_need.extend(c_set[key][0])
            counter = counter + 1
    return counter, content_num, extra_num, lack_num


with open("./data/test_rptree_499.json", 'r', encoding='utf-8') as fr:
    # type = list, len = 200
    test_499 = json.load(fr)

with open("./data/train_rptree_1000.json", 'r', encoding='utf-8') as fq:
    train_1000 = json.load(fq)

with open("./data/test_rptree_5008.json", 'r', encoding='utf-8') as fq:
    test_5008 = json.load(fq)


c_2_set = get_content_from_rps("../rps0602/rps/rps_supp_2.json")
c_3_set = get_content_from_rps("../rps0602/rps/rps_supp_3.json")
# content_write(c_3_set, 3)
c_4_set = get_content_from_rps("../rps0602/rps/rps_supp_4.json")
# content_write(c_4_set, 4)
c_5_set = get_content_from_rps("../rps0602/rps/rps_supp_5.json")
# content_write(c_5_set, 5)
c_6_set = get_content_from_rps("../rps0602/rps/rps_supp_6.json")
# content_write(c_6_set, 6)


# r_2_set = get_restricts_from_rps("../rps0602/rps/rps_supp_2.json")
# restricts_write(r_2_set, 2)
# r_3_set = get_restricts_from_rps("../rps0602/rps/rps_supp_3.json")
# restricts_write(r_3_set, 3)
# r_4_set = get_restricts_from_rps("../rps0602/rps/rps_supp_4.json")
# restricts_write(r_4_set, 4)
# r_5_set = get_restricts_from_rps("../rps0602/rps/rps_supp_5.json")
# restricts_write(r_5_set, 5)
# r_6_set = get_restricts_from_rps("../rps0602/rps/rps_supp_6.json")
# restricts_write(r_6_set, 6)
c_g_set = get_content_from_kg("./data/train_rptree_1000.json")
# content_write(c_g_set, "g")
# c_g_set_499 = get_content_from_kg("./data/test_rptree_499.json")
# content_write(c_g_set_499, "g_499")
c_g_set_5008 = get_content_from_kg("./data/test_rptree_5008.json")
# content_write(c_g_set_5008, "g_5008")


def e0_write():
    content_num_record = []
    with open("e0_without_rp_res_5508.txt", 'w', encoding='utf-8') as f1:
        num = 0
        str_tab_1 = "No"
        str_tab_2 = "Content_num"
        str_tab_3 = "Round"
        str_tab_4 = "cover"
        f1.write('{:^10}{:^10}{:^10}{:^10}'.format(str_tab_1, str_tab_2, str_tab_3, str_tab_4))
        f1.write("\n")
        for i in test_499:
            num = num + 1
            res, content_num = calculate_e0_round(i)
            f1.write('{:^10}{:^10}{:^10}{:^10}'.format(str(num), str(content_num), str(res), "1.0"))
            f1.write("\n")
            content_num_record.append(content_num)
        for i in test_5008:
            num = num + 1
            res, content_num = calculate_e0_round(i)
            f1.write('{:^10}{:^10}{:^10}{:^10}'.format(str(num), str(content_num), str(res), "1.0"))
            f1.write("\n")
            content_num_record.append(content_num)
    with open("e0_content_num_record.txt", 'w', encoding='utf-8') as f1:
        f1.write(str(content_num_record))


def e1_write():
    with open("e0_content_num_record.txt", 'r', encoding='utf-8') as ff:
        record = eval(ff.read())
    # print(type(record))
    with open("./test_res/e1_with_kg_res_5508.txt", 'w', encoding='utf-8') as f1:
        num = 0
        # str_tab = "NO. \tRound \tOrigin_Content_Amount \tLack_Content_Amount \tExtra_Content_Amount \tFinal_Cover\n"
        # f1.write(str_tab)
        f1.write('{:^10}{:^10}{:^15}{:^15}{:^15}{:^15}'.format("NO.", "Round", "Ori_Content", "Lack_Content", "Extra_Content", "Final_Cover"))
        f1.write("\n")
        for i in test_499:
            num = num + 1
            round, c_num, e_num, l_num = calculate_e1_kg_round_cover(i)
            str_round_e1 = str(num) + " \t" + str(round) + " \t"
            str_c_res_e1 = str(c_num - e_num) + " \t" + str(l_num) + " \t" + str(e_num) + " \t"
            final_cover = str((c_num - l_num)/c_num-e_num) + "\n"
            str_e1 = str_round_e1 + str_c_res_e1 + final_cover
            # f1.write(str_e1)
            f1.write('{:^10}{:^10}{:^15}{:^15}{:^15}{:^15}'.format(str(num), str(round), str(record[num-1]),
                                                                   str(int(record[num-1]) - c_num + e_num), str(e_num),
                                                                   str(c_num/int(record[num-1]))))
            f1.write("\n")
        for i in test_5008:
            num = num + 1
            round, c_num, e_num, l_num = calculate_e1_kg_round_cover(i)
            str_round_e1 = str(num) + " \t" + str(round) + " \t"
            str_c_res_e1 = str(c_num) + " \t" + str(l_num) + " \t" + str(e_num) + " \t"
            final_cover = str((c_num + e_num - l_num)/c_num) + "\n"
            str_e1 = str_round_e1 + str_c_res_e1 + final_cover
            f1.write('{:^10}{:^10}{:^15}{:^15}{:^15}{:^15}'.format(str(num), str(round), str(record[num - 1]),
                                                                   str(int(record[num-1]) - c_num + e_num), str(e_num),
                                                                   str(c_num / int(record[num-1]))))
            f1.write("\n")


# mode 1-ran 2-mod
def e2_rpdb_write(k, mode):
    with open("e0_content_num_record.txt", 'r', encoding='utf-8') as ff:
        record = eval(ff.read())
    # print(type(record))
    if mode == 2:
        file_name = "./test_res/e2_with_rpdb_" + str(k) + "_mod_5508.txt"
    if mode == 1:
        file_name = "./test_res/e2_with_rpdb_" + str(k) + "_ran_5508.txt"
    with open(file_name, 'w', encoding='utf-8') as f1:
        num = 0
        # str_tab = "NO. \tRound \tOrigin_Content_Amount \tLack_Content_Amount \tExtra_Content_Amount \tFinal_Cover\n"
        # f1.write(str_tab)
        f1.write('{:^10}{:^10}{:^15}{:^15}{:^15}{:^15}'.format("NO.", "Round", "Ori_Content", "Lack_Content", "Extra_Content", "Final_Cover"))
        f1.write("\n")
        for i in test_499:
            num = num + 1
            round, c_num, e_num, l_num = calculate_e2_rpdb_round_cover(i, k, num, mode)
            str_round_e1 = str(num) + " \t" + str(round) + " \t"
            str_c_res_e1 = str(c_num - e_num) + " \t" + str(l_num) + " \t" + str(e_num) + " \t"
            final_cover = str((c_num - l_num)/c_num-e_num) + "\n"
            str_e1 = str_round_e1 + str_c_res_e1 + final_cover
            # f1.write(str_e1)
            f1.write('{:^10}{:^10}{:^15}{:^15}{:^15}{:^15}'.format(str(num), str(round), str(record[num-1]),
                                                                   str(int(record[num-1]) - c_num + e_num), str(e_num),
                                                                   str(c_num/int(record[num-1]))))
            f1.write("\n")
        for i in test_5008:
            num = num + 1
            round, c_num, e_num, l_num = calculate_e2_rpdb_round_cover(i, k, num, mode)
            str_round_e1 = str(num) + " \t" + str(round) + " \t"
            str_c_res_e1 = str(c_num) + " \t" + str(l_num) + " \t" + str(e_num) + " \t"
            final_cover = str((c_num + e_num - l_num)/c_num) + "\n"
            str_e1 = str_round_e1 + str_c_res_e1 + final_cover
            f1.write('{:^10}{:^10}{:^15}{:^15}{:^15}{:^15}'.format(str(num), str(round), str(record[num - 1]),
                                                                   str(int(record[num-1]) - c_num + e_num), str(e_num),
                                                                   str(c_num / int(record[num-1]))))
            f1.write("\n")


def e2_rpdb_write_v2(k):
    with open("e0_content_num_record.txt", 'r', encoding='utf-8') as ff:
        record = eval(ff.read())
    # print(type(record))
    file_name = "e2_ran_rpdb_" + str(k) + "_res_5508_v2.txt"
    with open(file_name, 'w', encoding='utf-8') as f1:
        num = 0
        # str_tab = "NO. \tRound \tOrigin_Content_Amount \tLack_Content_Amount \tExtra_Content_Amount \tFinal_Cover\n"
        # f1.write(str_tab)
        f1.write('{:^10}{:^10}{:^15}{:^15}{:^15}{:^15}'.format("NO.", "Round", "Ori_Content", "Lack_Content", "Extra_Content", "Final_Cover"))
        f1.write("\n")
        for i in test_499:
            num = num + 1
            round, c_num, e_num, l_num = calculate_e2_rpdb_round_cover_v2(i, k, num)
            str_round_e1 = str(num) + " \t" + str(round) + " \t"
            str_c_res_e1 = str(c_num - e_num) + " \t" + str(l_num) + " \t" + str(e_num) + " \t"
            final_cover = str((c_num - l_num)/c_num-e_num) + "\n"
            str_e1 = str_round_e1 + str_c_res_e1 + final_cover
            # f1.write(str_e1)
            f1.write('{:^10}{:^10}{:^15}{:^15}{:^15}{:^15}'.format(str(num), str(round), str(record[num-1]),
                                                                   str(int(record[num-1]) - c_num + e_num), str(e_num),
                                                                   str(c_num/int(record[num-1]))))
            f1.write("\n")
        for i in test_5008:
            num = num + 1
            round, c_num, e_num, l_num = calculate_e2_rpdb_round_cover_v2(i, k, num)
            str_round_e1 = str(num) + " \t" + str(round) + " \t"
            str_c_res_e1 = str(c_num) + " \t" + str(l_num) + " \t" + str(e_num) + " \t"
            final_cover = str((c_num + e_num - l_num)/c_num) + "\n"
            str_e1 = str_round_e1 + str_c_res_e1 + final_cover
            f1.write('{:^10}{:^10}{:^15}{:^15}{:^15}{:^15}'.format(str(num), str(round), str(record[num - 1]),
                                                                   str(int(record[num-1]) - c_num + e_num), str(e_num),
                                                                   str(c_num / int(record[num-1]))))
            f1.write("\n")


def e3_rpdb_kg_write(k, mode):
    with open("e0_content_num_record.txt", 'r', encoding='utf-8') as ff:
        record = eval(ff.read())
    # print(type(record))
    if mode == 1:
        file_name = "./test_res/e3_rpdb_kg_" + str(k) + "_ran_5508.txt"
    if mode == 2:
        file_name = "./test_res/e3_rpdb_kg_" + str(k) + "_mod_5508.txt"
    with open(file_name, 'w', encoding='utf-8') as f1:
        num = 0
        # str_tab = "NO. \tRound \tOrigin_Content_Amount \tLack_Content_Amount \tExtra_Content_Amount \tFinal_Cover\n"
        # f1.write(str_tab)
        f1.write('{:^10}{:^10}{:^15}{:^15}{:^15}{:^15}'.format("NO.", "Round", "Ori_Content", "Lack_Content", "Extra_Content", "Final_Cover"))
        f1.write("\n")
        for i in test_499:
            num = num + 1
            round, c_num, e_num, l_num = calculate_e3_rpdb_round_cover(i, k, num, mode)
            str_round_e1 = str(num) + " \t" + str(round) + " \t"
            str_c_res_e1 = str(c_num - e_num) + " \t" + str(l_num) + " \t" + str(e_num) + " \t"
            final_cover = str((c_num - l_num)/c_num-e_num) + "\n"
            str_e1 = str_round_e1 + str_c_res_e1 + final_cover
            # f1.write(str_e1)
            f1.write('{:^10}{:^10}{:^15}{:^15}{:^15}{:^15}'.format(str(num), str(round), str(record[num-1]),
                                                                   str(int(record[num-1]) - c_num + e_num), str(e_num),
                                                                   str(c_num/int(record[num-1]))))
            f1.write("\n")
        for i in test_5008:
            num = num + 1
            round, c_num, e_num, l_num = calculate_e3_rpdb_round_cover(i, k, num, mode)
            str_round_e1 = str(num) + " \t" + str(round) + " \t"
            str_c_res_e1 = str(c_num) + " \t" + str(l_num) + " \t" + str(e_num) + " \t"
            final_cover = str((c_num + e_num - l_num)/c_num) + "\n"
            str_e1 = str_round_e1 + str_c_res_e1 + final_cover
            f1.write('{:^10}{:^10}{:^15}{:^15}{:^15}{:^15}'.format(str(num), str(round), str(record[num - 1]),
                                                                   str(int(record[num-1]) - c_num + e_num), str(e_num),
                                                                   str(c_num / int(record[num-1]))))
            f1.write("\n")


def e4_grc_write(k):
    with open("e0_content_num_record.txt", 'r', encoding='utf-8') as ff:
        record = eval(ff.read())
    # print(type(record))
    file_name = "./test_res/e4_grc_bottom_to_top_" + str(k) + "_5508.txt"
    with open(file_name, 'w', encoding='utf-8') as f1:
        num = 0
        # str_tab = "NO. \tRound \tOrigin_Content_Amount \tLack_Content_Amount \tExtra_Content_Amount \tFinal_Cover\n"
        # f1.write(str_tab)
        f1.write('{:^10}{:^10}{:^15}{:^15}{:^15}{:^15}'.format("NO.", "Round", "Ori_Content", "Lack_Content", "Extra_Content", "Final_Cover"))
        f1.write("\n")
        for i in test_499:
            num = num + 1
            round, c_num, e_num, l_num = calculate_e4_grc_bottom_to_top_round_cover(i, k)
            str_round_e1 = str(num) + " \t" + str(round) + " \t"
            str_c_res_e1 = str(c_num - e_num) + " \t" + str(l_num) + " \t" + str(e_num) + " \t"
            final_cover = str((c_num - l_num)/c_num-e_num) + "\n"
            str_e1 = str_round_e1 + str_c_res_e1 + final_cover
            # f1.write(str_e1)
            f1.write('{:^10}{:^10}{:^15}{:^15}{:^15}{:^15}'.format(str(num), str(round), str(record[num-1]),
                                                                   str(int(record[num-1]) - c_num + e_num), str(e_num),
                                                                   str(c_num/int(record[num-1]))))
            f1.write("\n")
        for i in test_5008:
            num = num + 1
            round, c_num, e_num, l_num = calculate_e4_grc_bottom_to_top_round_cover(i, k)
            str_round_e1 = str(num) + " \t" + str(round) + " \t"
            str_c_res_e1 = str(c_num) + " \t" + str(l_num) + " \t" + str(e_num) + " \t"
            final_cover = str((c_num + e_num - l_num)/c_num) + "\n"
            str_e1 = str_round_e1 + str_c_res_e1 + final_cover
            f1.write('{:^10}{:^10}{:^15}{:^15}{:^15}{:^15}'.format(str(num), str(round), str(record[num - 1]),
                                                                   str(int(record[num-1]) - c_num + e_num), str(e_num),
                                                                   str(c_num / int(record[num-1]))))
            f1.write("\n")


def e5_grc_top_to_bottom_write(k):
    with open("e0_content_num_record.txt", 'r', encoding='utf-8') as ff:
        record = eval(ff.read())
    # print(type(record))
    file_name = "./test_res/e5_grc_top_to_bottom_" + str(k) + "_5508.txt"
    with open(file_name, 'w', encoding='utf-8') as f1:
        num = 0
        # str_tab = "NO. \tRound \tOrigin_Content_Amount \tLack_Content_Amount \tExtra_Content_Amount \tFinal_Cover\n"
        # f1.write(str_tab)
        f1.write('{:^10}{:^10}{:^15}{:^15}{:^15}{:^15}'.format("NO.", "Round", "Ori_Content", "Lack_Content", "Extra_Content", "Final_Cover"))
        f1.write("\n")
        for i in test_499:
            num = num + 1
            round, c_num, e_num, l_num = calculate_e5_grc_top_to_bottom_round_cover(i, k)
            str_round_e1 = str(num) + " \t" + str(round) + " \t"
            str_c_res_e1 = str(c_num - e_num) + " \t" + str(l_num) + " \t" + str(e_num) + " \t"
            final_cover = str((c_num - l_num)/c_num-e_num) + "\n"
            str_e1 = str_round_e1 + str_c_res_e1 + final_cover
            # f1.write(str_e1)
            f1.write('{:^10}{:^10}{:^15}{:^15}{:^15}{:^15}'.format(str(num), str(round), str(record[num-1]),
                                                                   str(int(record[num-1]) - c_num + e_num), str(e_num),
                                                                   str(c_num/int(record[num-1]))))
            f1.write("\n")
        for i in test_5008:
            num = num + 1
            round, c_num, e_num, l_num = calculate_e5_grc_top_to_bottom_round_cover(i, k)
            str_round_e1 = str(num) + " \t" + str(round) + " \t"
            str_c_res_e1 = str(c_num) + " \t" + str(l_num) + " \t" + str(e_num) + " \t"
            final_cover = str((c_num + e_num - l_num)/c_num) + "\n"
            str_e1 = str_round_e1 + str_c_res_e1 + final_cover
            f1.write('{:^10}{:^10}{:^15}{:^15}{:^15}{:^15}'.format(str(num), str(round), str(record[num - 1]),
                                                                   str(int(record[num-1]) - c_num + e_num), str(e_num),
                                                                   str(c_num / int(record[num-1]))))
            f1.write("\n")


def e5_grc_top_to_bottom_write_fill(k):
    with open("e0_content_num_record.txt", 'r', encoding='utf-8') as ff:
        record = eval(ff.read())
    # print(type(record))
    file_name = "./test_res/e5_grc_top_to_bottom_fill" + str(k) + "_5508.txt"
    with open(file_name, 'w', encoding='utf-8') as f1:
        num = 0
        # str_tab = "NO. \tRound \tOrigin_Content_Amount \tLack_Content_Amount \tExtra_Content_Amount \tFinal_Cover\n"
        # f1.write(str_tab)
        f1.write('{:^10}{:^10}{:^15}{:^15}{:^15}{:^15}'.format("NO.", "Round", "Ori_Content", "Lack_Content", "Extra_Content", "Final_Cover"))
        f1.write("\n")
        for i in test_499:
            num = num + 1
            round, c_num, e_num, l_num = calculate_e5_grc_top_to_bottom_round_cover_fill(i, k)
            str_round_e1 = str(num) + " \t" + str(round) + " \t"
            str_c_res_e1 = str(c_num - e_num) + " \t" + str(l_num) + " \t" + str(e_num) + " \t"
            final_cover = str((c_num - l_num)/c_num-e_num) + "\n"
            str_e1 = str_round_e1 + str_c_res_e1 + final_cover
            # f1.write(str_e1)
            f1.write('{:^10}{:^10}{:^15}{:^15}{:^15}{:^15}'.format(str(num), str(round), str(record[num-1]),
                                                                   str(int(record[num-1]) - c_num + e_num), str(e_num),
                                                                   str(c_num/int(record[num-1]))))
            f1.write("\n")
        for i in test_5008:
            num = num + 1
            round, c_num, e_num, l_num = calculate_e5_grc_top_to_bottom_round_cover_fill(i, k)
            str_round_e1 = str(num) + " \t" + str(round) + " \t"
            str_c_res_e1 = str(c_num) + " \t" + str(l_num) + " \t" + str(e_num) + " \t"
            final_cover = str((c_num + e_num - l_num)/c_num) + "\n"
            str_e1 = str_round_e1 + str_c_res_e1 + final_cover
            f1.write('{:^10}{:^10}{:^15}{:^15}{:^15}{:^15}'.format(str(num), str(round), str(record[num - 1]),
                                                                   str(int(record[num-1]) - c_num + e_num), str(e_num),
                                                                   str(c_num / int(record[num-1]))))
            f1.write("\n")


def e4_grc_fill_write(k):
    with open("e0_content_num_record.txt", 'r', encoding='utf-8') as ff:
        record = eval(ff.read())
    # print(type(record))
    file_name = "./test_res/e4_grc_fill_bottom_to_top_" + str(k) + "_5508.txt"
    with open(file_name, 'w', encoding='utf-8') as f1:
        num = 0
        # str_tab = "NO. \tRound \tOrigin_Content_Amount \tLack_Content_Amount \tExtra_Content_Amount \tFinal_Cover\n"
        # f1.write(str_tab)
        f1.write('{:^10}{:^10}{:^15}{:^15}{:^15}{:^15}'.format("NO.", "Round", "Ori_Content", "Lack_Content", "Extra_Content", "Final_Cover"))
        f1.write("\n")
        for i in test_499:
            num = num + 1
            round, c_num, e_num, l_num = calculate_e4_grc_fill_round_cover(i, k)
            str_round_e1 = str(num) + " \t" + str(round) + " \t"
            str_c_res_e1 = str(c_num - e_num) + " \t" + str(l_num) + " \t" + str(e_num) + " \t"
            final_cover = str((c_num - l_num)/c_num-e_num) + "\n"
            str_e1 = str_round_e1 + str_c_res_e1 + final_cover
            # f1.write(str_e1)
            f1.write('{:^10}{:^10}{:^15}{:^15}{:^15}{:^15}'.format(str(num), str(round), str(record[num-1]),
                                                                   str(int(record[num-1]) - c_num + e_num), str(e_num),
                                                                   str(c_num/int(record[num-1]))))
            f1.write("\n")
        for i in test_5008:
            num = num + 1
            round, c_num, e_num, l_num = calculate_e4_grc_fill_round_cover(i, k)
            str_round_e1 = str(num) + " \t" + str(round) + " \t"
            str_c_res_e1 = str(c_num) + " \t" + str(l_num) + " \t" + str(e_num) + " \t"
            final_cover = str((c_num + e_num - l_num)/c_num) + "\n"
            str_e1 = str_round_e1 + str_c_res_e1 + final_cover
            f1.write('{:^10}{:^10}{:^15}{:^15}{:^15}{:^15}'.format(str(num), str(round), str(record[num - 1]),
                                                                   str(int(record[num-1]) - c_num + e_num), str(e_num),
                                                                   str(c_num / int(record[num-1]))))
            f1.write("\n")


def e2_rpdb_fill_write(k, mode):
    with open("e0_content_num_record.txt", 'r', encoding='utf-8') as ff:
        record = eval(ff.read())
    # print(type(record))
    if mode == 2:
        file_name = "./test_res/e2_rpdb_fill_" + str(k) + "_mod_5508.txt"
    if mode == 1:
        file_name = "./test_res/e2_rpdb_fill_" + str(k) + "_ran_5508.txt"
    with open(file_name, 'w', encoding='utf-8') as f1:
        num = 0
        # str_tab = "NO. \tRound \tOrigin_Content_Amount \tLack_Content_Amount \tExtra_Content_Amount \tFinal_Cover\n"
        # f1.write(str_tab)
        f1.write('{:^10}{:^10}{:^15}{:^15}{:^15}{:^15}'.format("NO.", "Round", "Ori_Content", "Lack_Content", "Extra_Content", "Final_Cover"))
        f1.write("\n")
        for i in test_499:
            num = num + 1
            round, c_num, e_num, l_num = calculate_e2_rpdb_round_cover_fill(i, k, num, mode)
            str_round_e1 = str(num) + " \t" + str(round) + " \t"
            str_c_res_e1 = str(c_num - e_num) + " \t" + str(l_num) + " \t" + str(e_num) + " \t"
            final_cover = str((c_num - l_num)/c_num-e_num) + "\n"
            str_e1 = str_round_e1 + str_c_res_e1 + final_cover
            # f1.write(str_e1)
            f1.write('{:^10}{:^10}{:^15}{:^15}{:^15}{:^15}'.format(str(num), str(round), str(record[num-1]),
                                                                   str(int(record[num-1]) - c_num + e_num), str(e_num),
                                                                   str("1.0")))
            f1.write("\n")
        for i in test_5008:
            num = num + 1
            round, c_num, e_num, l_num = calculate_e2_rpdb_round_cover_fill(i, k, num, mode)
            str_round_e1 = str(num) + " \t" + str(round) + " \t"
            str_c_res_e1 = str(c_num) + " \t" + str(l_num) + " \t" + str(e_num) + " \t"
            final_cover = str((c_num + e_num - l_num)/c_num) + "\n"
            str_e1 = str_round_e1 + str_c_res_e1 + final_cover
            f1.write('{:^10}{:^10}{:^15}{:^15}{:^15}{:^15}'.format(str(num), str(round), str(record[num - 1]),
                                                                   str(int(record[num - 1]) - c_num + e_num),
                                                                   str(e_num),
                                                                   str("1.0")))
            f1.write("\n")


def e2_rpdb_fill_write_v2(k):
    with open("e0_content_num_record.txt", 'r', encoding='utf-8') as ff:
        record = eval(ff.read())
    # print(type(record))
    file_name = "e2_rpdb_fill_" + str(k) + "_5508_v2.txt"
    with open(file_name, 'w', encoding='utf-8') as f1:
        num = 0
        # str_tab = "NO. \tRound \tOrigin_Content_Amount \tLack_Content_Amount \tExtra_Content_Amount \tFinal_Cover\n"
        # f1.write(str_tab)
        f1.write('{:^10}{:^10}{:^15}{:^15}{:^15}{:^15}'.format("NO.", "Round", "Ori_Content", "Lack_Content", "Extra_Content", "Final_Cover"))
        f1.write("\n")
        for i in test_499:
            num = num + 1
            round, c_num, e_num, l_num = calculate_e2_rpdb_fill_v2(i, k, num)
            str_round_e1 = str(num) + " \t" + str(round) + " \t"
            str_c_res_e1 = str(c_num - e_num) + " \t" + str(l_num) + " \t" + str(e_num) + " \t"
            final_cover = str((c_num - l_num)/c_num-e_num) + "\n"
            str_e1 = str_round_e1 + str_c_res_e1 + final_cover
            # f1.write(str_e1)
            f1.write('{:^10}{:^10}{:^15}{:^15}{:^15}{:^15}'.format(str(num), str(round), str(record[num-1]),
                                                                   str(int(record[num-1]) - c_num + e_num), str(e_num),
                                                                   str("1.0")))
            f1.write("\n")
        for i in test_5008:
            num = num + 1
            round, c_num, e_num, l_num = calculate_e2_rpdb_fill_v2(i, k, num)
            str_round_e1 = str(num) + " \t" + str(round) + " \t"
            str_c_res_e1 = str(c_num) + " \t" + str(l_num) + " \t" + str(e_num) + " \t"
            final_cover = str((c_num + e_num - l_num)/c_num) + "\n"
            str_e1 = str_round_e1 + str_c_res_e1 + final_cover
            f1.write('{:^10}{:^10}{:^15}{:^15}{:^15}{:^15}'.format(str(num), str(round), str(record[num - 1]),
                                                                   str(int(record[num - 1]) - c_num + e_num),
                                                                   str(e_num),
                                                                   str("1.0")))
            f1.write("\n")


def e3_rpdb_kg_fill_write(k, mode):
    with open("e0_content_num_record.txt", 'r', encoding='utf-8') as ff:
        record = eval(ff.read())
    # print(type(record))
    if mode == 1:
        file_name = "./test_res/e3_rpdb_kg_fill_" + str(k) + "_ran_5508.txt"
    if mode == 2:
        file_name = "./test_res/e3_rpdb_kg_fill_" + str(k) + "_mod_5508.txt"
    with open(file_name, 'w', encoding='utf-8') as f1:
        num = 0
        # str_tab = "NO. \tRound \tOrigin_Content_Amount \tLack_Content_Amount \tExtra_Content_Amount \tFinal_Cover\n"
        # f1.write(str_tab)
        f1.write('{:^10}{:^10}{:^15}{:^15}{:^15}{:^15}'.format("NO.", "Round", "Ori_Content", "Lack_Content", "Extra_Content", "Final_Cover"))
        f1.write("\n")
        for i in test_499:
            num = num + 1
            round, c_num, e_num, l_num = calculate_e3_rpdb_kg_fill(i, k, num, mode)
            str_round_e1 = str(num) + " \t" + str(round) + " \t"
            str_c_res_e1 = str(c_num - e_num) + " \t" + str(l_num) + " \t" + str(e_num) + " \t"
            final_cover = str((c_num - l_num)/c_num-e_num) + "\n"
            str_e1 = str_round_e1 + str_c_res_e1 + final_cover
            # f1.write(str_e1)
            f1.write('{:^10}{:^10}{:^15}{:^15}{:^15}{:^15}'.format(str(num), str(round), str(record[num-1]),
                                                                   str(int(record[num-1]) - c_num + e_num), str(e_num),
                                                                   str((int(record[num-1]) + e_num)/ int(record[num-1]))))
            f1.write("\n")
        for i in test_5008:
            num = num + 1
            round, c_num, e_num, l_num = calculate_e3_rpdb_kg_fill(i, k, num, mode)
            str_round_e1 = str(num) + " \t" + str(round) + " \t"
            str_c_res_e1 = str(c_num) + " \t" + str(l_num) + " \t" + str(e_num) + " \t"
            final_cover = str((c_num + e_num - l_num)/c_num) + "\n"
            str_e1 = str_round_e1 + str_c_res_e1 + final_cover
            f1.write('{:^10}{:^10}{:^15}{:^15}{:^15}{:^15}'.format(str(num), str(round), str(record[num - 1]),
                                                                   str(int(record[num - 1]) - c_num + e_num),
                                                                   str(e_num),
                                                                   str((int(record[num - 1]) + e_num) / int(
                                                                       record[num - 1]))))
            f1.write("\n")


# mode 1-e4cal  2-e4fill
def e4_grc_write_support(k, mode):
    with open("e0_content_num_record.txt", 'r', encoding='utf-8') as ff:
        record = eval(ff.read())
    # print(type(record))
    if mode == 1:
        file_name = "./test_res/e4_grc_bottom_to_top_" + str(k) + "_5508.txt"
    if mode == 2:
        file_name = "./test_res/e4_grc_fill_bottom_to_top_" + str(k) + "_5508.txt"
    with open(file_name, 'w', encoding='utf-8') as f1:
        num = 0
        # str_tab = "NO. \tRound \tOrigin_Content_Amount \tLack_Content_Amount \tExtra_Content_Amount \tFinal_Cover\n"
        # f1.write(str_tab)
        f1.write('{:^10}{:^10}{:^15}{:^15}{:^15}{:^15}'.format("NO.", "Round", "Ori_Content", "Lack_Content", "Extra_Content", "Final_Cover"))
        f1.write("\n")
        for i in test_499:
            num = num + 1
            if (k == 3) and (mode == 1):
                round, c_num, e_num, l_num = k3_calculate_e4_grc_bottom_to_top_round_cover(i, k)
            if (k == 3) and (mode == 2):
                round, c_num, e_num, l_num = k3_calculate_e4_grc_fill_round_cover(i, k)
            if (k == 4) and (mode == 1):
                round, c_num, e_num, l_num = k4_calculate_e4_grc_bottom_to_top_round_cover(i, k)
            if (k == 4) and (mode == 2):
                round, c_num, e_num, l_num = k4_calculate_e4_grc_fill_round_cover(i, k)
            if (k == 5) and (mode == 1):
                round, c_num, e_num, l_num = k5_calculate_e4_grc_bottom_to_top_round_cover(i, k)
            if (k == 5) and (mode == 2):
                round, c_num, e_num, l_num = k5_calculate_e4_grc_fill_round_cover(i, k)
            if (k == 6) and (mode == 1):
                round, c_num, e_num, l_num = k6_calculate_e4_grc_bottom_to_top_round_cover(i, k)
            if (k == 6) and (mode == 2):
                round, c_num, e_num, l_num = k6_calculate_e4_grc_fill_round_cover(i, k)
            str_round_e1 = str(num) + " \t" + str(round) + " \t"
            str_c_res_e1 = str(c_num - e_num) + " \t" + str(l_num) + " \t" + str(e_num) + " \t"
            final_cover = str((c_num - l_num)/c_num-e_num) + "\n"
            str_e1 = str_round_e1 + str_c_res_e1 + final_cover
            # f1.write(str_e1)
            f1.write('{:^10}{:^10}{:^15}{:^15}{:^15}{:^15}'.format(str(num), str(round), str(record[num-1]),
                                                                   str(int(record[num-1]) - c_num + e_num), str(e_num),
                                                                   str(c_num/int(record[num-1]))))
            f1.write("\n")
        for i in test_5008:
            num = num + 1
            if (k == 3) and (mode == 1):
                round, c_num, e_num, l_num = k3_calculate_e4_grc_bottom_to_top_round_cover(i, k)
            if (k == 3) and (mode == 2):
                round, c_num, e_num, l_num = k3_calculate_e4_grc_fill_round_cover(i, k)
            if (k == 4) and (mode == 1):
                round, c_num, e_num, l_num = k4_calculate_e4_grc_bottom_to_top_round_cover(i, k)
            if (k == 4) and (mode == 2):
                round, c_num, e_num, l_num = k4_calculate_e4_grc_fill_round_cover(i, k)
            if (k == 5) and (mode == 1):
                round, c_num, e_num, l_num = k5_calculate_e4_grc_bottom_to_top_round_cover(i, k)
            if (k == 5) and (mode == 2):
                round, c_num, e_num, l_num = k5_calculate_e4_grc_fill_round_cover(i, k)
            if (k == 6) and (mode == 1):
                round, c_num, e_num, l_num = k6_calculate_e4_grc_bottom_to_top_round_cover(i, k)
            if (k == 6) and (mode == 2):
                round, c_num, e_num, l_num = k6_calculate_e4_grc_fill_round_cover(i, k)
            str_round_e1 = str(num) + " \t" + str(round) + " \t"
            str_c_res_e1 = str(c_num) + " \t" + str(l_num) + " \t" + str(e_num) + " \t"
            final_cover = str((c_num + e_num - l_num)/c_num) + "\n"
            str_e1 = str_round_e1 + str_c_res_e1 + final_cover
            f1.write('{:^10}{:^10}{:^15}{:^15}{:^15}{:^15}'.format(str(num), str(round), str(record[num - 1]),
                                                                   str(int(record[num-1]) - c_num + e_num), str(e_num),
                                                                   str(c_num / int(record[num-1]))))
            f1.write("\n")


def e5_grc_top_to_bottom_support(k, mode):
    with open("e0_content_num_record.txt", 'r', encoding='utf-8') as ff:
        record = eval(ff.read())
    # print(type(record))
    if mode == 1:
        file_name = "./test_res/e5_grc_top_to_bottom_" + str(k) + "_5508.txt"
    if mode == 2:
        file_name = "./test_res/e5_grc_top_to_bottom_fill" + str(k) + "_5508.txt"
    with open(file_name, 'w', encoding='utf-8') as f1:
        num = 0
        # str_tab = "NO. \tRound \tOrigin_Content_Amount \tLack_Content_Amount \tExtra_Content_Amount \tFinal_Cover\n"
        # f1.write(str_tab)
        f1.write('{:^10}{:^10}{:^15}{:^15}{:^15}{:^15}'.format("NO.", "Round", "Ori_Content", "Lack_Content", "Extra_Content", "Final_Cover"))
        f1.write("\n")
        for i in test_499:
            num = num + 1
            if (k == 3) and (mode == 1):
                round, c_num, e_num, l_num = k3_calculate_e5_grc_top_to_bottom_round_cover(i, k)
            if (k == 3) and (mode == 2):
                round, c_num, e_num, l_num = k3_calculate_e5_grc_top_to_bottom_round_cover_fill(i, k)
            if (k == 4) and (mode == 1):
                round, c_num, e_num, l_num = k4_calculate_e5_grc_top_to_bottom_round_cover(i, k)
            if (k == 4) and (mode == 2):
                round, c_num, e_num, l_num = k4_calculate_e5_grc_top_to_bottom_round_cover_fill(i, k)
            if (k == 5) and (mode == 1):
                round, c_num, e_num, l_num = k5_calculate_e5_grc_top_to_bottom_round_cover(i, k)
            if (k == 5) and (mode == 2):
                round, c_num, e_num, l_num = k5_calculate_e5_grc_top_to_bottom_round_cover_fill(i, k)
            if (k == 6) and (mode == 1):
                round, c_num, e_num, l_num = k6_calculate_e5_grc_top_to_bottom_round_cover(i, k)
            if (k == 6) and (mode == 2):
                round, c_num, e_num, l_num = k6_calculate_e5_grc_top_to_bottom_round_cover_fill(i, k)
            str_round_e1 = str(num) + " \t" + str(round) + " \t"
            str_c_res_e1 = str(c_num - e_num) + " \t" + str(l_num) + " \t" + str(e_num) + " \t"
            final_cover = str((c_num - l_num)/c_num-e_num) + "\n"
            str_e1 = str_round_e1 + str_c_res_e1 + final_cover
            # f1.write(str_e1)
            f1.write('{:^10}{:^10}{:^15}{:^15}{:^15}{:^15}'.format(str(num), str(round), str(record[num-1]),
                                                                   str(int(record[num-1]) - c_num + e_num), str(e_num),
                                                                   str(c_num/int(record[num-1]))))
            f1.write("\n")
        for i in test_5008:
            num = num + 1
            if (k == 3) and (mode == 1):
                round, c_num, e_num, l_num = k3_calculate_e5_grc_top_to_bottom_round_cover(i, k)
            if (k == 3) and (mode == 2):
                round, c_num, e_num, l_num = k3_calculate_e5_grc_top_to_bottom_round_cover_fill(i, k)
            if (k == 4) and (mode == 1):
                round, c_num, e_num, l_num = k4_calculate_e5_grc_top_to_bottom_round_cover(i, k)
            if (k == 4) and (mode == 2):
                round, c_num, e_num, l_num = k4_calculate_e5_grc_top_to_bottom_round_cover_fill(i, k)
            if (k == 5) and (mode == 1):
                round, c_num, e_num, l_num = k5_calculate_e5_grc_top_to_bottom_round_cover(i, k)
            if (k == 5) and (mode == 2):
                round, c_num, e_num, l_num = k5_calculate_e5_grc_top_to_bottom_round_cover_fill(i, k)
            if (k == 6) and (mode == 1):
                round, c_num, e_num, l_num = k6_calculate_e5_grc_top_to_bottom_round_cover(i, k)
            if (k == 6) and (mode == 2):
                round, c_num, e_num, l_num = k6_calculate_e5_grc_top_to_bottom_round_cover_fill(i, k)
            str_round_e1 = str(num) + " \t" + str(round) + " \t"
            str_c_res_e1 = str(c_num) + " \t" + str(l_num) + " \t" + str(e_num) + " \t"
            final_cover = str((c_num + e_num - l_num)/c_num) + "\n"
            str_e1 = str_round_e1 + str_c_res_e1 + final_cover
            f1.write('{:^10}{:^10}{:^15}{:^15}{:^15}{:^15}'.format(str(num), str(round), str(record[num - 1]),
                                                                   str(int(record[num-1]) - c_num + e_num), str(e_num),
                                                                   str(c_num / int(record[num-1]))))
            f1.write("\n")
e0_write()
# e1_write()
# e2_rpdb_write(2)
# e2_rpdb_fill_write(2)
#
# e3_rpdb_kg_write(2)
# e3_rpdb_kg_fill_write(2)
#
# e4_grc_write(2)
# e4_grc_fill_write(2)
# e5_grc_bottom_to_top_write(2)
# e5_grc_bottom_to_top_write_fill(2)

e2_rpdb_write(3, 1)
# e2_rpdb_write(3, 2)
# e2_rpdb_write(4, 1)
# e2_rpdb_write(4, 2)
# e2_rpdb_write(5, 1)
# e2_rpdb_write(5, 2)
# e2_rpdb_write(6, 1)
# e2_rpdb_write(6, 2)
#
# e2_rpdb_fill_write(3, 1)
# e2_rpdb_fill_write(3, 2)
# e2_rpdb_fill_write(4, 1)
# e2_rpdb_fill_write(4, 2)
# e2_rpdb_fill_write(5, 1)
# e2_rpdb_fill_write(5, 2)
# e2_rpdb_fill_write(6, 1)
# e2_rpdb_fill_write(6, 2)
#
# e3_rpdb_kg_write(3, 1)
# e3_rpdb_kg_write(3, 2)
# e3_rpdb_kg_write(4, 1)
# e3_rpdb_kg_write(4, 2)
# e3_rpdb_kg_write(5, 1)
# e3_rpdb_kg_write(5, 2)
# e3_rpdb_kg_write(6, 1)
# e3_rpdb_kg_write(6, 2)
#
# e3_rpdb_kg_fill_write(3, 1)
# e3_rpdb_kg_fill_write(3, 2)
# e3_rpdb_kg_fill_write(4, 1)
# e3_rpdb_kg_fill_write(4, 2)
# e3_rpdb_kg_fill_write(5, 1)
# e3_rpdb_kg_fill_write(5, 2)
# e3_rpdb_kg_fill_write(6, 1)
# e3_rpdb_kg_fill_write(6, 2)


# e4_grc_write_support(3, 1)
# e4_grc_write_support(3, 2)
# e5_grc_top_to_bottom_support(3, 1)
# e5_grc_top_to_bottom_support(3, 2)

# e4_grc_write_support(4, 1)
# e4_grc_write_support(4, 2)
# e5_grc_top_to_bottom_support(4, 1)
# e5_grc_top_to_bottom_support(4, 2)

e4_grc_write_support(5, 1)
e4_grc_write_support(5, 2)
e5_grc_top_to_bottom_support(5, 1)
e5_grc_top_to_bottom_support(5, 2)

e4_grc_write_support(6, 1)
e4_grc_write_support(6, 2)
e5_grc_top_to_bottom_support(6, 1)
e5_grc_top_to_bottom_support(6, 2)


