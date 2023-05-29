# ProcessPDF


What have I done?
1. download https://mozilla.github.io/pdf.js/
2. unzip pdfjs-3.6.172-dist.zip
3. mv ~/Download/pdfjs-3.6.172-dist/web ~/myprojects/PDFProcess/static/.
4. mv ~/Download/pdfjs-3.6.172-dist/build ~/myprojects/PDFProcess/static/.
5. create app.py, template/pdf_viewer.html, template/upload.html

app.py load one page pdf, click mouse to add annotation.

How to run this app.py ?
1. brew install python
2. pip install FLASK
3. python -m venv PDFenv
4. source PDFenv/bin/activate
5. python app.py
6. go to browswer http://127.0.0.1:4555

pdfapp.py adds pagination, if the line contains the word 'boss', it will highlight the lines. 
1. python pdfapp.py
2. go to browswer http://127.0.0.1:5000

Bugs needs to be fixed: the highlighted position is incorrect.

Other Info:
https://github.com/mozilla/pdf.js/wiki/Frequently-Asked-Questions
https://stackoverflow.com/questions/33063213/pdf-js-with-text-selection
