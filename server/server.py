from flask import Flask, request, jsonify
import util
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/get_pincodes')
def get_pincodes():
    response = jsonify({
        'pincodes': util.get_pincodes()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/get_avg_price', methods=['GET'])
def get_avg_price():
    pincode = request.args.get('pincode', type=int)
    avg_price = util.get_avg_price(pincode)
    return jsonify({'avg_price': avg_price})


@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    area = request.json['area']
    bed = request.json['bed']
    bath = request.json['bath']
    balc = request.json['balc']
    status = request.json['status']
    parking = request.json['parking']
    furn = request.json['furn']
    lift = request.json['lift']
    price_sqft = request.json['price_sqft']
    kitc = request.json['kitc']
    neworold = request.json['neworold']
    building_type = request.json['building_type']
    pincode = request.json['pincode']

    flat = False
    house = True
    new = True
    resale = False

    if neworold == 'new property':
        new = True
        resale = False
    elif neworold == 'resale':
        new = False
        resale = True

    if building_type == 'flat':
        flat = True
        house = False
    elif building_type == 'house':
        flat = False
        house = True

    response = jsonify({
        'estimated_price': util.predict_price(area, bed, bath, balc, status, parking, furn, lift, price_sqft, kitc, new,
                                              resale, flat, house, pincode)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    print("Staring Python Flask Server for Housing Price Prediction...")
    app.run()
