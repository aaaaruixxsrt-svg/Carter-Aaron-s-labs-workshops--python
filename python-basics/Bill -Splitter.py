running_total = 0


num_of_friends = 4


appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21


running_total += appetizers + main_courses + desserts + drinks
print('Total bill so far:', running_total)


tip = running_total * 0.25
print('Tip amount:', tip)


running_total += tip
print('Total with tip:', running_total)


final_bill = running_total / num_of_friends
print('Bill per person:', final_bill)


each_pays=round(final_bill, 2)
print('Each person pays:',each_pays)



Report card printer


name = 'Carter'
print(name, type(name))


is_student = True
print(is_student, type(is_student))


age = 20
print(age, type(age))


score = 80.5
print(isinstance(score, float))
print(score,type(score))

