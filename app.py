from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>Flask er flottast</h1><a href="/sida1">Siða 1</a>'
    
    
@app.route('/sida1')
def sida1():
	return '<h1>Síða 1</h1><a href="/">Heim</a>'

if __name__ == "__main__":
	app.run(debug=True)