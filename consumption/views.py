import datetime
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
# Create your views here.
# 快速导包快捷键  alt+enter
from django.views import View
import json
from consumption.models import LifeInfo


# def index(request):
#     return HttpResponse('index')

class LifeView(View):
    def get(self,request):
        all_life = LifeInfo.objects.all()  # 获取所有数据
        return render(request, 'index.html', context={'lifelist':all_life})

    def post(self, request):
        data = request.POST   # 接收数据
        try:
            # 创建对象
            life = LifeInfo(
                date = data.get('date'),
                consumption_matters = data.get('consumption_matters'),
                amount = data.get('amount'),
                total = data.get('total'),
            )
            life.save()
            return JsonResponse({'data':"添加成功"})
        except Exception as e:
            return JsonResponse({'data': "添加失败"})


    def put(self, request):
        data = json.loads(request.body.decode()) # 接收数据
        life_id = data.get('id')   # 根据id获取对象
        try:
            life = LifeInfo.objects.get(id=life_id)
            # 修改更新数据
            life.date = datetime.datetime.strptime(data.get('date'), '%Y年%m月%d日')
            life.consumption_matters = data.get('consumption_matters')
            life.amount = data.get('amount')
            life.total = data.get('total')

            life.save()
            return JsonResponse({'data':'修改成功'})
        except Exception as e:
            return JsonResponse({'data': '修改失败'})

    def delete(self, request):
        life_id = json.loads(request.body.decode()).get('id') # 拿到消费id
        try:
            life = LifeInfo.objects.get(id=life_id)   # 获取该ID的对象
            life.delete()
            return JsonResponse({'data':'删除成功'})
        except Exception as e:
            return JsonResponse({'data': '删除失败'})
        finally:
            pass



'''
# 闭包 在一个函数内部仔定义一个函数，并且这个函数可以使用外部函数的变量

# 装饰器 本质上是一个函数，它让其他函数在不需要变更代码的情况下，额外添加其他的功能，其返回值也是一个函数对象

# tcp三次握手
# 第一次握手：建立连接时，客户端发送syn包（syn=x）到服务器，并进入SYN_SENT状态，等待服务器确认；SYN：同步序列编号（Synchronize Sequence Numbers）。
# 第二次握手：服务器收到syn包，必须确认客户的SYN（ack=x+1），同时自己也发送一个SYN包（syn=y），即SYN+ACK包，此时服务器进入SYN_RECV状态；
# 第三次握手：客户端收到服务器的SYN+ACK包，向服务器发送确认包ACK(ack=y+1），此包发送完毕，客户端和服务器进入ESTABLISHED（TCP连接成功）状态，完成三次握手。

# session、token、cookie三者的区别
# cookie存放在客户的浏览器上，session存储在服务器上
# cookie不是很安全，session相对cookie比较安全
# session会在一定时间内保存在服务器上，当访问增多，会比较占用服务器的性能，应当使用cookie
# token验证是无状态的，cookie是有状态的
# token相对于session,cookie是最安全的
# session需要存储空间，token可以不需要存储空间
# sessionID会自动由浏览器带上，token需要代码才能带上

# is和==的区别
# is判断的是A对象是否就是B对象，通过id来判断；
# ==判断的是对象的值是否相等，通过value来判断

# init和new的区别
# init在对象创建后，初始化对象
# new是创建对象之前创建一个对象，并将该对象返回给init

# 进程、线程的区别、协程gevent,三者的关系
# 进程是并行（同一时刻多个任务运行），线程是并发（同一时间段内，多个任务运行，存在交替执行的情况）
# 进程是资源分配的最小单位，线程是程序执行的最小单位
# 线程占用的资源要比进程少，开销也比进程小
# 线程共享全局变量，进程不共享全局变量
# 进程里有线程，线程里有协程

# 什么是锁，有哪几种锁，悲观锁与乐观锁的理解与区别
# 锁是python提供的对线程控制的对象，有互斥锁，可重入锁，全局解释器锁GIL（限制多线程同时执行，保证同一时间只有一个线程执行）
# 悲观锁：总是假设最坏的情况，每次去拿数据的时候都认为别人会修改数据，所以在每次拿取数据的时候都会上锁
# 乐观锁：总是假设最好的情况，每次去拿数据的时候都认为别人不会修改数据，所以在每次拿取数据的时候都不会上锁

# IO密集型与CPU密集型的区别
# IO密集型：系统运作，硬盘/内存读写操作
# CPU密集型：计算、逻辑判断等cpu操作

# 数据库设计，优化
遵循三范式原则
尽量使用int类型；能使用varchar就不要使用char；使用索引；尽量避免使用<>\!=等操作符号；尽量少的直接操作数据库，使用redis做数据缓存，

# 事务的特性
# 原子性、一致性、隔离性、持久性
默认的事务隔离级别是：可重复读

# 集群怎么搭建

# elasticsearch怎么搭建
下载镜像，解压，修改添加配置

# celery的三个重要组件是什么，应用场景
# 客户端 任务队列 任务处理者
# 在项目中主要用来处理耗时任务，消息队列

# restful api的理解
'''


