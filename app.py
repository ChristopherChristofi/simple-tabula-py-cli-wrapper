import os
import time
import tabula
from flask import Flask, flash, render_template, request, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config['UPLOAD_EXTENSIONS'] = ['.pdf']
app.config['SECRET_KEY'] = os.urandom(12).hex()

@app.route('/')
def index():
   return render_template('process.html')

@app.route('/convert', methods = ['POST'])
def convert_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            print('Incorrect no file')
            return render_template('process.html')

    selected = request.form['page-param']
    try:
        if selected == '':
            print("No page selection provided")
            return render_template('process.html')
        elif selected != "all":
            page = int(selected)
        elif selected == "all":
            page = selected
        else:
            return render_template('process.html')
    except Exception as err:
        print("Error found:", err)
        return render_template('process.html')

    timestamp = time.strftime("%d%m%Y%M%H%S")
    output_file_name = "spreadsheet-{pg}-{stamp}".format(pg=page, stamp=timestamp)
    save_path = "data/{converted}.csv".format(converted=output_file_name)

    f = request.files['file']
    filename = secure_filename(f.filename)
    if f.filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            print('Cannot accept this file type')
            return render_template('process.html')
        if file_ext in app.config['UPLOAD_EXTENSIONS']:
            tabula.convert_into(f, save_path, output_format="csv", pages=page)
            print('File: {upload} converted to: {converted} in data directory.'.format(upload=filename, converted=output_file_name))
    return render_template('process.html')

if __name__ == '__main__':
   app.run(debug = True)