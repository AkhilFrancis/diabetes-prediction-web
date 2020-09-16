from flask import Flask,render_template,redirect,request

from sklearn.externals import joblib

app=Flask(__name__)
model=joblib.load("model.pkl")

@app.route('/')
def hello():
    return render_template("index.html")


@app.route('/',methods=['POST'])
def marks():
    if request.method=='POST':
        preg=float(request.form['preg'])
        glucose=float(request.form['glucose'])
        bp=float(request.form['bp'])
        skin=float(request.form['skin'])
        insulin=float(request.form['insulin'])
        bmi=float(request.form['bmi'])
        diabpedi=float(request.form['diabpedi'])
        age=float(request.form['age'])
        
        prediction=model.predict([[preg,glucose,bp,skin,insulin,bmi,diabpedi,age]])
        if(prediction==1):
            result="Person has Diabetes"
        elif(prediction==0):
            result="Person has no Diabetes"
        else:
            result=""
        return render_template("index.html",resultstring=result)    

if __name__=='__main__':
    app.run(debug=True)
    