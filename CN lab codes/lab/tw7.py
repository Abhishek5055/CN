def crc_remainder(input_bitstring,polynomial):
    dividend = input_bitstring + '0'*(len(polynomial)-1)
    dividend = list(dividend)
    polynomial = list(polynomial)
    
    for i in range(len(input_bitstring)):
        if dividend[i]=='1':
            for j in range(len(polynomial)):
                dividend[i+j] = str(int(dividend[i+j])^int(polynomial[j]))
    
    remainder = ''.join(dividend)[-len(polynomial)+1:]
    codeword = input_bitstring+remainder
    return remainder,codeword

def crc_check(codeword,polynomial):
    remainder,temp = crc_remainder(codeword,polynomial)
    return remainder == '0'*(len(polynomial)-1)


if __name__ == "__main__":
    input_bitstrig =input("enter the message in bit format :")
    polynomial =input("enter the polynomial in bit format: ")
    
    remainder,codeword = crc_remainder(input_bitstrig,polynomial)
    
    print("input string : ",input_bitstrig)
    print("polynomial : ",polynomial)
    print("Remainder : ",remainder)
    print("codeword : ",codeword)
    
    choice  = int(input("enter ur choice \n1.error free transmission\n2.error transmission\n"))
    if choice == 1:
        is_valid = crc_check(codeword,polynomial)
    else:
        error_position = int(input("enter the index to simulate the error : "))
        codeword = codeword[:error_position] + ('1' if codeword[error_position]=='0' else '0')+ codeword[error_position+1:] 
        print("recieved codeword with error : ",codeword)
        is_valid = crc_check(codeword,polynomial)
        
    if is_valid:
        print("ther is no errror in the transmission and message is valid : ",codeword)
    else :
        print("there wase an error in the tramission of the message and the message is invalid :: ",codeword)