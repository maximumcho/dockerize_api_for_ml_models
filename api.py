from flask import Flask, request, jsonify
import numpy
import pickle
import json

app = Flask(__name__)


@app.route('/iris/predict', methods=['POST'])
def predict():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        req_json = request.json
        
    X = numpy.array(json.loads(req_json['data']))

    print("x: " + str(X))

    with open('model.pickle', 'rb') as pickle_in:
        model = pickle.load(pickle_in)
    
    print("Test 1")
    prediction = model.predict(X)
    print("Test 2")


    print("prediction: " + str(prediction))

    return jsonify(prediction.tolist())

# 當啟動 server 時先去預先 load model 每次 request 都要重新 load 造成效率低下且資源浪費
if __name__ == '__main__':
     app.run(debug=True)