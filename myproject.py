from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file('index.html')
    # return "<h1 style='color:blue'>Hello!</h1>"

@app.route('/api/yandex/search', methods=['POST'])
def register():
    json_data = request.json
    searchkey = json_data['key']
    searchtab = json_data['tab']
    print searchkey
    print searchtab

    results = []
    results.append({'title': 'asd', 'link': 'qwe', 'description': 'zxc'})
    return jsonify({'results': results})

if __name__ == "__main__":
    app.run(host='0.0.0.0')
