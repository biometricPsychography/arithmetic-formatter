def arithmetic_arranger(problems):
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
            if problem.find('+') != -1 :
                operands = problem.split('+')
                if len(operands) > 2 :
                    raise Exception("Only one operator is permitted.")

                for operand in operands :
                   operand = int(operand)

            elif problem.find('-') != -1 :
                operands = problem.split('-')
                if len(operands) > 2 :
                    raise Exception("Only one operator is permitted.")

                for operand in operands :
                   parsed_operands_list.append(int(operand))
            
            operands = parsed_operands_list
            return operands


    except Exception as e:
        return 'Error: ' + str(e)

    arranged_problems = None

    return arranged_problems

print(arithmetic_arranger(['5 - 2']))