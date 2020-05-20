from flask import Flask, render_template, redirect,request,url_for
from derivative import parse_input,derive,get_vals,gen_latex

app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def home():

    #defaults
    equation = 'x^2'
    derivative = ''
    start_range = -10
    end_range = 10
    error_message = ''

    if request.method == 'POST':
        try:
            equation = request.form["eq_in"]
            start_range = int(request.form["x_min"])
            end_range = int(request.form["x_max"])
            error_message = ''
        except:
            equation = 'x^2'
            start_range = -10
            end_range = 10
            error_message = 'Please Enter Valid Input'

        if start_range > end_range:
            #invalid range, set to defaults
            start_range = -10
            end_range = 10
            error_message = 'Please Enter Valid Range'
    
    #call functions from derivative.py
    try:
        eq = parse_input(equation)
    except:
        #use default if user enters incorrect equation format
        eq = parse_input('x^2')
        error_message = 'Please Enter Valid Equation Format'
    
    d = derive(eq)
    X, D = get_vals(d,start_range,end_range)
    X, Y = get_vals(eq,start_range,end_range)
    derivative_text = gen_latex(d)
    equation = gen_latex(eq)
            
    return render_template('layout.html',labels = X, values = Y,deriv= D,display_orig=equation ,display_derivative=derivative_text, error_mess=error_message)
    



##run app
if __name__ == '__main__':
    app.run()