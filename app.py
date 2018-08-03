from flask import Flask, request, jsonify, send_from_directory
from Levenshtein import distance
app = Flask(__name__)

places = []
with open("data/pl.txt") as f:
  places = f.read().splitlines()

@app.route('/search')
def search():
  results = sorted(places, key=lambda p: distance(p.lower(), request.args.get('s')))
  return jsonify(results[:100])

@app.route('/<path:path>')
def serve_static(path):
  return send_from_directory('public', path)

@app.route('/')
def serve_index():
  return serve_static('index.html')

if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)
