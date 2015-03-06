from flask import Flask, jsonify    #only import what we need
import pyWMATA
import urllib                       #needed to support decoding URLs

app = Flask(__name__)

apikey = 'kfgpmgvfgacx98de9q3xazww' #WMATA's example key. If you are using this in a production environment, get your own api key from api.wmata.com
api = pyWMATA.WMATA(apikey)

@app.route('/WMATA/route/<string:start>/<string:end>/', methods=['GET']) #define the route to the API (using 2 different variables)
def getRoute(start,end):
    start = urllib.unquote(start).decode('ascii')   #encode both of the variables to ascii (from URL encoding)
    end = urllib.unquote(end).decode('ascii')
    path = api.getPath(start,end)
    output = {}                                     #Create a dict to store the output in
    for station in path:                            #We don't want a list of all the stops along the route, instead we only want the start, transfer, and output ones
        if '(Start towards'.lower() in station.lower(): #Use lower case to ensure that it matches
            output['Start'] = station
        if '(Transfer'.lower() in station.lower():
            output['Transfer'] = station
        if '(Exit'.lower() in station.lower():
            output['End'] = station
    return jsonify(output)  #convert our dict to a json output before returning it

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True)  #host='0.0.0.0' because we want this to be accessible from more than localhost
                                                #port=80 to specify the port
                                                #debug=True to make it automatically reload changes to the source along with more useful debugging output
