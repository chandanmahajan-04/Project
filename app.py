from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        print(f"Contact Form: Name={name}, Email={email}, Message={message}")
        return redirect(url_for('home'))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
