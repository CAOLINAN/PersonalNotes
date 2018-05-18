# coding=utf-8
# Copyright (c) 2016-2018 The Ulord Core Developers
# @File  : test1.py
# @Author: Ulord_PuJi
# @Date  : 2018/5/17 0017

class Test1():
    """
    This a test1.I'm Test1
    """

    def hello(self):
        """
        hello function

        :return: None.print a sentense.
        """
        print("人人可以学Python")

    def renren(self, para):
        """
        renren functions

        .. code-block:: python

            >>> with io.open('nurseryrhyme.txt', 'w', encoding='utf-8') as f:
            ...     numbytes = f.write('Mary had a little lamb')
            >>> c.add('nurseryrhyme.txt')
            {'Hash': 'QmZfF6C9j4VtoCsTp4KSrhYH47QMd3DNXVZBKaxJdhaPab',
             'Name': 'nurseryrhyme.txt'}

        :type para: unicode
        :param para: test param para
        :return: None.Print a sentense.
        """
        print("自动生成文档")


class Test2():

    def test_2(self):
        '''
        我也不知道写什么好，反正我们这里是用来写文档的

        :return:
        '''
        print("文档自动生成测试2")

    def renren_2(self):
        '''
        所以我们开发的时候就应该在这里写好文档，然后用Sphinx自动生成

        :return:
        '''
        print("自动生成文档2")
