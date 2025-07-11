from flask import Flask, jsonify, request

app = Flask(__name__)

capital_data = {
    "France": "Paris",
    "Germany": "Berlin",
    "India": "New Delhi",
    "Japan": "Tokyo",
    "USA": "Washington, D.C."
}

@app.route('/')
def home():
    return "Welcome to the Capital Cities API! Use /capital?country=NAME"

@app.route('/capital', methods=['GET'])
def get_capital():
    country = request.args.get('country')
    if not country:
        return jsonify({"error": "Country parameter is required"}), 400
    
    capital = capital_data.get(country.title())
    if capital:
        return jsonify({"country": country, "capital": capital})
    else:
        return jsonify({"error": "Country not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
