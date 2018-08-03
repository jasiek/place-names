from flask import Flask, request, jsonify, send_from_directory
from Levenshtein import distance
app = Flask(__name__)

places = []
with open("data/pl.txt") as f:
  places = [pn.lower() for pn in f.read().splitlines()]

def sort_by_edit_distance(places, query):
  query = query.lower()
  return sorted(places, key=lambda p: distance(p, query))
  
@app.route('/search')
def search():
  certain_of_first_letter = request.args.get('certain')
  query = request.args.get('s')
  if certain_of_first_letter:
    results = sort_by_edit_distance([pn for pn in places if ord(pn[0]) == ord(query[0])], query)
  else:
    results = sort_by_edit_distance(places, query)
  return jsonify(results[:30])

@app.route('/<path:path>')
def serve_static(path):
  return send_from_directory('public', path)

@app.route('/')
def serve_index():
  return serve_static('index.html')

if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)
