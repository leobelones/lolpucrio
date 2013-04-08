import webapp2


class contato(webapp2.RequestHandler):
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
				              <li><a href="index">Inicio</a></li>
				              <li><a href="cadastro">Cadastro</a></li>
				              <li><a href="membros">Membros</a></li>
				              <li class="active"><a href="contato">Contato</a></li>
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
    <h1>Leonardo Kaplan</h1>
	<p class="lead">contato dot leonardokaplan at gmail dot com<br></p>
				Estou usando Python 2.7 e Google App Engine

				
	

		</div>
	</div>
    <script src="http://code.jquery.com/jquery.js"></script>
    <script src="js/bootstrap.min.js"></script>
  </body>
</html>
"""
		self.response.write(page)

app = webapp2.WSGIApplication([('/contato', contato)],
                              debug=True)	
		        		
