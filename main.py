from flask import Flask, render_template, request, make_response
import email_engine
import os

app = Flask(__name__ , template_folder="html/templates", static_folder="html/static")

@app.route("/")
def home():
	domain = request.args.get('domain')
	mails = []
	if domain:
		mails = email_engine.get_emails(domain)
		
	return render_template('index.html',mails = mails)

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(debug=True, port=port)