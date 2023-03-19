# Булева алгебра - це розділ математичної логіки в якому вивчаються логічні операції над виразами

# бінарна логіка -> True or False (1 or 0)

# і, або, не -> and, or, not


# and(*)
#   A      B      A and B
# True   True      True   # 1 * 1 -> 1
# True   False     False  # 1 * 0 -> 0
# False  True      False  # 0 * 1 -> 0
# False  False     False  # 0 * 0 -> 0

print(True and False)


# or(+)
#   A      B      A or B
# True   True      True   # 1 + 1 -> 1
# True   False     True  # 1 + 0 -> 1
# False  True      True  # 0 + 1 -> 1
# False  False     False  # 0 + 0 -> 0

print(True or False)


# not(заперечення)
#   A     not A
#  True   False
#  False  True

print(not 2 < 0)
