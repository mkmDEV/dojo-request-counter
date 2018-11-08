from flask import Flask, request, url_for, render_template, redirect

app = Flask(__name__)
counts = 0


@app.route('/')
def home():
    return render_template("index.html", counter=counts)


@app.route('/request-counter', methods=['GET', 'POST'])
def request_counter():
    global counts
    if request.method == 'GET':
        counts += 1
        return redirect('/')


if __name__ == '__main__':
    app.run(
        debug=True
    )
