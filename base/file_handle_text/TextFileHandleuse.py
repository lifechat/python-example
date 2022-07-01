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


def display_words():
    '''
    从文本文件STORY.TXT中读取行数
    从一个文本文件STORY.TXT中读取行数。
    使用读取功能
    并显示那些少于4个字符的单词。
    :return: count 单词数量
    '''
    with open("story.txt") as F:
        lines = F.read();
        words = lines.split()
        count = 0;
        for word in words:
            if(len(word) > 4):
                print(word)
                count += 1
    return count;

'''
编写一个函数
1.向文件写入内容:它将读取名为"happy.txt"的文本文件的内容并计算
2.读取名为"happy.txt"的文本文件的内容并计算以"I"或 "M"开头的行数。
'''
def write_to_file():
    with open('story.txt','a') as F:
        while True:
            text = input("enter any text:")
            F.write(text+"\n")
            choice = input("input more info,y/n:");
            if choice == "n":
                break

def check_first_letter():
    with open("happy.txt") as F:
        value = F.read();
        count  = 0
        line = value .split()
        for i in line:
            if i[0] in ['m','M',"i","I"]:
                count += 1;
                print(i)
        return count;


'''
计算文本文件 "happy.txt "中小写字母的数量。小写字母的数量"""
'''
def GetWordsLowOrUper():
    count_lower = 0
    count_upper = 0
    with open('happy.txt') as F:
        value = F.read();

        for i in value:
            if i.islower():
                count_lower += 1;
            elif i.isupper():
                count_upper += 1;

        return count_lower,count_upper

if __name__ == '__main__':
    print(GetWordsLowOrUper())