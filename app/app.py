from flask import Flask, request, jsonify
import pickle
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
model_path = "models/model_v1.pkl"

with open(model_path, "rb") as file:
  try:
    model = pickle.load(file)
  except Exception as e:
    logging.error(f"Model \"{model_path}\" could not be loaded")

@app.route("/api", methods=["GET"])
def api_info():
  return jsonify({
    "status": "ok",
    "info": "Accepts POST request with JSON body containing a \"features\" key with a list of features like given this request, dont use string cotations for the value",
    "features": "[[year, power, driven_mk, passengers, second_hand_count]]"
  })

@app.route("/api", methods=["POST"])
def predict():
  try:
    data = request.get_json(force=True)
    predict = model.predict(data["features"])
    return jsonify({"price": predict.tolist()[0]})
  except Exception as e:
    logging.exception(e)
    return jsonify({"error": "Something went wrong"}), 500

if __name__ == "main":
  app.run(debug=True)