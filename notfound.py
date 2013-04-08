import webapp2


class notfound(webapp2.RequestHandler):
	def get(self):
		page = """
<html>
  <head>
    <title>Opa</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Bootstrap -->
    <link href="css/bootstrap.min.css" rel="stylesheet" media="screen">
  
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
    <h1>Opa Opa Opa</h1>
	<p class="lead">Essa pagina n&atildeo existe</p>
	</div>
	</div>
    <script src="http://code.jquery.com/jquery.js"></script>
    <script src="js/bootstrap.min.js"></script>
  </body>
</html>
"""
		self.response.write(page)

app = webapp2.WSGIApplication([('/.*', notfound)],
                              debug=True)	
		        		