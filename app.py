#nltk.download('punkt')
from flask import Flask, render_template, request
app = Flask(__name__)
authorinfo = {}
@app.route('/')
def blog():
   return render_template('blog.html')

@app.route('/home',methods = ['POST', 'GET'])
def home():
      return render_template("blog.html")

@app.route('/contactus',methods = ['POST', 'GET'])
def contactus():
      return render_template("contactus.html")

@app.route('/about',methods = ['POST', 'GET'])
def about():
      return render_template("about.html")

#machine learning laptop mapping
@app.route('/laptop_machine_learning',methods = ['POST', 'GET'])
def laptop_machine_learning():
      authorinfo['name'] = "Karan Kumar Rajput"
      return render_template("laptop_machine_learning.html",author = authorinfo)

#machine learning laptop mapping
@app.route('/ML_DL_Interview_Question',methods = ['POST', 'GET'])
def ML_DL_Interview_Question():
      authorinfo['name'] = "Karan Kumar Rajput"
      return render_template("ML_DL_Interview_Question.html",author = authorinfo)

#machine learning laptop mapping
@app.route('/Gradient_Descent',methods = ['POST', 'GET'])
def Gradient_Descent():
      authorinfo['name'] = "Karan Kumar Rajput"
      return render_template("Gradient_Descent.html",author=authorinfo)

#Why to Appear in GATE CSE
@app.route('/Why_Appear_GATE_CSE',methods = ['POST', 'GET'])
def Why_Appear_GATE_CSE():
      authorinfo['name'] = "Karan Kumar Rajput"
      return render_template("Why_Appear_GATE_CSE.html",author= authorinfo)

@app.route('/LSTM_Text_Classification',methods = ['POST', 'GET'])
def LSTM_Text_Classification():
      authorinfo['name'] = "Karan Kumar Rajput"
      return render_template("LSTM_Text_Classification.html",author= authorinfo)

#text data preprocessing using python
@app.route('/Text_Data_Preprocessing',methods = ['POST', 'GET'])
def Text_Data_Preprocessing():
      authorinfo['name'] = "Karan Kumar Rajput"
      return render_template("Text_Data_Preprocessing.html",author= authorinfo)

#karan profile
@app.route('/aboutkaran',methods = ['POST', 'GET'])
def aboutkaran():
  authorinfo['name'] = "Karan Kumar Rajput"
  return render_template("aboutkaran.html",author= authorinfo)


if __name__ == '__main__':
   app.run(debug = True)
