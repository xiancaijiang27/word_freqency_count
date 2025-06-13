# python love xiancai,xiancai is a femle,which want to be pretty pretty beautiful
"""
xiancai的恋爱观(求对象ing)
只要不是太丑都可以接受，也不卡学历。
我更在意一个人的精神状态，希望你是一个比较乐观、不太容易陷入抱怨情绪的人。
我喜欢能互相分享日常、听我唠叨的人。同理，我也愿意倾听你的烦恼。
如果长期异地，我们可以不用天天聊天，但希望看到对方的消息都能尽量在一天内回复，不忽略彼此。
希望我们都能专一认真地对待这段感情，可以保有个人的小空间，但不脚踏多条船。
我如果爱一个人，就会很认真，希望你也一样。
你不需要赚很多钱，但希望你能有一份自己的工作，至少养得起自己。(虽然目前还是大学生，但是已经在努力了qwq)
约会吃饭可以互相请客，我也希望我们是平等的恋爱关系。
希望你把我当成女孩子而不是男朋友，尽管我是跨性别女生。
"""
# 新列表=[处理后的元素 for 每个元素 in 原列表 if 满足条件]         用来生成新列表
# 变量.get(元素a,0)+1                                       get(元素,0)表示若 元素 已经存在，返回当前次数;否则返回0;而+1实现对元素的统计
# for word, count in 变量.items():                         依次取出字典中的每一对key和value并赋值给目标变量
# 变量.items():                                            把{'a':3,'b':1}转换成[('a':3),('b':1)]
# sorted(容器,key=函数lambda,reverse=True)
# lambda x: x[1]                                          排序元组;这里的x只是一个临时变量,后续不会使用;lambda的处理对象由sorted依次传入
# 等价于:
# def func(x):
#    return x[1]

# clean_words=[word.strip() for word in words if word.strip() != ''] 等价于:
# clean_words=list()
# for word in words:
#     if word.strip() != '':
#         clean_words.append(word.strip())

# word_count[word]=word_count.get(word,0)+1 等价于:
# if word in word_count:
#     word_count[word]+=1
# else:
#     word_count[word]=1

#需要提前在PyCharm里的Terminal(Alt+F12)安装jieba,输入:pip install jieba
import sys
import string
import jieba

print(f"请输入中文或英文文本(输入 Ctrl+D 结束):")
text=sys.stdin.read()
new_text=text #如果不希望text数据丢失
punctuation=string.punctuation+'·~@#￥%&*（）——-+={}|：“”《》？【】、；‘’，。/' #string.punctuation是字符串
for i in punctuation:
    new_text=new_text.replace(i,' ')
words=new_text.split(' ')
words=jieba.lcut(new_text)
clean_words=[word.strip() for word in words if word.strip() != ''] #去除空字符串
new_words=set(clean_words)
word_count=dict()
for word in clean_words:
    word_count[word]=word_count.get(word,0)+1 #统计次数并放在字典的value里
print("----------词频统计(按ASCII码表)----------")
for word in sorted(word_count.keys()):
    print(f"{word}:{word_count[word]}")
print()
print("-----------词频统计(按频率排序)-----------")
sorted_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
for word, count in sorted_count:
    print(f"{word}: {count}")



