# Program 28: Write a program that accepts a sentence and calculate the number of letters and digits.

stri=input("enter your choice alphanumeric")
count=0
dcount=0
for c in stri:
    if c>='0' and c<='9':
        count=count+1
    elif (c>='A' and c<='Z') or(c>='a' and c<='z'):
        dcount=dcount+1
    else:
        pass
print('number of digit in th entered in string is ',count)
print('number of alphabet in th entered in string is ',dcount)    
