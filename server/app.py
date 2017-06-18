from flask import Flask, request, render_template, jsonify

from util.connections import Connections

app = Flask(__name__)

@app.route('/api/search')
def search():
    if 'src' not in request.args:
        return 'src node not provided', 400
    if 'dest' not in request.args:
        return 'dest node not provided', 400
    
    src = request.args.get('src')
    dest = request.args.get('dest')

    conns = Connections(src)
    path = conns.search(dest)
    
    response = {
        "path": get_serialized_path(path)
    }

    return jsonify(response)

@app.route('/api/politician/search')
def politician_seach():
    if 'q' not in request.args:
        query = ""

    query = request.args.get('q')

    response = {
        "results": []
    }

    return jsonify(response)

@app.route('/')
def index():
    return render_template('index.html')

def get_serialized_path(path):
    bfs_path = [] 
    for vertex in path:
        obj = {
            "id": vertex.id_,
            "name": ""
        }
        bfs_path.append(obj)
    return bfs_path

if __name__ == '__main__':
    app.run()
