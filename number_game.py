import random
from flask import Flask, render_template, redirect, request, session, Markup
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/', methods=['GET','POST'])
def index():
    if 'num' not in session:
        session['num'] = random.randrange(1,101)
    print(session['num'])

    result = ""
    color = ""
    button = ""

    if request.method == 'POST':
        display = ""
        guess = request.form['guess']
        print(guess)
        if int(guess) > session['num']:
            result = "Too high!"
            color = "red"
        elif int(guess) < session['num']:
            result = "Too low!"
            color = "red"
        elif int(guess) == session['num']:
            result = str(session['num']) + " was the number!"
            color = "green"
            button = Markup("<a href='/reset' class='button'>Play again!</a>")
    else: 
        display = "hidden"

    return render_template('index.html', result=result, color=color, button=button)

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)