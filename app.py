from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    data = {'message':'it works'}
    return render_template('index.html', data = data)

@app.route("/hello_form")
def hello_form():
    return render_template('hello_form.html', data=None)
    
@app.route("/hello_results", methods=["POST"])
def hello_results():
    data = {'message': request.form.get('name')}
    return render_template('hello_results.html', data=data)
   

if __name__=='__main__':
    app.run()
