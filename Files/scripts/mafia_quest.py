import random

# Перед стартом прописать, чтобы небыло взятых квестов и этот квест не был пройден.


def start(l_char, gf):
	print('Это, друг мой, местная мафия, я если честно её ненавижу.')
	gf.enter()
	print('Каждые 2 дня они здесь появляются с грохотом, шумом. И ведь')
	print('им ничего не скажешь, ничего не сделаешь, у них оружия вогон,')
	print('да и наёмников прилично. Причём не простых наёмников, а из элитного отряда.')
	gf.enter()
	print('Хоть днём они почти бессильны, ночью они правят городом.')
	gf.enter()
	print('Я знаю где их логово, вот если бы кто помог бы мне их грохнуть,')
	print('стало бы намного лучше. Да и влогове их полно денег.')
	gf.enter()
	print('')

	print('1 - Я помогу (Начать задание)')
	print('2 - Да, не повезло тебе, помочь тебе к сожалению я ничем не могу (Уйти)')

	ch = gf.player_ask_selection('', 1, 2)

	if ch == 2: return 'Выход'

	l_char.work = 'Избавление от мафии'
	global team
	team = None

	print(' - Дааа, таких смельчаков я ещё не встречал, но это даже к лучшему.')
	gf.enter()
	print('Дело это оооочень не простое, поэтому я думаю нам нужна команда.')
	print('')

	print('1 - Безусловно нужна.')
	print('2 - У меня есть свои люди.')
	print('3 - Мы справимся и без команды.')

	ch = gf.player_ask_selection('', 1, 3)

	if ch == 1:
		team = True
		print('Отлично, позже мы найдём команду.')
	elif ch == 2:
		team = False
		print('Хорошо, надеюсь они не подведут.')
	else:
		team = False
		print('Гм. Дело рискованное, но думаю попробовать стоит.')
	gf.enter()
	print('Рюмку белого дракона пожалуйста. *Игрок казино*')
	print('В общем ступай, как будешь готов к делу, приходи. Меня к стати Алан зовут. - Бармен')
	return 'Выход'



def mafia_quest(l_char, gf):
	print('Подойдя к барной стройке вы слышите шум распахивающихся дверей.')
	gf.enter()
	print('В казино входят три мужика, похожих на бандита и два качка вместе с ними.')
	gf.enter()
	print('- Слышь, отпрыск, налей нам по рюмке красного дракона, да не жалей, я')
	print('поиграть сегодня знатно хочу.')
	gf.enter()
	print('Бармен со страхом быстро наливает 5 рюмок красного дракона и приподнимает руки.')
	gf.enter()
	print(' - Разбирайте и пойдёмте. - сказал мужик и кинул деньги на стойку.')
	gf.enter()

	l_char.work_finish.append('Разговор в казино про мафию')

	print('1 - Спросить у бармена кто это (Перейти к возможности начать задание)')
	print('2 - Заказать выпивку')
	print('3 - Уйти')

	ch = gf.player_ask_selection('', 1, 3)

	if ch == 1:
		start(l_char, gf)
	elif ch == 2: return 'Заказ выпивки'
	else: return 'Выход'




def mafia_quest_part_2(l_char, gf):
	global team
	print('Ну здравтвуй, как тебя зовут, спросить забыл?')
	gf.enter()
	print(' - ', l_char.name.title())
	gf.enter()
	print('Отлично, ', l_char.name.title())

	if team:
		print('Так, давай для начала соберём команду.')
		collect_team(l_char, gf)
	
	print('Чтож, пойдём за мной, обсудим план.')