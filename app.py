from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/get')
def test():
    return 'Testting page'

@app.route('/page1')
def load():
    return render_template('testpage.html',value="Value1",title="Title",listval=[1,2,3,4,5])

if __name__=="__main__":
   app.run(debug='true')
