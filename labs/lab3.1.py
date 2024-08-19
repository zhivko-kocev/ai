from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    problem.addVariable("Marija_prisustvo", [0, 1])
    problem.addVariable("Simona_prisustvo", [1])
    problem.addVariable("Petar_prisustvo", [0, 1])
    problem.addVariable("vreme_sostanok", [13, 14, 16, 19])

    problem.addConstraint(lambda a, b: b in [12, 13, 16, 17, 18, 19] or a == 0, ["Petar_prisustvo", "vreme_sostanok"])
    problem.addConstraint(lambda a, b: b in [14, 15, 18] or a == 0, ["Marija_prisustvo", "vreme_sostanok"])
    problem.addConstraint(lambda a, b, c: a != 0 and (b == 1 or c == 1),
                          ["Simona_prisustvo", "Marija_prisustvo", "Petar_prisustvo"])

    for solution in problem.getSolutions():
        print("{", end="")
        print(
            f''''Simona_prisustvo': {solution["Simona_prisustvo"]}, 'Marija_prisustvo': {solution["Marija_prisustvo"]}, 'Petar_prisustvo': {solution["Petar_prisustvo"]}, 'vreme_sostanok': {solution["vreme_sostanok"]}''',end="")
        print("}")
