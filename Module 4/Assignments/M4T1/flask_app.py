from flask import Flask, request, render_template, session

from processing import do_calculation, calculate_mode

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = "YTitsIsOx1Rq2aEK47S6WBbKVvBXUgtv"

@app.route("/add", methods=("GET", "POST"))
def adder_page():
    errors = ""
    number1 = None
    number2 = None
    value1 = ""
    value2 = ""
    if request.method == "POST":
        try:
            number1 = float(request.form["number1"])
            value1 = str(number1)
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["number1"])
        try:
            number2 = float(request.form["number2"])
            value2 = str(number2)
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["number2"])
        if number1 is not None and number2 is not None:
            result = do_calculation(number1, number2)
            return render_template("calculation.html", result=result)

    return render_template("form.html",errors=errors,number1=value1,number2=value2)

@app.route("/mode", methods=("GET", "POST"))
def mode_page():
    if "inputs" not in session:
        session["inputs"] = []

    error = None
    number = ""
    if request.method == "POST":
        if request.form["action"] == "add":
            try:
                number = request.form["number"]
                session["inputs"].append(float(number))
                session.modified = True
            except:
                error = "<p>{!r} is not a number.</p>\n".format(number)
        elif request.form["action"] == "calculate":
            result = calculate_mode(session["inputs"])

            session["inputs"].clear()
            session.modified = True

            return render_template("mode_result.html", result=result)

    return render_template("mode.html", numbers=session["inputs"], number=number,errors=error)
