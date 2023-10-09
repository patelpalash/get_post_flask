from flask import Flask , redirect,url_for,render_template,request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login",methods=["POST","GET"])
def login():
    if request.method=="POST":
        user = request.form["nm"]
        value = request.form["vl"]

        return redirect(url_for("user",usr=user,val=value))
       
    
    else:
        return render_template("login.html")
    
@app.route("/<usr>/<val>")
def user(usr,val):
    return f"<h1>User: {usr}</h1><h1>Value: {val}</h1>"   

if __name__=="__main__":
    app.run(debug=True)