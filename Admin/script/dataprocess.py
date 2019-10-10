import sys,re
sys.path.append(r"E:\PythonPro\LawLib\Admin\model") 

from MongoTool import MongoTool


def isNormalFileHead(line):
    # if re.match(r'^\s*第|^\s*\(.*\)',line)!=None:
    if re.match(r'^\s*第',line)!=None:
        valid=True
    else:
        valid=False
    return valid

def isFileHead(line):
    if re.match(r'^\s*[一,二,三,四,五,六,七,八,九,十]',line)!=None:
        valid=True
    else:
        valid=False
    return valid

def categorizeFile(data):
    # 文件种类
    normalFile=0
    capitalFile=0
    other=0
    for line in data:
        if isNormalFileHead(line):
            normalFile+=1
        elif isFileHead(line):
            capitalFile+=1
        else:
            other+=1
    if normalFile>capitalFile:
        return 0
    elif capitalFile>normalFile:
        return 1
    else:
        return 3



def processViewMode():
    db=MongoTool()
    datasub=db.selectData('lawsubject')
  
    for sub in datasub:
        data=db.selectColOfKey('lawcontent','lawid',sub['lawid'])    
        # print(type(data))
        contents=[]
        for item in data:
            contents.append(item['content'])
        flag=categorizeFile(contents)

        db.update_viewmode(sub['lawid'],flag)
    return True


if __name__ == "__main__":
    processViewMode()