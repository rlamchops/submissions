string = 'string = &&&\ncode = string.split("&&&")[0] + "\'" + string.encode(\'string_escape\') + "\'" + string.split("&&&")[1]\nfor i in range(2, 6):\n\tcode += ("&&&" + string.split("&&&")[i])\nprint code\n'
code = string.split("&&&")[0] + "'" + string.encode('string_escape') + "'" + string.split("&&&")[1]
for i in range(2, 6):
	code += ("&&&" + string.split("&&&")[i])
print code
