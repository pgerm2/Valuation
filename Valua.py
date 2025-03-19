
print ('Welcome!')
print('Please Follow the Instructions')
print('---------------------------')

def valuation():
    

    ticker= str(input("Please input company or ticker: "))
    print('\n')

    print(f"You chose: {ticker}")
    print('\n')

    pe= int(input("Please input the P/E: "))


    print('\n')

    print(f"You chose: {pe}")
    print('\n')

    pbv= int(input("Please input the PBV: "))
    print('\n')

    print(f"You chose: {pbv}")
    print('\n')

    eps= int(input("Please input the EPS: "))
    print('\n')

    print(f"You chose: {eps}")
    print('\n')

    #print("These are your selections: " + ticker +", " + pe +", "+ pbv +", "+eps)

    #Price Earnings Loop
    while True:
        if pe < 10:
            numq = 1
            perateq = numq + 1
            print(perateq)
            
            break
        
        elif pe > 10 and pe < 20:
            numw = 2
            peratew = numw + 1
            print(peratew)
            break
        
        elif pe > 20 and pe < 30:
            nume = 3
            peratee = nume + 1
            print(peratee)
            break
        
        else:
            print ('NO')
            break

    #Price to Book Value loop
    while True:
        if pbv < 100:
            numpbvq = 10
            pbvrateq = numpbvq + 2
            print(pbvrateq)
            break
        
        elif pbv > 100 and pbv < 200:
            numpbvw = 20
            pbvratew = numpbvw + 2
            print(pbvratew)
            break
        
        elif pbv > 200 and pbv < 300:
            numpbve = 30
            pbvratee = numpbve + 2
            print(pbvratee)
            break
        
        else:
            print ('NO')
            break

    #Earning Per Share loop
    while True:
        if eps < 10:
            numepsq = 100
            epsrateq = numepsq + 3
            print(epsrateq)
            break
        
        elif eps > 10 and eps < 20:
            numepsw = 200
            epsratew = numepsw + 2
            print(epsratew)
            break
        
        elif eps > 20 and eps < 30:
            numepse = 300
            epsratee = numepse + 2
            print(epsratee)
            break
        
        else:
            print ('NO')
            break

    print(perateq + pbvrateq + epsrateq)
    
valuation()





###Option A. The following only allows you to enter a integer. If you enter anything else you get a error
##    #Must add error exception
##
### An input is requested and stored in a variable
##test_text = input ("Enter a number: ")
##
### Converts the string into an integer. If you need
### to convert the user input into the decimal format,
### the float() function is used instead of int()
##test_number = int(test_text)
##
### Prints in the console the variable as requested
##print ("The number you entered is: ", test_number)
##
##
###This combines option A into one line
##test_number = int(input("Enter a number: "))
##print ("The number you entered is: ", test_number)




 


