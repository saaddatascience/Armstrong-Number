# armstrong number 
 
n = int(input("Enter the Number \n"))
sum = 0
length_n = len(str(n))
copy_n = n

while(n>0):
    digit = n % 10  # 8891 jab 10 se divide hoga to remainder bacha ga 1
    sum += digit ** length_n # pir 1 multiply hoga 4 sse 
    n = n//10  # pir 8891 '//' hoga 10 se answer will be 889.1 but show 889 hoga kyoke '//' decimal value ko ignore kar deta ha 
    
if (sum==copy_n):
    print(f"{copy_n} is an armstrong number")
    
else:
    print(f"{copy_n} is not an armstrong number")        


    