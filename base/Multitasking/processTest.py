
import multiprocessing
import time
import os

def dance():
    # current pid 当前编号
    print('dance...:', os.getpid())
    print('dance', multiprocessing.current_process())  # 当前进程
    print('dance:',os.getppid()) # parent pid
    for i in range(5):
        print('dance...')
        time.sleep(.2)


def sing():
    for i in range(5):
        print('sing...')
        time.sleep(.2)

def task(count):
    for i in range(count):
        print('task runing...')
        time.sleep(.2)
    else:
        print('task finish')


DataList = list();
def addData():
    for i in range(5):
        DataList.append(i)
        print('add:',i)
        time.sleep(.2)

    print('dataList',DataList)

def readData():
    print('read_data',DataList)
if __name__ == '__main__':
    # print('__main__...:', os.getpid())
    #
    # print('main:',multiprocessing.current_process())
    #
    # dance_process = multiprocessing.Process(target=dance,name='processdance');
    # sing_process = multiprocessing.Process(target=sing,name='processsing');
    #
    # dance_process.start();
    # sing_process.start();
    '''
    元组方式传参(args): 元组方式传参一定要和参数的顺序保持一致。
    字典方式传参(kwargs): 字典方式传参字典中的key一定要和参数名保持一致。
    进程之间不共享全局变量
    主进程会等待所有的子进程执行结束再结束
    '''
    # sub_process = multiprocessing.Process(target=task,args=(5,)) # args:通过元祖的方式传入
    # sub_process = multiprocessing.Process(target=task,kwargs={'count':3}) # 字典的形式传入
    # sub_process.start();

    add_data = multiprocessing.Process(target=addData)
    read_data = multiprocessing.Process(target=readData)

    add_data.start()
    add_data.join()

    read_data.start()

    print("main",DataList)
