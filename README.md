# **Pipe Lang**

***Discover a new way of coding, following the pipe...***

&nbsp;

&nbsp;



# I] Description

Have you ever though about coding in another way than only from up to down, line by line, execution after execution...
What about a program that is not always following the same direction, but the one you told him.

That's exactly the reason why the **Pipe** programming language has been made for.
Draw a shape, a pipe circuit and your program will follow the path as far as possible !

There are so many possibilities, action and reaction, direction and redirection...
Who knows what can be done with this language ?

Maybe it's time for you to test it...

&nbsp;

&nbsp;



## II] Installation

**WARNING : Make sur you don't have a** ***'pipe'*** **command already installed on your system.**
**(Keep calm, Pipe_lang will not overwrite it in any cases)**

### Install
To install Pipe_lang :

Get the repository from GitHub :
```bash
git clone https://github.com/iasebsil83/Pipe_lang
```
Then launch the installer :
```bash
./Pipe_lang/install
```

Now, open a new terminal.
You should be able to run these new command 'pipe'.

### Uninstall
To uninstall Pipe_lang :
```bash
rm -rf /opt/Pipe_lang /usr/bin/pipe   #requires root privileges
```

There you go !

&nbsp;

&nbsp;



## III] Use

### Syntax
The Pipe language has a pretty simple syntax consisting in 3 types of statements :
 - Nodes   (o)
 - Pipes   (| - / \ < > ^ v)
 - Command (x=2, echo $x...)
Any other statement will not be interpreted, it is just floating text.

### Start
When execution starts, Pipe is looking for the first character 'o' in the file.
This is the first node.

### Executing node
Each time a node is reached, the command written to the right of this node is executed.
Then, depending on the exit code of this command, execution continues :
 - DOWN : if error code is 0     (No problem in command)
 - LEFT : if error code is not 0 (Problem occured)

### Catching execution
As we said, execution goes LEFT or DOWN depending on the last command executed.
**It is MANDATORY to have a character receiving the execution if it occurs.**
If the execution goes to a pipe character, it will follow the pipe.
If it is another character, program stops here.

### Pipe redirection
In the case execution goes to a pipe character, the execution flow will follow the line until a next node is found.
Here is some rules on pipe redirection :
```
- A node have 1 input (UP) and 2 possible outputs (DOWN/LEFT)

- A pipe has no proper 'sens'
  (The same character '|' can be either traveled from UP to DOWN and from DOWN to UP)

- Depending on the sens the execution goes, the flow can be turned.
  (At X, going to the RIGHT :      |
                               X---/  Flow is turning UP.
   BUT
   At X, going to the LEFT :   /---X
                               |      Flow is turning DOWN.
  )

- Flow can be fully returned in the opposite way by using a pipe as a wall.
  (At X, going to the RIGHT :  X---|
   Flow will go back to the LEFT after touching the wall)

- Character '+' is allowing pipes to be crossed without changing their direction.
  (Don't confuse this:    |     with this:    |
                       ---|---             ---+---
                          |                   |
                    UP/DOWN line        UP/DOWN line
                    LEFT/RIGHT walls    LEFT/RIGHT line
  )

- To force the flow to go in a precise direction, use '< > ^ v'
  (At X, going to the RIGHT :  X---<---
   Flow will go to the LEFT at '<'
   Very useful in intersections)
```

That's it for the Pipe language, hoping it leads to beautiful codes !

&nbsp;

&nbsp;



*Contact     : i.a.sebsil83@gmail.com*<br>
*Youtube     : https://www.youtube.com/user/IAsebsil83*<br>
*GitHub repo : https://github.com/iasebsil83*<br>

Let's Code ! &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;By I.A.
