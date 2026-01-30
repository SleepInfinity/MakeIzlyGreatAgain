from flask import Flask, request, render_template
import izly_api

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the username and password from the form
        username = request.form['username']
        password = request.form['password']
        request_type = request.form['button']

        credentials = izly_api.get_credentials(*izly_api.get_csrf(), username, password)
        if request_type == 'qr':
            # Generate the QR code from Izly
            base64_qrcodes = izly_api.get_qrcode(credentials)
            base64_image = base64_qrcodes["images"][0]
            validity_date = base64_qrcodes["validityDate"]

            return render_template('dashboard.html', qr_image=base64_image, validity_date=validity_date)
        elif request_type == 'balance':
            balance = str(izly_api.get_balance(credentials))
            return render_template('dashboard.html', balance=balance)
    else:
        # If the request is a GET request, return the HTML form
        return render_template('index.html')


if __name__ == '__main__':
    #from waitress import serve
    #serve(app, host="0.0.0.0", port=8080)
    app.run(host="0.0.0.0", port=8080)