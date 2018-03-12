# 说明
protobuf-win32是Protocol buffer的windows二进制文件，可从官网处下载。
addressbook_pb2.py 是生成的。
命令为protoc -I=$SRC_DIR --python_out=$DST_DIR $SRC_DIR/addressbook.proto