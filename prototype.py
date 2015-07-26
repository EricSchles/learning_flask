#Lesson for lior
from flask import Flask,render_template,request,url_for,jsonify,redirect
import json
app = Flask(__name__)

#a test method
@app.route("/",methods=["GET","POST"])
def index():
    return "hello there" # we can pass strings to "routes"

#for redirect
@app.route("/new_page",methods=["GET","POST"])
def new_page():
    return "oooohhhh yea"

#api stuff, as easy as pi
@app.route("/api",methods=["POST"])
def api():
    thing = []
    dicter = {}
    dicter["name"] = "Eric"
    thing.append(dicter)
    dicter2 = {}
    dicter2["name"]="Lior"
    thing.append(dicter2)
    return json.dumps(thing)

#a method that actually renders some html
@app.route("/index",methods=["GET","POST"])
def index2():
    if request.method=="POST":
        name = request.form.get("name")
        return render_template("index",name=name) 
        #return redirect(url_for("new_page"))  #how to do redirects
    return render_template("index.html") #returns an html page, rendered with any jinja templating stuff

app.run(
    debug=True,#this will tell you if there are any errors with your code, remember to turn this off in production, it is a huge security vulnerability.
    port=5010,#by default is set to 5000
    host="0.0.0.0", #broadcast mode
    threaded=True #only use for production, otherwise your processes will never end
)
