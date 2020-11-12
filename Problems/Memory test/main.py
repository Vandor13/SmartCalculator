numbers = input().split()
answers = input().split()
correct_set = set()
for number in numbers:
    correct_set.add(number)
answer_set = set()
for answer in answers:
    answer_set.add(answer)
print(correct_set == answer_set)
