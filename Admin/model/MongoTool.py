from pymongo import MongoClient
import re,sys

SERVER_IP='127.0.0.1'
PORT=27017
DBNAME="lawdb"


def isEdit(line):
    if re.match(r'^\s*第[一,二,三,四,五,六,七,八,九,十]\s*[编,章,节]',line)!=None:
        valid=True
    else:
        valid=False
    return valid
def ishead(line):
    if re.match(r'^\s*第*[一,二,三,四,五,六,七,八,九,十,\
        (一),(二),(三),(四),(五),(六),(七),(八),(九)]\s*',line)!=None:
        valid=True
    else:
        valid=False
    return valid

class MongoTool:
    def __init__(self):
        self.conn = MongoClient(SERVER_IP, PORT)
        self.__selDB(DBNAME)
       
    def __selDB(self,dbname):
        self.db=self.conn[dbname]

    def insertData(self,colname,data):
        self.colname=self.db[colname]
        self.colname.insert(data)

    def selectData(self,colname):
        self.colname=self.db[colname]
        data=[]
        for item in self.colname.find():
            item.pop("_id")
            data.append(item)
        return data
            # for key in item:

    def selectDatabyKey(self,colname,lawid,id):
        self.colname=self.db[colname]
        query={"lawid":lawid,"id":id}
        item =self.colname.find_one(query)
        return item

    def selectColOfKey(self,colname,key,uuid):
        data=[]
        self.colname=self.db[colname]
        for item in self.colname.find({key:uuid}):
            item.pop("_id")
            #正则添加显示字段
            # print(item['content'])
            data.append(item)
        return data

    def filterData(self,colname,key,uuid):

        data=[]
        self.colname=self.db[colname]
        for item in self.colname.find({key:uuid}):
            item.pop("_id")
            #正则添加显示字段
            # print(item['content'])
            if isEdit(item['content']) or ishead(item['content'])!=1:
                item['isedit']=0
            else:
                item['isedit']=1
            data.append(item)
           
        return data
        # 更新标签状态   
    def update_viewmode(self,lawid,flag):
        # try:
  
        self.colname=self.db['lawsubject']
        query={"lawid":lawid}
        # print(query)
        value={"$set":{'viewmode':flag}}
        self.colname.update_one(query, value)
        return True

    # 更新标签状态   
    def update_isedit(self,key,value):
        # try:
        uuid,id=key.split('+')
        print(uuid,id)
        self.colname=self.db['lawcontent']
        query={"lawid":uuid,"id":int(id)}
        # print(query)
        value={"$set":{'isedit':value}}
        self.colname.update_one(query, value)
        return True

    def update_state(self,key,value):
        uuid,id=key.split('+')
        self.colname=self.db['lawcontent']
        query={"lawid":uuid,"id":int(id)}
        # print(query)
        value={"$set":{'state':value}}
        self.colname.update_one(query, value)
        return True
   

    def selectCntBykey(self,title,lawnum,textno,lawtype):
        self.colname=self.db['lawsubject']
        lawids=[]
        result=[]
        # print("model function")
        # print(lawtype)
        # print(title)
        # find({"title":{'$regex': '刑法'},"lawtype":"刑法"}):
        for item in self.colname.find({"title":{'$regex': title},"lawtype":lawtype}):
            item.pop("_id")
            lawids.append(item)
        print("###########")
        print(lawids)
        lawNo=
        for lawid in lawids:
            self.colname=self.db['lawcontent'] 
            # print(lawid)
            # print(lawnum)
            id=self.colname.find_one({"lawid":lawid["lawid"],"content":{'$regex': '^'+lawnum}},{"id":1})
            # print(id["id"])
            realid=id["id"]+int(textno)
            data=self.colname.find_one({"lawid":item["lawid"],"id":realid})
            data.pop("_id")
            data["title"]=lawid["title"]
           
            result.append(data)
        print(result)
        return result
       

    # //搜索标题，法条
    def selectByTitle(self,searchkey):
        print("inner %s" %searchkey)
        self.colname=self.db['lawsubject']
        result=[]
        for item in self.colname.find({"title":{'$regex': searchkey}}):
            item.pop("_id")
            result.append(item)
        # print("###########")
        print(result)    
        return result
    
    def addflag(self,flagname,flagtype):
        # insertData(self,colname,data):
        try:
            data={"flagname":flagname,"flagtype":flagtype}
            self.insertData("lawflag",data)
            return True
        except:
            return False

    def listFlag(self):
        try:
            data=self.selectData("lawflag")
            return data
        except:
            return None

    def addcontentFlag(self,contentid,flags):
        lawid,id=contentid.split('+')
        # print(lawid,id)
        self.colname=self.db['lawcontent']
        query={"lawid":lawid,"id":int(id)}
        # print(flags)
        value={"$set":{'flag':flags}}
        self.colname.update_one(query, value)
        return True


    def upd_sub_state(self,lawid,value,lawtype):
        self.colname=self.db['lawsubject']
        query={"lawid":lawid}
        # print(flags)
        value={"$set":{'isvalid':value,'type':lawtype}}
        self.colname.update_one(query, value)
        return True



    def addrel(self,remoteid,localid):
        # insertData(self,colname,data):
        # f5a07c6c-01f1-11e9-8dd0-2c337a197212+257"yuan myjs.js:191:17
        # ed17bce4-01f8-11e9-9a79-2c337a197212+2dest
        # data={"remotremid":remoteid,"localid":localid}
        # selectColOfKey(self,colname,key,uuid):
        remote_lawid,remote_id=remoteid.split('+')
        local_lawid,local_id=localid.split('+')
        print(local_lawid)
        print(type(local_lawid))
        self.colname=self.db['lawcontent']
        data=self.selectDatabyKey('lawcontent',local_lawid,int(local_id))
        try:
            query={"lawid":remote_lawid,"id":int(remote_id)}
            print(query)
            value={"$push" :{"relation":{"lawid":local_lawid,"id":int(local_id),'content':data['content'],"author":"用户","edittime":"2019-08-18"}}}
            # value={"$push":{"test": {"id":1,"name":'aa'} }}       
            self.colname.update(query,value)
            return True
        except:
            print(sys.exc_info()[0])
            return False
    
  

def testfind():
    conn = MongoClient(SERVER_IP, PORT)
    mydb=conn[DBNAME]
    mycol = mydb["lawsubject"]
    # for x in mycol.find({"title":"中华人民共和国刑法"}):
    for x in mycol.find({"title":{'$regex': '刑法'},"lawtype":"刑法"}):
        print(x["lawid"])




if __name__ == "__main__":
    mongodb=MongoTool()
    # flag=mongodb.addrel('f5a07c6c-01f1-11e9-8dd0-2c337a197212+4','ed17bce4-01f8-11e9-9a79-2c337a197212+2')
    # print(flag)
    # mongodb.selectDatabyKey('lawcontent','ed17bce4-01f8-11e9-9a79-2c337a197212',2)
    # # data=mongodb.filterData('lawcontent','lawid','f5a07c6c-01f1-11e9-8dd0-2c337a197212')
    # # print(data)
    # # description=mongodb.selectColOfKey("lawsubject","lawid","f5a07c6c-01f1-11e9-8dd0-2c337a197212")
    # # print(description)
    # # testlist()
    # # print(ishead("(二) 未经执行机关批准，不得行使言论、出版、集会、结社、游行、示威自由的权利"))
    # flag=mongodb.update_isedit('f5a07c6c-01f1-11e9-8dd0-2c337a197212+1',1)
    # print(flag)
    # testfind()
    # param={"title":"刑法","id":"1","lawtype":"法律"}
    # # mongodb.selectByTitle(param)
    # # title,lawnum,textno,lawtype
    # mongodb.selectCntBykey("刑法",'第三十三条',2,"法律")
    # mongodb.addflag("财产","离婚")
    # mongodb.listFlag()
    mongodb.selectByTitle('刑法')
    pass