import webapp2
from google.appengine.ext import db

inicio = """
        	<html>
	        	<link href="css/bootstrap.min.css" rel="stylesheet" media="screen">
	        	<head>
		        	<div class="navbar navbar-inverse navbar-fixed-Top">
				      <div class="navbar-inner">
				        <div class="container">
				          <button type="button" class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
				            <span class="icon-bar"></span>
				            <span class="icon-bar"></span>
				            <span class="icon-bar"></span>
				          </button>
				          <a class="brand" href="index">LoL Puc-Rio</a>
				          <div class="nav-collapse collapse">
				            <ul class="nav">
				              <li><a href="index">Inicio</a></li>
				              <li class="active"><a href="cadastro">Cadastro</a></li>
				              <li><a href="membros">Membros</a></li>
				              <li><a href="contato">Contato</a></li>
				            </ul>
				          </div><!--/.nav-collapse -->
				        </div>
				      </div>
				    </div>
   				</head>
	        	<body>
	        		<script src="http://code.jquery.com/jquery.js"></script>
	    		<script src="js/bootstrap.min.js"></script>
	    		  <style type="text/css">
					      body {
					        padding-Top: 20px;
					        padding-bottom: 40px;
					      }

					      /* Custom container */
					      .container-narrow {
					        margin: 0 auto;
					        max-width: 700px;
					      }
					      .container-narrow > hr {
					        margin: 30px 0;
					      }

					      /* Main marketing message and sign up button */
					      .jumbotron {
					        margin: 60px 0;
					        text-align: center;
					      }
					      .jumbotron h1 {
					        font-size: 72px;
					        line-height: 1;
					      }
					      .jumbotron .btn {
					        font-size: 21px;
					        padding: 14px 24px;
					      }

				</style>
				<div class="container-narrow">
    			<div class="jumbotron">
    		"""

class cadastro(webapp2.RequestHandler):
	def get(self):
		#inicio e estilo
		self.response.out.write(inicio)	

		lvl = ""
		tier = """
			<option value="VII">VII</option>
			<option value="VI">VI</option>
			<option	value="V">V</option>
			<option	value="IV">IV</option>
			<option value="III">III</option>
			<option	value="II">II</option>
			<option	value="I">I</option>


			"""
		liga = """
			<option	value = "Bronze">Bronze</option>
			<option	value = "Prata">Prata</option>
			<option	value = "Ouro">Ouro</option>
			<option	value = "Platina">Platina</option>
			<option	value = "Diamante">Diamante</option>

	
	"""
		for i in range(1,31):
		     lvl = lvl+ " " +"<option value=\"%d\">%d</option>" % (i,i)



		self.response.out.write("""
			              <form action="/bd" method="post">
		      	<fieldset>
		      	
		      	<legend><h1>Cadastro:</h1></legend>
		      	<input type="text" placeholder="Nome na RL (e sobrenome)" name="nomerl"><br>
		      	<input type="text" placeholder="Nick no LoL" name="nomelol"><br>
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
		      	
		      	<label class="checkbox ">
		      	<label class="checkbox inline"><input type="checkbox" name="3x3 Normal" value="3x3 Normal">3x3 Normal  </label>
		      	<label class="checkbox inline"><input type="checkbox" name="3x3 Ranked" value="3x3 Ranked">3x3 Ranked  </label><br>
		      	<label class="checkbox inline"><input type="checkbox" name="5x5 Normal" value="5x5 Normal">5x5 Normal  </label>
		      	<label class="checkbox inline"><input type="checkbox" name="5x5 Ranked" value="5x5 Ranked">5x5 Ranked  </label><br>
		      	
		      	<label class="checkbox inline"><input type="checkbox" name="Dominion Normal" value="Dominion Normal">Dominion Normal  </label>
		        <label class="checkbox inline"><input type="checkbox" name="ARAM" value="ARAM">ARAM  </label><br>
		        </label>
		      	
		      	</fieldset>
		      	<br>
		        <input type="submit" value="Submeter" class="btn">
		      </form>""")

		self.response.out.write('</div></div></body></html>')

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
		self.response.out.write('</p></div></div></body></html>')

app = webapp2.WSGIApplication([('/cadastro', cadastro),('/bd',bd)])
