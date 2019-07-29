# -*- coding: utf-8 -*-
# @Time    : 2019/7/29 20:16
# @Author  : SDYL
# @Email   : sdyl_1020@163.com
# @File    : sqList.py
# @Software: PyCharm


class SqList(object):
    def __init__(self, maxsize):
        self.curLen = 0                             # 顺序表的当前长度
        self.maxSize = maxsize                      # 顺序表的最大长度
        self.listItem = [None] * self.maxSize       # 顺序表的存储空间

    def clear(self):

        """将线性表置空"""
        self.curLen = 0

    def isEmpty(self):
        """判断线性表是否为空表"""
        return self.curLen == 0
     
    def length(self):
        """返回线性表的长度"""
        return self.curLen

    def get(self, i):
        """读取并返回线性表中的第i个数据元素"""
        if i < 0 or i > self.curLen -1:
            raise Exception("第i个元素不存在")
        return self.listItem[i]

    def insert(self, i, x):
        """插入x作为第i个元素"""
        if self.curLen == self.maxSize:
            raise Exception("---顺序表满---")
        if i < 0 or i > self.curLen:
            raise Exception("---插入位置非法---")
        for j in range(self.curLen, i - 1, -1):
            self.listItem[j] = self.listItem[j-1]
        self.listItem[i] = x
        self.curLen += i

    def remove(self, i):
        """删除第i个元素"""
        if i < 0 or i > self.curLen -1:
            raise Exception("---删除位置非法---")
        for j in range(self.curLen):
            self.listItem[j] = self.listItem[j + 1]
        self.curLen -= 1

    def index(self, x):
        """返回元素x首次出现的位序号"""
        for i in range(self.curLen):
            if self.listItem[i] == x:
                return i
        return -1

    def display(self):
        """输出线性表中各元素的值"""
        for i in range(self.curLen):
            print(self.listItem[i], end='')
