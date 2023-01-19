import random

def multiply_until_4():
    #generate random int A between 1 and 9
    A = random.randint(1, 9)
    #same as above
    B = random.randint(1, 9)
    #multiply A and B together to have C
    C = A * B
    
    #loop until C is equal to 4
    while C != 4:
        #print A and C
        print(f'A: {A}, C: {C}')
        #generate new random integers for A and B
        A = random.randint(1, 9)
        B = random.randint(1, 9)
        #multiply A and B again
        C = A * B

    #print success and A and B when C is equal to 4 instead
    print(f'Success! A: {A}, B: {B}')

#call function 
multiply_until_4()