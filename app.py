from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'votre_cle_secrete'

# Configuration email (exemple avec Gmail)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'devistk69@gmail.com'  # ➡️ Ton email
app.config['MAIL_PASSWORD'] = 'qslgxmyhxrhohscc'  # ➡️ Le mot de passe ou code d’application

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    nom = request.form.get('nom')
    email = request.form.get('email')
    message = request.form.get('message')

    # Envoyer l'email
    msg = Message(subject="📩 Nouveau message depuis votre site",
                  sender=app.config['MAIL_USERNAME'],
                  recipients=['devistk69@gmail.com'],  # ➡️ L’email où tu veux recevoir les messages
                  body=f"Nom : {nom}\nEmail : {email}\n\nMessage :\n{message}")
    mail.send(msg)

    flash('Votre message a bien été envoyé. Merci !')
    return redirect('/#contact')

if __name__ == '__main__':
    app.run(debug=True)
