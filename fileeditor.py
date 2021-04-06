def write(file, text):
	with open(file, 'w') as f:
		f.write(text)


def append(file, text):
	with open(file, 'a') as f:
		f.write(text)
