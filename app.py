from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>Flask er flottast</h1>   <a href="/sida1">Síða 1</a></h1>   <a href="/sida2">Síða 2</a>'
    
    
    
@app.route('/sida1')
def sida1():
	return '<h1>Síða 1</h1><a href="/">Heim</a> <a href="/sida2">Síða 2</a>'
    
@app.route('/sida2')
def sida2():
	return '<h1>Síða 2</h1><a href="/">Heim</a>  <a href="/sida1">Síða 1</a>'

if __name__ == "__main__":
	app.run(debug=True)