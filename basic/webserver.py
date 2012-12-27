from BaseHTTPServer import HTTPServer

if __name__ == '__main__':
    try:
        server = HTTPServer(('', 80))
        print("Started HTTP Server")
        server.serve_forever()
    except KeyboardInterupt:
        print("^C Received...")
        server.socket.close()while :
        	pass