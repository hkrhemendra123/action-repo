from flask import Flask,json,request
from flask.templating import render_template
from flask import jsonify


app =  Flask(__name__)

@app.route('/',methods=['POST'])
def index():
    if request.headers['Content-Type'] == 'application/json':
        res = json.dumps(request.json)
        print(res)
    with open('test.json','w') as outfile:
        json.dump(res,outfile)
    return 'success'
if __name__ == '__main__':
    app.run(debug=True)