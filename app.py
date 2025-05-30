from flask import Flask, request, jsonify, render_template
from analyzer import analyze_profile

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/results")
def results():
    return render_template("results.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.get_json()
        if not data or "url" not in data:
            print("No URL in request data:", data)
            return jsonify({"error": "No profile URL provided"}), 400
        
        profile_url = data["url"]
        print("Received URL:", profile_url)

        result = analyze_profile(profile_url)
        return jsonify(result)

    except Exception as e:
        print("Error in /analyze route:", str(e))
        return jsonify({"error": "Internal server error", "details": str(e)}), 500
    
@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)