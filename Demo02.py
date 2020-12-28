"""
打开文件 ,读取文件
"""
# 打开文件 读取
# f = open("file",'r')
# f = open("test.txt",'w') # w有就打开 没有给你创建一个
# f = open("test.txt",'a') # 追加
# print(f) # 文件对象
#
# f.close()
# ----------------------------------------------------
# 读取文件
# f = open('test.txt','r')
# data = f.read()
# print(data)
# while True:
#     # 读到文件结尾返回空字符串
#     data = f.read(1024)# 一次最多读100字符
#     if not data: # 读到结尾跳出循环
#         break
#     print(data)

# 读取一行内容
# data =  f.readline(10) # 读取前十个字符
# print("一行内容",data)
# data = f.readline() # 读完第一行剩余的内容
# print("一行内容",data)
# 将内容读取为列表 ,每行为列表一个元素
# data = f.readlines(16) # 前16个字符所在的行作为读取对象
# print(data)

# 将 f 为可迭代对象
# for i in f:
#     print(i) # 每次迭代到一行内容
# f.close()

#--------------------------------------------------------------
# 练习
"""
从终端输入一个单词 从单词本中找到这个单词,打印解释的内容
如果找不到 则打印找不到    10分钟写一下
"""


# def find_word(word):
#     f = open('dict.txt') # 读方式打开
#     # 逐行比对
#     for line in f:
#         # 提取出来这一行的单词
#         w = line.split(' ')[0]
#         #print(w)
#         # 如果遍历到单词已经大于word就结束查找
#         if w > word:
#             print("没有找到")
#             return
#         elif w == word:
#             print(line)
#             return
# word = input("请输入单词:")
# result = find_word(word)
# print(result)
# ------------------------------------------------------------------
# 写
# f = open('test.txt','a')
# # n = f.write(b"hello,XXXXXXXXX")
# # print(n)
# # f.write("哎呀摔倒啦\n".encode())
# info = ["感恩评价\n","西西不死\n"]
# f.writelines(info)
# f.close()

#---------------------------------------------------------------
# with open("test.txt",'r')as f:
#     data = f.read()
#     print(data)

# with 语句块结束 file 自动销毁

# -----------------------------------------------
# 将文件复制一份 (又读又写)
# 思路 : 一边读取一个文件的内容, 然后将其写入一个新的文件中
# 输入文件名字
# filename = input("File:")
# try:
#     # 二进制打开
#     fr = open(filename,'rb')
# except FileNotFoundError as e:
#     print(e)
# else:
#     # 二进制写入
#     fw = open('mv.jpg','wb')
#     # 循环读取 一边读一边写
#     while True:
#         data = fr.read(1024)
#         if not data: # 文件结束
#             break
#         fw.write(data)
#
#     fr.close()
#     fw.close()
#---------------------------------------------------------------------
# 缓冲刷新条件
# 1.缓冲满了  2. 行缓冲换行会自动更新
# 3. 程序运行结束或者文件close
# 4. 调用flush
# 制定缓冲大小
# f = open("test.txt",'wb',5) # 设置缓冲区大小
# while True:
#     info = input(">>")
#     if not info:
#         break
#     f.write(info.encode())
# f.close()


f = open("test.txt",'w')
while True:
    info = input(">>")
    if not info:
        break
    f.write(info)
    f.flush()   # 刷新缓冲

f.close()








