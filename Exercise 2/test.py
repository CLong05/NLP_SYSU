import xlrd
# 引入 word2vec
from gensim.models import word2vec
# 引入日志配置
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# 读取数据
data = xlrd.open_workbook('jieba_res.xls')
table = data.sheet_by_name('data')
url = table.cell_value(1,0)
title = table.cell_value(1,1)
content = table.cell_value(1,2)

# 处理句子，切分词汇
title += '。'
content = title+content
sentences=content.split('。')
p={'',' ','.','。','，','《','》','—','-','（','、','）','"','“','”','”'}
for i in range(len(sentences)):
    sentences[i]=sentences[i].split('/')
    for j in sentences[i]:
        if  j in p:
            sentences[i].remove(j)
# 构建模型
model = word2vec.Word2Vec(sentences, min_count=20,vector_size=100)
# 保存模型
model.save('model')
# 加载模型
model = word2vec.Word2Vec.load('model')

# 存储词向量
model.save("./url_word.model")
model.wv.save_word2vec_format("./url_wor2vec.txt")

# 查找与‘中国’接近的词并储存
with open("similar.txt","a") as f:
    for val in model.wv.similar_by_word("中国", topn=10):
        print(val[0], val[1])
        f.write(f"{val[0]}\t: {val[1]}\n")
        pass
