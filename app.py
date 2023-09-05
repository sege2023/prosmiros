from flask import Flask,render_template,request
import geopoint

app = Flask(__name__)

@app.route("/",methods = ["POST","GET"])
def caldistance():
    if request.method == "POST":
        coordA = request.form.get("coordA")
        coordB = request.form.get("coordB")
        lat1 = float(coordA.replace(" ","").split(",")[0])
        lon1 = float(coordA.replace(" ","").split(",")[1])
        lat2 = float(coordB.replace(" ","").split(",")[1])
        lon2 = float(coordB.replace(" ","").split(",")[1])
        # print(coordA,coordB)
        # print("hello")
        result = geopoint.haversine_distance(lat1,lon1,lat2,lon2)
        return render_template("home.html",answer = result )
    else:
        return render_template("home.html")

if __name__ =="__main__":
    app.run(debug = True)