from flask import Flask, render_template, url_for

app = Flask(__name__)
student_details = {
                        "Naeemah": 25,
                        "godwin": 26,
                        "Thapelo": 47,
                        "Vuyani": 23
                    }

# ADD A ROUTE DECORATOR TO TELL FLASK WHICH URL TO TRIGGER
@app.route("/<name>")
@app.route("/home/<name>")
def home(name, number):
    return render_template("home.html", name="VuyaniK", number=number)


@app.route("/times/<int:number>")
def times(number):
    return render_template("home.html", number=number, student_details=student_details)


@app.route("/number/<int:number>")
def number(number):
    return render_template("numbers.html", number=number)


if __name__ == "__main__":
    app.run(debug=True)