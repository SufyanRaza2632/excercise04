matriculation_number = input ("enter any number")                     #Number in String 
matriculation_number = int(matriculation_number)                      #convert string to integer
print (matriculation_number)
number = matriculation_number                                         #create another variable to store the value of entered number
sum_of_number = 0                                                     #create an integer variable to store the sum 

while matriculation_number != 0:
    sum_of_number = sum_of_number + (matriculation_number % 10)       #adds the last digit of number to sum
    matriculation_number = int (matriculation_number / 10)            #drops the last digit of  number


difference = number - sum_of_number                                   #subtracts digit sum from the orignal number
print("The difference of number is "
      + str(difference))                                              #convert the sum back to string before concatenating
