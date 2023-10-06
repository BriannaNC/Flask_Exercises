from flask import Flask, request, render_template, url_for

app=Flask(__name__)
@app.route("/", methods=["GET","POST"])
@app.route("/input",methods=["GET","POST"])
def home():
    if request.method == "POST":
        num = request.form.get("number")
        if num == "":
            message="No number provided!"
        else:
            try:
                number= int(num)
                if number % 2 ==0:
                    message= f"{number} is an even number!"
                else:
                    message= f"{number} is an odd number!"
            except (ValueError,TypeError):
                message= f"{num} is not an integer!"
        return render_template("result.html",message=message)
    return render_template("input.html")

if __name__=="__main__":
    app.run(debug=True)

