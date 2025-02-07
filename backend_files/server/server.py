from flask import Flask

app = Flask(__name__)

@app.route("/members", methods=["GET"])
def members():
	return {"members": ["Kevin", "Alice", "Bob"]}

if __name__ == "__main__":
    app.run(debug=True)