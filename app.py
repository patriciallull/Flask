import flask
import sys
import argparse
import sklearn
from flask import Flask, request, abort
from ie_nlp_utils.tokenisation import tokenise as tokenise_sentence

app = Flask(__name__)

# FOURTH FUNCTION - using the tokenise function that was created for the exercise
# @app.route("/tokenise")
# def tokenise():
#     args = dict(request.args)  # store the Arguments
#     if sentence := args.get("sentence"):
#         return {
#             "tokens": tokenise_sentence(sentence),
#             "sentence": sentence,
#         }
#     else:
#         abort(400)

# THIRD function - example:
@app.route("/greet/<name>")
def greet(name):
    return f"Howdy, {name}!"


# SECOND FUNCTION - return dict; listens on the /api url
@app.route("/api/<int:version>")
def api(version):
    args = dict(request.args)
    return {
        "python-version": sys.version[0:5],
        "status": "OK",
        "name": args.get("name", "<NOT GIVEN>"),
        "version": version,
        "scikit-learn-version": sklearn.__version__,
        "flask-version": flask.__version__,
    }


# FIRST FUNCTION - returns text
@app.route("/")
def hello():
    args = dict(request.args)
    if name := args.get("name"):
        return f"Hello, {name}!"
    # to introduce an error for the debugger: 'name_' instead of 'name'
    else:
        return f"Hello World!"


# to run from command line & add a parameter to turn debugger on:
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sample Flask application")
    parser.add_argument("-v", "--debug", action="store_true", help="Enable debug mode")
    args = parser.parse_args()
    app.run(debug=args.debug)
