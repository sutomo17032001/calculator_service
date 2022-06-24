from flask import Flask, render_template, request
from celery import Celery

Flask_App = Flask(__name__, template_folder="template")
#Flask_App = Celery('calculator', broker='pyamqp://guest@localhost//')

@Flask_App.route('/', methods=['GET'])
def index():
    """ Displays the index page accessible at '/' """

    return render_template('index.html')

@Flask_App.route('/operation_result/', methods=['POST'])
def operation_result():

    error = None

    result = []
    result2 = []

    first_input = request.form['Input1']
    second_input = request.form['Input2']
    operation = request.form['operation']

    try:
        input1 = int(first_input)
        input2 = int(second_input)

        if operation == "prime":
            prime_list = []
            for i in range (input1, input2):
                if i == 0 or i == 1:
                    continue
                else:
                    for j in range(2, int(i/2)+1):
                        if i % j == 0:
                            break
                    else:
                        prime_list.append(i)
            result = prime_list

        elif operation == "primepalindrome":
            prime_palindrome = []
            input1 = input1 + 1
            for i in range(input1, input2):
                if (str(i) == str(i)[::-1]):
                    if (i>1):
                        for input1 in range (2,i):
                            if (i % input1 == 0):
                                break
                        else:
                            prime_palindrome.append(i)
            result2 = prime_palindrome

        return render_template(
            'index.html',
            input1=input1,
            input2=input2,
            operation=operation,
            result=result,
            result2=result2,
            calculation_success=True
        )
        
    except ValueError:
        return render_template(
            'index.html',
            input1=first_input,
            operation=operation,
            result="Bad Input",
            calculation_success=False,
            error="Cannot perform numeric operations with provided input"
        )

if __name__ == '__main__':
    Flask_App.debug = True
    Flask_App.run()