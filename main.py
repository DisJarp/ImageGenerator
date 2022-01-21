from PIL import Image

img = Image.open('data/Holst.jpg') # Силует
head = Image.open("data/Head/001.png") #Голова
body = Image.open("data/Body/001.png") #Тело
hairstyle = Image.open('data/Hairstyle/001.png') #Волосы
pants = Image.open("data/Pants/004.png") #Штаны
leftHand = Image.open("data/LeftHand/001.png") #Левая рука
rightHand = Image.open("data/RightHand/001.png") #Правая рука
slippers = Image.open("data/Slippers/001.png") #Тапки
belt = Image.open("data/Belt/001.png") #Пояс
underwear = Image.open("data/Underwear/001.png") #Одежда
brows = Image.open("data/Brows/001.png") #Брови
eyes = Image.open("data/Eyes/001.png") #Глаза
ears = Image.open("data/Ears/001.png") #Уши
nose = Image.open("data/Nose/001.png") #Нос
beard = Image.open("data/Beard/004.png") #Борода
mouth = Image.open("data/Mouth/001.png") #Рот

img.paste(head, (258,73), head) # Координаты головы
img.paste(body,(295, 318), body) #Координаты тела
img.paste(leftHand, (212, 354), leftHand) #Координаты левой руки
img.paste(rightHand, (451, 357), rightHand) #Координаты правой руки
img.paste(belt, (295, 483), belt) #Координаты пояса
img.paste(pants, (295, 495), pants) #Координаты штанов
img.paste(slippers, (314, 634), slippers) #Координаты тапок
img.paste(hairstyle, (240, 20),  hairstyle) #Координаты волос
img.paste(underwear, (295,318), underwear) #Координаты одежды
img.paste(brows, (360, 180), brows) #Координаты бровей
img.paste(eyes, (367, 190), eyes) #Координаты глаз
img.paste(ears,(277,75), ears) #Координаты ушей
img.paste(nose, (420, 252), nose) #Координаты носа
img.paste(beard, (295, 232), beard) #Координаты бороды
img.paste(mouth, (383, 290), mouth) #Координаты рта





img.save("Result/Result.png")