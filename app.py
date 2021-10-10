import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://jjbocsmdipegxk:3d71afcd6756199393a25037b52dd43d576770b44a15464c72947aec12865130@ec2-52-0-93-3.compute-1.amazonaws.com:5432/d7fvitj0ia8476'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from rutas import *

if __name__ == '__main__':
    from rutas import *

    app.run(host='0.0.0.0', port=5000)
