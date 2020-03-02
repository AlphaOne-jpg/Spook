


class gameevents:
	options = []
	def __init__(self, name):
		self.name = name
		
		if name == "Test":
			self.description = "This is a test event\n if you not debugging and see this, please email alphaonecontactmail@gmail.com with subject \"Event Test Bug\"and a description.\n Thaks :-)"
			self.options.append("Test Yes")
			self.options.append("Test No")
			self.options.append("Test Maybe")
			
		elif name == "TagTest":
			self.description = "This is a test event\n if you not debugging and see this, please email alphaonecontactmail@gmail.com with subject \"Event Test Bug\"and a description.\n Thaks :-)"
			self.options.append("Human")
			self.options.append("Test No")
			self.options.append("Test Maybe")
		


	def printdescription(self):
		print(self.name+": "+self.description)
	
	def getdescription(self):
		return self.name+": "+self.description