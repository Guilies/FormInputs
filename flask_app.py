from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    # found in ../templates/
    return render_template("main_page.html")

@app.route('/process_inputs', methods=['POST'])
def process_inputs():

    Letter = request.form.get('Letter', '')
    Number = request.form.get('Number', '')
    Color = request.form.get('Color', '')

    FirstName = { 'Grumpy', 'Mopey', 'Stupid' }
    MiddleName = { 'Bob', 'Charlie', 'Joe' }
    LastName = { 'Lucky', 'Unlucky', 'Sally' }


    return render_template("main_page.html",
                           output=Letter + "'" + Number + "," + " " + "The" + " " + Color)
