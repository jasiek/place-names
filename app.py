from flask import Flask, request, jsonify
from Levenshtein import distance
app = Flask(__name__)

@app.route('/search')
def search():
  with open("data/pl.txt") as f:
    results = sorted(f.read().splitlines(), key=lambda p: distance(p, request.args.get('s')))
    return jsonify(results[:100])

if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)
