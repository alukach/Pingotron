f = open('/Users/anthony/Projects/Pingotron/scoreSheet.csv')
scores = f.readlines()

scorelist = []
for x in scores:
  game = []
  for y in x.split(','):
    game.append(y)
  scorelist.append(game)

names = {'js':'joseph', 'al':'anthony', 'rs':'ryan', 'dp':'don', 'go':'gino', 'jc':'jaime'}
for user in names.values():
    try:
        User.objects.get(username=user)
    except User.DoesNotExist:
        print "create user %s" % user
