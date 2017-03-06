#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from os import curdir, sep

import CHIP_IO.GPIO as GPIO
import time

GPIO.cleanup()

pins = ["XIO-P2","XIO-P3","XIO-P4","XIO-P5","XIO-P6","XIO-P7"]


for pin in pins:
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, GPIO.HIGH)
	

PIN1 = pins[0]
PIN2 = pins[1]
PIN3 = pins[2]
PIN4 = pins[3]
PIN5 = pins[4]
PIN6 = pins[5]


#for i in range(0,10):
#        GPIO.output(PIN, GPIO.LOW)
#        time.sleep(0.1)
#        GPIO.output(PIN, GPIO.HIGH)
#        time.sleep(0.1)
#GPIO.cleanup()


PORT_NUMBER = 80


def togglePin(pin):
	GPIO.output(pin, GPIO.LOW)
	time.sleep(1)
	GPIO.output(pin, GPIO.HIGH)



#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
	

	#Handler for the GET requests
	def do_GET(self):
		if self.path=="/":
			self.path="/index_example2.html"

		if self.path=="/1on":
			#self.path="/index_example2.html"
			togglePin(PIN1)

#			GPIO.output(PIN1, GPIO.HIGH)
#			time.sleep(0.1)
#			GPIO.output(PIN1, GPIO.LOW)
#			time.sleep(0.1)

		if self.path=="/1off":
			togglePin(PIN2)

#			GPIO.output(PIN1, GPIO.LOW)
#			time.sleep(0.1)


		if self.path=="/2on":
			togglePin(PIN3)

#			GPIO.output(PIN2, GPIO.HIGH)
#			time.sleep(0.1)

		if self.path=="/2off":

			togglePin(PIN4)

#			GPIO.output(PIN2, GPIO.LOW)
#			time.sleep(0.1)


		if self.path=="/3on":

			togglePin(PIN5)

#			GPIO.output(PIN3, GPIO.HIGH)
#			time.sleep(0.1)

		if self.path=="/3off":


			togglePin(PIN6)

#			GPIO.output(PIN3, GPIO.LOW)
#			time.sleep(0.1)



		self.send_response(200)
		self.send_header("Content-type", "text/html")
		self.end_headers()
		self.wfile.write("<html><head><title>Title goes here.</title></head>")
		self.wfile.write("<body><p>This is a test.</p>")
#  21         # If someone went to "http://something.somewhere.net/foo/bar/",
#  22         # then s.path equals "/foo/bar/".
		self.wfile.write("<p>You accessed path: %s</p>" % self.path)
		self.wfile.write("</body></html>")

		try:
			#Check the file extension required and
			#set the right mime type

			sendReply = False
			if self.path.endswith(".html"):
				mimetype='text/html'
				sendReply = True
			if self.path.endswith(".jpg"):
				mimetype='image/jpg'
				sendReply = True
			if self.path.endswith(".gif"):
				mimetype='image/gif'
				sendReply = True
			if self.path.endswith(".js"):
				mimetype='application/javascript'
				sendReply = True
			if self.path.endswith(".css"):
				mimetype='text/css'
				sendReply = True

			if sendReply == True:
				#Open the static file requested and send it
				f = open(curdir + sep + self.path) 
				self.send_response(200)
				self.send_header('Content-type',mimetype)
				self.end_headers()
				self.wfile.write(f.read())
				f.close()
			return


		except IOError:
			self.send_error(404,'File Not Found: %s' % self.path)

try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print 'Started httpserver on port ' , PORT_NUMBER
	
	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()
	
