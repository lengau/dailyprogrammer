#!/usr/bin/env python3
# Daily Programmer #213, intermediate edition: The Lazy Typist
# http://redd.it/351b0o


# Keyboards. The Pilcrow sign (¶) is used to indicate non-typing locations.
# The Not sign (¬) is used to indicate the shift symbol.
QWERTY_KEYBOARD = (
	(  # Upper case (with shift)
		'~!@#$%^&*()_+',
		'¶QWERTYUIOP{}',
		'¶ASDFGHJKL:"¶',
		'¬ZXCVBNM<>?¬¬',
		'¶¶¶¶¶¶¶¶¶¶¶¶¶',
	),(  # Lower case (no shift)
		'`1234567890-=',
		'¶qwertyuiop[]',
		"¶asdfghjkl;'\n",
		'¬zxcvbnm,./¬¬',
		'¶¶¶      ¶¶¶¶',
	)
)

DVORAK_KEYBOARD = (
	(  # Upper case (with shift)
		'~!@#$%^&*(){}',
		'¶"<>PYFGCRL?+',
		'¶AOEUIDHTNS_¶',
		'¬:QJKXBMWVZ¬¶',
		'¶¶¶¶¶¶¶¶¶¶¶¶¶',
	),(  # Lower case (no shift)
		'`1234567890[]',
		"¶',.pyfgcrl/=",
		'¶aoeuidhtns-\n',
		'¬;qjkxbmwvz¬¬',
		'¶¶¶      ¶¶¶¶',
	)
)
CASE = 0
ROW = 1
COLUMN = 2

class KeyboardStructureError(ValueError):
	"""Invalid structure of a keyboard."""


class KeyboardString(str):
	"""A Keyboard sttring.

	Like a regular string, but with a type() method that will describe how to
	type the contents of the string using a two-finger hunt and peck method.

	Examples:
	>>> KeyboardString('The quick brown fox').type()
	Space: Use left hand
	T: Use right hand
	H: Move right hand from T (effort: 1)
	E: Move left hand from T (effort: 5)
	Space: Move left hand from E (effort: 2)
	Q: Move left hand from Space (effort: 2)
	U: Move left hand from Q (effort: 3)
	I: Move left hand from U (effort: 1)
	C: Move right hand from H (effort: 2)
	K: Move left hand from I (effort: 2)
	Space: Move left hand from K (effort: 1)
	B: Move left hand from Space (effort: 3)
	R: Move right hand from C (effort: 1)
	O: Move left hand from B (effort: 5)
	W: Move right hand from R (effort: 3)
	N: Move right hand from W (effort: 2)
	Space: Move left hand from O (effort: 3)
	F: Move left hand from Space (effort: 6)
	O: Move left hand from F (effort: 5)
	X: Move left hand from O (effort: 4)
	Total effort: 51
	>>> KeyboardString('hello world').type()
	H: Use right hand
	E: Use left hand
	L: Move right hand from H (effort: 4)
	L: Use right hand again
	O: Move left hand from E (effort: 1)
	Space: Move left hand from O (effort: 3)
	W: Move right hand from L (effort: 4)
	O: Move left hand from Space (effort: 3)
	R: Move right hand from W (effort: 3)
	L: Move right hand from R (effort: 1)
	D: Move left hand from O (effort: 4)
	Total effort: 23
	>>> KeyboardString('Hello there DailyProgrammers').type()
	Space: Use left hand
	H: Use right hand
	E: Move left hand from H (effort: 4)
	L: Move right hand from H (effort: 4)
	L: Use right hand again
	O: Move left hand from E (effort: 1)
	Space: Move left hand from O (effort: 3)
	T: Move right hand from L (effort: 3)
	H: Move right hand from T (effort: 1)
	E: Move left hand from Space (effort: 2)
	R: Move right hand from H (effort: 3)
	E: Use left hand again
	Space: Move left hand from E (effort: 2)
	Space: Move right hand from R (effort: 4)
	D: Move left hand from Space (effort: 5)
	A: Move left hand from D (effort: 5)
	I: Move left hand from A (effort: 4)
	L: Move right hand from D (effort: 5)
	Y: Move left hand from I (effort: 1)
	Space: Move right hand from L (effort: 5)
	P: Move left hand from Y (effort: 1)
	R: Move right hand from P (effort: 5)
	O: Move left hand from P (effort: 3)
	G: Move right hand from R (effort: 2)
	R: Move right hand from G (effort: 2)
	A: Move left hand from O (effort: 1)
	M: Move right hand from R (effort: 4)
	M: Use right hand again
	E: Move left hand from A (effort: 2)
	R: Move right hand from M (effort: 4)
	S: Move right hand from R (effort: 2)
	Total effort: 69
	>>> KeyboardString('qpalzm woskxn').type()
	Q: Use left hand
	P: Move left hand from Q (effort: 4)
	A: Move left hand from P (effort: 4)
	L: Use right hand
	Z: Move right hand from L (effort: 2)
	M: Move right hand from Z (effort: 3)
	Space: Move right hand from M (effort: 1)
	W: Move right hand from Space (effort: 2)
	O: Move left hand from A (effort: 1)
	S: Move right hand from W (effort: 3)
	K: Move left hand from O (effort: 3)
	X: Move left hand from K (effort: 1)
	N: Move right hand from S (effort: 1)
	Total effort: 25
	>>> KeyboardString('QPgizm QFpRKbi Qycn').type()
	Space: Use right hand
	Q: Use left hand
	Space: Move right hand from Q (effort: 2)
	P: Move left hand from Q (effort: 4)
	G: Move right hand from P (effort: 3)
	I: Move left hand from P (effort: 2)
	Z: Move right hand from G (effort: 5)
	M: Move right hand from Z (effort: 3)
	Space: Move right hand from M (effort: 1)
	Space: Use right hand again
	Q: Move left hand from I (effort: 4)
	Space: Move right hand from Q (effort: 2)
	F: Move left hand from Q (effort: 6)
	P: Move left hand from F (effort: 2)
	Space: Move left hand from P (effort: 3)
	R: Move right hand from F (effort: 3)
	Space: Move right hand from R (effort: 4)
	K: Move left hand from R (effort: 7)
	B: Move left hand from K (effort: 2)
	I: Move left hand from B (effort: 2)
	Space: Move right hand from K (effort: 1)
	Space: Use right hand again
	Q: Move left hand from I (effort: 4)
	Y: Move left hand from Q (effort: 5)
	C: Move right hand from Q (effort: 8)
	N: Move right hand from C (effort: 2)
	Total effort: 64
	"""

	@property
	def keyboard_layout(self):
		try:
			return self.__keyboard_layout
		except AttributeError:
			self.__keyboard_layout = DVORAK_KEYBOARD
			return self.__keyboard_layout

	@keyboard_layout.setter
	def keyboard_layout(self, layout):
		if len(layout) != 2:
			raise KeyboardStructureError(
				'Include an upper case and a lower case.')
		self.__keyboard_layout = layout
		self.generate_reverse_model()

	def generate_reverse_model(self):
		self.__reverse_model = dict()
		for i,case in enumerate(self.keyboard_layout):
			for j,row in enumerate(case):
				for k,key in enumerate(row):
					if key not in self.__reverse_model:
						self.__reverse_model[key] = []
					self.__reverse_model[key].append([i,j,k])

	def minimum_distance(self, hand_location, key_locations):
		if hand_location is None:
			return 0, key_locations[0][1:]
		shortest = None
		for location in key_locations:
			manhattan_distance = (abs(hand_location[0] - location[ROW]) +
			                      abs(hand_location[1] - location[COLUMN]))
			if shortest is None or manhattan_distance < shortest[0]:
				shortest = [manhattan_distance, location[1:]]
		return shortest[0], shortest[1]

	NAMED_CHARACTERS = {
		' ': 'Space',
		'¬': 'Shift',
		'\n': 'Return',
	}

	@classmethod
	def _character_name(cls, character):
		"""Returns the name of the given character."""
		if character in cls.NAMED_CHARACTERS:
			return cls.NAMED_CHARACTERS[character]
		return character.upper()


	def type(self):
		# Hand locations
		left_hand = None
		right_hand = None
		total_effort = 0
		try:
			self.__reverse_model
		except AttributeError:
			self.generate_reverse_model()
		for character in self:
			try:
				locations = self.__reverse_model[character]
			except KeyError:
				raise ValueError('Character %s not on keyboard.' % character)
			use_left = False
			use_right = False
			for location in locations:
				if location[COLUMN] < 7:
					use_left = True
				else:
					use_right = True
			if use_left and use_right:
				left_instruction = self.minimum_distance(left_hand, locations)
				right_instruction = self.minimum_distance(right_hand, locations)
				if left_instruction[0] <= right_instruction[0]:
					effort, destination = left_instruction
					hand = 'left'
					hand_location = left_hand
				else:
					effort, destination = right_instruction
					hand = 'right'
					hand_location = right_hand
			elif use_left:
				effort, destination = self.minimum_distance(left_hand, locations)
				hand = 'left'
				hand_location = left_hand
			elif use_right:
				effort, destination = self.minimum_distance(right_hand, locations)
				hand = 'right'
				hand_location = right_hand
			else:
				raise KeyboardStructureError('Cannot find correct hand for %s' %
				                             character)
			if locations[0][0] == 0:  # If character is upper case
				if hand == 'left':
					shift_effort, shift_dest = self.minimum_distance(
						right_hand, self.__reverse_model[' '])
					self._print_instruction('right', right_hand, shift_effort,
							                ' ')
					right_hand = destination
				else:
					shift_effort, shift_dest = self.minimum_distance(
						left_hand, self.__reverse_model[' '])
					self._print_instruction('left', left_hand, shift_effort,
							                ' ')
					left_hand = destination

			self._print_instruction(hand, hand_location, effort,
			                        character)
			if hand == 'left':
				left_hand = destination
			else:
				right_hand = destination
			total_effort += effort
		print('Total effort:', total_effort)

	def _print_instruction(self, hand, old_loc, effort, character):
		"""Print the instruction passed in."""
		#print('Old location:', old_loc)
		character = self._character_name(character)
		if old_loc is None:
			print('%s: Use' % character, hand, 'hand')
			return
		if effort == 0:
			print('%s: Use' % character, hand, 'hand again')
			return
		last_character = self.__keyboard_layout[1][old_loc[0]][old_loc[1]]
		print('%s: Move' % character, hand, 'hand from',
		      self._character_name(last_character), '(effort: %d)' % effort)

if __name__ == '__main__':
	import doctest
	doctest.testmod()
