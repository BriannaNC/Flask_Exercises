from flask import Flask, render_template, request,redirect,url_for

app=Flask(__name__)

user_data={}

std_orgs=["Art Club","Theatre","Sports","Video Games","Idk..."]

@app.route("/",methods=["GET","POST"])
def register():
    if request.method=="POST":
        name= request.form.get("name")
        org= request.form.get("org")

        if not name or not org:
            return render_template("register.html",std_orgs=std_orgs, error= "Both name and org required")
        if org not in std_orgs:
            return render_template("register.html",std_orgs=std_orgs,error="Invalid org")
        
        user_data[name]= org
        return redirect(url_for("users"))
    
    return render_template("register.html",std_orgs=std_orgs)
@app.route("/users")
def users():
    return render_template("users.html",users=user_data)
if __name__=="__main__":
    app.run(debug=True)