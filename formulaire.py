from flask import Flask, render_template

app = Flask(__name__)

# Route pour la page principale "formulaire_tally"
@app.route('/')
def formulaire_tally():
    return render_template('formulaire_tally.html')

# Route pour la page "FAQ"
@app.route('/faq')
def faq():
    return render_template('faq.html')

if __name__ == '__main__':
    app.run(debug=True)

