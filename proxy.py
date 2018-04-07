from twisted.web import http, proxy
from twisted.internet import reactor

max_clients = input("Enter the number of maxmimum number of clients you wish to serve: ")
clients = []


class MyProtocol(proxy.Proxy):
	def connectionMade(self):
		self.client_host = self.transport.getPeer().host
		self.client_port = self.transport.getPeer().port
		if len(clients) >= max_clients:
			print("Number of clients exceeded")
			self.transport.loseConnection()
		else:
			clients.append((self.client_port, self.client_port))
			print clients


fac = http.HTTPFactory()
fac.protocol = MyProtocol
reactor.listenTCP(6969, fac)
reactor.run()
