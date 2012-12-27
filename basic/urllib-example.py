import socket
import sys


class Connector():
	def __init__(self, host, port):
		self.host = host
		self.port = port


	def connect(self):
		try:
			socket.gethostnamebyna