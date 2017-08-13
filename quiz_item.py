def quiz_item(question, solution):
	iteration = 0
	answer = ""
	if solution.isdigit():
		while answer != solution and iteration != 3:
			answer = input(question + "= ")
			if answer != solution:
				print("'" + answer + "' is incorrect, please try again.")
			else:
				message = "'" + answer + "' is correct, great job."
			iteration += 1
	else:
		while answer != solution and iteration != 3:
			answer = input(question + ": ")
			if answer != solution:
				print("'" + answer + "' is incorrect, please try again.")
			else:
				message = "'" + answer + "' is correct, great job."
			iteration += 1
	return message

quest1 = "10+10"
ans1 = "20"
quest2 = "Test str question"
ans2 = "test test"

q1 = print(quiz_item(quest1, ans1))
q2 = print(quiz_item(quest2, ans2))