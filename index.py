# import flask
from flask import Flask, render_template, url_for, request
from math import sin,cos,tan,sqrt

# object
app = Flask(__name__)



# route == link == url

# main route
@app.route("/")

def main():
    return render_template("index.html")

@app.route("/simple")
def simple():
    return render_template("simple.html")

@app.route("/advanced")
def advanced():
    return render_template("advanced.html")

@app.route("/calculate", methods=["post"])
def calculate():
    first_number = int(request.form["firstNumber"])
    operation = request.form["operation"]
    second_number = int(request.form["secondNumber"])
    note = ''
    color = "alert-success"
    if operation == "plus":
        result = first_number + second_number
        note = "Addition was perfomed successfully"
    elif operation == "minus":
        result = first_number - second_number
        note = "Sutraction was perfomed successfully"
    elif operation == "multiply":
        result = first_number * second_number
        note = "Multiplication was perfomed successfully"
    elif operation == "divide":
        result = first_number / second_number
        note = "Division was perfomed successfully"
    else:
        note = 'There is an error'
        color = "alert-warning"
        return render_template("simple.html", note=note, color=color)
        
    return render_template("simple.html", result=result, note = note, color = color)

@app.route("/calculate_advanced", methods = ["post"])
def calculate_advanced():
    first_number = int(request.form["firstNumber"])
    operation = request.form["operation"]
    note = ''
    color = "alert-success"
    if operation == "sin":
        result = sin(first_number)
        note = "Sin was perfomed successfully"
    elif operation == "cos":
        result = cos(first_number)
        note = "Cosin was perfomed successfully"
    elif operation == "tan":
        result = tan(first_number)
        note = "Tan was perfomed successfully"
    elif operation == "sqr":
        result = sqrt(first_number)
        note = "Square root was perfomed successfully"
    else:
        note = 'There is an error'
        color = "alert-warning"
        return render_template("advanced.html", note=note, color=color)
        
    return render_template("advanced.html", result=result, note = note, color = color)

    






















# to run application
if __name__ == "__main__":
    app.run(debug=True)
    # false because you dont want people to see the error message
    # true because we want to see the error message and fix our code