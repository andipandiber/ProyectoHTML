from flask import Flask, render_template

app=Flask(__name__)

# Pagina Principal
@app.route('/')
def home():
    return render_template('home.html')

# Pagina About
@app.route('/about')
def about():
    return render_template('about.html')

if __name__=='__main__':
    #Poner en Modo Prueba
    app.run(debug=True)
