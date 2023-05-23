
from flask import Flask, request, render_template, send_from_directory, redirect
from flask_cors import CORS, cross_origin
import os

app = Flask(__name__)
CORS(app)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'static/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)

    return redirect('/view-pdf/' + filename)

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("static", filename)

@app.route('/view-pdf/<filename>')
def view_pdf(filename):
    return render_template('pdf_viewer.html', filename=filename)

@app.route("/pdf_viewer_1/<filename>")
def pdf_viewer_1(filename):
    return render_template("pdf_viewer.html", filename=filename)

@app.route("/pdf_viewer_2/<filename>")
def pdf_viewer_2(filename):
    return render_template("pdf_viewer.html", filename=filename)



if __name__ == "__main__":
    app.run(port=4555, debug=True)

