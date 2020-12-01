from flask import Flask 
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin
from beans.myq import MySql
from beans.validator import Validator
import datetime

app = Flask(__name__) 
cors = CORS(app, resources={r"/": {"origins": "*"}})

# ROTAS

@app.route("/") 
@cross_origin(origin='*',headers=['Content- Type','Authorization'])
def home(): 
    return "API - V.1.0.0 "

@app.route("/users", methods=['POST']) 
@cross_origin(origin='http://localhost:4200',headers=['Content- Type','Authorization'])
def users(): 
    #recupera itens de json enviados por post
    body = request.get_json()
    #recupera a key hascode enviada por get
    hascode = request.args.get('hascode')

    # Implementação do método GET
    if request.method == 'GET':
        try:
            # Verificação se o usuário está logado
            if(not Validator().checkHash(hascode)):
                return jsonify({"error": "Usuário sem permissão de acesso!"})
            db = MySql()
            query = db.select('users', orderby="id desc")
            return jsonify(query)
        except:
            jsonify({"error": "Erro de requisição!"})
            
    # Implementação do método POST
    elif request.method == 'POST':
        try:
            db = MySql()
            body['dtupdate'] = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            body['hascode'] = Validator().getHascode(body['login'], body['senha'])
            del body['senha']
            del body['login']
            id = db.insert('users', body)
            query = db.select('users', where='id="%s"' % str(id), first= True)
            return jsonify(query)
        except:
            return jsonify({"error": "Erro de requisição!"})
    else:
        return jsonify({"error": 'Método não implementado!'})

@app.route("/login", methods=['POST']) 
@cross_origin(origin='http://localhost:4200',headers=['Content- Type','Authorization'])
def login(): 
    body = request.get_json()
    validator = Validator()
    
    if request.method == 'POST':
        try:
            m = MySql()
            user = validator.login(body['login'],body['senha'])
            if(bool(user)):
                return jsonify(user)
            return jsonify({"error":"Usuário não identificado!"})
            
        except Exception as e:
            print(e)
            return jsonify({"error": "Erro de login!"})
    else:
        return jsonify({"error": "Método não aceito!"}) 

@app.route("/temperature", methods=['GET','POST']) 
@cross_origin(origin='*',headers=['Content- Type','Authorization'])
def temperature(): 
    #recupera itens de json enviados por post
    body = request.get_json()
    #recupera a key hascode enviada por get
    hascode = request.args.get('hascode')
    
    # Verificação se o usuário está logado
    if(not Validator().checkHash(hascode)):
        return jsonify({"error": "Usuário sem permissão de acesso!"})
    
    # Implementação do método GET
    if request.method == 'GET':
        try:
            db = MySql()
            query = db.select('temperature', orderby="id desc")
            return jsonify(query)
        except:
            jsonify({"error": "Erro de requisição!"})
            
    # Implementação do método POST
    elif request.method == 'POST':
        try:
            db = MySql()
            body['dtupdate'] = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            id = db.insert('temperature', body)
            query = db.select('temperature', where='id="%s"' % str(id), first= True)
            return jsonify(query)
        except:
            return jsonify({"error": "Erro de requisição!"})
    else:
        return jsonify({"error": 'Método não implementado!'})
    
@app.route("/motor", methods=['GET','POST']) 
@cross_origin(origin='*',headers=['Content- Type','Authorization'])
def motor(): 
    #recupera itens de json enviados por post
    body = request.get_json()
    #recupera a key hascode enviada por get
    hascode = request.args.get('hascode')
    
    # Verificação se o usuário está logado
    if(not Validator().checkHash(hascode)):
        return jsonify({"error": "Usuário sem permissão de acesso!"})
    
    # Implementação do método GET
    if request.method == 'GET':
        try:
            db = MySql()
            query = db.select('motor', orderby="id desc")
            return jsonify(query)
        except:
            jsonify({"error": "Erro de requisição!"})
            
    # Implementação do método POST
    elif request.method == 'POST':
        try:
            db = MySql()
            body['dtupdate'] = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            id = db.insert('motor', body)
            query = db.select('motor', where='id="%s"' % str(id), first= True)
            return jsonify(query)
        except:
            return jsonify({"error": "Erro de requisição!"})
    else:
        return jsonify({"error": 'Método não implementado!'})

@app.route("/microswitch", methods=['GET','POST']) 
@cross_origin(origin='*',headers=['Content- Type','Authorization'])
def microswitch(): 
    #recupera itens de json enviados por post
    body = request.get_json()
    #recupera a key hascode enviada por get
    hascode = request.args.get('hascode')
    
    # Verificação se o usuário está logado
    if(not Validator().checkHash(hascode)):
        return jsonify({"error": "Usuário sem permissão de acesso!"})
    
    # Implementação do método GET
    if request.method == 'GET':
        try:
            db = MySql()
            query = db.select('microswitch', orderby="id desc")
            return jsonify(query)
        except:
            jsonify({"error": "Erro de requisição!"})
            
    # Implementação do método POST
    elif request.method == 'POST':
        try:
            db = MySql()
            body['dtupdate'] = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            id = db.insert('microswitch', body)
            query = db.select('microswitch', where='id="%s"' % str(id), first= True)
            return jsonify(query)
        except:
            return jsonify({"error": "Erro de requisição!"})
    else:
        return jsonify({"error": 'Método não implementado!'})

@app.route("/cooler", methods=['GET','POST']) 
@cross_origin(origin='*',headers=['Content- Type','Authorization'])
def cooler(): 
    #recupera itens de json enviados por post
    body = request.get_json()
    #recupera a key hascode enviada por get
    hascode = request.args.get('hascode')
    
    # Verificação se o usuário está logado
    if(not Validator().checkHash(hascode)):
        return jsonify({"error": "Usuário sem permissão de acesso!"})
    
    # Implementação do método GET
    if request.method == 'GET':
        try:
            db = MySql()
            query = db.select('cooler', orderby="id desc")
            return jsonify(query)
        except:
            jsonify({"error": "Erro de requisição!"})
            
    # Implementação do método POST
    elif request.method == 'POST':
        try:
            db = MySql()
            body['dtupdate'] = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            id = db.insert('cooler', body)
            query = db.select('cooler', where='id="%s"' % str(id), first= True)
            return jsonify(query)
        except:
            return jsonify({"error": "Erro de requisição!"})
    else:
        return jsonify({"error": 'Método não implementado!'})
 
@app.route("/level", methods=['GET','POST']) 
@cross_origin(origin='*',headers=['Content- Type','Authorization'])
def level(): 
    #recupera itens de json enviados por post
    body = request.get_json()
    #recupera a key hascode enviada por get
    hascode = request.args.get('hascode')
    
    # Verificação se o usuário está logado
    if(not Validator().checkHash(hascode)):
        return jsonify({"error": "Usuário sem permissão de acesso!"})
    
    # Implementação do método GET
    if request.method == 'GET':
        try:
            db = MySql()
            query = db.select('level', orderby="id desc")
            return jsonify(query)
        except:
            jsonify({"error": "Erro de requisição!"})
            
    # Implementação do método POST
    elif request.method == 'POST':
        try:
            db = MySql()
            body['dtupdate'] = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            id = db.insert('level', body)
            query = db.select('level', where='id="%s"' % str(id), first= True)
            return jsonify(query)
        except:
            return jsonify({"error": "Erro de requisição!"})
    else:
        return jsonify({"error": 'Método não implementado!'})
  
@app.route("/input_a", methods=['GET','POST']) 
@cross_origin(origin='*',headers=['Content- Type','Authorization'])
def input_a(): 
    #recupera itens de json enviados por post
    body = request.get_json()
    #recupera a key hascode enviada por get
    hascode = request.args.get('hascode')
    
    # Verificação se o usuário está logado
    if(not Validator().checkHash(hascode)):
        return jsonify({"error": "Usuário sem permissão de acesso!"})
    
    # Implementação do método GET
    if request.method == 'GET':
        try:
            db = MySql()
            query = db.select('input_a', orderby="id desc")
            return jsonify(query)
        except:
            jsonify({"error": "Erro de requisição!"})
            
    # Implementação do método POST
    elif request.method == 'POST':
        try:
            db = MySql()
            body['dtupdate'] = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            id = db.insert('input_a', body)
            query = db.select('input_a', where='id="%s"' % str(id), first= True)
            return jsonify(query)
        except:
            return jsonify({"error": "Erro de requisição!"})
    else:
        return jsonify({"error": 'Método não implementado!'})
  
@app.route("/input_b", methods=['GET','POST']) 
@cross_origin(origin='*',headers=['Content- Type','Authorization'])
def input_b(): 
    #recupera itens de json enviados por post
    body = request.get_json()
    #recupera a key hascode enviada por get
    hascode = request.args.get('hascode')
    
    # Verificação se o usuário está logado
    if(not Validator().checkHash(hascode)):
        return jsonify({"error": "Usuário sem permissão de acesso!"})
    
    # Implementação do método GET
    if request.method == 'GET':
        try:
            db = MySql()
            query = db.select('input_b', orderby="id desc")
            return jsonify(query)
        except:
            jsonify({"error": "Erro de requisição!"})
            
    # Implementação do método POST
    elif request.method == 'POST':
        try:
            db = MySql()
            body['dtupdate'] = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            id = db.insert('input_b', body)
            query = db.select('input_b', where='id="%s"' % str(id), first= True)
            return jsonify(query)
        except:
            return jsonify({"error": "Erro de requisição!"})
    else:
        return jsonify({"error": 'Método não implementado!'})
  
@app.route("/output_a", methods=['GET','POST']) 
@cross_origin(origin='*',headers=['Content- Type','Authorization'])
def output_a(): 
    #recupera itens de json enviados por post
    body = request.get_json()
    #recupera a key hascode enviada por get
    hascode = request.args.get('hascode')
    
    # Verificação se o usuário está logado
    if(not Validator().checkHash(hascode)):
        return jsonify({"error": "Usuário sem permissão de acesso!"})
    
    # Implementação do método GET
    if request.method == 'GET':
        try:
            db = MySql()
            query = db.select('output_a', orderby="id desc")
            return jsonify(query)
        except:
            jsonify({"error": "Erro de requisição!"})
            
    # Implementação do método POST
    elif request.method == 'POST':
        try:
            db = MySql()
            body['dtupdate'] = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            id = db.insert('output_a', body)
            query = db.select('output_a', where='id="%s"' % str(id), first= True)
            return jsonify(query)
        except:
            return jsonify({"error": "Erro de requisição!"})
    else:
        return jsonify({"error": 'Método não implementado!'})
  
@app.route("/acionamentomotor", methods=['GET','POST']) 
@cross_origin(origin='*',headers=['Content- Type','Authorization'])
def acionamentomotor(): 
    #recupera itens de json enviados por post
    body = request.get_json()
    #recupera a key hascode enviada por get
    hascode = request.args.get('hascode')
    motor = request.args.get('motor')
    
    # Verificação se o usuário está logado
    if(not Validator().checkHash(hascode)):
        return jsonify({"error": "Usuário sem permissão de acesso!"})
    
    # Implementação do método GET
    if request.method == 'GET':
        try:
            db = MySql()
            if bool(motor):
                query = db.select('acionamento_motor', where='idmotor="%s"' % motor)
            else:
                query = db.select('acionamento_motor')
            return jsonify(query)
        except:
            jsonify({"error": "Erro de requisição!"})
            
    # Implementação do método POST
    elif request.method == 'POST':
        try:
            db = MySql()
            body['dtupdate'] = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            id = db.insert('acionamento_motor', body)
            query = db.select('acionamento_motor', where='id="%s"' % str(id), first= True)
            return jsonify(query)
        except:
            return jsonify({"error": "Erro de requisição!"})
    else:
        return jsonify({"error": 'Método não implementado!'})
  
# Rotina principal de execução do WS    
if __name__ == '__main__':
    app.run()