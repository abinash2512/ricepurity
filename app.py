import constants

QUESTIONS = constants.QUESTIONS
# sum of weights of questions answered 'no'
points = 0
# sum of weights of all questions
maximum = 0

print('Welcome to rice purity 2.0. Answer y for yes and n for no.')
for question, weight in QUESTIONS.iteritems():
	response = ''
	# ask until a valid response is given
	print(question)
	# rip do-while loops :(
	response = raw_input()
	while not response.lower() in ['y', 'n']:
		print('Please respond either "y" or "n"')
		response = raw_input()
	# if 'n', purity increases
	if response.lower() == 'n':
		points += weight
	# maximumimum increases no matter what
	maximum += weight

score = int(points * 100 / maximum)
print('\n\n')
if (score >= 60):
	letter = ['a D', 'a C', 'a B', 'an A'][int(score / 10) - 6];
	if (score % 10 >= 7):
		letter += '+'
	elif (score % 10 <= 3):
		letter += '-'
else:
	letter = 'an F'

print('Your final score is ' + letter + ' (' + str(score) + ').')
