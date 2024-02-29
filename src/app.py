from flask import Flask, render_template, request, redirect, url_for


from config import config

app = Flask(__name__, template_folder='C:/Users/docky/OneDrive/Desktop/Templates Cancha/templates')


@app.route('/')
def index():
    return redirect (url_for ('login'))


@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        print(request.form['username'])
        print(request.form['password'])
        return render_template('login.html')
    else:
        return render_template('login.html') 



if __name__ =='__main__':
    app.config.from_object(config['development'])
    app.run()
