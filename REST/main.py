from flask import Flask
#, request
from flask_restful import Resource, Api
#, abort, reqparse

# this wraps our app in an api and this initializes a restful api
app = Flask(__name__)
api = Api(app)


# this starts both the server and the application
# debug=True says that we are in debug mode so we will see all of that output and any logging information, so if we have a bug it will tell us why
if __name__ == "__main__":
    app.run(debug=True)