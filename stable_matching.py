# The Stable Matching Problem originated, in part, in 1962,
# when David Gale and Lloyd Shapley two mathematical economists,
# asked the question: Could one design a college admissions process,
# or a job recruiting process, that was self-enforcing?
# What did they mean by this?
# Following Gale and Shapley, we observe that this special case can
# be viewed as the problem of devising a system by which each of n men
# and n women can end up getting married: our problem naturally has the
# analogue of two “genders”—the applicants and the companies—and in the
# case we are considering, everyone is seeking to be paired with exactly
# one individual of the opposite gender.

# Simplified first try
men = [0,1,2]
women = [0,1,2]

# All are single at the beginning
engaged_men = [False, False, False]
engaged_women = [False, False, False]

# Preference lists (in ordered form)
men_pref = [[1,2,0], [0,1,2], [2,1,0]]
women_pref = [[0,2,1], [0,1,2], [2,0,1]]

# Men who proposed
men_prop_women = [[False, False, False], [False, False, False], [False, False, False]]

# List of tuples (man, woman)
engaged_pairs = []

# This is pretty much pseudocode
def matching_couples():
    while False in engaged_men:
        man = men[engaged_men.index(False)]
        preferred_women = women_pref[man]
        for elem in preferred_women:
            if not men_prop_women[elem]:
                woman = women[elem]
                men_prop_women[man][elem] = True
                if not engaged_women[woman]:
                    engage(man, woman)
                    break
            # if woman is engaged:
            else:
                other_man = get_man(woman)
                if ranking(woman, man, other_man):
                    engage(man, woman)
                    break
    print(engaged_pairs)
    print("Job done!")

def engage(man, woman):
    engaged_pairs.append((man, woman))

def ranking(woman, man1, man2):
    rank = women_pref[woman]
    return rank.index(man1) < rank.index(man2)

def get_man(woman):
    pass

matching_couples()
