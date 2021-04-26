def users_sorting(user_rates):
    user_rates = sorted(user_rates, key=lambda x: x[0].lower())
    user_rat = []
    for i in range(len(user_rates)):
        user_rat.append((user_rates[i][0], list(str(user_rates[i][1]))))

    user_rates = user_rat
    for i in range(len(user_rates)):
        for j in range(1, len(user_rates) - i):
            if user_rates[i + j][0] == user_rates[i][0]:
                user_rates[i][1].append(str(user_rates[i + j][1][0]))

    user_rat = []
    for i in range(len(user_rates)):
        flag = False
        for j in range(len(user_rat)):
            if user_rat[j][0] == user_rates[i][0]:
                flag = True
        if not flag:
            user_rat.append(user_rates[i])
    user_rates = user_rat

    user_rat = []
    for i in range(len(user_rates)):
        user_rat.append((user_rates[i][0], ' '.join(user_rates[i][1])))

    return user_rat