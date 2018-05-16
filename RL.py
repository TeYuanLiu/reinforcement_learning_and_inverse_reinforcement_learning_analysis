######################
# Author: Te-Yuan Liu
######################

######################
# Import library
######################
import numpy as np

######################
# Define function
######################
def init_P(_w):
    # 0:up, 1:down, 2:left, 3:right
    w = _w
    P = np.zeros((4,100,100))

    P[0,0,0] = 1 - w + w/4 + w/4
    P[0,0,1] = w/4
    P[0,0,10] = w/4

    P[0,9,8] = 1 - w + w/4
    P[0,9,9] = w/4 + w/4
    P[0,9,19] = w/4

    P[0,90,90] = 1 - w + w/4 + w/4
    P[0,90,91] = w/4
    P[0,90,80] = w/4

    P[0,99,98] = 1 - w + w/4
    P[0,99,99] = w/4 + w/4
    P[0,99,89] = w/4

    P[1,0,0] = w/4 + w/4
    P[1,0,1] = 1 - w + w/4
    P[1,0,10] = w/4

    P[1,9,8] = w/4
    P[1,9,9] = 1 - w + w/4 + w/4
    P[1,9,19] = w/4

    P[1,90,90] = w/4 + w/4
    P[1,90,91] = 1 - w + w/4
    P[1,90,80] = w/4

    P[1,99,98] = w/4
    P[1,99,99] = 1 - w + w/4 + w/4
    P[1,99,89] = w/4

    P[2,0,0] = 1 - w + w/4 + w/4
    P[2,0,1] = w/4
    P[2,0,10] = w/4

    P[2,9,8] = w/4
    P[2,9,9] = 1 - w + w/4 + w/4
    P[2,9,19] = w/4

    P[2,90,90] = w/4 + w/4
    P[2,90,91] = w/4
    P[2,90,80] = 1 - w + w/4

    P[2,99,98] = w/4
    P[2,99,99] = w/4 + w/4
    P[2,99,89] = 1 - w + w/4

    P[3,0,0] = w/4 + w/4
    P[3,0,1] = w/4
    P[3,0,10] = 1 - w + w/4

    P[3,9,8] = w/4
    P[3,9,9] = w/4 + w/4
    P[3,9,19] = 1 - w + w/4

    P[3,90,90] = 1 - w + w/4 + w/4
    P[3,90,91] = w/4
    P[3,90,80] = w/4

    P[3,99,98] = w/4
    P[3,99,99] = 1 - w + w/4 + w/4
    P[3,99,89] = w/4
    
    for i in range(10):
        for j in range(10):
            if (i,j) not in ((0,0),(0,9),(9,0),(9,9)):
                P[0,i*10+j,i*10+max(j-1,0)] = 1 - w + w/4
                P[0,i*10+j,i*10+min(j+1,9)] = w/4
                P[0,i*10+j,max(i-1,0)*10+j] = w/4
                P[0,i*10+j,min(i+1,9)*10+j] = w/4

                P[1,i*10+j,i*10+max(j-1,0)] = w/4
                P[1,i*10+j,i*10+min(j+1,9)] = 1 - w + w/4
                P[1,i*10+j,max(i-1,0)*10+j] = w/4
                P[1,i*10+j,min(i+1,9)*10+j] = w/4

                P[2,i*10+j,i*10+max(j-1,0)] = w/4
                P[2,i*10+j,i*10+min(j+1,9)] = w/4
                P[2,i*10+j,max(i-1,0)*10+j] = 1 - w + w/4
                P[2,i*10+j,min(i+1,9)*10+j] = w/4

                P[3,i*10+j,i*10+max(j-1,0)] = w/4
                P[3,i*10+j,i*10+min(j+1,9)] = w/4
                P[3,i*10+j,max(i-1,0)*10+j] = w/4
                P[3,i*10+j,min(i+1,9)*10+j] = 1 - w + w/4
    return P

def init_R():
    R1 = np.zeros((10,10))
    R1[9,9] = 1

    R2 = np.zeros((10,10))
    R2[9,9] = 10
    R2[1:7,4] = -100
    R2[1,5:7] = -100
    R2[2:4,6] = -100
    R2[3,7:9] = -100
    R2[4:8,8] = -100
    R2[7,6:8] = -100
    R2[8,6] = -100

    return R1,R2

######################
# Main function
######################
def main():
    print("hello")
    R1, R2 = init_R()
    print(R2)
if __name__ == "__main__":
    main()
