from flask import Flask, jsonify

app = Flask(__name__)

# Sample data
live_scores = [
    {'game': 'Team A vs Team B', 'score': '1 - 2', 'status': 'Finished'},
    {'game': 'Team C vs Team D', 'score': '0 - 0', 'status': 'Ongoing'}
]

game_tables = [
    {'team': 'Team A', 'points': 10},
    {'team': 'Team B', 'points': 8},
    {'team': 'Team C', 'points': 7},
    {'team': 'Team D', 'points': 15}
]

@app.route('/live-scores')
def get_live_scores():
    return jsonify(live_scores)

@app.route('/game-tables')
def get_game_tables():
    return jsonify(game_tables)

@app.route('/update-score', methods=['POST'])
def update_score():
    # Here you would typically handle the logic to update scores
    return jsonify({'message': 'Score updated successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)