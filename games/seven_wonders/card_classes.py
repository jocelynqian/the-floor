
def Card(Object):
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
	"""
	gry_rsrc_list = ['LOOM','GLASSWORKS','PRESS']
	brwn_rsrc_list = ['WOOD','ORE','BRICK','STONE']

	def __init__(self, name, cost_req, tech_tree, age, min_players, color=None):
		"""cost_req is a list of costs required.  If there is a coin cost,
			enter an integer as one of the list items."""

		self.name = name
		assert( type(name) is str )
		self.tech_tree = tech_tree
		assert( type(tech_tree) is dict )
		assert( 'prev' in tech_tree.keys() )
		assert( 'next' in tech_tree.keys() )
		self.age = age
		assert( type(age) is int )
		self.min_players = min_players
		assert( type(min_players) is int )
			
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
			if cost in gry_rsrc_list:
				gry_rsrc_list += cost
			elif cost in brwn_rsrc_list:
				brwn_rsrc_list += cost

	def __str__(self):
		out_str = "Card name: " + self.name
		out_str += "\n Color: " + self.color
		return out_str

def ResourceCard(Card):
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
		has_rsrc: dictionary with either brwn_rsrc_list or gry_rsrc_list
			as the keys.  Each entry is a boolean.

		For example, a "2 stone" resource card would look the same as a
		"1 stone" resource card, except that tot_rsrc = 2 instead of 1

		A "stone/brick" resource card would have "True" under has_rsrc['STONE']
		and has_rsrc['BRICK'], but tot_rsrc=1

		A "stone" resource card would have "True under just has_rsrc['STONE']
		and have tot_rsrc=1
	"""
	
	def __init__(self, name, cost_req, tech_tree, age, min_players, tot_rsrc,\
			color=None):
		Card.__init__(self, name, cost_req, tech_tree, age, min_players, color)
		self.tot_rsrc = tot_rsrc
		assert( type(tot_rsrc) is int )
		assert( tot_rsrc > 0 )
		assert( tot_rsrc < 3 )
		assert( age < 3 )

		self.curr_rsrc = {}
		for player in ['left','owner','right']:
			self.curr_rsrc[player] = tot_rsrc
		self.has_rsrc = {}

def BrownResource(ResourceCard):
	"""Represents a brown resource card.
	"""
	def __init__(self, name, cost_req, tech_tree, age, min_players, \
					tot_rsrc, rsrc_list):
		""" rsrc_list is a list of rsrcs provided by the card """
		ResourceCard.__init__(self, name, cost_req, tech_tree, age, \
			min_players, "brown", tot_rsrc)
		
		for rsrc in rsrc_list:
			assert( rsrc in brwn_rsrc_list )

		for rsrc in brwn_rsrc_list:
			if rsrc in rsrc_list:
				has_rsrc[rsrc] = True
			else:
				has_rsrc[rsrc] = False 

def GrayResource(ResourceCard):
	"""Represents a gray resource card.
	"""
	def __init__(self, name, cost_req, tech_tree, age, min_players, rsrc_list):
		""" rsrc_list is a list of rsrcs provided by the card """
		ResourceCard.__init__(self, name, cost_req, tech_tree, age, \
			min_players, "gray", 1)
		
		for rsrc in rsrc_list:
			assert( rsrc in gry_rsrc_list )

		for rsrc in gry_rsrc_list:
			if rsrc in rsrc_list:
				has_rsrc[rsrc] = True
			else:
				has_rsrc[rsrc] = False 
