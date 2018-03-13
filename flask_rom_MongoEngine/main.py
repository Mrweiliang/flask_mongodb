# -*- coding: utf-8 -*-

import time
from flask import Flask
from flask import render_template,request


app=Flask(__name__)
from models import Users


@app.route('/')
def index():
	# return "Hello World"
	return render_template('index.html')


#注册方法
@app.route('/zhuce',methods=['POST'])
def zhuce():
	if request.method == 'POST':
		u = Users()  #插库的时候,需要将插入的内容,插到这里面
		list = ['uname','pwd','email','tel']
		for item in list:
			u[item]=request.form.get(item)
		updtime = time.strftime('%Y-%m-%d %H:%M:%S')    #将时间转换成整体显示
		# updtime = time.time()
		u.updtime = updtime
		u.createtime = updtime
		try:   #例外捕获
			u.save() #存入数据
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

#登录方法
@app.route('/login',methods=['POST'])
def login():
	if request.method == 'POST':
			uname=request.form.get('uname')  #前端页面提交上来的值,准备进行查库操作
			pwd = request.form.get('pwd')
			u = Users.objects(uname=uname,pwd=pwd).first() #将查询到的信息给u,如果有或者没有
			if u!=None:
				return '登录成功'
			else:
				return '账号/密码错误'


if __name__ == '__main__':
	app.run(debug=True) #如果你启用了调试支持，服务器会在代码修改后自动重新载入，并在发生错误时提供一个相当有用的调试器。   (port=80,改端口号,80为默认端口,浏览器打开时不输入端口,默认为80)