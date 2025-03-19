from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Store high scores (in-memory for simplicity)
high_scores = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_score', methods=['POST'])
def submit_score():
    data = request.json
    name = data.get('name')
    score = data.get('score')
    high_scores.append({'name': name, 'score': score})
    high_scores.sort(key=lambda x: x['score'], reverse=True)  # Sort by score
    return jsonify(success=True)

@app.route('/get_high_scores', methods=['GET'])
def get_high_scores():
    return jsonify(high_scores[:10])  # Return top 10 scores

if __name__ == '__main__':
    app.run(debug=True)
