# ciphers
A set of cyphers

## xor
An XOR cypher in assembly language.<br />
In cryptography, the simple XOR cipher is a type of additive
cipher, an encryption algorithm that operates, in binary,
according to the principles:<br />
   0 1 1
   0 1 0
=> 0 0 1

## nbralpha
A numbered alphabet cypher in python.
<br /><br />
During encryption, it takes command-line arguments, convert each argument to a series of numbers representing the position of each character in the alphabet, and prints the results.
<br /><br />
The reverse process is done during decryption.<br />
It can only decode numbers separated by spaces

### commands
```
// Install
cd nbralpha
pip install -r requirements.txt

// Usage
python nbralpha [source],...

-s: encryption: put spaces between numbers

```
