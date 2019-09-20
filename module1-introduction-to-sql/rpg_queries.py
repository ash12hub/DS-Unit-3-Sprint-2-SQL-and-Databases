import os
import pandas as pd
import sqlite3

CONN = sqlite3.connect('rpg_db.sqlite3')

cursor1 = CONN.cursor()

query1 = 'SELECT count(character_id) FROM charactercreator_character;'
character_count = cursor1.execute(query1).fetchone()[0]
print(f'Total number of players: {character_count}\n')

cursor1.close()


cursor2 = CONN.cursor()

query2_cleric = 'SELECT count(character_ptr_id) FROM charactercreator_cleric;'
clerics = cursor2.execute(query2_cleric).fetchone()[0]

query2_fighter = ('SELECT count(character_ptr_id)' +
                  ' FROM charactercreator_fighter;')
fighters = cursor2.execute(query2_fighter).fetchone()[0]

query2_mage = 'SELECT count(character_ptr_id) FROM charactercreator_mage;'
mages = cursor2.execute(query2_mage).fetchone()[0]
query2_necromancer = ('SELECT count(mage_ptr_id)' +
                      ' FROM charactercreator_necromancer;')
necromancers = cursor2.execute(query2_necromancer).fetchone()[0]

query2_thief = 'SELECT count(character_ptr_id) FROM charactercreator_thief;'
thieves = cursor2.execute(query2_thief).fetchone()[0]

print(f'Number of Clerics: {clerics}\n' +
      f'Number of Fighters: {fighters}\n' +
      f'Number of Mages: {mages}\n' +
      f'Number of Mages who are Necromancers: {necromancers}\n'
      f'Number of thieves: {thieves}\n')

cursor2.close()


cursor3 = CONN.cursor()

query3_item_count = 'SELECT count(item_id) FROM armory_item;'
item_count = cursor3.execute(query3_item_count).fetchone()[0]
print(f'Total number of items: {item_count}')
query3_weapon_count = 'SELECT count(item_ptr_id) FROM armory_weapon;'
weapon_count = cursor3.execute(query3_weapon_count).fetchone()[0]
print(f'Items that are weapons: {weapon_count}')
non_weapon_items = item_count - weapon_count
print(f'Items that are not weapons: {non_weapon_items}\n')

cursor3.close()


cursor4 = CONN.cursor()

query4_character_item_count = ('SELECT character_id, count(item_id) FROM ' +
                               'charactercreator_character_inventory ' +
                               'GROUP BY character_id')

character_items = cursor4.execute(query4_character_item_count).fetchall()
character_items = pd.DataFrame(character_items)
print(f'Number of items held by characters:\n{character_items}')

query4_character_weapon_count = ('SELECT character_id, count(item_id) ' +
                                 'FROM charactercreator_character_inventory ' +
                                 'WHERE character_id < 50 AND ' +
                                 'item_id in '
                                 '(SELECT item_ptr_id FROM armory_weapon)' +
                                 'GROUP BY character_id')

character_weapons = cursor4.execute(query4_character_weapon_count).fetchall()
character_weapons = pd.DataFrame(character_weapons,
                                 columns={'character_id', 'weapon_count'})
print(f'Number of weapons held by characters:\n{character_weapons}')

cursor4.close()


cursor5 = CONN.cursor()

print(sum(character_weapons['weapon_count']))
