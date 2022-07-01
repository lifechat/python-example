import sys


# 读取文件内容
def longlines():

    with open('story.txt','r',encoding='utf-8') as F:

        lines = F.readlines();

        for i in lines:
            if len(i) < 50:
                print(i,end=" ");


#  @desc: 根据用户输入的文件名称遍历文件，自动打开
#  strip([char]) 去除相关字符，或者空格
#  stream流 处理文件格式
def strenLoader():

    # 输出
    sys.stdout.writelines("输入文件名称:")
    file = sys.stdin.readline();

    with open(file.strip(),) as F:

        while True:
            ch = F.readlines()
            for (i) in ch:
                print(i,end="")
            else:
                sys.stderr.writelines('End of file reached\n');
                break;


def readFileLoader():

    F = open("happy.txt",'r')

    # val = F.read()
    # val = val.split()
    # for i in val:
    #     print(i,"*",end="---*  \n")
    # print("\n")

#     method2
    F.seek(0)
    value = F.readlines();
    for line in value:
        for word in line.split():
            print(word,"*",end="\n")

    F.close()




if __name__ == '__main__':

    readFileLoader();