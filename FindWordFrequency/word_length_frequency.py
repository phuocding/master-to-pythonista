import sys

puctuation_removal = [".", ",", "'", "!", "%", "$", "@", "#", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "}", "[", "]", "|", ";", ":", "<", ">", "?"]

def remove_punction(text_list):
	"""
		This Function removes any puctuation from provided text
		Punctuations, listed in puctuation_removal, will be removed
	"""
	for i in range(len(text_list)):
		for punc in puctuation_removal:
			text_list[i] = text_list[i].replace(punc, "")
	print(text_list)
	return text_list

def split_space_text(text_list):
	"""
		This Function splits text to words
	"""
	temp_text_list = []
	for i in range(len(text_list)):
		if " " in text_list[i]:
			temp_text_list.extend(text_list[i].split())
			text_list[i] = ""
			print(temp_text_list)
			print(text_list)
	text_list.extend(temp_text_list)
	return(text_list)

def find_word_length_frequency(text_list):
	"""
		This function calculates the frequency of
		word length
	"""
	text_list = split_space_text(text_list)
	text_length_list = [len(txt) for txt in remove_punction(text_list) if len(txt) > 0]
	freq_dict = {}
	unique_length_set = set(text_length_list)
	for i in unique_length_set:
		freq_dict[i] = text_length_list.count(i)
	return(freq_dict)

if __name__ == '__main__':

	if len(sys.argv) < 2:
		print("Please specify a text")
	else:
		freq_dict = find_word_length_frequency(sys.argv[1:])
		print(freq_dict)
