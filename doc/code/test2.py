# coding=utf-8
# Copyright (c) 2016-2018 The Ulord Core Developers
# @File  : test2.py
# @Author: Ulord_PuJi
# @Date  : 2018/5/17 0017

def init_test(t):
    """
    用于初始化项目测试，不需要任何参数

    :type t: <int>

    :return:
    """

    print("初始化项目")


def start(t):
    """
    启动项目入口

    :type t: <int>

    :param t: test

    :return:
    """
    test(3)

def test(v):
    """
    项目运行主要函数，需要传入一个参数

    :param v: int

    :type v: user's attribute and value

    :return:
    """

    print(v)
