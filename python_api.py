from flask import Flask, render_template

app = Flask(__name__)

@app.route('/server_address/display')
def show_penguins():
    return render_template('penguins.html')

if __name__ == '__main__':
    app.run( debug = True )
