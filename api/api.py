# 載入類別
import json

import calculation
from flask import Flask, jsonify, request

# 建立 Flask 類別實體
app = Flask(__name__)


# 配對網址和執行的函數
@app.route("/iris/predict", methods=["POST"])
def predict():
    # 判斷 Content-Type 是否為 json 格式
    content_type = request.headers.get("Content-Type")
    if content_type == "application/json":
        req_json = request.json

    # 取得傳入的訓練和測試資料 request json parameter
    data = json.loads(req_json["data"])
    # 執行預測模型
    prediction = calculation.evaluate_probs(data)
    print("prediction: " + str(prediction))

    return jsonify(prediction.tolist())


# 當啟動 server 時先去預先 load model 每次 request 都要重新 load 造成效率低下且資源浪費
if __name__ == "__main__":
    app.run(debug=True)
