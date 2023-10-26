from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin 

application = Flask(__name__) # initializing a flask app
app=application 

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html") 



if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)