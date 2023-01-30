import pdb
#module  - python file contains useful classes and fucntions wrote by developers

# Debugging in Python is facilitated by pdb module(python debugger) which comes built-in to the Python standard library.
#  It is actually defined as the class Pdb which internally makes
#  use of bdb(basic debugger functions) and cmd(support for line-oriented command interpreters) modules.
#  The major advantage of pdb is it runs purely in the command line thereby making it great for debugging code
#  on remote servers when we don’t have the privilege of a GUI-based debugger. 

# To start debugging within the program just insert import pdb, pdb.set_trace() commands.
# Run your script normally and execution will stop where we have introduced a breakpoint.
# So basically we are hard coding a breakpoint on a line below where we call set_trace().
# With python 3.7 and later versions, there is a built-in function called breakpoint() which works in the same manner.
# Refer following example on how to insert set_trace() function.

# A debugger or debugging tool is a computer program used to test and debug other programs (the "target" program).
# The main use of a debugger is to run the target program under controlled conditions that permit the programmer
# to track its operations in progress and monitor changes in 
# computer resources (most often memory areas used by the target program or the computer's operating system) that may indicate malfunctioning code.
# Typical debugging facilities include the ability to run or halt the target program at specific points,
# display the contents of memory, CPU registers or storage devices (such as disk drives),
# and modify memory or register contents in order to enter selected test data that might be a cause of faulty program execution.

# The code to be examined might alternatively be running on an instruction set simulator (ISS),
# a technique that allows great power in its ability to halt when specific conditions are encountered,
# but which will typically be somewhat slower than executing the code directly on the appropriate (or the same) processor.
# Some debuggers offer two modes of operation, full or partial simulation, to limit this impact.

# A "trap" occurs when the program cannot normally continue because of a programming bug or invalid data.
# For example, the program might have tried to use an instruction not available on the current version of the CPU
# or attempted to access unavailable or protected memory.
# When the program "traps" or reaches a preset condition,
# the debugger typically shows the location in the original code if it is a source-level debugger or symbolic debugger,
# commonly now seen in integrated development environments.
# If it is a low-level debugger or a machine-language debugger it shows the line in the disassembly
# (unless it also has online access to the original source code and can display the appropriate section of code from the assembly or compilation).

# Debugging is the process of finding and resolving defects or problem within a computer program that prevent correct operation of computer software or system.

# Why Debugging
# 1.) set trace
# 2.) execute code line by line

pdb.set_trace() # write it where where you think the error may happen
name = input("Please Type Your Name : ");
age = int(input("Enter Your age : "));
print(f"Hello {name} your age is {age}");
age2 = age +5
print(f"{name} your will be {age2} in next five years"); 
# type l in cmd to check on which line you are
# type n to run that line
# to check that variable enter that variable name  line in this case after running name command type name to check it

# type c to contine will run code as usual
#  type q to quit  
