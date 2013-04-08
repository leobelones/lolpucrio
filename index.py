import webapp2


class index(webapp2.RequestHandler):
	def get(self):
		page = """
<html>
  <head>
    <title>LoL Puc-Rio</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Bootstrap -->
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
				              <li class="active"><a href="index">Inicio</a></li>
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
    <h1>N&atildeo tem conta?</h1>
	<p class="lead">N&atildeo seja por isso, cadastre-se agora!</p>
	<a class="btn btn-large btn-success" href="cadastro">Cadastro</a>
	<p class="lead"><br>Site para os jogadores de League of Legends da PUC-Rio!<br><br>Em breve: <br> -Montaremos equipes<br>-Organizaremos torneios<br><br><br>Sugest&otildees,<br>
					Cr&iacuteticas,<br>
					Quer me ajudar?
					</p>

	<a class="btn btn-large btn" href="contato">Contato</a>

		</div>
	</div>
    <script src="http://code.jquery.com/jquery.js"></script>
    <script src="js/bootstrap.min.js"></script>
  </body>
</html>
"""
		self.response.write(page)

app = webapp2.WSGIApplication([('/index', index),('/', index)],
                              debug=True)	
		        		
