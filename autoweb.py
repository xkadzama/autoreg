from flask import Flask, render_template, request
# request


app = Flask(__name__)


@app.route('/')
def auto_page():
    return render_template('index.html')



@app.route('/result', methods=['POST'])
def end_page():
    login = request.form['login']
    password = request.form['password']
    # with open('E:\\fpython\\panel\\base.txt', mode='w', encoding='utf-8') as base:
    #     base.write(login)
    #     base.write(password)
    return render_template('res.html', login=login, password=password)


app.run(debug=True)