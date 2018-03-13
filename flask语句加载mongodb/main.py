# -*- coding: utf-8 -*-

import time
from flask import Flask
from flask import render_template,request
from pymongo import MongoClient
client = MongoClient('localhost',27017)
db=client.figer       #库名

app=Flask(__name__)
@app.route('/')
def index():
	# return "Hello World"
	return render_template('index.html')
	
@app.route('/zhuce',methods=['GET','POST'])
def zhuce():
	if request.method == 'POST':
		uname = request.form.get('uname')
		pwd = request.form.get('pwd')
		email = request.form.get('email')
		tel = request.form.get('tel')
		updtime = time.time()
		collection=db.users		#表名
		try:   #例外捕获
			collection.insert({'uname':uname,'pwd':pwd,'email':email,'tel':tel,'updtime':updtime,'createtime':updtime})
			return '插入成功'
		except Exception as err:
			estr = str(err)
			if estr.find('unameuiq')>0:
				return '用户名重复'
			elif estr.find('emailuiq')>0:
				return 'email重复'
			elif estr.find('teluiq')>0:
				return '电话号码重复'
			else:
				return '数据库异常'

if __name__ == '__main__':
	app.run(debug=True) #如果你启用了调试支持，服务器会在代码修改后自动重新载入，并在发生错误时提供一个相当有用的调试器。   (port=80,改端口号,80为默认端口,浏览器打开时不输入端口,默认为80)