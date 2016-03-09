import os
import sys

class Html:
	def __init__(self):
		filename = raw_input("Filename? ")
		os.system('touch ' + filename)
		f = open(filename, 'w')
		self.head(f)
		self.body(f)
		f.close()

	def head(self, f):
		f.write("<!DOCTYPE html>\n")
		f.write("<html>\n")
		f.write("<head>\n")
		title = raw_input("Title? ")
		self.bootstrap(f)
		self.jquery(f)
		f.write("\t<title>" + title + "</title>\n")
		f.write("</head>\n")

	def body(self, f):
		f.write("<body>\n")
		f.write("\t<h1>ready to go</h1>\n")
		f.write("\t<button class = 'btn btn-primary'>awesome</button>\n")
		f.write("</body>\n")
		f.write("</html>\n")

	def bootstrap(self, f):
		bootstrap = raw_input("Bootstrap? yes or no   ")
		if bootstrap == 'yes':
			f.write("\t<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css' integrity='sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7' crossorigin='anonymous'>\n")
		elif bootstrap == 'no':
			print "Bootstrap not being added"
		else:
			print "Did not understand "
			self.bootstrap(f)

	def jquery(self, f):
		jquery = raw_input("Jquery? yes or no    ")
		if jquery == 'yes':
			f.write("<script src='https://cdnjs.cloudflare.com/ajax/libs/jquery/2.2.1/jquery.js'></script>")
		elif jquery == 'no':
			print "Jquery not being added"
		else: 
			print "Did not understand command   "
			self.jquery(f)


if __name__ == "__main__":
    page = Html()

