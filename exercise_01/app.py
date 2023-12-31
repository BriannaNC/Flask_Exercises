from flask import Flask, render_template
import datetime

app= Flask(__name__)

@app.route("/")
def index():
    current_time = datetime.datetime.now().strftime("%A, %B %d, %H:%M:%S")
    return render_template('index.html', current_time=current_time)

if __name__=='__main__':
    app.run(debug=True)
