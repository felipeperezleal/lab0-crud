from flask import Flask, render_template
import os
import database as db

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
#Connecting Flask app with index.html
template_dir = os.path.join(template_dir, 'src', 'templates')

app = Flask(__name__, template_folder=template_dir)

#App routes
@app.route('/')
def home():

    return render_template('index.html')



#Launching the app
if __name__ == '__main__':
    app.run(debug=True)