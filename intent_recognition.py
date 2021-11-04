#!/usr/bin/env python

# encoding: utf-8
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/15 9:29
# @Author  : junruit
# @File    : intent_recognition.py
# @desc: PyCharm
'''
from base_rp_db import *
import re


def intent_bert(sentence):
    intent = []
    # todo 用户意图识别于提取
    # format = an arraylist
    # intent.append({'pro': {'housekeeper'}, 'price': {'low'}, 'gender': {'woman'}, 'age': {'young'}})
    # intent.append({'org': {'abc'}})
    intent.append({'pro': {'旅行'}})
    # print(type(intent))
    return intent


def deal_bert_result_into_nature_language_restricts(sentence, valuetype):
    if refuse_or_negative(sentence) == "我无所谓":
        return "random"

    if valuetype == "region":
        # todo 完善提取匹配字符串
        value = re.findall(r'\d+', sentence)
        return value[0] + "-" + value[1]
    else:
        return sentence


def deal_bert_result_into_extra_restricts(sentence):
    function_res = [-1, -1, -1, -1, -1, -1]
    if sentence == "没了":
        function_res[0] = 0
        return function_res
    temp_res = intent_bert(sentence)
    # todo temp_res 的结果由bert结论控制
    # temp_res 为一个数组，temp_res[0]为key ，后面元素分别对应不同类型的数据对应不同内容
    if temp_res == "时序":
        # valuetype 为 时序（after) 在。。。之后
        # temp_res[0] = key, temp_res[1] = value
        function_res[0] = 4
        function_res[1] = temp_res[0]
        function_res[5] = temp_res[1]
        function_res = communicate_of_new_restricts(function_res)
        return function_res
    elif temp_res == "范围":
        # valuetype 为 范围region
        # "key": "数量",
        # "valueType": "region",
        # "minValue": 15.0,
        # "maxValue": 20.0,
        # "unit": "桌",
        # "value": ""
        # temp_res[0] = key, temp_res[1] = minvalue, temp_res[2] = maxvalue, temp_res[3] = unit,
        function_res[0] = 2
        function_res[1] = temp_res[0]
        function_res[2] = temp_res[1]
        function_res[3] = temp_res[2]
        function_res[4] = temp_res[3]
        function_res = communicate_of_new_restricts(function_res)
        return function_res
    elif temp_res == "服务提供者":
        # valuetype 为 服务提供者（service-provider） 例：我要做南航的飞机
        # {
        #     "key": "服务提供者",
        #     "valueType": "service-provider",
        #     "minValue": 0.0,
        #     "maxValue": 9999.0,
        #     "unit": "0",
        #     "value": "地铁"
        # }
        # temp_res[0] = key, temp_res[1] = value
        function_res[0] = 3
        function_res[1] = temp_res[0]
        function_res[5] = temp_res[1]
        function_res = communicate_of_new_restricts(function_res)
        return function_res
    else:
        # 其他都按照枚举enum填写 valuetype 为枚举enum
        # 样例1 "离散,气氛,热闹"
        # 生成样例
        # {
        #   "key: "风格",
        #   valueType: "enum",
        #   minValue: 0.0,
        #   maxValue: 9999.0,
        #   unit: "0",
        #   value: "西式"
        # }
        # temp_res[0] = key, temp_res[1] = value
        function_res[0] = 1
        function_res[1] = temp_res[0]
        function_res[5] = temp_res[1]
        function_res = communicate_of_new_restricts(function_res)
        return function_res


def refuse_or_negative(sentence):
    # sentence 判定条件 可修改
    if sentence == "我无所谓":
        return "我无所谓"
    elif sentence == "我不需要":
        return "我不需要"
    elif sentence == "没有了":
        return "没有了"
    else:
        return 1


# 将用户的子意图新点选择提取出来
def get_content(sentence):
    res = sentence
    return res

