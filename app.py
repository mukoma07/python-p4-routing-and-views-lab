from flask import Flask

app = Flask(__name__)

# Index route
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# Print String route
@app.route('/print/<string:input_string>')
def print_string(input_string):
    print(input_string)  # Print the string to the console
    return f'<p>Printed string: {input_string}</p>'

# Count route
@app.route('/count/<int:num>')
def count(num):
    numbers = '\n'.join(str(i) for i in range(num + 1))
    return f'<pre>{numbers}</pre>'

# Math route
@app.route('/math/<float:num1><string:operation><float:num2>')
def math(num1, operation, num2):
    result = None

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Invalid operation'

    return f'<p>Result: {num1} {operation} {num2} = {result}</p>'

if __name__ == '__main__':
    app.run(debug=True)
