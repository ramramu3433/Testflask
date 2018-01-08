From ubuntu
Run apt-get update && apt-get install python python-pip libmysqlclient-dev -y
#Run apt-get install libmysqlclient-dev -y
#Run apt install python python-pip -y
Run pip install flask_mysqldb
Add ./requirements.txt /
Add ./app.py /
Add ./test.py /
Run pwd
Run pip install -r requirements.txt
Expose 5000
EntryPoint ["python","app.py"]


