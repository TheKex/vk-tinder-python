from vk import *


# Активируем бота
def start_bot():
    users_list = []  # list с информацией о пользователе
    current_user_index = 0  # Индекс текущей пары в списке найденных пар
    favorite_users = []  # Список избранных пар
    offset = 0  # Смещение относительно первого найденного пользователя для выборки определенного подмножества, он же обход ограничения count поиска
    # Бот начинает работу
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                request = event.text.lower()
                if request == "привет":
                    write_msg(event.user_id, "Здравствуйте, я бот VKinder. "
                                             "Я помогу найти вам пару в социальной сети ВКонтакте! "
                                             "Для начала работы, введите команду 'Ввести данные для поиска'.\n"
                                             "Если вы хотите завершить работу, то напишите 'пока'.")
                elif request == "пока":
                    write_msg(event.user_id, "До свидания, было приятно с вами работать!")
                elif request == "ввести данные для поиска":
                    city_name = get_city_name(event.user_id)
                    age = get_age(event.user_id)
                    write_msg(event.user_id, "Отлично, данные получены! Чтобы найти себе пару "
                                             "введите команду 'Найти пару' "
                                             "Если вы хотите ввести новые данные поиска, "
                                             "то повторите команду 'Ввести данные для поиска'.")
                elif request == "найти пару":
                    user_info = get_user_info(event.user_id)
                    found_users = search(user_info, city_name, age)
                    if found_users:
                        users_list = found_users
                        current_user_index = 0
                        user_photos = get_user_photos(users_list[current_user_index]["id"])
                        write_msg(event.user_id, format_user_info(users_list[current_user_index]),
                                  ",".join(user_photos))
                        write_msg(event.user_id, "Добавить пару в избранное?\n Да/Нет\n"
                                                 "Чтобы продолжить поиск введите команду 'Дальше'.")
                    else:
                        write_msg(event.user_id, "К сожалению, не найдено подходящей пары")
                elif request == "дальше":
                    try:
                        if users_list:
                            current_user_index = current_user_index + 1
                            user_photos = get_user_photos(users_list[current_user_index]["id"])
                            write_msg(event.user_id, format_user_info(users_list[current_user_index]),
                                      ",".join(user_photos))
                            write_msg(event.user_id, "Добавить пару в избранное?\n Да/Нет\n"
                                                     "Чтобы продолжить поиск введите команду 'Дальше'.")
                        else:
                            write_msg(event.user_id, "К сожалению, не найдено подходящей пары")
                    # Обход ограничения count поиска
                    except IndexError:
                        offset += 3
                        found_users = search(user_info, city_name, age, offset=offset)
                        if found_users:
                            users_list = found_users
                            current_user_index = 0
                            user_photos = get_user_photos(users_list[current_user_index]["id"])
                            write_msg(event.user_id, format_user_info(users_list[current_user_index]),
                                      ",".join(user_photos))
                            write_msg(event.user_id, "Добавить пару в избранное?\n Да/Нет\n"
                                                     "Чтобы продолжить поиск введи команду 'Дальше'.")
                elif request == "да":
                    if users_list:
                        favorite_users.append(users_list[current_user_index])
                        write_msg(event.user_id, "Пара добавлена в избранное. "
                                                 "Чтобы увидеть список избранных пар "
                                                 "введите команду 'избранное'.")
                    else:
                        write_msg(event.user_id, "Не удалось добавить пару в избранное.")
                elif request == "нет":
                    write_msg(event.user_id, "Пара не была добавлена в избранное.")
                elif request == "избранное":
                    if favorite_users:
                        favorite_list = "\n".join([format_user_info(user) for user in favorite_users])
                        write_msg(event.user_id, "Список избранных пар:\n" + favorite_list)
                    else:
                        write_msg(event.user_id, "Список избранных пар пуст.")
                else:
                    write_msg(event.user_id, "Не понял вашего ответа...")


if __name__ == "__main__":
    start_bot()
