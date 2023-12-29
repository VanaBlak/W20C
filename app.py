from flask import Flask, request, jsonify, make_response
from dbhelpers import run_statement, serialize_data
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)

@app.get("/api/animals")
def get_animals():
 try:
  result = run_statement('CALL flask_animal.get_animals()')
  print(result)
  format_data =serialize_data(["id", "name", "species"], result)
  return make_response(jsonify(format_data), 200)
 except Exception as error:
  return make_response(error, 500)
 

@app.get("/api/species/<string:species>")
def get_species(species):
 try:

  print(species)
  result = run_statement("CALL flask_animal.get_species(?)",[species])
  print(result)
  format_data =serialize_data(["id", "name", "species"], result)
  return make_response(jsonify(format_data), 200)
 except Exception as error:
  return make_response(error, 500)









@app.post("/api/test_post")
def test_two():
 try:
  return 'THIS IS A POS ROUJTET'
 except Exception as error:
  return make_response(error, 200)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
