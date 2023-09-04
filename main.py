from flask import Flask, render_template, request, url_for, redirect

portfoilo = Flask(__name__)

@portfoilo.route('/')
def main_page():
    return render_template('/index.html', page_tittle = 'EM Portfolio Website')

@portfoilo.route('/about')
def aboutMe_page():
    return render_template('/about.html', page_tittle = 'About Me')

@portfoilo.route('/contatc-us')
def contatc_page():
    return render_template('contatc-us.html', page_tittle = 'Contatc Us')



if __name__ == '__main__':
    portfoilo.run(debug= True, port=7000)