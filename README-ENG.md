intlang is an interpreter for a simple programming language called intlang. This language was created by Kamil Malicki. The interpreter allows you to perform simple arithmetic operations, manipulate registers and perform basic operations on them.

Supported operations:

PRINT: Prints the given arguments to the console.

SYNTAX:

a) PRINT 'what do you want to write'
b) PRINT $RAX
c) PRINT $RAY

SET: Sets the value of the RAX register.

SYNTAX:

SET {NUMBER MOVED TO RAX}

INC: Increments the value of the RAX register.

SYNTAX:

INC => {RAX+=1}

STORE: Stores the value in the given RAR register.

SYNTAX:

STORE {BIT NUMBER} {NUMBER MOVED TO RAR}

DATA: Displays the value from the given RAR register.

SYNTAX:

DATA {BIT NUMBER} => { PYTHON = print(RAR[bit number])}

DOUBLE: Multiplies the RAX register value by 2.

SYNTAX: DOUBLE => {RAX*=2}

MOV: Moves a value from one register to another.

SYNTAX:

a) MOV Y => {RAY<--RAX}

b) MOV X => {RAX<--RAY}

ITOA: Converts a register value to the appropriate character.

SYNTAX:

a) ITOA $RAX => { PYTHON = print(chr(RAX))}

b) ITOA $RAY => { PYTHON = print(chr(RAX))}

c) ITOA $RAR[bit number]= {PYTHON = print(chr(RAR[bit number]))}
  
ATOI: Converts a character to its corresponding numeric value.

SYNTAX:

a) ATOI $RAX => {RAX -= 48}

b) ATOI $RAY => {RAY -= 48}

c) ATOI $RAR[bit number] => {RAR[bit number] -= 48}

SUM: Adds the values ​​of the RAX and RAY registers.

SYNTAX: SUM => {RAX += RAY}

SUB: Subtracts the value of the RAY register from RAX.

SYNTAX: SUB => {RAX -= RAY}

NINC: Decrements the value of the RAX register.

SYNTAX: NINC => {RAX-=1}

GOTO: Goes to a specific line of code.

SYNTAX: GOTO {JUMP TO ANY LINE OF CODE}

PASS: Skips the current instruction.

SYNTAX: PASS

CMP: Compares the value of the RAX register with the given condition and takes action based on the comparison result.

SYNTAX: CMP {VALUE COMPARED WITH RAX} GOTO {JUMP TO SOME LINE OF CODE}

RARCMP: Compares values ​​in two RAR registers and takes action based on the comparison result.

SYNTAX: RARCMP {SOME BIT TO COMPARE FROM THE RAR REGISTER} {SOME BIT TO COMPARE FROM THE RAR REGISTER} GOTO {JUMP TO SOME LINE OF CODE}

INPUT: Takes a value from the user and stores it in the RAX register.

SYNTAX: INPUT

EXIT: Ends the program.

SYNTAX: EXIT

Startup instructions:
To run the intlang interpreter, use the command in the terminal:

python intlang.py <file.il>

Where <file.il> is the path to the file containing the intlang code.

Sample intlang code:

PRINT 'Hello, world!'

SET 10

INC

NINC

PRINT $RAX

Attention!
The intlang language is a simple interpreted language and does not support complex operations. Please make sure that the code written in this language is consistent with the documentation provided by Kamil Malicki, the author of the intLang language.

This README is intended to provide information on how to use the intlang interpreter and what operations are supported. Please remember that this program is protected by Kamil Malicki's copyright.

Software updates:

1.1.0: added a new RAR register which is divided into 8 bits (0,1,2,3,4,5,6,7).

1.0.5: added a new RAY register that can be used as additional memory to the RAX register.
