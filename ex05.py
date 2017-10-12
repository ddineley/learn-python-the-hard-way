my_name = 'Doug'
my_age = 56
my_height = 75 # inches
my_weight = 210 # pounds
my_eyes = 'Blue'
my_teeth = 'Gray'
my_hair = 'Absent'

print "Let's talk about %s." % my_name
print "He's %d years old." % my_age
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's kinda heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
   my_age, my_height, my_weight, my_age + my_height + my_weight )
