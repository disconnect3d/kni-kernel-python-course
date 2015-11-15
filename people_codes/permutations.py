from random import shuffle

# non-recursive
def factorial(n):
	f = 1
	while n > 0:
		f = f * n
		n -= 1
	return f

# return list of permutations
# of the given *word*
def permutations(word):
	p = [] # list of permutations
	for x in range(factorial(len(word))):
		while word in p: word = shuffle_word(word)
		p.append(word)
	return p

def shuffle_word(word):
	word = list(word)
	shuffle(word) # returns NoneType, so (sadly) I can't ''.join(shuffle(word))
	word = ''.join(word)
	return word # also Strings are immutable, which sucks so much in this case
	# why is that? Why can't I do_whatever_i_want_with(string)?

S = permutations('KOT')
print(S)
#print(permutations("abc"))