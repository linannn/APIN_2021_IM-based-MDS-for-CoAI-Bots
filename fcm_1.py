import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from skfuzzy.cluster import cmeans
import math
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler


# 从文件读数据并制定聚类数k
def fcm(filePath, k):
    dataSet = []
    fileIn = open(filePath)
    for line in fileIn.readlines():
        temp = []
        lineArr = line.strip().split('\t')
        for i in range(len(lineArr)):
            temp.append(float(lineArr[i]))
        dataSet.append(temp)
    fileIn.close()
    X = np.array(dataSet)
    X = X.T
    center, u, u0, d, jm, p, fpc = cmeans(X, m=2, c=k, error=0.005, maxiter=1000)
    # print(u)
    # print(center)
    for i in u:
        # print(i)
        label = np.argmax(u, axis=0)
    print(label)


def fcm_auto(filePath, support, mode):
    dataSet = []
    fileIn = open(filePath, encoding="utf-8")
    for line in fileIn.readlines():
        temp = []
        lineArr = line.strip().split(' ')
        for i in range(1, len(lineArr)):
            temp.append(float(lineArr[i]))
        dataSet.append(temp)
    fileIn.close()
    X = np.array(dataSet)
    X = X.T
    n = len(dataSet)
    max_fpc = 0
    c = 0
    for i in range(2, int(math.sqrt(len(dataSet))) + 1):
        center, u, u0, d, jm, p, fpc = cmeans(X, m=2, c=i, error=0.001, maxiter=1000)
        print(i)
        print(fpc)
        if fpc > max_fpc:
            max_fpc = fpc
            c = i
    print("fcm最佳聚类数：" + str(c))
    center, u, u0, d, jm, p, fpc = cmeans(X, m=2, c=c, error=0.001, maxiter=1000)
    for i in u:
        # print(i)
        label = np.argmax(u, axis=0)
    print(label)
    print(len(label))
    label = label.tolist()
    res_grc = {}
    for id_x, d_temp in enumerate(label):
        if d_temp not in res_grc:
            res_grc[d_temp] = [id_x]
            # print(res_grc[d_temp])
        else:
            res_grc[d_temp].append(id_x)
            # print(res_grc[d_temp])
    # file_write = "./k" + str(support) + "_Grc/divide_res_旅行" + str(support) + ".txt"
    # file_write = "./top_grc/divide_top_k" + str(support) + ".txt"
    file_write = "./top_grc/divide_top_k" + str(support) + "_" + str(mode) + ".txt"
    with open(file_write, 'w', encoding='utf-8') as wri:
        for k, v in res_grc.items():
            # wri.write(str(k))
            wri.write(str(v))
            wri.write("\n")




# train = X
# re_0 = []
# re_1 = []
# # for i in range(len(dataSet)):
# # 	if label[i] == 0:
# # 		print(dataSet[i])
# # 		re_0.append(dataSet[i])
# # 		# with open('sum_2_1.txt', 'a', newline='', encoding='utf-8')as f:
# # 		# 	for ele in dataSet[i]:
# # 		# 		f.write(str(ele) + " ")
# # 		# 	f.write("\n")
# # 		plt.scatter(train[4][i], 0.001, c='r')
# # # plt.savefig('fig2.jpg')
# # # plt.show()
# # print("\n")
# # for i in range(len(dataSet)):
# # 	if label[i] == 1:
# # 		# print(train[3][i])
# # 		print(dataSet[i])
# # 		re_1.append(dataSet[i])
# # 		# with open('sum_2_2.txt', 'a', newline='', encoding='utf-8')as f:
# # 		# 	for ele in dataSet[i]:
# # 		# 		f.write(str(ele) + " ")
# # 		# 	f.write("\n")
# # 		# dict_2.append(train[3][i])
# # 		plt.scatter(train[4][i], -0.001, c='g')
# # # plt.savefig('fig3.jpg')
# index = 2
# out = []
# for i in range(len(dataSet)):
# 	if label[i] == 0:
# 		print(dataSet[i])
# 		# plt.scatter(dataSet[i][4], dataSet[i][2], c='g')
# print("\n")
# for i in range(len(dataSet)):
# 	if label[i] == 1:
# 		print(dataSet[i])
# 		# plt.scatter(dataSet[i][4], dataSet[i][2], c='b')
# print("\n")
# # for i in range(len(dataSet)):
# # 	if label[i] == 2:
# # 		print(dataSet[i])
# # 		plt.scatter(dataSet[i][4], dataSet[i][2], c='r')
# # print("\n")
# # for i in range(len(dataSet)):
# # 	if label[i] == 3:
# # 		print(dataSet[i])
# # 		plt.scatter(dataSet[i][3], dataSet[i][2], c='orange')
# # print("\n")
# # plt.savefig("fig.jpg")
# # plt.show()
# # #
# re_2 = []
# re_3 = []
# for i in range(len(dataSet)):
# 	if label[i] == 0:
# 		if dataSet[i][index] not in out:
# 			re_0.append(dataSet[i])
# 	elif label[i] == 1:
# 		if dataSet[i][index] not in out:
# 			re_1.append(dataSet[i])
# # 	elif label[i] == 2:
# # 		if dataSet[i][index] not in out:
# # 			re_2.append(dataSet[i])
# # # 	elif label[i] == 3:
# # # 		if dataSet[i][index] not in out:
# # # 			re_3.append(dataSet[i])
# # writeFile("sum_2_temp_1.txt", re_0, index)
# # writeFile("sum_2_temp_2.txt", re_1, index)
# # writeFile("sum_2_temp_3.txt", re_2, index)
# # writeFile("sum_2_temp_14.txt", re_3, index)
# list_1 = []
# list_2 = []
# list_3 = []
# result_0,result_1 = overlap(re_0, re_1, index)
# for i in range(len(re_0)):
# 	if result_0[i] == 1:
# 		plt.scatter(re_0[i][index], -0.001, c='g')
# 		list_1.append(re_0[i])
# 	elif result_0[i] == 2:
# 		plt.scatter(re_0[i][index], -0.001, c='r')
# 		list_2.append(re_0[i])
# 	elif result_0[i] == 3:
# 		plt.scatter(re_0[i][index], -0.001, c='orange')
# 		list_3.append(re_0[i])
# for i in range(len(re_1)):
# 	if result_1[i] == 1:
# 		plt.scatter(re_1[i][index], 0.001, c='g')
# 		list_1.append(re_1[i])
# 	elif result_1[i] == 2:
# 		plt.scatter(re_1[i][index], 0.001, c='r')
# 		list_2.append(re_1[i])
# 	elif result_1[i] == 3:
# 		plt.scatter(re_1[i][index], 0.001, c='orange')
# 		list_3.append(re_1[i])
# print(list_1)
# print("\n")
# print(list_2)
# print("\n")
# print(list_3)
# print("\n")
# # writeFile("sum_6_xiao.txt", list_1, index)
# # writeFile("sum_6_zhong.txt", list_3, index)
# # writeFile("sum_6_da.txt", list_2, index)
# # writeFile("sum_6_xiao_1.txt", list_1, index)
# # writeFile("sum_6_xiao_2.txt", list_3, index)
# # writeFile("sum_6_xiao_3.txt", list_2, index)
# # writeFile("sum_6_young.txt", list_1, index)
# # writeFile("sum_6_ok.txt", list_3, index)
# # writeFile("sum_6_old.txt", list_2, index)
# # plt.savefig('fig.jpg')
# plt.show()


# 文件读数据并进行归一化
def read(filePath):
    dataSet = []
    fileIn = open(filePath, encoding="utf-8")
    for line in fileIn.readlines():
        temp = []
        lineArr = line.strip().split(' ')
        for i in range(0, len(lineArr)):
            temp.append(float(lineArr[i]))
        dataSet.append(temp)
    fileIn.close()
    # print(dataSet)
    # money = []
    # for ll in dataSet:
    # 	m_i = []
    # 	m_i.append(ll[9])
    # 	money.append(m_i)
    # # print(money)
    # minMax = MinMaxScaler()
    # # 将数据进行归一化
    # x_std = minMax.fit_transform(money)
    # # print(x_std)
    # for i in range(len(dataSet)):
    # 	dataSet[i][9] = x_std[i][0]
    # print(dataSet)
    return dataSet


# 多个员工数据中按照某一属性选出最大最小值
def max_min(array, index):
    record_i = []
    list_i = np.array(array)
    max = np.amax(list_i, axis=0)[index]
    min = np.amin(list_i, axis=0)[index]
    record_i.append(min)
    record_i.append(max)
    return record_i


# 输入数组，属性序号，保存图片名，x坐标名
# array:待聚类数组
# index：待聚类属性在众属性中的序号
# name:保存结果的图片名
# xlab:保存结果的图片中x坐标名
# def fcm_array(array, index, name, xlab):
#     X = np.array(array)
#     X = np.delete(X, 0, axis=1)
#     X = X.T
#     n = len(array)
#     max_fpc = 0
#     c = 0
#     for i in range(2, int(math.sqrt(len(array))) + 1):
# 	    center, u, u0, d, jm, p, fpc = cmeans(X, m=2, c=i, error=0.001, maxiter=1000)
# 	    if fpc > max_fpc:
# 		    max_fpc = fpc
# 		    c = i
#     print("fcm最佳聚类数：" + str(c))
#     center, u, u0, d, jm, p, fpc = cmeans(X, m=2, c=c, error=0.001, maxiter=1000)
#     for i in u:
# 		label = np.argmax(u, axis=0)
# 	print(label)
#     list_sum = []
#     record = []
# 	# 聚类数为2时，两类有重合时，调出重合部分分为三类并做图
# 	if c == 2:
# 		for i in range(c):
# 			list_i = []
# 			record_i = []
# 			for j in range(len(label)):
# 				if label[j] == i:
# 					list_i.append(array[j])
# 					print(array[j])
# 					# if label[j] == 0:
# 					# 	plt.scatter(array[j][index], 0.002, c='g')
# 					# else:
# 					# 	plt.scatter(array[j][index], -0.002, c='r')
# 			print(len(list_i))
# 			print("\n")
# 			record_i = max_min(list_i, index)
# 			record.append(record_i)
# 			# list_i = np.delete(np.array(list_i), index, axis=1)
# 			list_sum.append(list_i)
# 		# plt.show()
# 		# print(list_sum)
# 		fig_1, fig_2 = overlap(list_sum[0], list_sum[1], index)
# 		for i in range(len(list_sum[0])):
# 			if fig_1[i] == 1:
# 				plt.scatter(list_sum[0][i][index], -0.001, c='g')
# 			elif fig_1[i] == 2:
# 				plt.scatter(list_sum[0][i][index], -0.001, c='r')
# 			elif fig_1[i] == 3:
# 				plt.scatter(list_sum[0][i][index], -0.001, c='orange')
# 		for i in range(len(list_sum[1])):
# 			if fig_2[i] == 1:
# 				plt.scatter(list_sum[1][i][index], 0.001, c='g')
# 			elif fig_2[i] == 2:
# 				plt.scatter(list_sum[1][i][index], 0.001, c='r')
# 			elif fig_2[i] == 3:
# 				plt.scatter(list_sum[1][i][index], 0.001, c='orange')
# 		# plt.title(ti)
# 		plt.xlabel(xlab)
# 		plt.yticks([])
# 		plt.savefig(str(name) + ".jpg")
# 		plt.show()
# 		#聚类后结果处理，得到下一轮聚类数据
# 		for i in range(c):
# 			for j in range(i):
# 				r_1, r_2, r_3 = overlap1(list_sum[i], list_sum[j], index)
# 				if r_2 == []:
# 					continue
# 				else:
# 					list_sum[i] = r_1
# 					list_sum[j] = r_3
# 					list_sum.append(r_2)
# 					record[i] = max_min(r_1, index)
# 					record[j] = max_min(r_3, index)
# 					record.append(max_min(r_2, index))
# 		# print(list_sum)
# 		out = []
# 		for i in range(len(list_sum)):
# 			list_i = np.delete(np.array(list_sum[i]), index, axis=1)
# 			if len(list_i) > 8:
# 				out.append(list_i.tolist())
# 			else:
# 				print(record[i])
# 				# printFile1(list_i)
# 				# writeFile1("fcm.txt", list_i)
# 		print(record)
# 	else:
# 		for i in range(c):
# 			list_i = []
# 			record_i = []
# 			for j in range(len(label)):
# 				if label[j] == i:
# 					list_i.append(array[j])
# 					print(array[j])
# 			#当按照一个属性分类时，纵坐标自定义
# 			# for j in range(len(label)):
# 			# 	if label[j] == 0:
# 			# 		plt.scatter(array[j][index], 0.002, c='g')
# 			# 	elif label[j] == 1:
# 			# 		plt.scatter(array[j][index], 0, c='r')
# 			# 	elif label[j] == 2:
# 			# 		plt.scatter(array[j][index], -0.002, c='b')
# 			# 	elif label[j] == 3:
# 			# 		plt.scatter(array[j][index], -0.004, c='orange')
# 			# 	else:
# 			# 		plt.scatter(array[j][index], 0.004, c='y')
# 			# 当按照两个属性分类时，纵坐标为其中一个属性
# 			for j in range(len(label)):
# 				if label[j] == 0:
# 					plt.scatter(array[j][index], array[j][5], c='g')
# 				elif label[j] == 1:
# 					plt.scatter(array[j][index], array[j][5], c='r')
# 				elif label[j] == 2:
# 					plt.scatter(array[j][index], array[j][5], c='b')
# 				elif label[j] == 3:
# 					plt.scatter(array[j][index], array[j][5], c='orange')
# 				else:
# 					plt.scatter(array[j][index], array[j][5], c='y')
# 			plt.xlabel(xlab)
# 			plt.ylabel("service area")
# 			plt.savefig(str(name) + ".jpg")
# 			plt.show()
# 			print(len(list_i))
# 			print("\n")
# 			record_i = max_min(list_i, index)
# 			record.append(record_i)
# 			list_sum.append(list_i)
# 		out = []
# 		for i in range(len(list_sum)):
# 			list_i = np.delete(np.array(list_sum[i]), index, axis=1)
# 			if len(list_i) > 8:
# 				out.append(list_i.tolist())
# 			else:
# 				print(record[i])
# 				# printFile1(list_i)
# 				# writeFile1("fcm.txt", list_i)
# 		print(record)
# 	return c, out, record


# 重叠数据处理
# re_0:数组1
# re_1:数组2
# index:聚类属性序号
# 返回两个数组，分别为re_0,re_1所对应的每个数据在重叠处理中的所属类序号，比如3表示两数组重合部分
def overlap(re_0, re_1, index):
    list_0 = []
    list_1 = []
    for ele in re_0:
        list_0.append(ele[index])
    for ele in re_1:
        list_1.append(ele[index])
    max_0 = max(list_0)
    max_1 = max(list_1)
    min_0 = min(list_0)
    min_1 = min(list_1)
    result_0 = []
    result_1 = []
    out_1 = []
    out_2 = []
    out_3 = []
    # list_1是较大的集合
    if max_1 > max_0:
        for ele in re_1:
            if ele[index] > max_0:
                result_1.append(2)
            else:
                result_1.append(3)
        for ele in re_0:
            if ele[index] < min_1:
                result_0.append(1)
            else:
                result_0.append(3)
    # list_1较小
    else:
        for ele in re_0:
            if ele[index] > max_1:
                result_0.append(2)
            else:
                result_0.append(3)
        for ele in re_1:
            if ele[index] < min_0:
                result_1.append(1)
            else:
                result_1.append(3)
    return result_0, result_1


# 重叠数据处理
# re_0:数组1
# re_1:数组2
# index:聚类属性序号
# 返回将重合数据分为第三类后的三个数组
def overlap1(re_0, re_1, index):
    list_0 = []
    list_1 = []
    for ele in re_0:
        list_0.append(ele[index])
    for ele in re_1:
        list_1.append(ele[index])
    max_0 = max(list_0)
    max_1 = max(list_1)
    min_0 = min(list_0)
    min_1 = min(list_1)
    result_1 = []
    result_2 = []
    result_3 = []
    # list_1是较大的集合
    if max_1 > max_0:
        for i in range(len(re_1)):
            if re_1[i][index] > max_0:
                result_3.append(re_1[i])
            else:
                result_2.append(re_1[i])
        for i in range(len(re_0)):
            if re_0[i][index] < min_1:
                result_1.append(re_0[i])
            else:
                result_2.append(re_0[i])
    # list_1较小
    else:
        for i in range(len(re_0)):
            if re_0[i][index] > max_1:
                result_3.append(re_0[i])
            else:
                result_2.append(re_0[i])
        for i in range(len(re_1)):
            if re_1[i][index] < min_0:
                result_1.append(re_1[i])
            else:
                result_2.append(re_1[i])
    return result_1, result_2, result_3


def writeFile1(filepath, data, ):
    with open(filepath, 'a', newline='', encoding='utf-8')as f:
        for i in range(len(data)):
            f.write(str(data[i][0]))
            f.write("\n")
        # f.write(str(data[i][j]) + " ")
        f.write("\n")


def printFile1(data):
    for i in range(len(data)):
        print(str(data[i][0]))
    # f.write(str(data[i][j]) + " ")


def writeFile(filepath, data, ):
    with open(filepath, 'a', newline='', encoding='utf-8')as f:
        for i in range(len(data)):
            for j in range(len(data[i])):
                f.write(str(data[i][j]) + " ")
            f.write("\n")
        f.write("\n")


def writestr(filePath, str):
    with open(filePath, 'a', newline='', encoding='utf-8')as f:
        f.write(str)
        f.write("\n")


def readfcm(start, end):
    out = []
    with open("fcm.txt", 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for i in range(start - 1, end):
            out.append(float(lines[i]))
    print(out)
    return out


# dataSet = read('grc_epoch_divide_2.txt')
# c, dataSet, record = fcm_array(dataSet, 8, 5, "user evaluation")
# for i in range(len(dataSet)):
# 	writeFile("a_" + str(i) + ".txt", dataSet[i])
# 	c_i, dataSet_i, record_i = fcm_array(dataSet[i], 5, i, "work experience")
def fcm_path_1(k):
    file_path = "grc_epoch_divide_" + str(k) + ".txt"
    fcm_auto(file_path, k)


def fcm_path_2(k):
    file_path = "./top_grc/top_grc_fcm_k" + str(k) + ".txt"
    fcm_auto(file_path, k)


def fcm_path_3(k, mode):
    file_path = "./top_grc/record_top_grc_show_k" + str(k) + "_" + str(mode) + ".txt"
    fcm_auto(file_path, k, mode)


# fcm_path(3)
fcm_path_3(2, 4)

# dataSet = read('a_01.txt')
# c, dataSet, record = fcm_array(dataSet, 3, 5,"educational background")
# for i in range(len(dataSet)):
# # # 	# writeFile("a_" + str(i) + ".txt", dataSet[i])
# 	c_i, dataSet_i, record_i = fcm_array(dataSet[i], 5, i, "user evaluation")
# # 	# try:
# # 	# 	c_i, dataSet_i, record_i = fcm_array(dataSet[i], 5)
# # 	# except BaseException:
# # 	# 	c_i, dataSet_i, record_i = fcm_array(dataSet[i], 6)
# 	for j in range(len(dataSet_i)):
# 		c_j, dataSet_j, record_j = fcm_array(dataSet_i[j], 4, str(i) + str(j),"service area")
# 		for k in range(len(dataSet_j)):
# 			fcm_array(dataSet_j[k], 4,str(i) + str(j)+str(k) , "price")
# # 		# writeFile("a_" + str(i) + str(j) + ".txt", dataSet_i[j])
