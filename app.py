from flask import Flask, render_template
import sqlodbc 

app = Flask(__name__, template_folder='template')

@app.route('/')
def home():
    return render_template('home.html')
cnn = pyodbc.connect('DRIVER={}; Server=; Database=;')

if __name__ == '__main__':
    app.run()

    
