import webapp2
from google.appengine.ext import db

f = open('inicio', 'r')		
inicio = f.read()
f = open('fim', 'r')		
fim = f.read()

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

class cadastro(webapp2.RequestHandler):
	def get(self):
		#inicio e estilo
		self.response.out.write(inicio)	
		######### montando os dropdowns ##############
		lvl = ""
		tier = """
			<option value="Sem Tier">Sem Tier</option>
			<option value="VII">VII</option>
			<option value="VI">VI</option>
			<option	value="V">V</option>
			<option	value="IV">IV</option>
			<option value="III">III</option>
			<option	value="II">II</option>
			<option	value="I">I</option>


			"""
		liga = """
			<option value="Sem Liga">Sem Liga</option>
			<option	value = "Bronze">Bronze</option>
			<option	value = "Prata">Prata</option>
			<option	value = "Ouro">Ouro</option>
			<option	value = "Platina">Platina</option>
			<option	value = "Diamante">Diamante</option>
	"""
		for i in range(1,31):
		     lvl = lvl+ " " +"<option value=\"%d\">%d</option>" % (i,i)

		######## aqui comecamos a montar a pagina #############
		#chamando a biblioteca q valida
		self.response.out.write("""<script type="text/javascript" src="validate.min.js"></script>""")
		self.response.out.write("""
			              <form action="/bd" method="post" name="form_cadastro">
		      	<fieldset>
		      	
		      	<legend><h1>Cadastro:</h1></legend>  
		      	
				      	<input type="text" placeholder="Nome na RL (e sobrenome)" name="nomerl" >
				      	<br>
				      	<input type="text" placeholder="Nick no LoL" name="nomelol" >
				      	<br>
			     
		      	<span class="help-block">N&atildeo esque&ccedila das mai&uacutesculas!</span>
		      	

		      	Level: <select name="lvl">%s</select>	
		      	<br>
		      	Elo: <select name="liga">%s</select>	<select name="tier">%s</select>	<br>
		      	""" % (lvl,liga,tier))
		

		self.response.out.write("""<br><legend>Role:</legend>
		      	
		      	<label class="checkbox inline"><input type="checkbox" name="Top" value="Top">Top</label><br>
		      	<label class="checkbox inline"><input type="checkbox" name="Mid" value="Mid">Mid</label><br>
		      	<label class="checkbox inline"><input type="checkbox" name="ADC" value="ADC">ADC</label><br>
		      	<label class="checkbox inline"><input type="checkbox" name="Support" value="Support">Support</label><br>
		      	<label class="checkbox inline"><input type="checkbox" name="Jungler" value="Jungler">Jungler</label><br>
		      	
		      	<br><legend>Tipo de partida:</legend>
		      	
		      	
		      	<label class="checkbox inline"><input type="checkbox" name="3x3 Normal" value="3x3 Normal">3x3 Normal  </label>
		      	<label class="checkbox inline"><input type="checkbox" name="3x3 Ranked" value="3x3 Ranked">3x3 Ranked  </label><br>
		      	<label class="checkbox inline"><input type="checkbox" name="5x5 Normal" value="5x5 Normal">5x5 Normal  </label>
		      	<label class="checkbox inline"><input type="checkbox" name="5x5 Ranked" value="5x5 Ranked">5x5 Ranked  </label><br>
		      	
		      	<label class="checkbox inline"><input type="checkbox" name="Dominion Normal" value="Dominion Normal">Dominion Normal  </label>
		        <label class="checkbox inline"><input type="checkbox" name="ARAM" value="ARAM">ARAM  </label><br>
		        
		      	
		      	</fieldset>
		      	<br><el></el>
		        <input type="submit" value="Submeter" class="btn">
		      </form>""")
				
		#com o form montado, podemos dizer como valida-lo
	

		self.response.write(fim)

class bd(webapp2.RequestHandler):
	def post(self):
		usr = Usuario()
		usr.nomerl  = self.request.get("nomerl")
		usr.nomelol  = self.request.get("nomelol") 
		usr.lvl  = int(self.request.get("lvl"))
		usr.liga  = self.request.get("liga") 
		usr.tier  = self.request.get("tier")
		usr.Top  = self.request.get("Top")
		usr.Mid  = self.request.get("Mid")  
		usr.ADC  = self.request.get("ADC") 
		usr.Support  = self.request.get("Support") 
		usr.Jungler  = self.request.get("Jungler")
		usr.Normal3  = self.request.get("3x3 Normal") 
		usr.Ranked3  = self.request.get("3x3 Ranked") 
		usr.Normal5  = self.request.get("5x5 Normal") 
		usr.Ranked5  = self.request.get("5x5 Ranked") 
		usr.Normald  = self.request.get("Dominion Normal")
		usr.ARAM  = self.request.get("ARAM")
		usr.put()




		self.response.out.write(inicio + "<h1>O seguinte usuario foi incluido no sistema:</h1><br><p class=\"lead\"> ")
		cad = self.request.get("nomerl") + " " + self.request.get("nomelol") + " " + self.request.get("lvl") + " " + self.request.get("liga") + " " + self.request.get("tier")
		role = self.request.get("Top") + " " + self.request.get("Mid") + " " + self.request.get("ADC") + " " + self.request.get("Support") + " " + self.request.get("Jungler")
		part = self.request.get("3x3 Normal") + " " + self.request.get("3x3 Ranked") + " " + self.request.get("5x5 Normal") + " " + self.request.get("5x5 Ranked") + " " + self.request.get("Dominion Normal")+ " " + self.request.get("ARAM")
		self.response.out.write(cad + "<br>")
		self.response.out.write(role + "<br>")
		self.response.out.write(part + "<br>")
		self.response.out.write('</p>')
		self.response.write(fim)


app = webapp2.WSGIApplication([('/cadastro', cadastro),('/bd',bd)])
