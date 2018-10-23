#--------Flask Hello World-----------#

from flask import Flask

app = Flask(__name__)

app.config['DEBUG'] = True


@app.route('/test/<search_query>')
def search(search_query):
	return search_query

@app.route('/integer/<int:value>')
def int_type(value):
	print(value+1)
	return 'correct'

@app.route('/float/<float:value>')
def float_type(value):
	print(value+1)
	return 'correct'

@app.route('/path/<path:value>')
def path_type(value):
	print(value)
	return 'corret'

@app.route('/name/<name>')
def index(name):
	if name.lower() == 'michael':
		return f'Hello, {name}',200
	else:
		return f'Hello, {name}', 200


@app.route('/hello')
def hello_world():
	return('Hello, World!?!?')

if __name__=='__main__':
	app.run()