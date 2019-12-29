# mx_mul

This program is able to multiply two matrices, which are entered by user input. This is done without using numpy, or any other mathematical library. 

## Implementation details

Program first writes expected input and waits for user to put all required fields. In case of invalid input, error is raised. Type of error corresponds to type of users misstake. 

If users input was correct, the values are further processed and two Matrix objects are created. Matrix object contains dimensions of matrix and its content. Matrix class contains method for multiplying the current instance with another object of the same type. 

First of all, method checks, if dimensions of multiplied matrices are suitable for the operation. After that, the matrices are multiplied row by row. Multiplication uses zip function between rows of first matrix and the rows of transposed second matrix. Finally, the result is processed into another Matrix object. 

Profiling shown that the method which was using zip function was 2,23 times more time-effective than naive method, which was using three nested for loops in ikj-algorithm. Method was tested on two matrices of dimensions 5000x32 and 32x50.

Matrix class contains another method, which can print the matrix in human readable form. This function is then used to show the resulting matrix.


## Prerequisites

Program is created in python3. If you wish to run the tests you have to install pytest module. If you don't have it installed, you can install it by calling:

    $ pip install -r requirements.txt
inside your activated virtual environment.


## How to use

To run the program, you can clone this repository and then you can execute the mx_mul.py file inside:

    $ python3 mx_mul.py
    
After that command prompt will ask for user input. When user is asked to enter Matrix content, the values in row are separated by space character and the rows are separated by new line. Example (for width=3, height=2):
    
    Matrix A values: 
    1 2 3
    4 5 4

### Example

    $ python3 mx_mul.py

    Matrix A
    width: 2
    height: 3
    
    Matrix B
    width: 1
    height: 2
    
    Matrix A values:
    1 2
    5 3
    6 7
    
    Matrix B values:
    5
    1
    
    Result:
    7
    28
    37
