#!/usr/bin/python3






# ---- importations ----
import subprocess






# ---- declarations ----

#directions
UP    = 0
DOWN  = 1
LEFT  = 2
RIGHT = 3
dirNames = ("UP", "DOWN", "LEFT", "RIGHT")

#pipe globals
pipe_chars = ('-', '|', '/', '\\', '>', '<', '^', 'v', '+', 'o')
g = {
	'debug_on' : False,
	'lineMax'  : 0,
	'line'     : 0,
	'column'   : 0
}






# ---- utilities ----

#debug
def showCurrentChar(code):
	try:
		print("Current character at ({0},{1}) is [{2}].".format(
			g['line']+1,
			g['column']+1,
			code[ g['line'] ][ g['column'] ]
		), end=' ')
	except IndexError:
		print("Undefined character at ({0},{1}).".format(
			g['line']+1,
			g['column']+1
		), end=' ')

#max column reachable
def getMaxColumn(code):
	return len( code[ g['line'] ] )-1

#next character is a pipe ?
def nextAt_UP_isAPipe(code):

	#debug
	if g['debug_on']:
		showCurrentChar(code)
		print("=> Checking UP")

	#check
	return ( g['line'] > 0 and len(code[ g['line']-1 ]) > g['column'] and code[ g['line']-1 ][ g['column'] ] in pipe_chars )

def nextAt_DOWN_isAPipe(code):

	#debug
	if g['debug_on']:
		showCurrentChar(code)
		print("=> Checking DOWN")

	#check
	return ( g['line'] < g['lineMax'] and len(code[ g['line']+1 ]) > g['column'] and code[ g['line']+1 ][ g['column'] ] in pipe_chars )

def nextAt_LEFT_isAPipe(code):

	#debug
	if g['debug_on']:
		showCurrentChar(code)
		print("=> Checking LEFT")

	#check
	return ( g['column'] > 0 and code[ g['line'] ][ g['column']-1 ] in pipe_chars )

def nextAt_RIGHT_isAPipe(code):

	#debug
	if g['debug_on']:
		showCurrentChar(code)
		print("=> Checking RIGHT")

	#check
	return ( g['column'] < getMaxColumn(code) and code[ g['line'] ][ g['column']+1 ] in pipe_chars )

#check before forwarding
def checkNextAt_UP_thenForward(code):
	if not nextAt_UP_isAPipe(code):
		print("FATAL ERROR > line {0} : column {1} : No end for pipe (going up).".format( g['line']+1, g['column']+1))
		exit(1)
	forward(code, UP)

def checkNextAt_DOWN_thenForward(code):
	if not nextAt_DOWN_isAPipe(code):
		print("FATAL ERROR > line {0} : column {1} : No end for pipe (going down).".format( g['line']+1, g['column']+1))
		exit(1)
	forward(code, DOWN)

def checkNextAt_LEFT_thenForward(code):
	if not nextAt_LEFT_isAPipe(code):
		print("FATAL ERROR > line {0} : column {1} : No end for pipe (going to the left).".format( g['line']+1, g['column']+1))
		exit(1)
	forward(code, LEFT)

def checkNextAt_RIGHT_thenForward(code):
	if not nextAt_RIGHT_isAPipe(code):
		print("FATAL ERROR > line {0} : column {1} : No end for pipe (going to the right).".format( g['line']+1, g['column']+1))
		exit(1)
	forward(code, RIGHT)






# ---- follow the way ----
def noForcedDirection(code, nextPipe):
	if nextPipe == '^':
		checkNextAt_UP_thenForward(code)
		return False
	elif nextPipe == 'v':
		checkNextAt_DOWN_thenForward(code)
		return False
	elif nextPipe == '<':
		checkNextAt_LEFT_thenForward(code)
		return False
	elif nextPipe == '>':
		checkNextAt_RIGHT_thenForward(code)
		return False
	return True

def forward(code, direction):

	if g['debug_on']:
		print("Forwarding to {0} from ({1},{2})".format(
			dirNames[direction],
			g['line']+1, g['column']+1
		), end=' ')

	#1st direction
	if direction == UP:

		#forward in direction
		g['line'] -= 1
		nextPipe = code[ g['line'] ][ g['column'] ]

		#debug
		if g['debug_on']:
			print("to ({0},{1}).".format( g['line']+1, g['column']+1))

		#stop following pipe
		if nextPipe == 'o':

			#debug
			if g['debug_on']:
				print("\nFound node at : ({0},{1}).".format(g['line']+1, g['column']+1))

			return

		#forced directions
		if noForcedDirection(code, nextPipe):

			#oposite direction
			if nextPipe == '-':
				checkNextAt_DOWN_thenForward(code)

			#turns
			elif nextPipe == '/':
				checkNextAt_RIGHT_thenForward(code)
			elif nextPipe == '\\':
				checkNextAt_LEFT_thenForward(code)

			#same direction ('+' or '|')
			else:
				checkNextAt_UP_thenForward(code)

	#2nd direction
	elif direction == DOWN:

		#forward in direction
		g['line'] += 1
		nextPipe = code[ g['line'] ][ g['column'] ]

		#debug
		if g['debug_on']:
			print("to ({0},{1}).".format( g['line']+1, g['column']+1))

		#stop following pipe
		if nextPipe == 'o':

			#debug
			if g['debug_on']:
				print("\nFound node at : ({0},{1}).".format(g['line']+1, g['column']+1))

			return

		#forced directions
		if noForcedDirection(code, nextPipe):

			#oposite direction
			if nextPipe == '-':
				checkNextAt_UP_thenForward(code)

			#turns
			elif nextPipe == '/':
				checkNextAt_LEFT_thenForward(code)
			elif nextPipe == '\\':
				checkNextAt_RIGHT_thenForward(code)

			#same direction ('+' or '|')
			else:
				checkNextAt_DOWN_thenForward(code)

	#3rd direction
	elif direction == LEFT:

		#forward in direction
		g['column'] -= 1
		nextPipe = code[ g['line'] ][ g['column'] ]

		#debug
		if g['debug_on']:
			print("to ({0},{1}).".format( g['line']+1, g['column']+1))

		#stop following pipe
		if nextPipe == 'o':

			#debug
			if g['debug_on']:
				print("\nFound node at : ({0},{1}).".format(g['line']+1, g['column']+1))

			return

		#forced directions
		if noForcedDirection(code, nextPipe):

			#oposite direction
			if nextPipe == '|':
				checkNextAt_RIGHT_thenForward(code)

			#turns
			elif nextPipe == '/':
				checkNextAt_DOWN_thenForward(code)
			elif nextPipe == '\\':
				checkNextAt_UP_thenForward(code)

			#same direction ('+' or '-')
			else:
				checkNextAt_LEFT_thenForward(code)

	#4th direction
	elif direction == RIGHT:

		#forward in direction
		g['column'] += 1
		nextPipe = code[ g['line'] ][ g['column'] ]

		#debug
		if g['debug_on']:
			print("to ({0},{1}).".format( g['line']+1, g['column']+1))

		#stop following pipe
		if nextPipe == 'o':

			#debug
			if g['debug_on']:
				print("\nFound node at : ({0},{1}).".format(g['line']+1, g['column']+1))

			return

		#forced directions
		if noForcedDirection(code, nextPipe):

			#oposite direction
			if nextPipe == '|':
				checkNextAt_LEFT_thenForward(code)

			#turns
			elif nextPipe == '/':
				checkNextAt_UP_thenForward(code)
			elif nextPipe == '\\':
				checkNextAt_DOWN_thenForward(code)

			#same direction ('+' or '-')
			else:
				checkNextAt_RIGHT_thenForward(code)

	#internal error
	else:
		print("FATAL ERROR > INTERNAL ERROR : Pipe found an incorrect direction : " + str(direction))
		exit(2)






# ---- execution ----
def run(code, debugMode):

	#INIT

	#check whether code is empty
	if len(code) == 0:
		print("FATAL ERROR > line 0 : column 0 : Code is empty.")
		exit(1)

	#set global values
	g['lineMax']  = len(code)-1
	g['debug_on'] = debugMode
	g['line']     = 0           # just in case
	g['column']   = 0

	#debug
	if g['debug_on']:
		print("Code lineMax : " + str(g['lineMax']) )

	#skip all lines until a node is found (character 'o' followed by ' ')
	while True:

		#search for a node
		g['column'] = code[ g['line'] ].find('o ')
		if g['column'] != -1:
			break

		#no node found => try next line
		if g['line'] < g['lineMax']:
			g['line'] += 1
		else:
			print("FATAL ERROR > line {0} : column {1} : No node detected for execution.".format( g['line']+1, getMaxColumn(code)+1))
			exit(1)

	#debug
	if g['debug_on']:
		print("Found first node at : ({0},{1}).".format(g['line']+1, g['column']+1))



	#MAIN EXECUTION

	#infinite loop
	while True:

		#check if command exists after node
		maxColumn = getMaxColumn(code)
		if maxColumn < g['column']+1 or code[ g['line'] ][ g['column']+1 ] != ' ':
			print("FATAL ERROR > line {0} : column {1} : No command detected after node.".format( g['line']+1, g['column']+1))
			exit(1)

		#debug
		if g['debug_on']:
			print("Command to execute : \"" + code[ g['line'] ][ g['column'] +1:].replace('"','\\"') + "\".")

		#execute command after node
		error = subprocess.call([
			"bash",
			"-c",
			code[ g['line'] ][ g['column'] +1:]
		])

		#debug
		if g['debug_on']:
			print("Error code returned : [" + str(error) + "].")

		#no error occured
		if error == 0:

			#execution is catched by a pipe
			if nextAt_DOWN_isAPipe(code):
				forward(code, DOWN)

			#execution is not catched => end of program
			else:
				break

		#no error occured
		else:

			#execution is catched by a pipe ?
			if nextAt_LEFT_isAPipe(code):
				forward(code, LEFT)

			#execution is not catched => end of program
			else:
				break

	#end of program
	print("Pipe > End of program.")
