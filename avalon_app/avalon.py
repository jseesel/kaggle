from flask import Flask, jsonify, render_template, request
import pandas as pd

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/players', methods=['POST'])
def get_player_data():
    print request.method
    j = request.get_json()
    print j['10']
    print j.keys()
    df = pd.DataFrame.from_dict(j, orient='index')
    df = df[['name', 'role', 'seat', 'lady']]
    print df.head()
    df.to_csv("player_output.csv", index=False)
    return 'success', 200


@app.route('/api/game', methods=['POST'])
def get_game_data():
    print request.method
    j = request.get_json()
    print j
    df = pd.DataFrame.from_dict(j, orient='index')
    # df = df[['player_count', 'winner', 'mission_count', 'method']]
    print type(df)
    df.to_csv("game_output.csv", index=False)
    return 'success', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
