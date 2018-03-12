
# @File  : test_msgpack.py
# @Author: PuJi
# @Date  : 2018/3/9 0009

import msgpack
import time
import json


# a = "123"
a = {
    "test":1,
    2:"sss"
}
temp_result =  msgpack.packb(a)
print temp_result
print msgpack.unpackb(temp_result)
msgpack.packb(a)
json.dumps(a)
msgpack.unpackb(msgpack.packb(a))
json.loads(json.dumps(a))
temp_json_result = json.dumps(a)
print temp_json_result
print json.loads(temp_json_result)


