from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

things_to_do = ['Buy coffee', 'Send requirenment', 'Deliver a video']

@app.errorhandler(500)
def internal_server(error):
    return render_template('500.html', error=error)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello/'))
    response.set_cookie('user_ip', user_ip)
    return response


@app.route('/hello/')
def hello():
    user_ip = request.cookies.get('user_ip')
    context = {
         'user_ip': user_ip, 
         'things_to_do': things_to_do
    }
    
    return render_template('hello.html', **context)
