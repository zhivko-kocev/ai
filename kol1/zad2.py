from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    variables = ["S", "E", "N", "D", "M", "O", "R", "Y"]
    for variable in variables:
        problem.addVariable(variable, Domain(set(range(10))))

    #problem.addConstraint(lambda a, b: a != 0 and b != 0, ["S", "M"])
    problem.addConstraint(AllDifferentConstraint())
    problem.addConstraint(
        lambda s, e, n, d, m, o, r, y: (1000 * s + 100 * e + 10 * n + d) + (1000 * m + 100 * o + 10 * r + e) == (
                    10000 * m + 1000 * o + 100 * n + 10 * e + y),
        ["S", "E", "N", "D", "M", "O", "R", "Y"])

    print(problem.getSolution())
