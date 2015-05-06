#!/usr/bin/env python3
# Daily Programmer #213, easy edition: Pronouncing Hex
# http://redd.it/34rxkc

# NOTE: There are two minor differences in this module vs. the description in
# the challenge. The first is the spelling 'bytey'. The second is that 'bytey'
# is treated much like 'thousand' is in decimal. It is always separated by
# spaces. This is entirely intentional, as I believe it is the correct way to
# write the number. The tests have been adjusted to reflect these changes.


class Hex(int):
	"""A hexadecimal number.

	Works just like an integer, but outputs a pronounceable hexadecimal number
	when converted to a string.

	Tests based on the original challenge:
	>>> str(Hex('0xF5'))
	'fleventy-five'
	>>> str(Hex('0xB3'))
	'bibbity-three'
	>>> str(Hex('0xE4'))
	'ebbity-four'
	>>> str(Hex('0xBBBB'))
	'bibbity-bee bytey bibbity-bee'
	>>> str(Hex('0xA0C9'))
	'atta bytey city-nine'
	>>> str(Hex('0xdeadbeef'))
	'dickety-ee bytey atta-dee bytey bibbity-ee bytey ebbity-eff'
	"""

	def __new__(cls, value, base=16):
		if isinstance(value, str):
			value = int(value, base)
		return super().__new__(cls, value)

	TENS_WORDS = ['', 'teen', 'twenty', 'thirty', 'forty', 'fifty', 'sixty',
	              'seventy', 'eighty', 'ninety', 'atta', 'bibbity', 'city',
	              'dickety', 'ebbity', 'fleventy']

	DIGITS_WORDS = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
	                'eight', 'nine', 'ay', 'bee', 'see', 'dee', 'ee', 'eff']

	SPECIAL_CASES = {
		0: 'zero',
		16: 'ten',
		17: 'eleven',
		18: 'twelve',
		19: 'thirteen',
		21: 'fifteen',
	}

	def __str__(self):
		if self >= 256:
			value = self
			bytes = 0
			if value % 256 == 0:
				while value % 256 == 0:
					bytes += 1
					value = value // 256
				return self._pronounceable_byte(value) + ' bytey' * bytes
			return '%s bytey %s' % (
				Hex(self // 256).__str__(),
				self._pronounceable_byte(Hex(self % 256)))
		return self._pronounceable_byte(int(self))

	def __getitem__(self, key):
		return self

	@classmethod
	def _pronounceable_byte(cls, value):
		if value in cls.SPECIAL_CASES:
			return cls.SPECIAL_CASES[value]
		if value < 16:
			return cls.DIGITS_WORDS[value]
		tens = value // 16
		units = value % 16
		if tens == 1:
			return '%s%s' % (cls.DIGITS_WORDS[units],
			                 cls.TENS_WORDS[tens])
		if units == 0:
			return cls.TENS_WORDS[tens]
		return '%s-%s' % (cls.TENS_WORDS[tens],
		                  cls.DIGITS_WORDS[units])


if __name__ == '__main__':
	import doctest
	doctest.testmod()
