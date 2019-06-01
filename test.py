# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals

text = '''
将MOOC应用到传统课堂教学
随着大规模网络公开课的发展，教师可以考虑把在线教育的方法应用到自己的课堂教学中。MOOC的课程制作涉及比较复杂的技术，但使用这些课程几乎不费吹灰之力，而且成本也远远不及课程制作。没有加入edX或Coursera的大部分学校可以进行更多自创内容的尝试，就像自出版一样，这也是许多cMOOC的尝试。教师也可以向自己的目标努力。通过打开课堂，建立网络社区和制作教学视频，可以让更多的教师和学生享受到MOOC的投入带来的收益。
'''


from snownlp import normal
from snownlp import seg
from snownlp import SnowNLP
from snownlp.summary import textrank
import matplotlib.pyplot as plt
import numpy as np
import sys
import xlrd

# if __name__ == '__main__':
#     t = normal.zh2hans(text)
#     sents = normal.get_sentences(t)
#     doc = []
#     for sent in sents:
#         words = seg.seg(sent)
#         words = normal.filter_stop(words)
#         doc.append(words)
#     rank = textrank.TextRank(doc)
#     rank.solve()
#     for index in rank.top_index(5):
#         print(sents[index])
#     keyword_rank = textrank.KeywordTextRank(doc)
#     keyword_rank.solve()
#     for w in keyword_rank.top_index(5):
#         print(w)
sentimentslist=[]
data =xlrd.open_workbook('MOBICK.xlsx')
table=data.sheets()[0]
nrows=table.nrows
for i in range(nrows):
    str="".join('%s' % id for id in table.row_values(i))
    s = SnowNLP(str)
    print(table.row_values(i),s.sentiments)
    sentimentslist.append(s.sentiments)
fileObject = open('MOBICK.txt', 'w+')
for ip in sentimentslist:
    fileObject.write(__builtins__.str(ip))
    fileObject.write('\n')
fileObject.close()
fig1=plt.figure("sentiment")
plt.hist(sentimentslist,bins=np.arange(0,1,0.02))
plt.show()