import webapp2


class contato(webapp2.RequestHandler):
	def get(self):
		f = open('inicio', 'r')		
		inicio = f.read()
		f = open('fim', 'r')		
		fim = f.read()
		page = """

    <h1>Contato:</h1>
	<p class="lead">contato dot lolpucrio at gmail dot com<br></p>
				Estou usando Python 2.7 e Google App Engine	
"""		
		self.response.write(inicio)

		self.response.write(page)

		self.response.write(fim)
app = webapp2.WSGIApplication([('/contato', contato)],
                              debug=True)	
		        		
