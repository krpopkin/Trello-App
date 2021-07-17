##############################################################################################################################
# Render the run status reports (index.html) form, populating the "select project" dropdown with the Trello boards the user
# has access to.  Then submit the selected project or "all projects" back to the Trello App to produce the status reports.
##############################################################################################################################

# Helpful links:
# https://csveda.com/fill-a-dropdown-combo-in-flask-and-postgresql/

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# default page that will be used for additional development


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
