import webapp2
from google.appengine.ext import db

f = open('inicio', 'r')		
inicio = f.read()
f = open('fim', 'r')		
fim = f.read()

class Mensagem(db.Model):
	texto = db.StringProperty()

class forum(webapp2.RequestHandler):
	def get(self):
		self.response.out.write(inicio)	
		x = Mensagem.all()
		mensagens = "" 
		for msg in x:
			mensagens += "<tr>" + msg.texto + "<br></tr>"

		self.response.out.write("""
			              <form action="/forum" method="post">
		      	<fieldset>
		       	<input type="text" placeholder="Digite sua mensagem" name="texto"><br>
		       	<input type="submit" value="Submeter" class="btn">
		       	</fieldset>
		       	</form>
		       	<table class="table"> <thead></thead> 
        			<tbody>  
        			<p>%s</p>
		      
		      	"""%mensagens
		)
		self.response.write(fim)


		self.response.write(fim)
	def post(self):
		msg = Mensagem()
		a = self.request.get("texto")
		if a != "":
			msg.texto = a
			msg.put()
		self.get()



app = webapp2.WSGIApplication([('/forum', forum)])
