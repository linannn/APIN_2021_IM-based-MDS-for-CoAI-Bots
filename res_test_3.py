#!/usr/bin/env python

# encoding: utf-8
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/5 10:48
# @Author  : junruit
# @File    : res_test_3.py
# @desc: PyCharm
'''


#    NO.      Round     Ori_Content   Lack_Content   Extra_Content   Final_Cover
def get_data():
    res_set = []
    lack_set = []
    file_name = "./experiment_result/e1_with_kg_res_5508_1_5508.txt"
    with open(file_name, 'r', encoding='utf-8') as fr:
        value = fr.readline()
        value = fr.readline()
        while value:
            value = ' '.join(value.split())
            array_record = value.split()
            cover = eval(array_record[5])
            lack_set.append(array_record[3])
            res_set.append(cover)
            value = fr.readline()

    return res_set, lack_set


# support = 6
# experiment = 2
cover_res, lack_res = get_data()
mode_set = ["e2_mod_rpdb_1_5508.txt", "e2_ran_rpdb_1_5508.txt", "e3_mod_rp_kg_1_5508.txt", "e3_ran_rp_kg_1_5508.txt", "e4_grc_tb_1_5508.txt", "e5_grc_bt_1_5508.txt"]


def modefy(support, mode):
    file_path = "./experiment_result/k" + str(support) + "/" + mode_set[mode]
    file_path_new = "./experiment_result/k" + str(support) + "/new_" + mode_set[mode]
    with open(file_path_new, 'w', encoding='utf-8') as fw:
        with open(file_path, 'r', encoding='utf-8') as fr:
            value = fr.readline()
            fw.write(value)
            value = fr.readline()
            while value:
                value = ' '.join(value.split())
                array_record = value.split()
                test_id = eval(array_record[0])
                round = array_record[1]
                ori_content = array_record[2]
                lack = lack_res[test_id - 1]
                cov = cover_res[test_id - 1]
                fw.write('{:^10}{:^10}{:^15}{:^15}{:^15}{:^15}'.format(str(test_id), str(round), str(ori_content),
                                                                       str(lack),
                                                                       str(0),
                                                                       str(cov)))
                fw.write("\n")
                value = fr.readline()


# for mode in range(2, 6):
#     for support in range(2, 3):
#         modefy(support, mode)
def judge_rationality():
    cov_record = []
    cov_valid = []
    file_path_1 = "./experiment_result/k2/e2_mod_rpdb_1_3001.txt"
    file_path_2 = "./experiment_result/k2/e2_mod_rpdb_3001_5508.txt"
    file_path_valid = "./test_res/mod_e2/e2_with_rpdb_2_mod_5508.txt"
    with open(file_path_1, 'r', encoding='utf-8') as f1:
        sentence = f1.readline()
        sentence = f1.readline()
        while sentence:
            sentence = ' '.join(sentence.split())
            array_record = sentence.split()
            cov = eval(array_record[5])
            cov_record.append(cov)
            sentence = f1.readline()
    with open(file_path_2, 'r', encoding='utf-8') as f2:
        sentence = f2.readline()
        sentence = f2.readline()
        while sentence:
            sentence = ' '.join(sentence.split())
            array_record = sentence.split()
            cov = eval(array_record[5])
            cov_record.append(cov)
            sentence = f2.readline()

    with open(file_path_valid, 'r', encoding='utf-8') as fv:
        sentence = fv.readline()
        sentence = fv.readline()
        while sentence:
            sentence = ' '.join(sentence.split())
            array_record = sentence.split()
            cov = eval(array_record[5])
            cov_valid.append(cov)
            sentence = fv.readline()

    return cov_record, cov_valid


cov_record, cov_valid = judge_rationality()
for i in range(0, len(cov_record)):
    if cov_valid[i] == cov_record[i]:
        # print("pass")
        pass
    else:
        print(i + 1)


