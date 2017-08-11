from flask import Flask, request, jsonify
from scripts import yandex_scraper

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

    try:
        results = yandex_scraper.yandex_search(searchkey, searchtab)
    except Exception as e:
        return jsonify({'status': False, 'errmsg': str(e)})

    return jsonify({'status': True, 'results': results})


if __name__ == "__main__":
    app.run(host='0.0.0.0')
