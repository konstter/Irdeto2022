# Test assignment

## Exercise 1: coding

In the file *./ex1/ex1_coding.py*

1. The algorithm makes AND operation with elements of A which greater than 0 with 1.
2. If result of first step is 1, it increases a local counter by 1.
3. Then It makes another bitwise operation Right Shift with ever element from Step 1 and
appends it to a new array.
4. It compares the local counter from Step 2 and a global counter. If the local counter
is more, The global counter takes the local counter's value.
5. If length of the new array from Step 3 is more than the global counter then
the algorithm goes to Step 1 with A as the new array. 



## Exercise 2: Python real deal

In the file *./ex2/ex2_realdeal.py*

**How to run**
```bash
pip install argparse

./ex2_realdeal.py -h
usage: ex2_realdeal.py [-h] [-d D] [-p P]

options:
  -h, --help  show this help message and exit
  -d D        A directory to analyze files
  -p P        A percentage

#Example
./ex2_realdeal.py -d sample -p 25
```

**About testing**

Note: S for my solution

Positive Tests:
1. Check that S can read parameters from command line
2. S can read file in the directory
3. S can return right frame_numbers from one or more files
4. S can count files in the directory and determine the percentage of any frame_numbers
5. S can compare the percentage from case 3 and the user's percentage
6. S can create list of frame_numbers with right percentage
7. S can write the result to a file

Negative Tests (I didn't implement an exception handling in S):
1. S warns a user if directory is missing
2. S warns a user if directory is empty
3. S warns a user if he hasn't permission
4. S can process files with right structure and misses wrong files

Stress Testing and Memory usage testing.



## Exercise 3: Domain

In the file *./ex3/ex3_domain.py* (Card simulator) and the directory *./ex3/tests* (unit tests)

**How to run**
```bash
pytest -v
```

**Test cases**

More close technique is "decision table"

1. Query for first state (all correct)
Command: 'A4 20 00 00 00'
Expected response: '63 C5' (X = 5 is my retry count)

2. Invalid CLA and the next elements of header, params and body don't matter
Command: '20 20 00 00 00'
Expected response: '63 00' (verification failed)

3. Valid CLA and Invalid INS and the next elements of params and body don't matter
Command: '20 20 00 00 00'
Expected response: '63 00' (verification failed)

4. Valid CLA and INS, invalid P1 and the next elements don't matter
Command: 'A4 20 01 00 00'
Expected response: '6A 86' (incorrect parameters)

5. Valid CLA and INS, valid P1, invalid P2 and the next elements don't matter
Command: 'A4 20 00 03 00'
Expected response: '6A 86' (incorrect parameters)

6. Check retry counter
Command: 'A4 20 00 00 00'
Expected response: '63 C3'

7. Valid CLA and INS, valid P1-P2, invalid Lc and Data doesn't matter
Command: 'A4 20 00 00 01'
Expected response: '63 00' (verification failed)

8. Valid CLA and INS, valid P1-P2, invalid Lc and Data doesn't matter #2
Command: 'A4 20 00 01 00' or 'A4 20 00 02 00'
Expected response: '63 00' (verification failed)

9. Valid CLA and INS, valid P1-P2 Lc and Data don't match
Command: 'A4 20 00 01 03 00 00 00 00' or 'A4 20 00 02 05 05 05'
Expected response: '63 00' (verification failed)

10. Valid CLA and INS, valid P1-P2, valid Lc, and Data with invalid PIN
Command: 'A4 20 00 01 04 00 00 00 00'
Expected response: '63 00' (verification failed)

11. Valid CLA and INS, valid P1-P2, valid Lc, and Data with valid PIN
Command: 'A4 20 00 01 04 01 09 04 07'
Expected response: '90 00' and retry counter returns to 5 (verification passed)

13. Valid CLA and INS, valid P1-P2, valid Lc, and Data with invalid PIN
Command: 'A4 20 00 01 04 01 09 04 05' and retry counter = 1
Expected response: '69 83' (auth method is blocked)

NOTE: There is my understanding of df pin (in cases 14-18 and further). 
I suppose that DF pin is for unblock auth method

14. Valid CLA and INS, valid P1-P2, valid Lc, and Data with valid DF PIN, and verification is passed
Command: 'A4 20 00 02 05 05 07 01 00 02' (my 5-bytes DF PIN = 57102) 
Expected response: '90 00' (nothing happens verification is OK)

15. Valid CLA and INS, valid P1-P2, valid Lc, and Data with invalid DF PIN, and verification is passed
Command: 'A4 20 00 02 05 05 07 01 01 02'
Expected response: '90 00' (nothing happens verification is OK)

16. Valid CLA and INS, valid P1-P2, valid Lc, and Data with valid DF PIN, and verification is failed
Command: 'A4 20 00 02 05 05 07 01 00 02'
Expected response: '63 C5' (counter returns to 5)

17. Valid CLA and INS, valid P1-P2, valid Lc, and Data with valid DF PIN, and auth method is blocked
Command: 'A4 20 00 02 05 05 07 01 00 02'
Expected response: '63 C5' (counter returns to 5, auth is unblocked)

18. Valid CLA and INS, valid P1-P2, valid Lc, and Data with invalid DF PIN, and verification is failed 
or auth method is blocked
Command: 'A4 20 00 02 05 05 07 01 00 02'
Expected response: '69 83' (auth method is blocked)


NOTE: I suppose Le field matters when Verification is recuired

19. Valid CLA and INS, valid P1-P2, valid Lc, and Data with valid PIN (or Data is empty), 
Le is not empty, and retry counter > 1
Command: 'A4 20 00 01 04 01 09 04 07 00'
Expected response: '63 00' (verification failed)

10. Valid CLA and INS, valid P1-P2, valid Lc, and Data with valid PIN (or Data is empty), 
Le is not empty, and retry counter = 1
Command: 'A4 20 00 01 04 01 09 04 07 00'
Expected response: '69 83' (auth method is blocked)

