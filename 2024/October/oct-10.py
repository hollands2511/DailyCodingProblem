# October 10th 2024
# Andrew Hollands
#
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k
#

def find_sum_in_list( number_list , sum_to_find ):

    sum_in_list = False
    index = 0

    for number_1 in number_list:
        number_list_without_number_1 = number_list[index+1:index-1]
        index += 1
        for number_2 in number_list_without_number_1:
            result = number_1 + number_2
            if ( result == sum_to_find ):
                sum_in_list = True

    return sum_in_list

print( find_sum_in_list( [ 1 , 2 , 3 ] , 3 ) )
print( find_sum_in_list( [ 1 , 2 , 3 ] , 23 ) )

print( find_sum_in_list( [ 1 , 2 , 3 ] , 2 ) )

