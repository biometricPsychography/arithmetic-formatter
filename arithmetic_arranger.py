def arithmetic_arranger(problems, will_calc_answers):
    try:
        # Check for invalid input

        if type(problems) is not list :
            raise Exception('Passed argument not of type list.')

        if len(problems) > 5 :
            raise Exception('Too many problems.')

        for problem in problems :
            if problem.find('*') != -1 or problem.find('/') != -1:
                raise Exception("Operator must be '+' or '-'.")
            
            operands = None
            parsed_operands_list = []
            print(problem)
            
            # if '+' or '-' is present

            possible_plus_index = problem.find('+')
            possible_minus_index = problem.find('-')

            

            if possible_plus_index != -1 :
                operator = '+'
            elif possible_minus_index != -1 :
                operator = '-'
            else :
                raise Exception("A + or a - operator is required.")

            
            
            operands = problem.split(operator)
            if len(operands) > 2 or possible_minus_index != -1 and possible_plus_index != -1:
                raise Exception("Only one operator is permitted.")

            for operand in operands :
                try:
                    # remove padding and verify it's an int then, return to stringe
                    parsed_operands_list.append(str(int(operand)))
                except Exception as e:
                    return 'Numbers must only contain digits.'
            
            operands = parsed_operands_list

            for operand in operands :
                if len(str(operand)) > 4 :
                    raise Exception("Numbers cannot be more than four digits.")


            # find longest operand, else None
            longest_operand = operands[0] if len(operands[0]) > len(operands[1]) else operands[1]
            if len(operands[0]) > len(operands[1]) :
                longest_operand = operands[0]
            elif len(operands[0]) < len(operands[1]) :
                longest_operand = operands[1]
            else :
                longest_operand = None

            # determine padding for operator
            if longest_operand :
                
                operator_distance_to_line_break = len(longest_operand) + 1
            else :
                operator_distance_to_line_break = len(operands[0]) + 1

            operator_padding_length = operator_distance_to_line_break - len(operands[1])

            operator_padding_string = ''
            for number in range(operator_padding_length) :
                operator_padding_string += ' '


            first_operand_padding_length = operator_distance_to_line_break + 1 - len(operands[0])
            first_operand_padding_string = ''
            
            for number in range(first_operand_padding_length) :
                first_operand_padding_string += ' '

            underline = ''
            for number in range(operator_distance_to_line_break + 1) :
                underline += '-'


            return f'{first_operand_padding_string + operands[0]}\n{operator}{operator_padding_string + operands[1]}\n{underline}'

            

    except Exception as e:
        return 'Error: ' + str(e)

    arranged_problems = None

    return arranged_problems

print(arithmetic_arranger(['100 + 500']))