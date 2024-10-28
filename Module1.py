#this is a program by elijah gonzalez, on 10/27. each question will be stated as well
#as answered

#multiply the numbers of seconds in a minute by the numbers of second, as well
#as assign it to a variable called seconds_per_hour

#assign the variable to 60 x 60, x is multiplication, which is an asterisk * in python
seconds_per_hour = (60 * 60)

#print the variable by using calling upon it

#we do this with a simple print statement
print(seconds_per_hour)

#calculate the seconds, but in a day. we can do this by multiplying our variable by 24 and
#saving it to a var(variable) called seconds_per_day

#we make our variable name, and then multiple seconds_per_hour by 24, and set the day variable
#= to our new varibale. we do that like we did with seconds, but with 24 and the variable for
#it instead
seconds_per_day = (seconds_per_hour * 24)

#next, to ensure it works, its asked we divide the day var to the seconds var. we should get 24
#we do this with a print statement and a /, which is divide.
print(seconds_per_day/seconds_per_hour)

#finally, we use // for division to see if we get a floating-point value.
print(seconds_per_day//seconds_per_hour)

#we do not! good to know if you do not want a float.