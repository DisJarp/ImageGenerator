from PIL import Image
import os
import itertools
import difflib as df

dataAll = {}
count = 0
path = 'data/'
sovpal = False

with open("log/count.txt", "r") as file:
    for line in file:
        line = line.strip()
        count = int(line)
print("Общее число генераций = " + str(count))

for pathFolder,__, item in os.walk(path):
    dataAll[str(pathFolder.split("/")[1])] = item

c = list(itertools.product(dataAll['Fon'], dataAll["Head"], dataAll["Body"],dataAll["Hairstyle"],dataAll["Pants"],dataAll["LeftHand"],
                           dataAll["RightHand"],dataAll["Slippers"],dataAll["Belt"],dataAll["Sweatshirt"],dataAll["Brows"],dataAll["Eyes"],
                           dataAll["Ears"],dataAll["Nose"],dataAll["Beard"],dataAll["Mouth"]))

for i in c:
    with open("log/logFile.txt", "r") as file:
        for line in file:
            line = line.strip()
            if (str(line) == str(i)):
                print("\n\n\n")
                print("Есть совпадение")
                print("i = " + str(i) + "\n ---> \nline = " + str(line))
                print("\n\n\n")
                sovpal = True

    if not sovpal:
        img = Image.open('data/Fon/' + str(i[0]))  # Холст
        head = Image.open("data/Head/" + str(i[1])) #Голова
        body = Image.open("data/Body/" + str(i[2])) #Тело
        hairstyle = Image.open('data/Hairstyle/' + str(i[3])) #Волосы
        pants = Image.open("data/Pants/" + str(i[4])) #Штаны
        leftHand = Image.open("data/LeftHand/" + str(i[5])) #Левая рука
        rightHand = Image.open("data/RightHand/" + str(i[6])) #Правая рука
        slippers = Image.open("data/Slippers/" + str(i[7])) #Тапки
        belt = Image.open("data/Belt/" + str(i[8])) #Пояс
        sweatshirt = Image.open("data/Sweatshirt/" + str(i[9])) #Одежда
        brows = Image.open("data/Brows/" + str(i[10])) #Брови
        eyes = Image.open("data/Eyes/" + str(i[11])) #Глаза
        ears = Image.open("data/Ears/" + str(i[12])) #Уши
        nose = Image.open("data/Nose/" + str(i[13])) #Нос
        beard = Image.open("data/Beard/" + str(i[14])) #Борода
        mouth = Image.open("data/Mouth/" + str(i[15])) #Рот

        img.paste(head, (0,0), head) # Координаты головы
        img.paste(body,(0, 0), body) #Координаты тела
        img.paste(leftHand, (0, 0), leftHand) #Координаты левой руки
        img.paste(rightHand, (0, 0), rightHand) #Координаты правой руки
        img.paste(belt, (0, 0), belt) #Координаты пояса
        img.paste(pants, (0, 0), pants) #Координаты штанов
        img.paste(slippers, (0, 0), slippers) #Координаты тапок
        img.paste(hairstyle, (0, 0),  hairstyle) #Координаты волос
        img.paste(sweatshirt, (0,0), sweatshirt) #Координаты одежды
        img.paste(brows, (0, 0), brows) #Координаты бровей
        img.paste(eyes, (0, 0), eyes) #Координаты глаз
        img.paste(ears,(0,0), ears) #Координаты ушей
        img.paste(nose, (0, 0), nose) #Координаты носа
        img.paste(beard, (0, 0), beard) #Координаты бороды
        img.paste(mouth, (0, 0), mouth) #Координаты рта

        img.save("Result/"+str(count)+".png")
        count +=1

        with open("log/logFile.txt", "a") as file:
            file.write("\n" +str(i))
        print("Количество сгенерированных = "+ str(count))
    else:
        sovpal = False

with open("log/logFile.txt", "a") as file:
    file.write(str(count))
print("Генерация закончена! Сгенерированно:  " + str(count))

