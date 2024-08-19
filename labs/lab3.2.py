from constraint import *


def group_four(*variables):
    t1 = [item for item in variables if item == "T1"]
    t2 = [item for item in variables if item == "T2"]
    t3 = [item for item in variables if item == "T3"]
    t4 = [item for item in variables if item == "T4"]

    return 0 <= len(t1) <= 4 and 0 <= len(t2) <= 4 and 0 <= len(t3) <= 4 and 0 <= len(t4) <= 4


def group_three(*variables):
    t1 = [item for item in variables if item == "T1"]
    t2 = [item for item in variables if item == "T2"]
    t3 = [item for item in variables if item == "T3"]

    return 0 <= len(t1) <= 4 and 0 <= len(t2) <= 4 and 0 <= len(t3) <= 4


if __name__ == '__main__':
    num = int(input())

    papers = dict()

    paper_info = input()
    while paper_info != 'end':
        title, topic = paper_info.split(' ')
        papers[title] = topic
        paper_info = input()

    variables = [item for item in papers.items()]
    domain = [f'T{i + 1}' for i in range(num)]

    problem = Problem(BacktrackingSolver())

    problem.addVariables(variables, domain)

    ai = [item for item in variables if item[1] == "AI"]
    ml = [item for item in variables if item[1] == "ML"]
    nlp = [item for item in variables if item[1] == "NLP"]

    if 0 < len(ai) <= 4:
        problem.addConstraint(AllEqualConstraint(), ai)
    if 0 < len(ml) <= 4:
        problem.addConstraint(AllEqualConstraint(), ml)
    if 0 < len(nlp) <= 4:
        problem.addConstraint(AllEqualConstraint(), nlp)

    if num == 3:
        problem.addConstraint(group_three)
    if num == 4:
        problem.addConstraint(group_four)

    result = problem.getSolution()
    new_result = sorted(result, key=lambda x: x[0])
    new_result.append(new_result.pop(1))

    # Tuka dodadete go kodot za pechatenje
    [print(f'{item[0]} ({item[1]}): {result[item]}') for item in new_result]
