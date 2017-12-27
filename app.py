from flask import Flask,render_template
from flask_mysqldb import MySQL
app = Flask(__name__)
app.config.update({"MYSQL_PASSWORD":"password"})
mysql = MySQL(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/get')
def test():
    return 'Testting page'

@app.route('/page1')
def load():
    return render_template('testpage.html',value="Value1",title="Title",listval=[1,2,3,4,5])
@app.route('/msql')
def msql():
    #data=mysql.connect(passwd='password',user='root')
    data=mysql.connection.cursor()
    #dat=data.cursor()
    value=[]
    data.execute('SELECT * FROM db.test')
    val=data.fetchall()
    for row in val:
        value.append(str(row.num))
    return render_template('testpage.html',value="Value1",title="MSQL",listval=value)
#    return val
if __name__=="__main__":
   app.run(debug='true')
