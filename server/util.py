import json
import pickle
import numpy as np

__pincodes = None
__model = None
__data_columns = None
__avg_price_data = None


def predict_price(area, bed, bath, balc, status, parking, furn, lift, price_sqft, kitc, new, resale, flat, house, pincode):
    load_saved_artifacts()
    x = np.zeros(len(__data_columns))

    x[0] = area
    x[1] = bed
    x[2] = bath
    x[3] = balc
    x[4] = status
    x[5] = parking
    x[6] = furn
    x[7] = lift
    x[8] = price_sqft
    x[9] = kitc
    x[10] = new
    x[11] = resale
    x[12] = flat
    x[13] = house
    x[14] = pincode

    return float(__model.predict([x])[0])


def get_pincodes():
    load_saved_artifacts()
    return __pincodes


def get_avg_price(pincode):
    with open('./artifacts/avg_price_data.json') as f:
        data = json.load(f)
        for entry in data:
            if entry['pincode'] == pincode:
                avg_price = entry['average_price_per_sq_feet']
                return round(avg_price, 2)
    return 0  # Return 0 if pincode is not found in the data

def load_saved_artifacts():
    print("loading saved artifacts.... start")
    global __pincodes
    global __data_columns
    global __model
    global __avg_price_data

    with open("./artifacts/pincodes.json", 'r') as f:
        __pincodes = json.load(f)['unique_pincodes']

    with open("./artifacts/house_price_predictor.pickle", 'rb') as f:
        __model = pickle.load(f)
    print("loading saved artifacts.. done!")

    with open("./artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']

    # Load average price data from JSON file
    with open("./artifacts/avg_price_data.json", "r") as f:
        __avg_price_data = json.load(f)


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_pincodes())
    print(predict_price(1025, 2, 2, 2, 1, 0, 1, 2, 3512.195122, 2, False, True, True, False, 201206))
