from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, resources={r"/rota/*": {"origins": "*"}})

morse ={
    "" : "",
    "A" : ".-",
    "B" : "-...",
    "C" : "-.-.",
    "D" : "-..",
    "E" : ".",
    "F" : "..-.",
    "G" : "--.",
    "H" : "....",
    "I" : "..",
    "J" : ".---",
    "K" : "-.-",
    "L" : ".-..",
    "M" : "--",
    "N" : "-.",
    "O" : "---",
    "P" : ".--.",
    "Q" : "--.-",
    "R" : ".-.",
    "S" : "...",
    "T" : "-",
    "U" : "..-",
    "V" : "...-",
    "W" : ".--",
    "X" : "-..-",
    "Y" : "-.--",
    "Z" : "--..",
    "1" : ".----",
    "2" : "..---",
    "3" : "...--",
    "4" : "....-",
    "5" : ".....",
    "6" : "-....",
    "7" : "--...",
    "8" : "---..",
    "9" : "----.",
    "0" : "-----",
    ".\n" : ".-.-.-",
    "," : "--..--",
    ":" : "---...",
    "?" : "..--..",
    "'" : ".----.",
    "-" : "-....-",
    "/" : "-..-.",
    "@" : ".--.-.",
    "\n<BT>\n" : "-...-",
    "<SN>" : "...-.",
    "<KN>" : "-.--."
}
new_morse = dict([(value, key) for key, value in morse.items()])

def decodifica(cifra):
  arrCod = cifra.split(',')
  arr = []
  for item in arrCod:
    if(item != 'None'):
      arr.append(new_morse[f"{item}"])
    else:
      arr.append(' ')
  return ''.join(arr)

def codificacaoMorse(codifica):
  arrCod = list(codifica)
  arr = []
  for item in arrCod:
    if (item.isalpha()):
      item = item.upper()
    
    arr.append(morse[f"{item}"])
  return ''.join(arr)


letras = 'a,b,e,t,y,@'
letrasArr = letras.split(',')
api = Api(app)
class morseCode(Resource):
    def get(self):
        tipo =request.args.get('tipo')

        if tipo == 'codifica':
            dataPost = codificacaoMorse(request.args.get('mourse'))
        elif tipo == 'decodifica':
            dataPost = decodifica(request.args.get('mourse'))
        else:
            return {'erro': 'Nao é opcao valida'}
        responseJson = {
            'status': 404,
            'msg': "Working",
            'api_response': dataPost
        }

        return jsonify(responseJson)


class identifica(Resource):
    def get(self):
        codigo = request.args.get('codigo')
        convertido = []
        for letra in codigo:
            conv = morse.get(letra)
            if conv:
                convertido.append(conv)
        return convertido
        

# @app.route('/')
# def index():
#     lendo = 'vc'
#     return f"Comi o cu de quem ta lendo: {lendo}"

api.add_resource(morseCode, '/rota')
api.add_resource(identifica, '/get')
if __name__ ==  "__main__":
    app.run(debug=True)


