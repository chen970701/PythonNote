import os
print("getcwd:"+os.getcwd())  #获取工作目录
print("abspath"+os.path.abspath("."))
myPath=os.path.join(os.getcwd(),"第一个文件夹","子文件夹")
# os.chdir(myPath)
# print("getcwd:"+os.getcwd())  #获取工作目录
# print("abspath"+os.path.abspath(".")) #会跟着改到工作目录
#os.makedirs(myPath)

# print(os.path.isabs("/aa/b")) #True
# print(os.path.isabs("./aa/b")) #False
def getFolderSize(folderPath):
    if os.path.exists(folderPath)==False:
        print("can found {0}".format(folderPath))
        return -1
    if os.path.isdir(folderPath)==False:
        print("this is not a folder")
        return -1
    folderSize=0
    pathList=os.listdir(folderPath)
    for fileName in pathList:
        filePath=os.path.join(folderPath,fileName)
        if os.path.isfile(filePath):
            folderSize+=os.path.getsize(filePath)
        elif os.path.isdir(filePath):
            folderSize+=getFolderSize(filePath)
    return folderSize
print(getFolderSize(os.getcwd()))
print(getFolderSize(os.path.join(os.getcwd(),"testSize")))
print(getFolderSize("ab"))
