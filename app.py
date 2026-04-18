from flask import Flask, render_template,request
import pandas as pd 
import os 
app=Flask(__name__)
DATA_FILE='donnees etudiants.csv'

@app.route('/', methods=['GET' , 'POST'])
def index():
    if request.method == 'POST':
        nouvelle_donnee={
        'sexe': request.form.get('sexe'),
        'sommeil': request.form.get('sommeil'),
        'travail': request.form.get('travail'),
        'stress': request.form.get('stress'),
        'assiduite':request.form.get('assiduite'),
        'moyenne':request.form.get('moyenne')
         }
        df = pd.DataFrame([nouvelle_donnee])
        if not os.path.exists(DATA_FILE):
         df.to_csv(DATA_FILE, index=False)
        else:
         df.to_csv(DATA_FILE, mode='a', header=False,index=False)

        return "Merci ! Tes donnees ont ete enregistrees avec succes."
    return render_template("index.html")

if __name__=='__main__':
    app.run(debug=True)