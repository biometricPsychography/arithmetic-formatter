def arithmetic_arranger(problems, will_calc_answers):
    try:
        # Check for invalid input

        if type(problems) is not list :
            raise Exception('Passed argument not of type list.')

        if len(problems) > 5 :
            raise Exception('Too many problems.')

        formatted_problem_list = []
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


            

            

            answer = ''
            answer_padding_count = 0
            answer_padding = ''
            answer_line_break = ''
            if will_calc_answers :
                if operator == "+" :
                    answer = int(operands[0]) + int(operands[1])
                elif operator == "-" :
                    answer = int(operands[0]) - int(operands[1])
            
                answer = str(answer)


                answer_padding_count = len(underline) - len(answer)
                for number in range(answer_padding_count) :
                    answer_padding += ' '
                
                answer = str(answer)
                answer_line_break = '\n'


            formatted_problem_list.append(f'{first_operand_padding_string + operands[0]}\n{operator}{operator_padding_string + operands[1]}\n{underline}{answer_line_break + answer_padding + answer}')


        
        final_text_line_list = []
        # generate a 2D list where each 1st level list reps problem and inside is list of lines
        problem_spacing = '    '
        split_problems_list = []
        problem_index = 0
        for formatted_problem in formatted_problem_list :
            split_problems_list.append([])
            current_problem_textlines_list = formatted_problem.split('\n')
            for current_problem_textline in current_problem_textlines_list :
                if problem_index == 0 :
                    problem_spacing = ''
                else :
                    problem_spacing = '    '
                split_problems_list[problem_index].append(problem_spacing + current_problem_textline)
            
            problem_index += 1
        
        # collapse 2D list where each element represents a complete line of the final output
        for problem in split_problems_list :
          
            line_index = 0
            for line in problem :
                if len(final_text_line_list) < len(problem) :
                    final_text_line_list.append('')
                
                final_text_line_list[line_index] += line
                line_index += 1

        # turn list into one string

        arranged_problems = ''
        for line in final_text_line_list :
            arranged_problems += line + '\n'
                


        return (arranged_problems)

    except Exception as e:
        return 'Error: ' + str(e)
        

    

print(arithmetic_arranger(['100 - 5000', '22 + 66'], False))