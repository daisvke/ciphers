# ciphers
A set of ciphers

## xor
```
; void  xor_encrypt_decrypt(void *key, size_t key_length, void *data, size_t data_length)
;                              <rdi>           <rsi>        <rdx>            <rcx>
```
An XOR cipher in assembly language.<br />
In cryptography, the simple XOR cipher is a type of additive
cipher, an encryption algorithm that operates, in binary,
according to the principles:<br />
```
   0 1 1
   0 1 0
=> 0 0 1
```
Encryption and decryption is done by the same algorithm.


## nbralpha

### Description
A numbered alphabet cipher in python.
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

// Usage
python3 nbralpha [option] [source],...
// option
-s: spaces between numbers in encryption mode's output string.
-v: verbose mode. Useful to desactivate when reusing the
output through pipes, etc.

```

### Screenshot
 <p>
    <img src="/screenshots/nbralpha.png" width="60%" />
 </p>
 From Edgar Allan Poe's short story <i>"The Gold-Bug."</i>
