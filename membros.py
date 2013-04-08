import webapp2
import urllib
from google.appengine.ext import db

class Usuario(db.Model):
	nomerl = db.StringProperty()
	nomelol = db.StringProperty()
	lvl = db.IntegerProperty()
	liga = db.StringProperty()
	tier = db.StringProperty()

	Top = db.StringProperty()
	Mid = db.StringProperty()
	ADC = db.StringProperty()
	Support = db.StringProperty()
	Jungler = db.StringProperty()

	Normal3 = db.StringProperty()
	Ranked3 = db.StringProperty() 
	Normal5 = db.StringProperty() 
	Ranked5 = db.StringProperty() 
	Normald = db.StringProperty()
	ARAM = db.StringProperty()



class membros(webapp2.RequestHandler):
	def get(self):
		f = open('inicio', 'r')		
		inicio = f.read()
		f = open('fim', 'r')		
		fim = f.read()
		tat = ""
		x = Usuario.all()
		for usr in x:
			t = "<tr>" 
			t += "<td>" + str(usr.nomerl.encode('utf-8')) + "</td>"  
			t += "<td>" + str(usr.nomelol.encode('utf-8')) + "</td>"  
			t += "<td>" + str(usr.lvl) + "</td>"  
			t += "<td>" + str(usr.liga) + "</td>"  
			t += "<td>" + str(usr.tier) + "</td>"  
			t += "<td>" + str(usr.Top) + "<br>" + str(usr.Mid) + "<br>" + str(usr.ADC) + "<br>" + str(usr.Support ) + "<br>" + str(usr.Jungler) + "</td>" 
			t += "<td>" + str(usr.Normal3) + "<br>" + str(usr.Ranked3) + "<br>" + str(usr.Normal5) + "<br>" + str(usr.Ranked5) + str(usr.Normald) + "<br>" + str(usr.ARAM) + "</td>"  
			t += "</tr>"
			tat = tat + " " + t 

		page = """

    <h1>Membros:</h1>
	<table class="table">  
        <thead>  
          <tr>  
            <th>Nome na RL</th>  
            <th>Nome no LoL</th>  
            <th>Level</th>  
            <th>Liga</th>
            <th>Tier</th>
            <th>Role(s)</th>  
            <th>Tipo de partida</th>   
          </tr>  
        </thead> 
        <tbody>  
        	%s</p>
		
"""%tat
		
		self.response.write(inicio)
		self.response.write(page)
		self.response.write(fim)

app = webapp2.WSGIApplication([('/membros', membros)],
                              debug=True)	
		        		
