from flask import Flask,render_template,request,jsonify
from flask_cors import CORS,cross_origin
import pickle

app = Flask(__name__)

@app.route('/',methods=['GET'])
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET'])
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            item_weight = float(request.form['item_weight'])
            item_fat_content = float(request.form['item_fat_content'])
            item_visibility = float(request.form['item_visibility'])
            item_type = float(request.form['item_type'])
            item_mrp = float(request.form['item_mrp'])
            outlet_size = float(request.form['outlet_size'])
            outlet_location_type = float(request.form['outlet_location_type'])
            outlet_type = float(request.form['outlet_type'])

            filename = iNinternship1.pickle
            loaded_model = pickle.load(open(filename,'rb'))

            prediction = loaded_model.predict([[item_weight,item_fat_content,item_visibility,
                                                item_type,item_mrp,outlet_size,outlet_location_type,outlet_type]])

            print('Prediction is',prediction)
            return
            render_template('results.html',prediction)

        except Exception as e:
            print('The Exception message is: ',e)
            return 'Something is Wrong'
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)


