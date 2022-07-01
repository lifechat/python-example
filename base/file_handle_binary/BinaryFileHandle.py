import pickle


def DelBinaryFile():

    with open('class.dat',encoding="utf-8",errors='ignore') as F:
        stud = pickle.load(F);
        print(stud)

    rno = int(input("Enter the Roll no. to be deleted: "))

    with open("class.dat",encoding="utf-8",errors='ignore') as F:
        rec = [];
        for i in stud:
            if i[0] == rno:
                continue
            rec.append(i)
            pickle.dump(rec,F);

def searchBinaryFile():
    '''
    @desc:查找.dat文件的文件记录
    :return:返回查找行记录
    '''
    F = open('class.dat','rb')
    value = pickle.load(F);
    search = 0;
    rno = int(input("Enter serch roll no:"))
    for i in value:
        if i[0] == rno:
            print("Record List:")
            print(i)
            search = 1;
        if search == 0:
            print("Sorry,you didn't find records")
            break;
        F.close()

def insertBinaryFile():

    F=open('class.dat','ab')

    list = [
        [1, "Ramya", 30],
        [2, "vaishnavi", 60],
        [3, "anuya", 40],
        [4, "kamala", 30],
        [5, "anuraag", 10],
        [6, "Reshi", 77],
        [7, "Biancaa.R", 100],
        [8, "sandhya", 65],
    ]

#     按照层次结构序列化数据
    pickle.dump(list,F);
    F.close()

def remcount():
    F = open('class.dat','rb')
    val = pickle.load(F)
    count = 0;

    for i in val:
        if i[2] <= 60:
            print(i,'elig')
            count += 1;
    print(count)
    F.close()

def GetbestValue():
    F = open('class.dat','rb')
    val = pickle.load(F)
    main = []
    count = 0;

    for i in val:
        print(i)
        data = i[2]
        main.append(data)

    top = max(main) # 求最高分
    last = min(main) # 最低分
    print(top,"is the first mark")
    print(last, "is the min mark")

    F.seek(0)
    for i in val:
        if top == i[2] or last == i[2]:
            print(i)
            print("congrats")
            count += 1

    print(count)
    F.close()

def UpdateBinaryFile():

    F = open('class.dat','rb+')
    value = pickle.load(F) # 反序列化
    found = 0;
    roll = int(input("输入需要更新数据的行数"))
    for i in value:
        if roll == i[0]:
            print("cname",i[1])
            print("cmarks",i[2])
            i[1] = input('输入新的name')
            i[2] = int(input("输入新的marks"))
            found = 1
    if found == 0:
        print("没有找到数据")

    else:
        pickle.dump(value,F)
        F.seek(0)
        newval = pickle.load(F)
        print(newval)

    F.close()
if __name__ == '__main__':
    UpdateBinaryFile()
    GetbestValue()