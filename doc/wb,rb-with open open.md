
## with open 和 open 之间的区别
    使用open打开文件，必须要使用close关闭文件，所以，为了保证无论是否出错都能正确地关闭文件。
    with open可以不用close()方法关闭文件，无论在文件使用中遇到什么问题都能安全的退出，即使发生错误，退出运行时环境时也能安全退出文件并给出报错信息。

##关于python文件中"wb"与"rb"的理解

“rb”,”wb”这两种方式在操作文件时，直接跳过了系统的编码方式，在windows系统中，用的编码为gbk:


①：
```python

    with open(“a.txt”,”w”) as f1:
    f1.write(“aa”);
     # 默认用gbk进行编码并且写入。
```

②: 
```python

with open(“a.txt”,”r”) as f1:
Print(f1.read())
# 默认用gbk编码进行解码
```

③: 
```python
    with open(“a.txt”,”wb”) as f1:
    f1.write(“aa”.encode(“utf-8”))
```
跳过了系统的gbk而用的是utf-8进行编码，这跟”w”不一样，好像”w”只不过省略了一个步骤即：”aa”.encode(“gbk”),而”wb”只不过对作者要求的更多即：完成了计算机自动完成的步骤。

④：
```python
    with open(“a.txt”,”rb”) as f1:
    Print(f1.read().decode(“utf-8”))
# 程序员自己手动指定了二进制的解码方式为utf-8而不是gbk
```

⑤: 
```python
    with open(“a.txt”,”r”,encoding = “utf-8”) as f1:
    Print(f1.read())
#此时指定了”r”的编码方式为utf-8，跟”rb” 有一样的效果
```

**总结：**
  - 1、”wb”,”rb”能够跳过系统自带的编码方式
  - 2、是不是,如果是”rb”,那么在print(f1.read())之前已经将二进制转换为了字符串，所以才会有with open(“a.txt”,”r”,encoding = “utf-8”) as f1 中的encoding.