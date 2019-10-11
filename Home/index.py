from flask import Flask,redirect,url_for,request,render_template,Response
from Admin.model.MongoTool import MongoTool
app=Flask(__name__)

@app.route('/test')
def helle():
    return 'hello world'

@app.route('/')
def index():
	return render_template("index.html")

@app.route("/listsubBykey", methods=["post"])
def listsubjectByKey():
	serachkey=request.form.get('searchkey')
	mongodb=MongoTool()
	print("serachkey %s" % serachkey)
	data=mongodb.selectByTitle(serachkey)
	print(data)
	return render_template('search_detail.html', data=data)

if __name__=='__main__':
    app.run(debug=True)