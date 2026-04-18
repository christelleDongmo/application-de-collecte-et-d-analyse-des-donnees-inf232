from flask import Flask, render_template,request

app=Flask(__name__)

@pp.route('/', methods=['GET , POST'])
def index():
    if request.method == 'POST':


        return "Donnees recues avec succes !"
    return render_template("index.html")

if __name__=='__main__':
    app.run(debug=True)