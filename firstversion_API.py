from flask import Flask, jsonify, request
import json,csv


app = Flask(__name__)


list_of_transactions = []

@app.route('/hello')
def aff():
    return "Hello"	 

#------------------------------------------------------------------------------------------------------------------------------------------------------------
#E1 - Enregistrer une transaction
#curl --X POST -H "Content-type:application/json" --data-binary "{\"sender\":\"Pepa\",\"receiver\":\"Salma\",\"Amount\":100.0,\"date\":\"2023-01-11\"}" http://localhost:5000/record
#curl --X POST -H "Content-type:application/json" --data-binary "{\"sender\":\"Waren\",\"receiver\":\"Salma\",\"Amount\":200.0,\"date\":\"2023-01-12\"}" http://localhost:5000/record
#curl --X POST -H "Content-type:application/json" --data-binary "{\"sender\":\"Ryane\",\"receiver\":\"Tom\",\"Amount\":150.0,\"date\":\"2023-01-13\"}" http://localhost:5000/record
#curl --X POST -H "Content-type:application/json" --data-binary "{\"sender\":\"Salma\",\"receiver\":\"Albert\",\"Amount\":70.0,\"date\":\"2023-01-14\"}" http://localhost:5000/record
@app.route('/record' , methods = ['POST'])
def add():
    data = request.get_json()
    format = {
		'date' : data['date'], 
		'sender':data['sender'],
		'receiver':data['receiver'],
		'Amount':data['Amount']
	}
    list_of_transactions.append(format)
    return "Magnifique"

#------------------------------------------------------------------------------------------------------------------------------------------------------------
#E2 - Afficher une liste de toutes les transactions dans l’ordre chronologique en fonction de la date
@app.route('/display' , methods = ['GET'])
def index():
    list_of_transactions.sort(key=lambda x: x['date'])
    return jsonify(list_of_transactions)

#------------------------------------------------------------------------------------------------------------------------------------------------------------
#E3 - Afficher une liste des transactions dans l’ordre chronologique liées à une personne
#curl http://localhost:5000/display_for_someone?p=Salma
#Le resultat apparaitra dans la console
@app.route('/display_for_someone' , methods = ['GET'])
def a():
    p = request.args.get("p")
    if p:
      p_transactions = [i for i in list_of_transactions if i['receiver']==p]
      p_sorted = sorted(p_transactions,key=lambda x: x['date'])
      return str(p_sorted)	 
    return " "

#------------------------------------------------------------------------------------------------------------------------------------------------------------

#E4 - Afficher le solde du compte de la personne
#curl http://localhost:5000/display_balance_of_someone?p=Salma
@app.route('/display_balance_of_someone' , methods = ['GET'])
def b():
    p = request.args.get("p")
    if p:
      p_transactions = [i for i in list_of_transactions if i['sender']==p]
      balance1 = sum([i['Amount'] for i in p_transactions])
      
      p_transactions = [i for i in list_of_transactions if i['receiver']==p]
      balance2 = sum([i['Amount'] for i in p_transactions])
	
      if balance1>balance2 :
       newbalance = balance2 - balance1
       return "Prennez garde vous avez dépassé le plafond. Pensez à rechager votre compte. Compte:" + str(newbalance)

      if balance2>balance1 :
       newbalance = balance2 - balance1
       return "Compte:"+str(newbalance)
      return " "

#------------------------------------------------------------------------------------------------------------------------------------------------------------
#E5 - Importer des données depuis un fichier csv.
with open('fichier.csv') as file:
	reader = csv.reader(file)
	header = next(reader)
	for i in reader:
		sender,receiver,Amount,date=i
		list_of_transactions.append({"sender":sender,"receiver":receiver,"Amount":float(Amount),"date":date})
#-------------------------------------------------------------------------------------------------------------------------------------------------------------		

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == "check_syntax":
            print("Build [ OK ]")
            exit(0)
        else:
            print("Passed argument not supported ! Supported argument: check_syntax")
            exit(1)
		
    app.run(debug=True)
