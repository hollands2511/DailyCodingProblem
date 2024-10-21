# ============================================================================
# Andrew Hollands
# October 22 2024
# Geeks for geeks coding question
# Find the sum of an array.
# =============================================================================


# input:
# process:
# output:
def find_sum_of_array( array ):
    sum_of_array = 0

    for item in array:
        sum_of_array += item

    return sum_of_array


array = [ 1 , 2 , 3 ]

assert find_sum_of_array( array ) == 6
print( find_sum_of_array( array ) == 6 )

