from PIL import Image
import os
import itertools

dataAll = []
count = 1
path = 'data/'
for pathFolder,__, item in os.walk(path):
    print(str(pathFolder) +" " + str(item))
    dataAll.append(item)



print("\n\n\n")
c = list(itertools.product(dataAll[1], dataAll[2], dataAll[3],dataAll[4],dataAll[5],dataAll[6],dataAll[7],dataAll[8],dataAll[9],dataAll[10],dataAll[11],dataAll[12],
                           dataAll[13],dataAll[14],dataAll[15],dataAll[16]))
print("\n\n\n")
print()
for i in c:
    # print(i)
    # img = Image.open('data/Fon/' + str(i[12]))  # Холст
    # head = Image.open("data/Head/" + str(i[6])) #Голова
    # body = Image.open("data/Body/" + str(i[3])) #Тело
    # hairstyle = Image.open('data/Hairstyle/' + str(i[5])) #Волосы
    # pants = Image.open("data/Pants/" + str(i[0])) #Штаны
    # leftHand = Image.open("data/LeftHand/" + str(i[15])) #Левая рука
    # rightHand = Image.open("data/RightHand/" + str(i[4])) #Правая рука
    # slippers = Image.open("data/Slippers/" + str(i[10])) #Тапки
    # belt = Image.open("data/Belt/" + str(i[7])) #Пояс
    # sweatshirt = Image.open("data/Sweatshirt/" + str(i[14])) #Одежда
    # brows = Image.open("data/Brows/" + str(i[13])) #Брови
    # eyes = Image.open("data/Eyes/" + str(i[8])) #Глаза
    # ears = Image.open("data/Ears/" + str(i[1])) #Уши
    # nose = Image.open("data/Nose/" + str(i[9])) #Нос
    # beard = Image.open("data/Beard/" + str(i[11])) #Борода
    # mouth = Image.open("data/Mouth/" + str(i[2])) #Рот
    #
    # img.paste(head, (0,0), head) # Координаты головы
    # img.paste(body,(0, 0), body) #Координаты тела
    # img.paste(leftHand, (0, 0), leftHand) #Координаты левой руки
    # img.paste(rightHand, (0, 0), rightHand) #Координаты правой руки
    # img.paste(belt, (0, 0), belt) #Координаты пояса
    # img.paste(pants, (0, 0), pants) #Координаты штанов
    # img.paste(slippers, (0, 0), slippers) #Координаты тапок
    # img.paste(hairstyle, (0, 0),  hairstyle) #Координаты волос
    # img.paste(sweatshirt, (0,0), sweatshirt) #Координаты одежды
    # img.paste(brows, (0, 0), brows) #Координаты бровей
    # img.paste(eyes, (0, 0), eyes) #Координаты глаз
    # img.paste(ears,(0,0), ears) #Координаты ушей
    # img.paste(nose, (0, 0), nose) #Координаты носа
    # img.paste(beard, (0, 0), beard) #Координаты бороды
    # img.paste(mouth, (0, 0), mouth) #Координаты рта
    #
    # img.save("Result/"+str(count)+".png")
    count +=1

print(count)

