from flask import Flask, render_template
app = Flask(__name__) # creating app variable __name__ is the name of the module == __main__

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html')


@app.route("/about")
def about():
	return render_template('about.html')


if __name__ == '__main__': # true if we run the script directly
	app.run(debug=True)