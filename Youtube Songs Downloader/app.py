from flask import Flask,render_template,request
from downloader import download_song
from mailsender import send_mail
from createzip import create_zip

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def main_page():
    if request.method == "POST":
        keyword = request.form['keyword'].replace(' ','').lower()
        emailid = request.form['emailid']
        limit = int(request.form['limit'])
        download_song(keyword,limit)
        create_zip()
        send_mail(emailid)
        # print(keyword,emailid,limit)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True,port=8000)