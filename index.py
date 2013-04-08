import webapp2


class index(webapp2.RequestHandler):
	def get(self):
		f = open('inicio', 'r')		
		inicio = f.read()
		f = open('fim', 'r')		
		fim = f.read()
		page = """

    <h1>N&atildeo tem conta?</h1>
	<p class="lead">N&atildeo seja por isso, cadastre-se agora!</p>
	<a class="btn btn-large btn-success" href="cadastro">Cadastro</a>
	<p class="lead"><br>Site para os jogadores de League of Legends da PUC-Rio!<br>Agora com suporte oficial da representa&ccedil&atildeo PUC-Rio perante a Riot!<br><br>Em breve: <br> -Montaremos equipes<br>-Organizaremos torneios<br><br><br>Sugest&otildees,<br>
					Cr&iacuteticas,<br>
					Quer me ajudar?
					</p>

	<a class="btn btn-large btn" href="contato">Contato</a>
"""		
		self.response.write(inicio)
		self.response.write(page)
		self.response.write(fim)

app = webapp2.WSGIApplication([('/index', index),('/', index)],
                              debug=True)	
		        		
