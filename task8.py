name_list = []
place_list = []
autor_list = []
while True:
    name = input("Введите название трека(Для завершения введите off):")
    if name != "off":
        name_list.append(name)
        place = input("Введите место в чарте:")
        place_list.append(place)
        autor = input("Введите исполнителя:")
        autor_list.append(autor)
    else:
        break
dict = {
    name_list[0]: [place_list[0], autor_list[0]],