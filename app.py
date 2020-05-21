from flask import Flask, render_template, redirect,request,url_for
from derivative import parse_input,derive,get_vals,gen_latex,get_defaults,check_range

app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def home():

    if request.method == 'POST':
        try:
            equation = request.form["eq_in"]
            start_range = int(request.form["x_min"])
            end_range = int(request.form["x_max"])

            if check_range(start_range,end_range) == -1:
                raise Exception

            eq = parse_input(equation)
            d = derive(eq)
            X, D = get_vals(d,start_range,end_range)
            X, Y = get_vals(eq,start_range,end_range)
            derivative_text = gen_latex(d)
            equation = gen_latex(eq)
            error_message = ''
            return render_template('layout.html',labels = X, values = Y,deriv= D,display_orig=equation ,display_derivative=derivative_text, error_mess=error_message)

        except:
            X,Y,D,equation,derivative_text,error_message = get_defaults('Please Enter Valid Input')
            return render_template('layout.html',labels = X, values = Y,deriv= D,display_orig=equation ,display_derivative=derivative_text, error_mess=error_message)


    X,Y,D,equation,derivative_text,error_message = get_defaults('')
    return render_template('layout.html',labels = X, values = Y,deriv= D,display_orig=equation ,display_derivative=derivative_text, error_mess=error_message)
    



##run app
if __name__ == '__main__':
    app.run()