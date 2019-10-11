from flask import Flask,redirect,url_for,request,render_template,Response
import os
import json
from model.MongoTool import MongoTool
from util import util


app=Flask(__name__)

@app.route('/test')
def helle():
    return 'hello world'


root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "html")#html是个文件夹


@app.route('/')
def index():
    return render_template("index.html")    



@app.route("/listsubject", methods=["post"])
def listsubject():
    mongodb=MongoTool()
    data=mongodb.selectData("lawsubject")

    return render_template('search_detail.html', data=data)

@app.route("/listsubBykey", methods=["post"])
def listsubjectByKey():
    # id="第"+util.dig_to_ch(request.form.get('id'))+"条"
    serachkey=request.form.get('searchkey')
    mongodb=MongoTool()
    print("serachkey %s" % serachkey)
    data=mongodb.selectByTitle(serachkey)
    print(data)
    # resp=Response(json.dumps(data))
    # resp.headers["Access-Control-Allow-Origin"] = "*"
    # print(data)
    return render_template('search_detail.html', data=data)


@app.route("/upd_subject_state", methods=["post"])
def upd_subject_state():
    # id="第"+util.dig_to_ch(request.form.get('id'))+"条"
    lawid=request.form.get("lawid")
    value=request.form.get("value")
    lawtype=request.form.get("lawtype")
    print(lawid)
    print(value)
    mongodb=MongoTool()
    flag=mongodb.upd_sub_state(lawid,value,lawtype)
    # resp=Response(json.dumps(data))
    # resp.headers["Access-Control-Allow-Origin"] = "*"
    # print(data)
    if flag:
        return "ok"
    else:
        return "errro"





@app.route("/listlawcontent/<lawid>", methods=["get","post"])
def listlawcontent(lawid):
    mongodb=MongoTool()

    description=mongodb.selectColOfKey("lawsubject","lawid",lawid)
    data=mongodb.selectColOfKey("lawcontent","lawid",lawid)
    # resp=Response(json.dumps(data))
    # resp.headers["Access-Control-Allow-Origin"] = "*"
    # print(data)
    # print(description['title'])
    # print(data[0])
    return render_template('view_content.html', data=data,desc=description)


# 通过标题关键字查询法条 "刑法",'第三十三条',2,"法律"
@app.route("/listcntByKey", methods=["post"])
def listcntByKey():
    # var data={"titlekey":titlekey,"textid":textid,"textchild_no":textchild_no}
    titlekey=request.form.get("titlekey")
    textidnum=request.form.get("textid")
    textid=util.dig_to_ch(int(textidnum))
    textchild_no=request.form.get("textchild_no")
    lawtype=request.form.get("lawtype")
    mongodb=MongoTool()
    result=mongodb.selectCntBykey(titlekey,textid,textchild_no,lawtype)
    return json.dumps(result)
 
    

# 编辑法条
@app.route("/upd_lawcontent_isedit", methods=["post"])
def upd_lawcontent_isedit():
    # data=str(request.get_data('data'),encoding="utf-8")
    # print(type(data))
    key=request.form.get('key')
    value=request.form.get('value')
    print(key,value)
    mongodb=MongoTool()
    flag=mongodb.update_isedit(key,value)
    if flag:
        return 'ok'
    else:
        return 'error'

@app.route("/listflag", methods=["get"])
def listflag():
    mongodb=MongoTool()
    data=mongodb.listFlag()
    return render_template('editflag.html',data=data)

@app.route("/listflagByKey", methods=["post"])
def listflag_data():
    mongodb=MongoTool()
    data=json.dumps(mongodb.listFlag())
 
    print(json.dumps(data))
    # return 'hh'
    return data


@app.route("/addflag", methods=["post"])
def addflag():
    # data=str(request.get_data('data'),encoding="utf-8")
    # print(type(data))
    flagname=request.form.get('flagname')
    flagtype=request.form.get('flagtype')
   
    mongodb=MongoTool()
    flag=mongodb.addflag(flagname,flagtype)
    if flag:
        return 'ok'
    else:
        return 'error'
@app.route("/addcontentflag", methods=["post"])
def addcontentflag():
    # data=str(request.get_data('data'),encoding="utf-8")
    # print(type(data))
    flags=request.form.get('flags').rstrip('|')
    contentid=request.form.get('contentid')
    # flagtype=request.form.get('flagtype')
    print('##########')
    print(flags)
    print(contentid)
    mongodb=MongoTool()
    flag=mongodb.addcontentFlag(contentid,flags)
    if flag:
        return 'ok'
    else:
        return 'error'

@app.route("/upd_lawcontent_state",methods=["post"])
def upd_lawcontent_state():
    # data=str(request.get_data('data'),encoding="utf-8")
    # print(type(data))
    dataid=request.form.get('dataid')
    value=request.form.get('value')
    # print(key,value)
    mongodb=MongoTool()
    flag=mongodb.update_state(dataid,value)
    if flag:
        return 'ok'
    else:
        return 'error'


@app.route("/addrel", methods=["post"])
def addrel():
    # data=str(request.get_data('data'),encoding="utf-8")
    # print(type(data))
    remoteid=request.form.get('remoteid')
    localid=request.form.get('localid')
    print(remoteid)
    print(localid)
    mongodb=MongoTool()
    flag=mongodb.addrel(remoteid,localid)
    if flag:
        return 'ok'
    else:
        return 'error'





if __name__=='__main__':
    app.run(debug=True)
