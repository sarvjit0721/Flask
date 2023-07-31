from flask import Flask
from flask import request

app=Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1> Hello, Python </h1>"

@app.route("/test")
def hello_test():
    data=request.args.get('x')
    return "This is input:{}".format(data)


if __name__=='__main__':
    app.run(host="0.0.0.0")