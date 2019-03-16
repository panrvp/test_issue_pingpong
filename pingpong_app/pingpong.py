import datetime
from bottle import template, Bottle

app=Bottle()
version=open('VERSION', 'r').read()

@app.get('/ping')
def index(answer="pong"):
    return template('{{answer}}\nversion={{version}}\n{{date}}',
                    version=version, answer=answer, date=datetime.datetime.now())
@app.get('/test')
def test(answer="ok"):
    return template('{{answer}}', answer=answer)

app.run(host="localhost", port="8080")