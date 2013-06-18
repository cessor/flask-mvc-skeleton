from controllers import home

routes = [
	("/", home.index),
	("/item/<name>", home.item),
	("/create", home.create),
]