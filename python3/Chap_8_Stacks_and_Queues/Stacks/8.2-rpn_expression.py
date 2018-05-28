#!/usr/local/bin/python3


def get_operator_fn(op):
    return {
        '+' : lambda x, y: x + y,
        '-' : lambda x, y: x - y,
        '*' : lambda x, y: x * y,
        '/' : lambda x, y: x // y,
        }[op]


def evaluate_rpn(exp_str):
    if exp_str.find(',') == -1: # simple expression with just digits
        return int(exp_str)

    op_idx = exp_str.rfind(',') + 1
    b_idx  = exp_str.rfind(',', 0, op_idx -1) + 1
    if(b_idx == 0):
        raise ValueError('Invalid RPN Expression string: {}'.format(exp_str))
    # print(op_idx, b_idx)
    a = evaluate_rpn(exp_str[0:b_idx-1])
    b = evaluate_rpn(exp_str[b_idx:op_idx-1])
    op = get_operator_fn(exp_str[op_idx:])

    if not op:
        raise ValueError("Operator {} not supported".format(expn_str[op_idx]))

    return op(a, b)

def evaluate_rpn_better(exp_str):
    comps = exp_str.rsplit(',', maxsplit=2)
    if len(comps) == 1:
        return int(comps[0])

    if len(comps) < 3:
        raise ValueError('Invalid RPN Expression string: {}'.format(exp_str))

    # print(comps)
    a = evaluate_rpn_better(comps[0])
    b = evaluate_rpn_better(comps[1])
    op = get_operator_fn(comps[2])

    return op(a, b)

def evaluate_rpn_using_stack(exp_str):
    temp_results = []
    OPS = {
        '+' : lambda x, y: x + y,
        '-' : lambda x, y: x - y,
        '*' : lambda x, y: x * y,
        '/' : lambda x, y: x // y,
    }
    for token in exp_str.split(','):
        if token in OPS:
            temp_results.append(OPS[token](temp_results.pop(), temp_results.pop()))
        else:
            temp_results.append(int(token))

    return temp_results.pop()


if __name__ == '__main__':
    print('Evaluate RPN Expressions')

    rpn_str = '1729'
    print("'{:>15s}' -> {}".format(rpn_str, evaluate_rpn_using_stack(rpn_str)))
    rpn_str = '-42'
    print("'{:>15s}' -> {}".format(rpn_str, evaluate_rpn_using_stack(rpn_str)))
    rpn_str = '3,4,+,2,*,1,+'
    print("'{:>15s}' -> {}".format(rpn_str, evaluate_rpn_better(rpn_str)))


