from cards import *


################ AGE 1 CARDS ####################
age_1_cards = []
age = 1
tech_tree = {}
tech_tree['prev'] = []

#Blue cards:
name = "ALTAR"
cost_req = []
tech_tree['next'] = ["TEMPLE",]
min_players = 3
card = BlueCard(name, cost_req, tech_tree, age, min_players,2)
age_1_cards += [card,]
min_players = 5
card = BlueCard(name, cost_req, tech_tree, age, min_players,2)
age_1_cards += [card,]
###
name = "BATHS"
cost_req = ["STONE",]
tech_tree['next'] = ["AQUEDUCT",]
min_players = 3
card = BlueCard(name, cost_req, tech_tree, age, min_players,3)
age_1_cards += [card,]
min_players = 7
card = BlueCard(name, cost_req, tech_tree, age, min_players,3)
age_1_cards += [card,]
###
name = "PAWNSHOP"
cost_req = []
tech_tree['next'] = []
min_players = 4
card = BlueCard(name, cost_req, tech_tree, age, min_players,3)
age_1_cards += [card,]
min_players = 7
card = BlueCard(name, cost_req, tech_tree, age, min_players,3)
age_1_cards += [card,]
###
name = "THEATER"
cost_req = []
tech_tree['next'] = ['STATUE',]
min_players = 3
card = BlueCard(name, cost_req, tech_tree, age, min_players,2)
age_1_cards += [card,]
min_players = 6
card = BlueCard(name, cost_req, tech_tree, age, min_players,2)
age_1_cards += [card,]

#Brown cards:
name = "CLAY PIT"
cost_req = [1,]
tot_rsrc = 1
rsrc_list = ['BRICK','ORE']
min_players = 3
card = BrownResource(name, cost_req,  age, min_players, tot_rsrc, rsrc_list)
age_1_cards += [card,]
###
name = "CLAY POOL"
cost_req = []
min_players = 3
tot_rsrc = 1
rsrc_list = ['BRICK']
card = BrownResource(name, cost_req,  age, min_players, tot_rsrc, rsrc_list)
age_1_cards += [card,]
min_players = 5
card = BrownResource(name, cost_req,  age, min_players, tot_rsrc, rsrc_list)
age_1_cards += [card,]
###
name = "EXCAVATON"
cost_req = [1,]
min_players = 4
tot_rsrc = 1
rsrc_list = ['STONE','BRICK']
card = BrownResource(name, cost_req,  age, min_players, tot_rsrc, rsrc_list)
age_1_cards += [card,]
###
name = "FOREST CAVE"
cost_req = [1,]
min_players = 5
tot_rsrc = 1
rsrc_list = ['WOOD','ORE']
card = BrownResource(name, cost_req,  age, min_players, tot_rsrc, rsrc_list)
age_1_cards += [card,]
###
name = "LUMBER YARD"
cost_req = []
min_players = 3
tot_rsrc = 1
rsrc_list = ['WOOD']
card = BrownResource(name, cost_req,  age, min_players, tot_rsrc, rsrc_list)
age_1_cards += [card,]
min_players = 4
card = BrownResource(name, cost_req,  age, min_players, tot_rsrc, rsrc_list)
age_1_cards += [card,]
###
name = "MINE"
cost_req = [1,]
min_players = 6
tot_rsrc = 1
rsrc_list = ['STONE','ORE']
card = BrownResource(name, cost_req,  age, min_players, tot_rsrc, rsrc_list)
age_1_cards += [card,]
###
name = "ORE VEIN"
cost_req = []
min_players = 3
tot_rsrc = 1
rsrc_list = ['ORE']
card = BrownResource(name, cost_req,  age, min_players, tot_rsrc, rsrc_list)
age_1_cards += [card,]
min_players = 4
card = BrownResource(name, cost_req,  age, min_players, tot_rsrc, rsrc_list)
age_1_cards += [card,]
###
name = "STONE PIT"
cost_req = []
min_players = 3
tot_rsrc = 1
rsrc_list = ['STONE']
card = BrownResource(name, cost_req,  age, min_players, tot_rsrc, rsrc_list)
age_1_cards += [card,]
min_players = 5
card = BrownResource(name, cost_req,  age, min_players, tot_rsrc, rsrc_list)
age_1_cards += [card,]
###
name = "TIMBER YARD"
cost_req = [1,]
min_players = 3
tot_rsrc = 1
rsrc_list = ['STONE','WOOD']
card = BrownResource(name, cost_req,  age, min_players, tot_rsrc, rsrc_list)
age_1_cards += [card,]
###
name = "TREE FARM"
cost_req = [1,]
min_players = 6
tot_rsrc = 1
rsrc_list = ['WOOD','BRICK']
card = BrownResource(name, cost_req,  age, min_players, tot_rsrc, rsrc_list)
age_1_cards += [card,]


#Gray cards:
name = "GLASSWORKS"
min_players = 3
card = GrayResource(name, age, min_players)
age_1_cards += [card,]
min_players = 6
card = GrayResource(name, age, min_players)
age_1_cards += [card,]
###
name = "LOOM"
min_players = 3
card = GrayResource(name, age, min_players)
age_1_cards += [card,]
min_players = 6
card = GrayResource(name, age, min_players)
age_1_cards += [card,]
###
name = "PRESS"
min_players = 3
card = GrayResource(name, age, min_players)
age_1_cards += [card,]
min_players = 6
card = GrayResource(name, age, min_players)
age_1_cards += [card,]

#Green cards:
name = "APOTHECARY"
cost_req = []
tech_tree['next'] = ["STABLES","DISPENSARY"]
min_players = 3
science_type = "COMPASS"
card = YellowCard(name, cost_req, tech_tree, age, min_players, \
		science_type)
age_1_cards += [card,]
min_players = 5
card = YellowCard(name, cost_req, tech_tree, age, min_players, \
		science_type)
age_1_cards += [card,]
###
name = "SCRIPTORIUM"
cost_req = []
tech_tree['next'] = ["COURTHOUSE","LIBRARY"]
min_players = 3
science_type = "TABLET"
card = YellowCard(name, cost_req, tech_tree, age, min_players, \
		science_type)
age_1_cards += [card,]
min_players = 4
card = YellowCard(name, cost_req, tech_tree, age, min_players, \
		science_type)
age_1_cards += [card,]
###
name = "WORKSHOP"
cost_req = []
tech_tree['next'] = ["LABORATORY","ARCHERY RANGE"]
min_players = 3
science_type = "WHEEL"
card = YellowCard(name, cost_req, tech_tree, age, min_players, \
		science_type)
age_1_cards += [card,]
min_players = 7
card = YellowCard(name, cost_req, tech_tree, age, min_players, \
		science_type)
age_1_cards += [card,]

#Red cards:
name = "BARRACKS"
cost_req = ["ORE",]
tech_tree['next'] = []
min_players = 3
card = RedCard(name, cost_req, tech_tree, age, min_players)
age_1_cards += [card,]
min_players = 5
card = RedCard(name, cost_req, tech_tree, age, min_players)
age_1_cards += [card,]
###
name = "GUARD TOWER"
cost_req = ["BRICK",]
tech_tree['next'] = []
min_players = 3
card = RedCard(name, cost_req, tech_tree, age, min_players)
age_1_cards += [card,]
min_players = 4
card = RedCard(name, cost_req, tech_tree, age, min_players)
age_1_cards += [card,]
###
name = "STOCKADE"
cost_req = ["WOOD",]
tech_tree['next'] = []
min_players = 3
card = RedCard(name, cost_req, tech_tree, age, min_players)
age_1_cards += [card,]
min_players = 7
card = RedCard(name, cost_req, tech_tree, age, min_players)
age_1_cards += [card,]

#Yellow cards:
name = "MARKETPLACE"
cost_req = []
tech_tree['next'] = ["CARAVANSERY",]
min_players = 3
descrip = "Allows you to buy gray resources from either of your "
descrip += "two neighbors for 1 coin instead of 2"
card = YellowCard(name, cost_req, tech_tree, age, min_players,\
		descrip)
age_1_cards += [card,]
min_players = 6
card = YellowCard(name, cost_req, tech_tree, age, min_players,\
		descrip)
age_1_cards += [card,]
####
name = "TAVERN"
cost_req = []
tech_tree['next'] = []
min_players = 4
descrip = "Gives 5 gold instantly."
card = YellowCard(name, cost_req, tech_tree, age, min_players,\
		descrip)
age_1_cards += [card,]
min_players = 5
card = YellowCard(name, cost_req, tech_tree, age, min_players,\
		descrip)
age_1_cards += [card,]
min_players = 7
card = YellowCard(name, cost_req, tech_tree, age, min_players,\
		descrip)
age_1_cards += [card,]
###
name = "EAST TRADING POST"
cost_req = []
tech_tree['next'] = ["FORUM",]
min_players = 3
descrip = "Allows you to buy brown resources from your "
descrip += "right neighbor for 1 coin instead of 2"
card = YellowCard(name, cost_req, tech_tree, age, min_players,\
		descrip)
age_1_cards += [card,]
min_players = 7
card = YellowCard(name, cost_req, tech_tree, age, min_players,\
		descrip)
age_1_cards += [card,]
###
name = "WEST TRADING POST"
cost_req = []
tech_tree['next'] = ["FORUM",]
min_players = 3
descrip = "Allows you to buy brown resources from your "
descrip += "left neighbor for 1 coin instead of 2"
card = YellowCard(name, cost_req, tech_tree, age, min_players,\
		descrip)
age_1_cards += [card,]
min_players = 7
card = YellowCard(name, cost_req, tech_tree, age, min_players,\
		descrip)
age_1_cards += [card,]
###

###############################################################
###############################################################
###############################################################
###############################################################
###############################################################
###############################################################
###############################################################

age_2_cards = []
age = 2
tech_tree = {}

###############################################################
###############################################################
###############################################################
###############################################################
###############################################################

age_3_cards = []
age = 3
tech_tree = {}

###############################################################
###############################################################
###############################################################
###############################################################
###############################################################

#Test:
histogram = [0 for i in range(8)]
for card in age_1_cards:
	histogram[card.min_players] += 1
	print card
print histogram
assert( histogram[3] == 21 )
for i in range(4,8):
	assert(histogram[i]==7)
print "There are " + str(len(age_1_cards)) +" cards"


