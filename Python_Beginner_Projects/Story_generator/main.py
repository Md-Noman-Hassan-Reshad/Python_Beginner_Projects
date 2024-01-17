import random
when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago','On 20th Jan']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle','a cat']
name = ['Ali', 'Miriam','daniel', 'Hoouk', 'Starwalker', 'Alex', 'Mike', 'Ben']
residence = ['Barcelona','India', 'Germany', 'Venice', 'England', 'jungle']
went = ['cinema', 'university','seminar', 'school', 'laundry', 'America']
happened = ['made a lot of friends','Eats a burger', 'found a secret key', 'solved a mistery', 'wrote a book', 'find omnitrix']

print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened) + '... this is described by ' + random.choice(name))