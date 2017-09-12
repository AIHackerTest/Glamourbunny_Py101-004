from sys import argv
from os.path import exists

script, from_file, to_file = argv

print ("Copying from %s to %s" % (from_file, to_file))

#We could do these two on one lines too, how?
print ("Let's check! The origin file: \n" + open(from_file).read())


open(to_file, 'w').write(open(from_file).read())

print( "Alright, all done.")
print ("Let's check! The newfile: \n" + open(to_file).read())


open(to_file).close()
open(from_file).close()

