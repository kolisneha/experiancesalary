from flask import Flask,render_template,request

import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import PolynomialFeatures

app = Flask(__name__)
@app.route('/')
def hello_world():
	return render_template('login.html')
@app.route('/predict',methods=['POST'])
def get_result():
	poly = pickle.load(open('poly1.pkl', 'rb'))
	model=pickle.load(open('model_lr.pkl', 'rb'))
	print(request.form['exp'])
	query=[[float(request.form['exp'])]]
	X_query=poly.transform(query)
	sal=model.predict(X_query)
	return 'Dear'+request.form["name"]+'your expected salary after:'+request.form["exp"]+'Experiencne is'+str(sal)
if __name__=='__main__':
	app.run(debug=True)
