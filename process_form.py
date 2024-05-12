from flask import Flask, render_template, request

import bill
import main
from tkinter import messagebox

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('input_form.html')


@app.route('/submit', methods=['POST'])
def submit_form():
    input_field1_value = request.form['inputField1']
    input_field2_value = request.form['inputField2']

    # Process the data (you can replace this with your own logic)
    main.data(input_field1_value, input_field2_value)
    bill.main()
    return "DATA ENTERED INTO MEHTA CREDIT"


if __name__ == '__main__':
    app.run(debug=True)
