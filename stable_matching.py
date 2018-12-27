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

from random import sample

class StableMatch:
    def __init__(self, quantity):
        self.quantity = quantity
        self.men = range(quantity)
        self.women = range(quantity)
        self.engaged_men = [False] * quantity
        self.engaged_women = [False] * quantity
        self.engaged_pairs = {}
        self.men_preferences = [sample(self.women, self.quantity) for elem in range(self.quantity)]
        self.women_preferences = [sample(self.men, self.quantity) for elem in range(self.quantity)]
        self.men_who_proposed = [[False] * quantity for elem in range(quantity)]

    def match_couples(self):
        while False in self.engaged_men:
            man = self.men[self.engaged_men.index(False)]
            preferred_women = self.men_preferences[man]
            for elem in preferred_women:
                if not self.men_who_proposed[man][elem]:
                    woman = self.women[elem]
                    self.men_who_proposed[man][elem] = True
                    if not self.engaged_women[woman]:
                        self.engage(man, woman)
                        break
                    else: # woman is engaged
                        other_man = self.get_fiance(woman)
                        if self.rank_man(woman, man, other_man):
                            self.engage(man, woman)
                            self.engaged_men[other_man] = False
                            break

    def engage(self, man, woman):
        self.engaged_pairs[woman] = man
        self.engaged_women[woman] = True
        self.engaged_men[man] = True

    def rank_man(self, woman, man1, man2):
        preferred = self.women_preferences[woman]
        return preferred.index(man1) < preferred.index(man2)

    def get_fiance(self, woman):
        return self.engaged_pairs[woman]

def test_class():
    c = StableMatch(10)
    c.match_couples()
    sorted_couples = sorted(list(c.engaged_pairs.items()))
    #print(f'quantity: {c.quantity}')
    #print(f'men who proposed: {c.men_who_proposed}')
    #print(f'men preferences: {c.men_preferences}')
    #print(f'women preferences: {c.women_preferences}')
    print(f'engaged pairs: {sorted_couples}')

test_class()
