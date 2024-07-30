from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def get_root():
    return jsonify({"service": "flask-app", "version": "0.0.1"})


@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    return jsonify({"item_id": item_id, "item_name": "an item"})


@app.route("/items", methods=["POST"])
def create_item():
    data = request.json
    return jsonify({"item": data, "status": "created"}), 201


@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    data = request.json
    return jsonify({"item_id": item_id, "item": data, "status": "updated"})


@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    return jsonify({"item_id": item_id, "status": "deleted"})


if __name__ == "__main__":
    app.run(debug=True)
