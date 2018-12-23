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
MEN = [1,2,3]
WOMEN = [1,2,3]

# All are single at the beginning
men_married_status = [False, False, False]
women_married_status = [False, False, False]

# Preference lists (in ordered form)
men_preferences = [[1,2,3], [3,1,2], [2,1,3]]
women_preferences = [[3,2,1], [3,1,2], [2,3,1]]

# List of tuples (man, woman)
engaged_pairs = []

# This is pretty much pseudocode
def matching_couples(engaged_pairs):
    while there_are_singles():
        man = select_single_man()
        woman = preferred_woman(man)
        if is_free(woman):
            engage(man, woman)
        else:
            other_man = get_man(woman)
            if rank(other_man, man) > 0:
                pass
            else:
                engage(man, woman)
                free(other_man)
    return modified_engaged_pairs

def there_are_singles():
    pass
