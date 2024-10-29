from flask import Flask, jsonify, request
import pickle as pk

with open("./dv.bin", 'rb') as f_out:
   dv =  pk.load(f_out)
with open("./model1.bin", 'rb') as f_out:
   model =  pk.load(f_out)

app = Flask(__name__)

@app.route("/score", methods=["POST"])
def score():
     client = request.get_json()
     X = dv.transform([client])
     result = round(model.predict_proba(X)[0,1] , 3)
     return jsonify(result)


if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0", port=3030)