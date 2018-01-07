Test flask app

For developement install virtualenvironment 

apt-get install python-pip
pip install virtualenv virtualenvwrapper
add $WORKON directory to ./bashrc
printf '\n%s\n%s\n%s' '# virtualenv' 'export WORKON_HOME=~/virtualenvs' \
'source /usr/local/bin/virtualenvwrapper.sh' >> ~/.bashrc

source ./bash_rc
mkdir -p WORKON_HOME
mkvirtualenv api


pip install flask for installing flask


create app.py file
add if __name__=="__main":
for running file as startup

from flask import render_template toadd support for jinja2 templating

render_template('file','variables')

{{ }} -> to add variable
{% %} -> code in jinja templating 
Added Hook sample
@app.route()


