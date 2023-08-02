from flask import Flask,request,render_template,jsonify
from flask import request

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home_page():
    return render_template('index.html')

@app.route('/math',methods=['POST'])
def math_ops():
    operation=request.form['operation']
    num1=int(request.form['num1'])
    num2=int(request.form['num2'])
    if operation=='add':
        result=num1+num2
        addresult=f"Addition of {num1} and {num2} is: {result} "

    elif operation=='substract':
        result=abs(num1-num2)
        addresult=f"Substarction of {num1} and {num2} is: {result} "

    elif operation=='multiply':
        result=num1*num2
        addresult=f"Multiplication of {num1} and {num2} is: {result} "

    elif operation=='divide':
        result=num1/num2
        addresult=f"Division of {num1} and {num2} is: {result} "

    else:
        addresult=f"{operation} is either not arithmetic or its not supported"
    return render_template('results.html',result=addresult)
   

@app.route("/")
def hello_world():
    return "<h1> Hello, Python </h1>"

@app.route("/test")
def hello_test():
    data=request.args.get('x')
    return "This is input:{}".format(data)

@app.route("/loggin")
def hello_loggin():
    return "<h2>I am logged in<h2>"

if __name__=='__main__':
    app.run(host="0.0.0.0")