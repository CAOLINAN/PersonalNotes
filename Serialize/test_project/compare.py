# coding=utf-8
# @File  : compare.py
# @Author: PuJi
# @Date  : 2018/3/10 0010

import time
import sys
import msgpack
import json
import avro

class Pack():
    def __init__(self, name, pack, unpack):
        self.name = name
        self.pack = pack
        self.unpack = unpack

    # 循环序列化
    def pack_cycle(self, num, input):
        start = time.time()
        while(num):
            input = self.pack(input)
            num -= 1
        end = time.time()
        print "packing {} \t\t cost \t\t{}".format(self.name, (end - start))
        return input

    # 序列化一次
    def pack_cost_time(self, input):
        start = time.time()
        result = self.pack(input)
        end = time.time()
        print "packing {} \t\t cost \t\t{}".format(self.name, (end - start))
        return result

    # 序列化后大小
    def get_size(self, result):
        self.size = sys.getsizeof(result)
        print "packing {} \t\t takes \t\t{}".format(self.name, self.size)
        return self.size

    def unpack_cost_time(self, input):
        start = time.time()
        result = self.unpack(input)
        end = time.time()
        print "unpacking {} \t\t cost \t\t{}".format(self.name, (end - start))
        return result
# def cycle(function, num, input):
#     start = time.time()
#     while(num):
#         # input = msgpack.packb(input)
#         input = function(input)
#         num -= 1
#     end = time.time()
#     print (end - start)
#     return input

def cycle_dict(num):
    result = {}
    while num:
        result.update({
            num : num
        })
        num -= 1
    return result

def cost_time(function, input):
    start = time.time()
    result = function(input)
    end = time.time()
    print (end - start)
    return result

cycle_num = 1000000
result = cycle_dict(cycle_num)

# 实例化pack
messagepack = Pack("msgpack", msgpack.packb, msgpack.unpackb)
jsonpack = Pack("json", json.dumps, json.loads)
# xmlpack = Pack("xml", )
# protopack = Pack("protocol",)
# thriftpack = Pack("thrift", )
# avropack = Pack("avro", avro.protocol.)

packs = []
packs.append(messagepack)
packs.append(jsonpack)
for pack in packs:
    pack_result = pack.pack_cost_time(result)
    pack.get_size(pack_result)
    unpakc_result = pack.unpack_cost_time(pack_result)
# msgpack_pack = cost_time(msgpack.packb, result)
# json_pack = cost_time(json.dumps, result)
# # xmlpack = cost_time()
#
# original_size = sys.getsizeof(result)
# msg_size = sys.getsizeof(msgpack_pack)
# json_size = sys.getsizeof(json_pack)
#
# msgpack_recover = cost_time(msgpack.unpackb, msgpack_pack)
# json_recover = cost_time(json.loads, json_pack)
# # xml_recover = cost_time()