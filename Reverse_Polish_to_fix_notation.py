def rpn_to_infix(expression):
    stack = []
    tokens = expression.split()
    
    # Operators we are looking for
    operators = {'+', '-', '*', '/'}
    
    for token in tokens:
        if token in operators:
            # Pop the right operand first (LIFO)
            right = stack.pop()
            # Pop the left operand second
            left = stack.pop()
            
            # Combine them into a bracketed string
            # Using f-strings, but "{}{}{}".format works too!
            new_expression = f"({left}{token}{right})"
            stack.append(new_expression)
        else:
            # It's a number, just push it to the stack
            stack.append(token)
            
    # The final result is the only item left in the stack
    return stack[0]
  print(rpn_to_infix(input()))
