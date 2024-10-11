# Andrew Hollands
# October 11th 2024
#
# Given an array of integers, return a new array such that each element at index i of the new array 
# is the product of all the numbers in the original array except the one at i.

# input:    A list of numbers.
# process:  Loop through the list and calculate the product of all of the numbers.
#           Create an empty list to store the products.
#           Loop through the provided list again, subtracting the number at the current index from the sum of all the numbers.
#           Then store this new sum in the local list.
# output:   Return the list of products without index
            
def get_product_of_list_without_index( number_list ):

    index = 0
    number_list_length = len( number_list )
    list_of_products = []

    while ( index < number_list_length ):
        number_list_copy = number_list.copy()
        number_list_copy.pop( index )
        product_without_index = get_product_of_list( number_list_copy )
        list_of_products.append( product_without_index )

        index += 1

    return list_of_products

def get_product_of_list( number_list ):

    number_list_length = len( number_list )
    index = 1   # starting at 1 because the value of product will start as number_list[ 0 ]
    product = number_list[ 0 ]

    while ( index <  number_list_length ):
        product *= number_list[ index ] 
        index += 1

    return product

list_1 = [ 1 , 2 , 3 ]

print( list_1 )
print( get_product_of_list_without_index( list_1 ) )
print( "Expecting: [ 6 , 3 , 2 ]" )
