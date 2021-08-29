import jieba
import wordcloud
import imageio 
file1=open("./词云文档.txt","r",encoding="utf-8")
mask=imageio.imread("rocket.jpg")
words=file1.read()
file1.close()
afterWords=jieba.lcut(words,cut_all=False)

wc=wordcloud.WordCloud(font_path="msyh.ttc",width=500,height=800,mask=mask).generate(" ".join(afterWords))
wc.to_file("词云.jpg")

