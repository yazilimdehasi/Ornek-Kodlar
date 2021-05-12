import random
print("Şifre hangilerini içersin ?:")
print("1. Sadece Küçük Harf")
print("2. Küçük ve Büyük Harf")
print("3. Küçük-Büyük Harf ve Rakam")
print("4. Küçük-Büyük Harf, Rakam ve Özel Karakterler")
option = int(input("Seçenek : "))
length = int(input("Şifre uzunluğu: "))

option1 = "abcdefghijklmnopqrstuvwxyz"
option2 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
option3 = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
option4 = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

if(option == 1):
    password =  "".join(random.sample(option1,length ))
elif(option == 2):
    password =  "".join(random.sample(option2,length ))
elif(option == 3):
    password =  "".join(random.sample(option3,length ))
elif(option == 4):
    password =  "".join(random.sample(option4,length ))

print ("Şifreniz: {0}".format(password))