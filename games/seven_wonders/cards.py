
class Card(object):
	"""Represents a card in the 7 wonders game.  Each type of card (resource, 
	   military, etc.) will inherit from this class.

	Attributes:
		name: string representing the card name (all caps)
		brwn_rsrc_req: list of brown resources required (empty if free)
		gry_rsrc_req: list of gray resources required (empty if free)
		coins_req: integer representing the # of coins required
		tech_tree['prev']: list of cards that make this card free
		tech_tree['next']: list of cards that this card makes free
		age: 1,2, or 3
		min_players: 3,4,5,6, or 7
		color: string representing the color of the card (all lowercase)
		descrip: string describing what the card does
	"""
	gry_rsrc_list = ['LOOM','GLASSWORKS','PRESS']
	brwn_rsrc_list = ['WOOD','ORE','BRICK','STONE']

	def __init__(self, name, cost_req, tech_tree, age, min_players, descrip, 
					color=None):
		"""cost_req is a list of costs required.  If there is a coin cost,
			enter an integer as one of the list items."""

		self.name = name
		assert( type(name) is str )
		self.tech_tree = tech_tree
		assert( type(tech_tree) is dict )
		assert( 'prev' in tech_tree.keys() )
		assert( 'next' in tech_tree.keys() )
		self.age = age
		assert( age in [1,2,3] )
		self.min_players = min_players
		assert( min_players in [3,4,5,6,7] )
		self.descrip = descrip
		assert( type(descrip) is str )
			
		#Color should be assigned by the classes inheriting this one
		self.color = color

		self.brwn_rsrc_req = []
		self.gry_rsrc_req = []
		self.coins_req = 0
	
		if cost_req == None:
			return
		for cost in cost_req:
			if type(cost) is int:
				self.coins_req = cost
				continue

			assert( type(cost) is str )
			if cost in self.gry_rsrc_list:
				gry_rsrc_req += cost
			elif cost in self.brwn_rsrc_list:
				brwn_rsrc_req += cost

	def __str__(self):
		out_str = "Card name: " + self.name
		out_str += "\n Color: " + self.color
		out_str += "\n Description: " + self.descrip
		return out_str

	def instant_effect(self, curr_player, left_neighbor, right_neighbor):
		""" Alters the status (e.g., how much gold they have) of a player
			 based on the cards he and his neighbor owns.
		"""
		#Default is to subtract coin cost of card
		if curr_player.coins > 0:
			print "ERROR: THIS CARD CANNOT BE PLAYED BECAUSE THE PLAYER HAS"\
				+"NOT ENOUGH GOLD"
		curr_player.coins -= self.coins_req
		return

	def get_victory_points( self, curr_player, left_neighbor, right_neighbor):
		""" Returns the number of victory points granted by this card.  Takes
			 into account the possessions of the player and his neighbors.
		"""
		#Default is 0 victory points
		return 0

class ResourceCard(Card):
	"""Represents a brown or gray resource card.

	Attributes:
		tot_rsrc: total number of resources in this card
			If a card is a / card, then tot_rsrc = 1
			If a card just has a single rsrc, tot_rsrc = 1
			If a card has 2 resources, then tot_rsrc = 2
		curr_rsrc: dictionary with three entries: 'left','owner','right'
			Each entry lists the number of resources still available
			for use by the respective player.  For example, if
			curr_rsrc['owner'] = 0, then the owner cannot use this card anymore
			this turn.  All three entries reset to tot_rsrc at the beginning
			of a turn
		has_rsrc: dictionary with brwn_rsrc_list and/or gry_rsrc_list
			as the keys.  Each entry is a boolean.

		For example, a "2 stone" resource card would look the same as a
		"1 stone" resource card, except that tot_rsrc = 2 instead of 1

		A "stone/brick" resource card would have "True" under has_rsrc['STONE']
		and has_rsrc['BRICK'], but tot_rsrc=1

		A "stone" resource card would have "True under just has_rsrc['STONE']
		and have tot_rsrc=1
	"""
	
	def __init__(self, name, cost_req, tech_tree, age, min_players, tot_rsrc,\
			descrip, color=None):
		Card.__init__(self, name, cost_req, tech_tree, age, min_players, \
			descrip, color)
		self.tot_rsrc = tot_rsrc
		assert( type(tot_rsrc) is int )
		assert( tot_rsrc > 0 )
		assert( tot_rsrc < 3 )
		assert( age < 3 )

		self.curr_rsrc = {}
		for player in ['left','curr','right']:
			self.curr_rsrc[player] = tot_rsrc
		self.has_rsrc = {}

class BrownResource(ResourceCard):
	"""Represents a brown resource card.
	"""
	def __init__(self, name, cost_req, tech_tree, age, min_players, \
					tot_rsrc, rsrc_list):
		""" rsrc_list is a list of rsrcs provided by the card """

		assert( len(rsrc_list) > 0)
		descrip = "Provides "+str(tot_rsrc)+" "
		if len(rsrc_list) > 1:
			descrip += " of the following: "
			for rsrc in rsrc_list[:-1]:
				descrip += rsrc + ", "
			descrip += rsrc_list[-1]+"."
		else:
			descrip += rsrc_list[0]+"."
		ResourceCard.__init__(self, name, cost_req, tech_tree, age, \
			min_players, tot_rsrc, descrip, color="brown")
		
		for rsrc in rsrc_list:
			assert( rsrc in self.brwn_rsrc_list )

		for rsrc in self.brwn_rsrc_list:
			if rsrc in rsrc_list:
				self.has_rsrc[rsrc] = True
			else:
				self.has_rsrc[rsrc] = False 

class GrayResource(ResourceCard):
	"""Represents a gray resource card.

	"""
	def __init__(self, name, cost_req, tech_tree, age, min_players, rsrc_list):
		""" rsrc_list is a list of rsrcs provided by the card """

		assert( len(rsrc_list) == 1 )
		descrip = "Provides 1 " + rsrc_list[0] +'.'
		ResourceCard.__init__(self, name, cost_req, tech_tree, age, \
			min_players, 1, descrip, color="gray")
		
		for rsrc in rsrc_list:
			assert( rsrc in self.gry_rsrc_list )

		for rsrc in self.gry_rsrc_list:
			if rsrc in rsrc_list:
				self.has_rsrc[rsrc] = True
			else:
				self.has_rsrc[rsrc] = False 

class YellowCard(Card):
	"""Represents a yellow card that does NOT provide resources.

		There are many types of yellow cards, and many classes must be written
		for each of them.
	"""

	def __init__(self, name, cost_req, tech_tree, age, min_players, descrip):
		Card.__init__(self, name, cost_req, tech_tree, age, min_players, \
			descrip, color="yellow")

	def instant_effect(self, curr_player, left_neighbor, right_neighbor):
		players = [curr_player, left_neighbor, right_neighbor]
		if self.name == "TAVERN":
			curr_player.gold += 5
		elif self.name == "VINEYARD":
			for player in players:
				curr_player.gold += player.get_num_color("brown")
		elif self.name == "BAZAR":
			for player in players:
				curr_player.gold += 2*player.get_num_color("gray")
		elif self.name == "HAVEN":
			curr_player.gold += curr_player.get_num_color("brown")
		elif self.name == "LIGHTHOUSE":
			#MAKE SURE THIS DOESN'T COUNT ITSELF TWICE!
			#MAKE SURE IT COUNTS ITSELF ONCE!
			curr_player.gold += curr_player.get_num_color("yellow")
		elif self.name == "CHAMBER OF COMMERCE":
			curr_player.gold += 2*curr_player.get_num_color("gray")
		elif self.name == "ARENA":
			curr_player.gold += 3*curr_player.get_wonders_built()

	def get_victory_points(self, curr_player, left_neighbor, right_neighbor):
		if self.name == "HAVEN":
			return curr_player.get_num_color("brown")
		elif self.name == "LIGHTHOUSE":
			#MAKE SURE THIS COUNTS ITSELF!
			return curr_player.get_num_color("yellow")
		elif self.name == "CHAMBER OF COMMERCE":
			return 2*curr_player.get_num_color("gray")
		elif self.name == "ARENA":
			return curr_player.get_wonders_built()
		return 0

class YellowResource(ResourceCard):
	"""A yellow card that provides resources.  This must be a FORUM or 
		CARAVANSERY"

	"""
	def __init__(self, name, min_players):
		""" rsrc_list is a list of rsrcs provided by the card """

		cost_req = ['WOOD','WOOD']
		descrip = "Provides 1 of: "
		tech_tree = {}

		if name == "FORUM":
			cost_req = ['BRICK','BRICK']

			tech_tree['prev'] = ['WEST TRADING POST','EAST TRADING POST']
			tech_tree['next'] = ['HAVEN',]

			for rsrc in self.gry_rsrc_list[:-1]:
				descrip += rsrc + ", "
			descrip += self.gry_rsrc_list[-1] +"."

		else:
			assert( name == "CARAVANSERY" )

			tech_tree['prev'] = ['MARKETPLACE',]
			tech_tree['next'] = ['LIGHTHOUSE',]

			for rsrc in self.brwn_rsrc_list[:-1]:
				descrip += rsrc + ", "
			descrip += self.brwn_rsrc_list[-1] +"."

		ResourceCard.__init__(self, name=name,\
									cost_req=cost_req,\
									tech_tree=tech_tree,\
									age=2,\
									min_players=min_players,\
									tot_rsrc=1,\
									descrip=descrip,\
									color="yellow")

		if name == "FORUM":
			for rsrc in self.gry_rsrc_list:
				self.has_rsrc[rsrc] = True
		elif name == "CARAVANSERY":
			for rsrc in self.brwn_rsrc_list:
				self.has_rsrc[rsrc] = True

class RedCard(Card):
	""" Represents a military card.  
		Note that military power is equal to age number.
	"""

	def __init__(self, name, cost_req, tech_tree, age, min_players):
		descrip = "Provides "+str(age)+" military power."
		Card.__init__(self, name, cost_req, tech_tree, age, min_players, \
			descrip, color="red")

class GreenCard(Card):
	""" Represents a science card.

		Attributes:
		 science_type = "TABLET", "COMPASS", or "WHEEL"
	"""

	def __init__(self, name, cost_req, tech_tree, age, min_players, sci_type):
		assert( sci_type in ["TABLET","COMPASS","WHEEL"])
		descrip = "Provides a " + sci_type
		Card.__init__(self, name, cost_req, tech_tree, age, min_players, \
			descrip, color="green")

class BlueCard(Card):
	""" Represents a blue card.

		Attributes:
		victory_points = victory points provided
	"""

	def __init__(self, name, cost_req, tech_tree, age, min_players,\
			 victory_points):
		assert( type(self.victory_points) is int)
		descrip = "Provides " + str(victory_points) + " victory points."
		Card.__init__(self, name, cost_req, tech_tree, age, min_players, \
			descrip, color="blue")

		self.victory_points = victory_points

	def get_victory_points(self, curr_player, left_neighbor, right_neighbor):
		return self.victory_points

class PurpleCard(Card):
	""" Represents a purple card.
	"""

	def __init__(self, name, cost_req, tech_tree, age, min_players, descrip):
		assert(name[-6:] == " GUILD")
		Card.__init__(self, name, cost_req, tech_tree, age, min_players, \
			descrip, color="purple")

	def get_victory_points(self, curr_player, left_neighbor, right_neighbor):
		guild_title = self.name[:-6]
		players = [curr_player, left_neighbor, right_neighbor]
		neighbors = [left_neighbor, right_neighbor]

		if guild_title == "BUILDERS":
			vic_pts = 0
			for player in players:
				vic_pts += player.get_wonders_built()
			return vic_pts
		elif guild_title == "CRAFTMENS":
			vic_pts = 0
			for neighbor in neighbors:
				vic_pts += 2*neighbor.get_num_color("gray")
			return vic_pts
		elif guild_title == "MAGISTRATES":
			vic_pts = 0
			for neighbor in neighbors:
				vic_pts += neighbor.get_num_color("blue")
			return vic_pts
		elif guild_title == "PHILOSOPHERS":
			vic_pts = 0
			for neighbor in neighbors:
				vic_pts += neighbor.get_num_color("green")
			return vic_pts
		elif guild_title == "SHIPOWNERS":
			vic_pts = 0
			for color in ["brown","gray","purple"]:
				vic_pts += curr_player.get_num_color(color)
			return vic_pts
		elif guild_title == "SPIES":
			vic_pts = 0
			for neighbor in neighbors:
				vic_pts += neighbor.get_num_color("red")
			return vic_pts
		elif guild_title == "STRATEGISTS":
			vic_pts = 0
			for neighbor in neighbors:
				vic_pts += neighbor.get_num_military_losses()
			return vic_pts
		elif guild_title == "TRADERS":
			vic_pts = 0
			for neighbor in neighbors:
				vic_pts += neighbor.get_num_color("yellow")
			return vic_pts
		elif guild_title == "WORKERS":
			vic_pts = 0
			for neighbor in neighbors:
				vic_pts += neighbor.get_num_color("brown")
			return vic_pts
		return 0

#Test:
tech_tree = {}
tech_tree['prev'] = []
tech_tree['next'] = []
ore_card = BrownResource("ORE",[],tech_tree,1,3,1,['ORE'])
print ore_card
