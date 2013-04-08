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
	Rankedd = db.StringProperty()
	ARAM = db.StringProperty()

incio = """
<!DOCTYPE>
<html>
  <head>
    <title>LoL Puc-Rio</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Bootstrap -->
    <meta charset="utf-8" />
    <link href="css/bootstrap.min.css" rel="stylesheet" media="screen">
  	<div class="navbar navbar-inverse navbar-fixed-top">
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
				              <li><a href="cadastro">Cadastro</a></li>
				              <li class="active"><a href="membros">Membros</a></li>
				              <li><a href="contato">Contato</a></li>
				            </ul>
				          </div><!--/.nav-collapse -->
				        </div>
				      </div>
				    </div>
  </head>
  <body>
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
    			<div class="jumbotron">"""

class membros(webapp2.RequestHandler):
	def get(self):
		tat = ""
		x = Usuario.all()
		for usr in x:
			t = "<tr>" 
			t += "<td>" + str(usr.nomerl.encode('utf-8')) + "</td>"  
			t += "<td>" + str(usr.nomelol.encode('utf-8')) + "</td>"  
			t += "<td>" + str(usr.lvl) + "</td>"  
			t += "<td>" + str(usr.liga) + "</td>"  
			t += "<td>" + str(usr.tier) + "</td>"  
			t += "<td>" + str(usr.Top) + " " + str(usr.Mid) + " " + str(usr.ADC) + " " + str(usr.Support ) + " " + str(usr.Jungler) + "</td>" 
			t += "<td>" + str(usr.Normal3) + " " + str(usr.Ranked3) + " " + str(usr.Normal5) + " " + str(usr.Ranked5) + str(usr.Normald) + " " + str(usr.Rankedd) + " " + str(usr.ARAM) + "</td>"  
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
		</div>
	</div>
    <script src="http://code.jquery.com/jquery.js"></script>
    <script src="js/bootstrap.min.js"></script>
  </body>
</html>
"""%tat
		
		self.response.write(incio)
		self.response.write(page)

app = webapp2.WSGIApplication([('/membros', membros)],
                              debug=True)	
		        		
