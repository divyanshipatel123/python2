def swapData():
    #Taking the inputs from the user
    fileA = input('Enter the first file name : ')
    fileB = input('Enter the second file name : ')
    #storing data of files in variable data_a and data_b
    with open(fileA,'r') as a :
        data_a = a.read()
    with open(fileB,'r') as b :
        data_b = b.read()
    #writing the data in the files in reversed order
    with open(fileA,'w') as ab :
        ab.write(data_b)
    with open(fileB,'w') as ba :
        ba.write(data_a)
    #Printing completion message
    print('Your data has been reversed successfully !!')

swapData()