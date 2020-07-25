#Quiz: Calculate
#In this quiz you're going to do some calculations for a tiler. Two parts of a floor need tiling. .
 

#One part is 9 tiles wide by 7 tiles long and to calculate for the area is 9 * 7
first_part = 63

# the other is 5 tiles wide by 7 tiles long and to calculate for the area is 5 * 7
second_part = 35

#Tiles come in packages of 6.
one_pack = 6

# You buy 17 packages of tiles containing 6 tiles each and 17 * 6 is the total tiles bought
bought_tiles = 102


# to calculate for number of tiles that are needed. we add tiles needed for noth areas together
needed_tiles = first_part + second_part
print(needed_tiles)


#Number of tiles that will be left over. subtracting needed tiles from the bought tiles
left_overs = bought_tiles - needed_tiles
print(left_overs)