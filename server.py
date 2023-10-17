# from flask import Flask,request,jsonify
# import util
# app=Flask(__name__)
# # @app.route('/hello')
# # def hello():
# #     return "hii"
# @app.route('/get_location_name')
# def get_location_name():
#     return "hiiz"
#     response =jsonify({
#         'locations':util.get_location_name()
#     })
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response

# @app.route('/predict_price',methods=['POST'])
# def predict_price():
#       total_sqft=float(request.form['sqft'])
#       location=request.form['location']
#       bhk=int(request.form['bhk'])
#       bath=int(request.form['bath'])

#       response=jsonify({
#         'estimated_price':util.get_price(location,sqft,bhk,bath)
#       })
#       response.headers.add('Access-Control-Allow-Origin', '*')
#       return response

 


# if __name__=="__main__":
#     print("start server")
#     util.get_details
#     app.run()

from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_name()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    sqft = float(request.form['sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_price(location,sqft,bhk,bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.get_details()
    app.run()