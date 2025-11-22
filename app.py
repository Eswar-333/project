from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/extract', methods=['POST'])
def extract():
    file = request.files['file']
    # TODO: Call OCR + GenAI here
    extracted_data = {
        "Patient_Name": "John Doe",
        "Age": "45",
        "Diagnosis": "Diabetes"
    }
    return render_template('result.html', data=extracted_data)

if __name__ == '__main__':
    app.run(debug=True)
