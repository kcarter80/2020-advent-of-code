def evaluate_with_same_precedence(expression):
	list_expression = expression.split(' ')
	while (len(list_expression) >= 3):
		operand_1 = list_expression.pop(0)
		operator = list_expression.pop(0)
		operand_2 = list_expression.pop(0)
		
		list_expression.insert(0,eval('%s%s%s' %(operand_1,operator,operand_2)))
	return str(list_expression[0])

def evaluate_expression(expression):
	while expression.find(')') != -1:
		end_index = expression.find(')')
		start_index = expression.rfind('(',0,end_index)
		result_inside_the_parantheses = evaluate_with_same_precedence(expression[start_index+1:end_index])
		expression = expression[:start_index] + result_inside_the_parantheses + expression[end_index+1:]
	return evaluate_with_same_precedence(expression)

# placing the rows from the input file into a list
with open('input-1') as input_file:
	input_lines = input_file.readlines()

sum = 0
for input_line in input_lines:
	sum += int(evaluate_expression(input_line.rstrip()))

print(sum)