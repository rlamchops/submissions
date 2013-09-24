print "testing....\n"
def mattsjoke():
	#joke taken from http://www.explosm.net/comics/3260/

	y = 1

	name = raw_input("Enter your name. \n")
	while y == 1:
		print "\nHello %s, please answer 'yes' or 'no':" % name
		a1 = raw_input("Are you interested in the Oddity Out-of-Body Audi Autobody free car audit?\n") 
		if a1 == "yes":
			z = 1
			while z == 1 :
				print "\nAnswer 'no' or 'no', %s:" % name
				a2 = raw_input("Do you have an outwards bellybutton? \n \n")
				if a2 == "yes":
					print "\nI couldn't hear you %s, what did you say?" % name
				elif a2 == "no":
					z = 2
					print "\nI'm sorry %s, but only oddities get the Out-of-Body Audi Autobody Outie Audit." % name
					print "You should have brought someone with an outwards bellybutton!"
					return
				else:
					print "\nI couldn't hear you %s, what did you say?" % name
		elif a1 == "no":
			print "\nWhy did you run me then? :("
			break
		else: 
			print "\nI couldn't hear you %s, what did you say?" % name
mattsjoke()	