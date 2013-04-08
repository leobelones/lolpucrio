import cgi

from google.appengine.api import users
from google.appengine.ext import webapp2
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db

class MainPage(webapp.RequestHandler):
	def get(self):
		#inicio e estilo
		self.response.out.write("""
        	<html>
	        	<link href="css/bootstrap.min.css" rel="stylesheet" media="screen">
	        	<head>
		        	<div class="navbar navbar-inverse navbar-fixed-top">
				      <div class="navbar-inner">
				        <div class="container">
				          <button type="button" class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
				            <span class="icon-bar"></span>
				            <span class="icon-bar"></span>
				            <span class="icon-bar"></span>
				          </button>
				          <a class="brand" href="#">LoL Puc-Rio</a>
				          <div class="nav-collapse collapse">
				            <ul class="nav">
				              <li class="active"><a href="#">Inicio</a></li>
				              <li><a href="cadastro">Cadastro</a></li>
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
					        padding-top: 20px;
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
    	)

		lvl = ""
		tier = """
			<option>VII</option>
			<option>VI</option>
			<option>V</option>
			<option>IV</option>
			<option>III</option>
			<option>II</option>
			<option>I</option>
			"""
		liga = """
			<option>Bronze</option>
			<option>Prata</option>
			<option>Ouro</option>
			<option>Platina</option>
			<option>Diamante</option>
			"""
		for i in range(1,31):
		     lvl = lvl+"<option>%d</option>" % i



		self.response.out.write("""
			              <form action="/sign" method="post">
		      	<fieldset>
		      	<legend>Cadastro:</legend>
		      	<input type="text" placeholder="Nome na RL"><br>
		      	<input type="text" placeholder="Nick no LoL"><br>
		      	<span class="help-block">N&atildeo esque&ccedila das mai&uacutesculas!</span>
		      	Level: <select>%s</select>	
		      	<br>
		      	Elo: <select>%s</select>	<select>%s</select>	<br>
		      	""" % (lvl,liga,tier))
		self.response.out.write("""<legend>Role:</legend>
		      	
		      	<label class="checkbox inline"><input type="checkbox">Top</label><br>
		      	<label class="checkbox inline"><input type="checkbox">Mid</label><br>
		      	<label class="checkbox inline"><input type="checkbox">ADC</label><br>
		      	<label class="checkbox inline"><input type="checkbox">Support</label><br>
		      	<label class="checkbox inline"><input type="checkbox">Jungler</label><br>
		      	
		      	<legend>Tipo de partida:</legend>
		      	
		      	<label class="checkbox ">
		      	<label class="checkbox inline"><input type="checkbox">3x3 Normal   </label>
		      	<label class="checkbox inline"><input type="checkbox">3x3 Ranked   </label><br>
		      	<label class="checkbox inline"><input type="checkbox">5x5 Normal  </label>
		      	<label class="checkbox inline"><input type="checkbox">5x5 Ranked  </label><br>
		      	
		      	<label class="checkbox inline"><input type="checkbox">Dominion Normal  </label>
		        <label class="checkbox inline"><input type="checkbox">Dominion Ranked  </label><br>
		        <label class="checkbox inline"><input type="checkbox">ARAM  </label><br>
		        </label>
		      	
		      	</fieldset>

		        <input type="submit" value="Submeter" class="btn">
		      </form>""")

		self.response.out.write('</div></div></body></html>')

app = webapp2.WSGIApplication([('/', MainPage)])
