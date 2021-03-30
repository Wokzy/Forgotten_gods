import random
import data_4



def shop_loc_2(l_char, gf, shop):

	shop.show_intro(l_char)

	l_char.loc_town = 2

	if l_char.find_work(5): ch = gf.player_ask_selection_iq("", shop.sel_min, shop.sel_max)
	else: ch = gf.player_ask_selection_iq("", shop.sel_min, shop.sel_max)

	if gf.is_exit_code(ch):
		return

	'''
	elif shop.is_drinks_selected(ch):

	elif shop.is_food_selected(ch):

	elif shop.is_weapons_selected(ch):

	elif shop.is_clothes_selected(ch):

	elif shop.is_special_selected(ch):

	elif shop.is_info_selected(ch):
	'''

	if shop.is_drinks_selected(ch):

		ch = shop.show_drinks(gf)

		if shop.is_drink_elixirs_selected(ch):

			ch = shop.ask_elixir_selection(gf, l_char)

			if gf.is_exit_code(ch):
				return

			if shop.is_elixir_info(ch):
				shop.show_elixir_info()
				gf.enter()
			else:
				item = shop.get_elixir(ch)

				if l_char.can_afford(item.price):
					l_char.buy_item(item, item.code)
					gf.update(l_char)

			shop_loc_2(l_char, gf, shop)
		if shop.is_drink_el_selected(ch):

			ch = shop.ask_el_selection(gf, l_char)

			if gf.is_exit_code(ch):
				return

			if shop.is_elixir_info(ch):
				shop.show_el_info()
				gf.enter()
			else:
				item = shop.get_el(ch)

				if l_char.can_afford(item.price):
					l_char.buy_item(item, item.code)
					gf.update(l_char)

			shop_loc_2(l_char, gf, shop)
		if shop.is_drink_hardel_selected(ch):

			ch = shop.ask_hardel_selection(gf, l_char)

			if gf.is_exit_code(ch):
				return

			if shop.is_elixir_info(ch):
				shop.show_hardel_info()
				gf.enter()
			else:
				item = shop.get_hardel(ch)

				if l_char.can_afford(item.price):
					l_char.buy_item(item, item.code)
					gf.update(l_char)

			shop_loc_2(l_char, gf, shop)
		if shop.is_drink_whitedragon_selected(ch):

			ch = shop.ask_whitedragon_selection(gf, l_char)

			if gf.is_exit_code(ch):
				return

			if shop.is_elixir_info(ch):
				shop.show_whitedragon_info()
				gf.enter()
			else:
				item = shop.get_whitedragon(ch)

				if l_char.can_afford(item.price):
					l_char.buy_item(item, item.code)
					gf.update(l_char)

			shop_loc_2(l_char, gf, shop)
		if shop.is_drink_reddragon_selected(ch):

			ch = shop.ask_reddragon_selection(gf, l_char)

			if gf.is_exit_code(ch):
				return

			if shop.is_elixir_info(ch):
				shop.show_reddragon_info()
				gf.enter()
			else:
				item = shop.get_reddragon(ch)

				if l_char.can_afford(item.price):
					l_char.buy_item(item, item.code)
					gf.update(l_char)

			shop_loc_2(l_char, gf, shop)
		if shop.is_drink_snake_selected(ch):

			ch = shop.ask_snake_selection(gf, l_char)

			if gf.is_exit_code(ch):
				return

			if shop.is_elixir_info(ch):
				shop.show_snake_info()
				gf.enter()
			else:
				item = shop.get_snake(ch)

				if l_char.can_afford(item.price):
					l_char.buy_item(item, item.code)
					gf.update(l_char)

			shop_loc_2(l_char, gf, shop)
		if shop.is_drink_vodka_selected(ch):

			ch = shop.ask_vodka_selection(gf, l_char)

			if gf.is_exit_code(ch):
				return

			if shop.is_elixir_info(ch):
				shop.show_vodka_info()
				gf.enter()
			else:
				item = shop.get_vodka(ch)

				if l_char.can_afford(item.price):
					l_char.buy_item(item, item.code)
					gf.update(l_char)

			shop_loc_2(l_char, gf, shop)

	elif shop.is_food_selected(ch):

		ch = shop.show_food(gf)

		if shop.is_food_pig_selected(ch):
			ch = shop.ask_pig_selection(gf, l_char)

			if gf.is_exit_code(ch):
				return

			if shop.is_elixir_info(ch):
				shop.show_pig_info()
				gf.enter()
			else:
				item = shop.get_pig(ch)

				if l_char.can_afford(item.price):
					l_char.buy_item(item, item.code)
					gf.update(l_char)

			shop_loc_2(l_char, gf, shop)

		elif shop.is_food_mutton_selected(ch):
			ch = shop.ask_mutton_selection(gf, l_char)

			if gf.is_exit_code(ch):
				return

			if shop.is_elixir_info(ch):
				shop.show_mutton_info()
				gf.enter()
			else:
				item = shop.get_mutton(ch)

				if l_char.can_afford(item.price):
					l_char.buy_item(item, item.code)
					gf.update(l_char)

			shop_loc_2(l_char, gf, shop)

		elif shop.is_food_beef_selected(ch):
			ch = shop.ask_beef_selection(gf, l_char)

			if gf.is_exit_code(ch):
				return

			if shop.is_elixir_info(ch):
				shop.show_beef_info()
				gf.enter()
			else:
				item = shop.get_beef(ch)

				if l_char.can_afford(item.price):
					l_char.buy_item(item, item.code)
					gf.update(l_char)

			shop_loc_2(l_char, gf, shop)

		elif shop.is_food_dragonmeat_selected(ch):
			ch = shop.ask_dragonmeat_selection(gf, l_char)

			if gf.is_exit_code(ch):
				return

			if shop.is_elixir_info(ch):
				shop.show_dragonmeat_info()
				gf.enter()
			else:
				item = shop.get_dragonmeat(ch)

				if l_char.can_afford(item.price):
					l_char.buy_item(item, item.code)
					gf.update(l_char)

			shop_loc_2(l_char, gf, shop)

		elif shop.is_food_yagodi_selected(ch):
			ch = shop.ask_yagodi_selection(gf, l_char)

			if gf.is_exit_code(ch):
				return

			if shop.is_elixir_info(ch):
				shop.show_yagodi_info()
				gf.enter()
			else:
				item = shop.get_yagodi(ch)

				if l_char.can_afford(item.price):
					l_char.buy_item(item, item.code)
					gf.update(l_char)

			shop_loc_2(l_char, gf, shop)

		elif shop.is_food_health_grass_selected(ch):
			ch = shop.ask_health_garss_selection(gf, l_char)

			if gf.is_exit_code(ch):
				return

			if shop.is_elixir_info(ch):
				shop.show_health_grass_info()
				gf.enter()
			else:
				item = shop.get_health_grass(ch)

				if l_char.can_afford(item.price):
					l_char.buy_item(item, item.code)
					gf.update(l_char)

			shop_loc_2(l_char, gf, shop)

	elif shop.is_weapons_selected(ch):

		ch = shop.show_weapon(gf)

		if shop.is_weapon_bows_selected(ch):
			ch = shop.ask_bows_selection(gf, l_char)

			if gf.is_exit_code(ch):
				return

			if shop.is_elixir_info(ch):
				shop.show_bows_info()
				gf.enter()
			else:
				item = shop.get_bows(ch)

				if l_char.can_afford(item.price):
					l_char.buy_weapon(item, item.code)
					gf.update(l_char)

			shop_loc_2(l_char, gf, shop)

		elif shop.is_weapon_arrows_selected(ch):
			ch = shop.ask_arrows_selection(gf, l_char)

			if gf.is_exit_code(ch):
				return

			if shop.is_elixir_info(ch):
				shop.show_arrows_info()
				gf.enter()
			else:
				item = shop.get_arrows(ch)

				if l_char.can_afford(item.price):
					l_char.buy_patron(item, item.code)
					gf.update(l_char)

			shop_loc_2(l_char, gf, shop)

		elif shop.is_weapon_pistols_selected(ch):
			ch = shop.ask_pistols_selection(gf, l_char)

			if gf.is_exit_code(ch):
				return

			if shop.is_elixir_info(ch):
				shop.show_pistols_info()
				gf.enter()
			else:
				item = shop.get_pistols(ch)

				if l_char.can_afford(item.price):
					l_char.buy_weapon(item, item.code)
					gf.update(l_char)

			shop_loc_2(l_char, gf, shop)

		elif shop.is_weapon_cold_weapon_selected(ch):
			ch = shop.ask_cold_weapon_selection(gf, l_char)

			if gf.is_exit_code(ch):
				return

			if shop.is_elixir_info(ch):
				shop.show_cold_weapon_info()
				gf.enter()
			else:
				item = shop.get_cold_weapon(ch)

				if l_char.can_afford(item.price):
					l_char.buy_weapon(item, item.code)
					gf.update(l_char)

			shop_loc_2(l_char, gf, shop)

		elif shop.is_weapon_patrons_selected(ch):
			ch = shop.ask_patrons_selection(gf, l_char)

			if gf.is_exit_code(ch):
				return

			if shop.is_elixir_info(ch):
				shop.show_patrons_info()
				gf.enter()
			else:
				item = shop.get_patrons_weapon(ch)

				if l_char.can_afford(item.price):
					l_char.buy_patron(item, item.code)
					gf.update(l_char)

			shop_loc_2(l_char, gf, shop)

	elif shop.is_clothes_selected(ch):

		ch = shop.show_clothes(gf)

		if shop.is_clothes_Head_clothes_selected(ch):
			ch = shop.ask_head_clothes_selection(gf, l_char)

			if gf.is_exit_code(ch):
				return

			if shop.is_elixir_info(ch):
				shop.show_head_clothes_info()
				gf.enter()
			else:
				item = shop.get_head_clothes(ch)

				if l_char.can_afford(item.price):
					l_char.buy_clothes(item, item.code)
					gf.update(l_char)

		elif shop.is_clothes_top_selected(ch):
			ch = shop.ask_top_selection(gf, l_char)

			if gf.is_exit_code(ch):
				return

			if shop.is_elixir_info(ch):
				shop.show_top_info()
				gf.enter()
			else:
				item = shop.get_top(ch)

				if l_char.can_afford(item.price):
					l_char.buy_clothes(item, item.code)
					gf.update(l_char)

		elif shop.is_clothes_bottom_selected(ch):
			ch = shop.ask_bottom_selection(gf, l_char)

			if gf.is_exit_code(ch):
				return

			if shop.is_elixir_info(ch):
				shop.show_bottom_info()
				gf.enter()
			else:
				item = shop.get_bottom(ch)

				if l_char.can_afford(item.price):
					l_char.buy_clothes(item, item.code)
					gf.update(l_char)

		elif shop.is_clothes_shoes_selected(ch):
			ch = shop.ask_shoes_selection(gf, l_char)

			if gf.is_exit_code(ch):
				return

			if shop.is_elixir_info(ch):
				shop.show_shoes_info()
				gf.enter()
			else:
				item = shop.get_shoes(ch)

				if l_char.can_afford(item.price):
					l_char.buy_clothes(item, item.code)
					gf.update(l_char)

		elif shop.is_clothes_gloves_selected(ch):
			ch = shop.ask_gloves_selection(gf, l_char)

			if gf.is_exit_code(ch):
				return

			if shop.is_elixir_info(ch):
				shop.show_gloves_info()
				gf.enter()
			else:
				item = shop.get_gloves(ch)

				if l_char.can_afford(item.price):
					l_char.buy_clothes(item, item.code)
					gf.update(l_char)

		elif shop.is_clothes_bronya_selected(ch):
			ch = shop.ask_bronya_selection(gf, l_char)

			if gf.is_exit_code(ch):
				return

			if shop.is_elixir_info(ch):
				shop.show_bronya_info()
				gf.enter()
			else:
				item = shop.get_bronya(ch)

				if l_char.can_afford(item.price):
					l_char.buy_clothes(item, item.code)
					gf.update(l_char)

		elif shop.is_clothes_mechanic_bronya_selected(ch):
			ch = shop.ask_mechanic_bronya_selection(gf, l_char)

			if gf.is_exit_code(ch):
				return

			if shop.is_elixir_info(ch):
				shop.show_mechanic_bronya_info()
				gf.enter()
			else:
				item = shop.get_mechanic_bronya(ch)

				if l_char.can_afford(item.price):
					l_char.buy_clothes(item, item.code)
					gf.update(l_char)

		elif shop.is_clothes_konkistodor_selected(ch):
			ch = shop.ask_konkistodor_selection(gf, l_char)

			if gf.is_exit_code(ch):
				return

			if shop.is_elixir_info(ch):
				shop.show_konkistodor_info()
				gf.enter()
			else:
				item = shop.get_konkistodor(ch)

				if l_char.can_afford(item.price):
					l_char.buy_clothes(item, item.code)
					gf.update(l_char)

	elif shop.is_special_selected(ch):

		ch = shop.show_special(gf)

		if shop.is_zelya_selected(ch):
			ch = shop.ask_zelya_selection(gf, l_char)

			if gf.is_exit_code(ch):
				return

			if shop.is_elixir_info(ch):
				shop.show_zelya_info()
				gf.enter()
			else:
				item = shop.get_zelya(ch)

				if l_char.can_afford(item.price):
					l_char.buy_item(item, item.code)
					gf.update(l_char)

		elif shop.is_scopes_selected(ch):
			ch = shop.ask_scopes_selection(gf, l_char)

			if gf.is_exit_code(ch):
				return

			if shop.is_elixir_info(ch):
				shop.show_scopes_info()
				gf.enter()
			else:
				item = shop.get_scopes(ch)

				if l_char.can_afford(item.price):
					l_char.buy_item(item, item.code)
					gf.update(l_char)

		elif shop.is_dop_for_weapon_selected(ch):
			ch = shop.ask_dop_for_weapon_selection(gf, l_char)

			if gf.is_exit_code(ch):
				return

			if shop.is_elixir_info(ch):
				shop.show_dop_for_weapon_info()
				gf.enter()
			else:
				item = shop.get_dop_for_weapon(ch)

				if l_char.can_afford(item.price):
					l_char.buy_item(item, item.code)
					gf.update(l_char)

		elif shop.is_off_noise_selected(ch):
			ch = shop.ask_off_noise_selection(gf, l_char)

			if gf.is_exit_code(ch):
				return

			if shop.is_elixir_info(ch):
				shop.show_off_noise_info()
				gf.enter()
			else:
				item = shop.get_off_noise(ch)

				if l_char.can_afford(item.price):
					l_char.buy_item(item, item.code)
					gf.update(l_char)



	elif shop.is_sell_selected(ch):
		while True:
			ch = shop.show_trades(gf)

			if shop.is_trades_selected(ch):
				print("Выберите рыбу для продажи:")

				k, n = 0, []
				for g in range(len(l_char.invent)):
					i = l_char.invent[g]
					if i.__class__.__name__ == 'Fish':
						k += 1
						print(k, '-', i.name, ',', i.price, 'медяков')
						n.append(g)

					#print(str(i+1) + " - " + str(g.name))


				ch = gf.player_ask_selection("", 1, len(n))

				ch_item = l_char.invent[n[ch-1]]
				del l_char.invent[n[ch-1]]

				print('Вы продали рыбу за ', ch_item.price, 'медяков.')
				l_char.mon += ch_item.price
				#shop.trade(l_char, ch_item, gf)
				gf.update(l_char)
			elif ch == 4:
				return
			elif ch == 2:
				c = 1
				idx = []
				for i in range(len(l_char.invent)):
					if l_char.invent[i].__class__.__name__ == 'Clothes':
						print(c, '-', l_char.invent[i], '-', l_char.invent[i].price, 'медяков.')
						c+=1
						idx.append(i)
				ch = gf.player_ask_selection('', 1, c)
				ch_item = l_char.invent[idx[ch-1]]
				del l_char.invent[idx[ch-1]]

				print('Вы продали одужду за ', ch_item.price, 'медяков.')
				l_char.mon += ch_item.price
				gf.update(l_char)
			elif ch == 3:
				for i in range(len(l_char.weap)):
					print(i, '-', l_char.weap[i], '-', l_char.weap[i].price, 'медяков.')

				ch_item = l_char.weap[gf.player_ask_selection('', 1, len(l_char.weap))-1]
				l_char.weap.remove(ch_item)

				print('Вы продали оружие за ', ch_item.price, 'медяков.')
				l_char.mon += ch_item.price
				gf.update(l_char)
			elif ch == -1:
				gf.get_player_info(l_char)
		'''
		elif shop.is_cancel_trades_selected(ch):
			if len(l_char.in_trade) == 0:
				print("У вас нет продающихся предметов!")
				gf.enter()
				gf.update(l_char)

			else:
				for i in range(len(l_char.in_trade)):
					g = l_char.in_trade[i]

					print(str(i+1) + " - " + str(g.name))

				ch = gf.player_ask_selection("", 0, len(l_char.in_trade))

				l_char.invent.append(l_char.in_trade[ch-1])
				print("Предмет " + str(l_char.in_trade[ch-1].name) + " находится в вашем инвентаре.")

				del l_char.in_trade[ch-1]

				gf.update(l_char)
		'''



	elif shop.is_talk_selected(ch):

		ch = shop.show_talk(gf, l_char)

		if ch == 1:
			if l_char.find_work(5):
				data_4.work_005(l_char, gf)
			else:
				print("1 - Как жизнь?")
				print("2 - Дарова!")
				print("3 - Bonan Avon (Привет на локрийском.)")
				print("4 - Приветствую мой друг.")
				print("5 - Пшп. Есть Харонт пару ягод.")


