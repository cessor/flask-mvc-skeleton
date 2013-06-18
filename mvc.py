from importlib import import_module
from flask import request
modules = []

def append_method(function, method):
	methods = getattr(function, 'methods', None)
	if methods is None:
		function.methods = []
	function.methods.append(method.upper())
	return function

def bind(dict, obj):
	for key,value in dict.items():
		setattr(obj, key, value)
	return obj

def marshall(_type):
	def decorator(function):
		def wrapper(*args,**kwargs):
			parameter = _type()
			parameter = bind(request.form, parameter)
			result = function(parameter)
			return result
		return wrapper
	return decorator

def get(function):
	return append_method(function, get.__name__)

def post(function):
	return append_method(function, post.__name__)

def put(function):
	return append_method(function, put.__name__)

def delete(function):
	return append_method(function, delete.__name__)

def options(function):
	return append_method(function, options.__name__)

def register(routes, app):
	for route in routes:
		path = route[0]
		function = route[1]
		name = function.__name__
		app.add_url_rule(path, name, function)