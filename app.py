import mvc
from flask import Flask
from routes import routes

app = Flask(__name__)

app.config.from_object(__name__)
mvc.register(routes, app)

if __name__ == '__main__':
	app.run(debug=True)