from flask import Flask, render_template, request
import mailtrap as mt

app = Flask(__name__)
@app.route('/')
def contact():
    return render_template('contact.html')

@app.route("/submit", methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    message = request.form.get('message')
    mail = mt.Mail(
        sender=mt.Address(email="hello@demomailtrap.co", name=name),
        to=[mt.Address(email="mythresh.naveen@gmail.com")],
        subject=f"Dawn Blogs - Message from {name}",
        text=f"DETAILS:\nName:{name}\nEmail:{email}\nPhone:{phone}\n\n\n{message}",
        category="Work",
    )

    client = mt.MailtrapClient(token="?????")
    response = client.send(mail)
    return "Submitted!"

if __name__ == '__main__':
    app.run(debug=True)