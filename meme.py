import sys
import os

sys.path.insert(0, '../')
from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api, random
import pyowm
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
login, password = "1log", "2par"


vk_session = vk_api.VkApi(login=login, password=password, app_id=2685278)
vk_session.auth(token_only=True)


session_api = vk_session.get_api()

longpoll = VkLongPoll(vk_session)

def send_message(peer_id, message=None, attachment=None, keyboard=None, payload=None):
    session_api.messages.send(peer_id=peer_id, message=message, random_id=random.randint(-2147483648, +2147483648),
                              attachment=attachment, keyboard=keyboard, payload=payload)



def next_string():
    strings = ('Правда!', 'Ложь!')
    if next_string.i < 0:
        try:
            with open("i.idx", 'r') as file:
                next_string.i = int(file.read())
        except Exception:
            pass
    next_string.i = (next_string.i + 1) % len(strings)
    with open("i.idx", 'w') as file:
        file.write(str(next_string.i))
    return strings[next_string.i]
next_string.i = -1



owm = pyowm.OWM('65a882aa1daf61d377752a1416d35c75', language="ru")
observation = owm.weather_at_place('Almaty')
w = observation.get_weather()
temp = w.get_temperature('celsius')['temp']
o=(' В Алматы сейчас '  + w.get_detailed_status())


p= (
        " Температура сейчас около " + str(temp)+' градусов')
topp=  '@damirka999 @tm_0999 @bumblebee004 @aristoooon @itssjennyferr @id584241530 @17nara770 @vikulishna29 @amiiiiina @id479145245 @pervutinskyarj1 @totsamyi077 @alekkkkssssandr @id443561996 @id404865326 @id345528912 @id504482091 @iloooonaaaa @l.brussel @io_ackles @anna.donetskaya @victoriakimm @m.shekhzade13 @kill_youself_lll @ekusherova @youngxr @ali_is_aitkali @poshelvpupok @szaykovsky @kammi_2306 @id301068083 @jojojo123 ,Че этому пидору надо?!'
anek='Летят как то в самолёте Путин, Трамп, Зеленский, Трамп значит говорит сейчас я сброшу 100$ и порадую одного человека! А Зеленский отвечает а вот я сейчас, сброшу 2 купюры по порадую двух людей! Путин сухмылкой:Я вот сейчас, двух долбоебов сброшу и весь мир обрадую!'


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        print('Текст сообщения: ' + str(event.text))
        response = event.text.lower()
        if response =='стас':
            send_message(peer_id=event.peer_id,message='Че надо сука?')



        if response == 'чё по погоде':
                send_message(peer_id=event.peer_id, message= o +
                p )
        if response == 'че по погоде':
                send_message(peer_id=event.peer_id, message= o +
                p )

        if response == 'правда?':
                send_message(peer_id=event.peer_id, message= '(next_string())' )
        if response == 'правда':
                send_message(peer_id=event.peer_id, message= '(next_string())' )
        if response == 'позвать всех':
                send_message(peer_id=event.peer_id, message= topp )
        if response == 'тварь':
                send_message(peer_id=event.peer_id, message='Да пошел ты нахуй,чертила!?')
        if response == 'фулл 1':
                send_message(peer_id=event.peer_id, attachment='video-174949577_456239541' )
        if response == 'фулл 2':
                send_message(peer_id=event.peer_id, attachment='video-174949577_456239078')
        if response == 'фулл 3':
                send_message(peer_id=event.peer_id, attachment='video-174949577_456239073')
        if response == 'фулл 4':
                send_message(peer_id=event.peer_id, attachment='video-174949577_456239060')
        if response == 'фулл 5':
                send_message(peer_id=event.peer_id, attachment='video-174949577_456239050')
        if response == 'фулл 6':
                send_message(peer_id=event.peer_id, attachment='video-174949577_456239612')
        if response == 'фулл 7':
                send_message(peer_id=event.peer_id, attachment='video-174949577_456239059')
        if response == 'фулл 8':
                send_message(peer_id=event.peer_id, attachment='video-174949577_456239052')
        if response == ' фулл 9':
                send_message(peer_id=event.peer_id, attachment='video-174949577_456239054')
        if response == ' фулл 10':
                send_message(peer_id=event.peer_id, attachment='video-174949577_456239053')
        if response == 'Видос':
                send_message(peer_id=event.peer_id, attachment='video-47949197_456251634')
        if response == 'не смешно':
                send_message(peer_id=event.peer_id, attachment='video51477544_456239146')
        if response == 'папич':
                send_message(peer_id=event.peer_id, attachment='video195739141_456239326')
        if response == 'что это было':
                send_message(peer_id=event.peer_id, attachment='video-30316056_456325255')
        if response == 'смешной':
                send_message(peer_id=event.peer_id, attachment='video-156480091_456259213')
        if response == 'пинг':
                send_message(peer_id=event.peer_id, message='понг')
        if response == 'пошел нахуй':
                send_message(peer_id=event.peer_id, attachment='photo484415038_457243592')
        if response == 'иди нахуй':
                send_message(peer_id=event.peer_id, attachment='photo484415038_457243592')
        if response == '+':
                send_message(peer_id=event.peer_id, message='++')
        if response == 'привет всем':
            send_message(peer_id=event.peer_id, message='Здарова,чувствуй себя как дома;)')
        if response == 'привет':
            send_message(peer_id=event.peer_id, message='Здарова,чувствуй себя как дома;)')
        if response == 'фулл':
                send_message(peer_id=event.peer_id,  message='Вбей фулл и цифру от 1 до 10')
        if response == 'соси':
                send_message(peer_id=event.peer_id,  message='А может быть ты!?')
        if response == 'кто я?':
                send_message(peer_id=event.peer_id,  message='Ты вероятнее всего малолетний дибил')
        if response == 'сука':
                send_message(peer_id=event.peer_id,  message='Че злой такой?!')
        if response == 'да':
                send_message(peer_id=event.peer_id,  message='Пизда')
        if response == 'ахуел?':
                send_message(peer_id=event.peer_id,  message='Ладно извини если быканул')
        if response == 'ахуел':
                send_message(peer_id=event.peer_id,  message='Ладно извини если быканул')
        if response == 'ахуел что ли':
                send_message(peer_id=event.peer_id,  message='Ладно извини если быканул')
        if response == 'ахуел что ли?':
                send_message(peer_id=event.peer_id,  message='Ладно извини если быканул')
        if response == 'ахуел что ле':
                send_message(peer_id=event.peer_id,  message='Ладно извини если быканул')
        if response == 'бля':
                send_message(peer_id=event.peer_id,  message='Извини если быканул')
        if response == 'нахуй':
                send_message(peer_id=event.peer_id,  message='да по приколу заебал)')
        if response == 'нахуй?':
                send_message(peer_id=event.peer_id,  message='да по приколу заебал)')
        if response == 'кто?':
                send_message(peer_id=event.peer_id, message='Да неважно уже')
        if response == 'кто':
                send_message(peer_id=event.peer_id, message='Да неважно уже')
        if response == '-':
                send_message(peer_id=event.peer_id, message='++')
        if response == 'жиза':
                send_message(peer_id=event.peer_id, message='++')
        if response == 'анекдот':
                send_message(peer_id=event.peer_id,  message= anek)










