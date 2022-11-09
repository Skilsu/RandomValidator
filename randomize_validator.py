def random_variance(number_of_games=1000, repetition_of_game=10000):
    erg = []
    for a in range(int(number_of_games/2)):
        erg.append(0)
    for i in range(repetition_of_game):
        var = 0
        for j in range(number_of_games):
            if bool(random.getrandbits(1)):
                var += 1
        var -= int(number_of_games / 2)
        if var < 0:
            var -= 2 * var
        erg[var] = erg[var] + 1
    var = 0
    for idx, i in enumerate(erg):
        var += i
        if i > 0:
            print(str(idx) + ": " + str(i) + " = " + str(idx / number_of_games * 100)[:4] + "% -> " +
                  str(var / repetition_of_game * 100)[:4] + "%")
