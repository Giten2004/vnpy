# vn.rpc

### 简介

提供跨进程服务调用的RPC模块，同时支持服务端向客户端的主动数据推送，用于实现vn.py框架下模块的多进程解耦。

### 说明

1. 使用zmq作为底层通讯库

2. 目前支持两种数据序列化方案：msgpack（默认）和json，用户在RpcObject中可以自行添加其他方案

3. 客户端和服务端通过REQ-REP模式实现跨进程服务调用

4. 客户端和服务端通过SUB-PUB模式实现主动数据推送

5. RpcClient的send和RpcServer的publish函数不是多线程安全的，在多线程中使用时需要用户自行加锁，否则可能导致zmq底层崩溃

6. 考虑到vn.rpc的主要应用场景是本机多进程或者局域网内分布式架构，网络可靠性较高，因此没有在模块中提供心跳功能，用户可以视乎自己的需求添加

7. 大体可优化项：
   1）使用 Protocol buffers  序列化
   2）服务端客户端 ZMQ套接字优化


## How to run the test script


* ValueError: Attempted relative import in non-package

Solution: https://stackoverflow.com/questions/72852/how-to-do-relative-imports-in-python

The real reason why this problem occurs with relative imports, is that relative imports works by taking the __name__ property of the module. If the module is being directly run, then __name__ is set to __main__ and it doesn't contain any information about package structure. And, thats why python complains about the relative import in non-package error.

So, by using the -m switch you provide the package structure information to python, through which it can resolve the relative imports successfully.

```
E:\CodeRepository\GitHub\vnpy\vnpy>dir
 Volume in drive E has no label.
 Volume Serial Number is 1A15-1631

 Directory of E:\CodeRepository\GitHub\vnpy\vnpy

2019/01/09  22:52    <DIR>          .
2019/01/09  22:52    <DIR>          ..
2019/01/09  22:52    <DIR>          api
2019/01/09  22:46    <DIR>          data
2019/01/11  22:53    <DIR>          event
2018/11/24  00:02    <DIR>          pricing
2019/01/11  22:59    <DIR>          rpc
2019/01/10  20:26    <DIR>          trader
2019/01/09  22:46                68 __init__.py
2019/01/09  22:52               205 __init__.pyc
               2 File(s)            273 bytes
               8 Dir(s)  139,814,129,664 bytes free

E:\CodeRepository\GitHub\vnpy\vnpy>python -m rpc.testServer
```
