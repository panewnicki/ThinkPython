import random

def sort_by_length(words):
	t = []
	for word in words:
		t.append((len(word), random.random(), word))
	t.sort(reverse=True)

	res = []
	for length, random_value, word in t:
		res.append(word)
	return res
