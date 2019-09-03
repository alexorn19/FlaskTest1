from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>Flask er flottast</h1><a href="/sida1">Siða 1</a>'
    return '<h1>Síða 2</h1><a href="/">Síða 2</a>'
    
    
@app.route('/sida1')
def sida1():
	return '<h1>Síða 1</h1><a href="/">Heim</a>'
    return '<h1>Síða 2</h1><a href="/">Síða 2</a>'
    
@app.route('/sida2')
def sida2():
	return '<h1>Síða 2</h1><a href="/">Heim</a>'
    return '<h1>Síða 1</h1><a href="/">Síða 1</a>'

if __name__ == "__main__":
	app.run(debug=True)