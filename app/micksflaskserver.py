import flask
import json

# Instantiate the Flask object with the __name__ provided as input.
# You'll be using this object to communicate with the Flask Framework.
app = flask.Flask(__name__)

# Defines the function that will be run when you try to send a GET request.
@app.route('/')
def sendback_landing_page():
	return flask.render_template('landingpage.html')

@app.route('/json/')
def sendback_json():
	json_obj = json.dumps({"FirstName":"Mukund","LastName":"Chandra","Text":"I welcome you to this place"})
	return json_obj

@app.route('/submitrequest/')
def sample_form1():
	return flask.render_template('testinputpage.html')

@app.route('/postrequesttest/',methods=['POST'])
def get_posted_data():
	if flask.request.method == 'POST':
		check1 = flask.request.form.get('CheckboxTest1')
		text1 = flask.request.form.get('TextboxTest1')
		print(check1,text1)
		json_obj = json.dumps({"Checkbox":check1,"Text":text1})
		return json_obj


if __name__ == "__main__":
	# app.run() starts the Flask app, you need to call this function to start it.
	# It will most likely by running on http://127.0.0.1:5000/
	app.run()
