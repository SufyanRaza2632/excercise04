matriculation_number = input ("enter any number")                     #Number in String 
matriculation_number = int(matriculation_number)                      #convert string to integer
print (matriculation_number)
sum_of_number = 0                                                     #create an integer variable to store the sum 

while matriculation_number != 0:
    sum_of_number = sum_of_number + (matriculation_number % 10)       #adds the last digit of number to sum
    matriculation_number = int (matriculation_number / 10)            #drops the last digit of  number

print("The digit sum of number is "
      + str(sum_of_number))                                           #convert the sum back to string before concatenating
