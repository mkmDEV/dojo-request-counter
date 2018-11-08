from flask import Flask, request, url_for, render_template, redirect

app = Flask(__name__)
counts = {
    'GET': 0,
    'POST': 0,
    'PUT': 0,
    'DELETE': 0,
    }


@app.route('/')
def home():
    return render_template("index.html", counter=counts)


@app.route('/request-counter', methods=['GET', 'POST', 'PUT', 'DELETE'])
def request_counter():
    global counts
    # request_type = request.method

    if request.method == 'GET':
        counts['GET'] += 1
    elif request.method == 'POST':
        counts['POST'] += 1
    elif request.method == 'PUT':
        counts['PUT'] += 1
    elif request.method == 'DELETE':
        counts['DELETE'] += 1
    return redirect('/')


if __name__ == '__main__':
    app.run(
        debug=True
    )
