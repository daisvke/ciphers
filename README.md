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
Encryption and decryption is done by the same algorithm.


## nbralpha

### Description
A numbered alphabet cypher in python.
* During encryption, it takes command-line arguments, convert each argument to a series of numbers representing the position of each character in the alphabet, and prints the results.
* The reverse process is done during decryption.<br />
<br />
It can only decode numbers separated by spaces.
* Handled alphabetical characters include ranges: a-z, Ç-Ü, á-Ñ.
* Handles punctuations.

### Commands
```
// Install
cd nbralpha
pip install -r requirements.txt

// Usage
python nbralpha [source],...

-s: encryption: put spaces between numbers

```
