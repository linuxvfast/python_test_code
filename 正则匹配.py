# REGULAR EXPRESSIONS / PATTERN MATCHING
# Count the number of times a pattern appears in a string
string = "The quick brown fox jumps over the lazy dog."
string_list = string.split()
pattern = re.compile(r"The", re.I)  #匹配the，忽略大小写
count = 0
for word in string_list:
    if pattern.search(word):
    	count += 1
print("Output #38: {0:d}".format(count))




# Print the pattern each time it is found in the string
string = "The quick brown fox jumps over the lazy dog."
string_list = string.split()
pattern = re.compile(r"(?P<match_word>The)", re.I) #匹配字符The，并可以通过组名match_word调用
print("Output #39:")
for word in string_list:
    if pattern.search(word):
		print("{:s}".format(pattern.search(word).group('match_word')))
    
    
    

# Substitute the letter "a" for the word "the" in the string
string = "The quick brown fox jumps over the lazy dog."
string_to_find = r"The"
pattern = re.compile(string_to_find, re.I)
print("Output #40: {:s}".format(pattern.sub("a", string)))  #替换字符串中的字符
