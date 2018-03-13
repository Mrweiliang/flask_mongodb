# -*- coding: utf-8 -*-

from flask import Flask
from flask_mongoengine import MongoEngine
app=Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
	'db':'figer',
	'host':'localhost',
	'port':27017
}

#创建mongo原型
mdb = MongoEngine()
mdb.init_app(app)

#类名定义 collection
class Users(mdb.Document):
		_id = mdb.ObjectIdField()
		uname = mdb.StringField()
		pwd = mdb.StringField()
		email = mdb.StringField()
		tel = mdb.StringField()
		updtime = mdb.StringField()
		createtime = mdb.StringField()  #FloatField 浮点类型

