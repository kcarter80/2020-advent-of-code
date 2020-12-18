def evaluate_with_advanced_precedence(expression):
	list_expression = expression.split(' ')
	i = 1
	while (i < len(list_expression)):
		if list_expression[i] == '+':
			operand_1 = int(list_expression.pop(i-1))
			list_expression.pop(i-1) # removes the operator
			operand_2 = int(list_expression.pop(i-1))
			result = operand_1 + operand_2
			list_expression.insert(i-1,str(result))
		else:
			i += 1
	# takes care of the remaining multiplications
	result = str(eval(''.join(list_expression)))
	return result

def evaluate_expression(expression):
	while expression.find(')') != -1:
		end_index = expression.find(')')
		start_index = expression.rfind('(',0,end_index)
		result_inside_the_parantheses = evaluate_with_advanced_precedence(expression[start_index+1:end_index])
		expression = expression[:start_index] + result_inside_the_parantheses + expression[end_index+1:]
		print(expression)
	return evaluate_with_advanced_precedence(expression)

# placing the rows from the input file into a list
with open('input-1') as input_file:
	input_lines = input_file.readlines()
sum = 0
for input_line in input_lines:
	sum += int(evaluate_expression(input_line.rstrip()))
print(sum)