from flask import Flask, render_template


app =Flask(__name__)

@app.route('/')

def index():
    first_name='jimbala'
    stuff=' <strong>test123</strong>  '
    return render_template("index.html",
                           first_name=first_name,
                           stuff=stuff)

#localhost:5000/user/John
@app.route('/user/<name>')

def user(name):
    return render_template("user.html",user_name=name)



if __name__ == "__main__":
  app.run(debug=True)

#invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

#internal server error message
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"),500

