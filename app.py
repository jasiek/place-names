from flask import Flask, request, jsonify, send_from_directory
from Levenshtein import distance
app = Flask(__name__)


@app.route('/search')
def search():
  with open("data/pl.txt") as f:
    results = sorted(f.read().splitlines(), key=lambda p: distance(p.lower(), request.args.get('s')))
    return jsonify(results[:100])

@app.route('/<path:path>')
def serve_static(path):
  return send_from_directory('public', path)

@app.route('/')
def serve_index():
  return serve_static('index.html')

if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)
