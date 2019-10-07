from flask import Flask,render_template,request
import requests

api_key ="e3e50ae10a1772bbef889b17c9c3e379"
url ="http://data.fixer.io/api/latest?access_key=" + api_key

app = Flask(__name__)
@app.route("/",methods = ["GET","POST"])
def index():
    if request.method =="POST":
       firstCurrency = request.form.get("firstCurrency")#USD
       secondCurrency = request.form.get("secondCurrency")#TRY
       amount = request.form.get("amount")
       response = requests.get(url)#bu responun degeri 200 kodlu bir response olacak
       app.logger.info(response)
       infos = response.json()
       

       firstValue = infos["rates"][firstCurrency] #diyelimki Usd sectik bu veri 1.23 mis 
       secondValue = infos["rates"][secondCurrency]# try de 4.69 mus 
       result = (secondValue/firstValue)*float(amount)
       currencyInfo = dict()
       currencyInfo["firstCurrency"]=firstCurrency
       currencyInfo["secondCurrency"] = secondCurrency
       currencyInfo["amount"] = amount 
       currencyInfo["result"] = result
       return render_template("index.html",info = currencyInfo)
       #app.logger.info(infos)

    else:
        return render_template("index.html")
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug = True)
