#!/usr/bin/python3






# ---- importations ----
import sys
import reader






# ---- main ----

#empty => internal error (shall never be executed without at least 1 argument)
if len(sys.argv) < 2:
	print("FATAL ERROR > INTERNAL ERROR : Don't execute this script this way.")
	exit(2)


#get script fileName
fileName = sys.argv[1]

#check for debug option
debugMode = False
if len(sys.argv) > 2:
	if sys.argv[1] == '-d' or sys.argv[1] == '--debug':
		debugMode = True
		fileName = sys.argv[2]
	elif sys.argv[2] == '-d' or sys.argv[2] == '--debug':
		debugMode = True

#check if fileName is not an action
if fileName[0] == '-':
	print("pipe: Filename expected, got '" + fileName + "'.")
	exit(1)

#get script content
try:
	f = open(fileName, "r")
	code = f.read().split('\n')
	f.close()

	#execute script
	reader.run(code, debugMode)
except FileNotFoundError:
	print("pipe: File '" + fileName + "' not found.")
	exit(1)
