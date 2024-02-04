from flask import Flask, render_template, request
import qrcode
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    qr_code = None

    if request.method == 'POST':
        data = request.form['data']
        qr_code = generate_qr_code(data)

    return render_template('index.html', qr_code=qr_code)

def generate_qr_code(data):
    code = request.form["data"]
    qr_img = qrcode.make(code)
    path =('.\\static\\image.jpg')
    qr_img.save(path) 

# app.register_blueprint(views, url_prefix="/views")


if __name__ == '__main__':
    app.run(debug=True)