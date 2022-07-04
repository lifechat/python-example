
import threading
import time



def sing():
    for i in range(3):
        print("sing..%d"%i)
        time.sleep(1)

def dance():
    for i in range(3):
        print('dance..%d'%i)
        time.sleep(1)

listData = list()

# 写入数据
def write_data():
    for i in range(5):
        listData.append(i)
        time.sleep(.1)
    print("write_data",listData)
def read_data():
    print("read_data:",listData)

g_num = 0;

# 加锁

lock = threading.Lock()

def sum_num1():
    lock.acquire()
    for i in range(10000):
        global g_num
        g_num += 1;
    print('sum1:',g_num)

    lock.release()

def sum_num2():
    lock.acquire()
    for i in range(10000):
        global g_num
        g_num += 1;
    print('sum2:',g_num)
    lock.release()
if __name__ == '__main__':
    '''
       线程之间共享全局变量：
线程之间执行是无序的
主线程会等待所有的子线程执行结束再结束
线程之间共享全局变量
线程之间共享全局变量数据出现错误问题

       互斥锁：
       
       死锁
    '''
    sing_thread = threading.Thread(target=sum_num1);

    dance_thread = threading.Thread(target=sum_num2);


    sing_thread.start()

    dance_thread.start()