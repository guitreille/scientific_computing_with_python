def arithmetic_arranger(problems, solve = False):
  print(len(problems))
  if (len(problems) > 5):
    #raise Exception("Error: Too many problems.")
    return "Error: Too many problems."

  arranged_problems = ''
  first_numbers = []
  second_numbers = []
  operands = []
  solutions = []
  for sproblem in problems:
    buffer = sproblem.split(' ')
    try:
      numberOne = int(buffer[0])
      numberTwo = int(buffer[2])
    except:
      return "Error: Numbers must only contain digits."
    operand = buffer[1] #string
    # check operand 
    if (operand != "+") and (operand != "-"):
      #raise Exception("Error: Operator must be '+' or '-'.")
      return "Error: Operator must be '+' or '-'."
      
    first_numbers.append(numberOne)
    operands.append(operand)
    second_numbers.append(numberTwo)
    if (solve):
      solutions.append(solveExpression(numberOne, numberTwo, operand))

  first_line = ''
  second_line = ''
  bars = ''
  solution_line = ''
  for i in range(len(first_numbers)):
    max_number_length = max(len(str(first_numbers[i])), len(str(second_numbers[i])))
    if (max_number_length > 4):
      #raise Exception('Error: Numbers cannot be more than four digits.')
      return 'Error: Numbers cannot be more than four digits.'
    format_first_line = '{:>' + str(max_number_length+2) +'}'
    format_second_line = '{:>' + str(max_number_length+1) +'}'
    first_line = first_line + format_first_line.format(str(first_numbers[i])) + '    '
    second_line = second_line + operands[i] + format_second_line.format(str(second_numbers[i])) + '    '
    bars = bars + format_first_line.format('-'*(max_number_length+2)) + '    '
    if (solve):
      solution_line = solution_line + format_first_line.format(str(solutions[i])) + '    '
  first_line = first_line.rstrip() #remove trailing white spaces
  second_line = second_line.rstrip()
  bars = bars.rstrip()
  arranged_problems = first_line + '\n' + second_line + '\n' + bars
  if (solve):
    solution_line = solution_line.rstrip()
    arranged_problems +=  '\n'  + solution_line

  return arranged_problems

def solveExpression(numberOne, numberTwo, operator_str):
  if (operator_str == "+"):
    return numberOne + numberTwo
  elif (operator_str == "-"):
    return numberOne - numberTwo
  else:
    return null
    

    
    