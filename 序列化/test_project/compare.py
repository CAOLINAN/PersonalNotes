# coding=utf-8
# @File  : compare.py
# @Author: PuJi
# @Date  : 2018/3/10 0010

import time
import sys
import msgpack
import json

def cycle(function, num, input):
    start = time.time()
    while(num):
        # input = msgpack.packb(input)
        input = function(input)
        num -= 1
    end = time.time()
    print (end - start)
    return input

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

msgpack_pack = cost_time(msgpack.packb, result)
json_pack = cost_time(json.dumps, result)
# xmlpack = cost_time()

original_size = sys.getsizeof(result)
msg_size = sys.getsizeof(msgpack_pack)
json_size = sys.getsizeof(json_pack)

msgpack_recover = cost_time(msgpack.unpackb, msgpack_pack)
json_recover = cost_time(json.loads, json_pack)
# xml_recover = cost_time()