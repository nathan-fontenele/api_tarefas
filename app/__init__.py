from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

from app import routes  # Importa as rotas após a inicialização do app
