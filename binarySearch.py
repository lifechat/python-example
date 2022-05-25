#  二分法查找
from prettytable import PrettyTable
# 递归

"""
   array : 测试数组
   l：左边边界值
   r：右边边界值
   value: 查找的值
"""
def binary_serach(array,l,r,value):
    # 基本判断
    if r>=l:

        mid = int(l+(r-l)/2); #中间值

        # 刚好选中最中间
        if array[mid] == value:
            return mid;
        elif arr[mid] > value:
            print("你的答案在左边，我往右边移动了")
        else:
            print("你的答案在右边，我往右边移动了")
            binary_serach(array,mid+1,r,value)
        return 1
    else:
        #不存在
        return -1
    print('递归')


# 非递归


def binary_serch(array):
    low = 0;
    high = len(array)-1;

    while low <= high:
        mid = int((low+high)/2)
        guess = array[mid];

        if guess == item:
            return mid;
        if guess > item:
            high = mid -1;
        else:
            low = mid -1;

        return None;
        print(mid);

    print(high);
    print(array)





if __name__ == '__main__':
    # 测试数组
    arr = [2, 3, 4, 10, 40];
    res = binary_serach(arr,0,len(arr)-1,3);

"""
    table = PrettyTable(['编号', '云编号', '名称', 'IP地址'])
    table.add_row(['1', 'server01', '服务器01', '172.16.0.1'])
    table.add_row(['2', 'server02', '服务器02', '172.16.0.2'])
    table.add_row(['3', 'server03', '服务器03', '172.16.0.3'])
    table.add_row(['4', 'server04', '服务器04', '172.16.0.4'])
    table.add_row(['5', 'server05', '服务器05', '172.16.0.5'])
    table.add_row(['6', 'server06', '服务器06', '172.16.0.6'])
    table.add_row(['7', 'server07', '服务器07', '172.16.0.7'])
    table.add_row(['8', 'server08', '服务器08', '172.16.0.8'])
    table.add_row(['9', 'server09', '服务器09', '172.16.0.9'])
    print(table)
"""


