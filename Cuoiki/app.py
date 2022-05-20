from flask import Flask, render_template, request
from flask_mail import Mail, Message

app=Flask(__name__)
mail=Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'chinhthucgas@gmail.com'
app.config['MAIL_PASSWORD'] = 'chinhthuc'
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def index():
	return render_template("form.html")

@app.route("/result", methods=['POST', 'GET'])
def result():
	if request.method == "POST":
		msg = Message(request.form.get("Subject"), sender= 'chinhthucgas@gmail.com', recipients= [request.form.get("Email")])
		msg.body = "Cảm ơn bạn đã tin tưởng sử dụng dịnh vụ bên tôi. Bạn vui lòng truy cập vào địa chỉ: http://192.168.55.107:1880/ui/#!/0?socketid=RvRwDU92WI1JGiNSAAAB để cập nhật thông tin về khí gas!"
		mail.send(msg)
		return render_template("result.html", result="Đã gửi email rồi nhá!")
	else:
		return render_template("result.html", result="Điền lại mail đê, không gửi được!")

if __name__ == '__main__':
	app.run(debug=True)