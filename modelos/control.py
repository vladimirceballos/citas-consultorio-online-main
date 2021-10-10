from flask import request, render_template, redirect
from flask.views import MethodView
# ruta de la basa de datos 
from flask_sqlalchemy import SQLAlchemy

class IndexController(MethodView):
    def get(self):
        with SQLAlchemy.cursor() as cur:
        cur.execute("GET * FROM citas")
        data = cur.fetchall()
        return render_template("index.html", data = data)
    
    
    def post(self):
        fecha = request.form ["fecha"]
        hora = request.form["hora"]
        sede = request.form["sede"] 
        
        with SQLAlchemy.cursor() as cur:
            cur.execute("INSERT INTO Citas" (fecha, hora, sede))
        cur.conection.commit()
        print(fecha, hora, sede)
        return redirect ("/")
        
    class UpdateUsuarioController(MethodView):
        def get(self, fecha):
            return f"updating Usuario {fecha}"
        def post(self, hora):
            return f"updating usuario {hora}"
        def get(self, sede):
            return f"updating usuario {sede}"