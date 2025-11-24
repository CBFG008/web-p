from flask import Flask, render_template, url_for, request
import csv

app = Flask(__name__)

@app.route('/' )
def index():
    return render_template('index.html')

def write_to_csv(data):
    with open ('web4.CSV', mode='a' , newline='') as Database:
        email = data ["email"]
        name = data ["name"]
        subject = data ["subject"]
        message = data ["message"]
        csv_writer = csv.writer(Database , delimiter= ',')
        csv_writer.writerow([email,name,subject,message])

@app.route('/webs4.py', methods=['POST'])
def html_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)    
        return "form submitted"
    else:
        return "went wrong"

if __name__ == '__main__':
    app.run(debug=True)