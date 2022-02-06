import random
lower="qwertyuiopasdfghjklzxcvbnm"
upper="QWERTYUIOPASDFGHJKLZXCVBNM"
number="1234567890"
sybol="!@#$%&()}{[]\?"
all=lower+upper+number+sybol
length=30
password="".join(random.sample(all,length))
print("Your new password is : ",password)