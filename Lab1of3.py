#Note that this code uses scientific notation to define large numbers. 4.445e8 is equal to 4.445 * 10 ** 8 which is equal to 444500000.0.

# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445 ** 8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5 ** 6

# decrease the rainfall variable by 10% to account for runoff
runoff = rainfall / 0.1

# add the rainfall variable to the reservoir_volume variable
addition = rainfall + reservoir_volume

# increase reservoir_volume by 5% to account for stormwater that flows into the reservoir in the days following the storm
stormwater = reservoir_volume * 0.5

# decrease reservoir_volume by 5% to account for evaporation
evaporation_account = reservoir_volume / 0.5

# subtract 2.5e5 cubic metres from reservoir_volume to account for water that's piped to arid regions.
arid_regions_water = 2.5 ** 5 - reservoir_volume


# print the new value of the reservoir_volume variable
new_reservoir_volume = arid_regions_water + evaporation_account + stormwater
print(new_reservoir_volume)