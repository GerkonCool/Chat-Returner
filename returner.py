import vk, time
toReturn = []
print("                                          Returner [0.0.1]"
      "\nВаши данные (логин, пароль) никому не передаются, и для полной безопасности, после работы программы"
      " Переменные login и password будут обнулены.\nПрограмма имеет доступ только к методу \'messages\', она используется"
      " для получения списка бесед, и ничего более.\nЕсли на аккаунте установлена двухэтапная аутентификация, то, к сожалению,"
      " программа не сможет работать, т.к. не пройдет авторизацию.\nПрограмма предназначена для выхода из бесед, из которых вы вышли и удалили "
      " диалог беседы, если Вас выгнали из беседы, то данная программа не вернет Вас туда.\nВ списке бесед видно только те беседы, в которые можно вернуться.")
try:
      login = input("\nЛогин [телефон]: ")
      password = input("\nПароль: ")
      session = vk.AuthSession("6044369", login, password, scope="messages")
      vk = vk.API(session)
except Exception as E:
      print("Ошибка: ", E)
      print("Попробуйте выполнить вход еще раз.")
      exit()
print("Получение списка бесед...")
for i in range(1,1000):
      try:
            i += 1
            if vk.messages.getChat(chat_id=i).get('left') == 1:
                  toReturn.append(vk.messages.getChat(chat_id=i).get('chat_id'))
                  print("Найдено: ", len(toReturn), "бесед, в которые можно вернуться.")
            time.sleep(1)
      except Exception:
            break
print("Беседы, в которые можно вернуться:")
for i in toReturn:
      print("{0}. {1}".format(i, vk.messages.getChat(chat_id=i).get('title')))
ReturnToChat = int(input(("Введите номер беседы, в которую нужно вернуться: ")))
vk.messages.send(chat_id=ReturnToChat, message=".")
print("Вы вернулись в беседу {0}!".format(vk.messages.getChat(chat_id=ReturnToChat).get('title')))
print("Спасибо за использование программы!")
login = 0
password = 0
exit("Логин и пароль обнулены для безопасности, выход.")
