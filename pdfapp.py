import os
from flask import Flask, render_template, request

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Check if a file was uploaded
        if 'pdf_file' in request.files:
            pdf_file = request.files['pdf_file']
            filename = pdf_file.filename

            # Save the uploaded file temporarily
            temp_path = os.path.join(app.config['UPLOAD_FOLDER'], 'temp.pdf')
            pdf_file.save(temp_path)

            return render_template('pdf_pages_viewer.html', pdf_path=temp_path)

    return render_template('pdf_upload.html')

if __name__ == '__main__':
    app.run(debug=True)
