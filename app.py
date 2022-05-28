from flask import Flask, render_template, request
import TMDB_Movies



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



@app.route("/test")
def test(): 
    movies = TMDB_Movies.recommend("Home Alone")
   
    data = {'movies': movies}
    return render_template('test_results.html', data = data)

if __name__=='__main__':
    app.run()

@app.route("/test_results", methods=["POST"])
def test_results(): 
    movies = TMDB_Movies.recommend(request.form.get('movie'))
    print("+++++++++")
    print(movies)
    data = {'movies': movies}
    return render_template('test_results.html', data = data)

@app.route("/test_form")
def test_form(): 
    return render_template('test_form.html')

