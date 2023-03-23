from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def getHomePage():
    return render_template('index.html')

@app.route('/phone-number', methods=['POST'])
def postPhoneNumber():
    print('\033[96mThe user submitted the phone number:', request.form.get('phone'), '\033[37m')
    return "Successful!"

if __name__ == "__main__":
    app.run()
