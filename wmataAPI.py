from flask import Flask, jsonify
import pyWMATA
import urllib

app = Flask(__name__)

apikey = 'kfgpmgvfgacx98de9q3xazww' #Developer key
api = pyWMATA.WMATA(apikey)

@app.route('/WMATA/route/<string:start>/<string:end>/', methods=['GET'])
def getRoute(start,end):
    start = urllib.unquote(start).decode('ascii')
    end = urllib.unquote(end).decode('ascii')
    path = api.getPath(start,end)
    output = {}
    for station in path:
        if '(Start towards'.lower() in station.lower():
            output['Start'] = station
        if '(Transfer'.lower() in station.lower():
            output['Transfer'] = station
        if '(Exit'.lower() in station.lower():
            output['End'] = station
    return jsonify(output)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True)
