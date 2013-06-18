from flask import request, render_template, redirect, url_for
from mvc import *
from models.item import Item

def index():
	return "Hello, World!"

def item(name=None):
	return "Item: <strong>%s</strong>" % name

@get
@post
@marshall(Item)
def create(item=None):
	if request.method == "POST":
		print item.name, item.value
		redirect(url_for('index'))
	return render_template("create.html")