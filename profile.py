from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/about")
def about():
	return render_template("about.html",
		title = "About Me")

@app.route("/skills")
def skills():
	skills = {
		'Platforms' : ['IBM Mainframe - z/OS/MVS', 'Windows', 'Mac OS', 'Linux'],
		'Databases' : ['IMS', 'DB2', 'Teradata', 'MySql'],
		'Languages' : ['Python', 'HTML/CSS', 'SAS', 'REXX', 'COBOL']
	}
	return render_template("skills.html",
		title = "Skills",
		skills = skills)

@app.route("/contact")
def contact():
	return render_template("contact.html",
		title = "Contact Me")

if __name__ == '__main__':
	app.run(debug=True)