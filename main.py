from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = 'siodjrfowiewr08uwijdsiofm'
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

# @app.route('/about')
# def about():
#     return render_template('about.html')

# @app.route('/services')
# def services():
#     return render_template('services.html')

@app.route('/dashboard',methods=['GET','POST'])
def dashboard():
    return render_template('dashboard.html')

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/tables')
def tables():
    return render_template('tables.html')

@app.route('/upgrade')
def upgrade():
    return render_template('upgrade.html')

@app.route('/user')
def user():
    return render_template('user.html')

if __name__ == '__main__':
    app.run(debug=True)
