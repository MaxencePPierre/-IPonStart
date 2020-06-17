from flask import Flask, render_template, escape, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
	#name = request.args.get("name", "World")
	return render_template('menu.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
