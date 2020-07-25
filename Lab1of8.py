# To Calculate and print the total sales for the week from the data provided. 


mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"


#converting the string values to integers
mon_sales = int(mon_sales)
tues_sales = int(tues_sales)
wed_sales = int(wed_sales)
thurs_sales = int(thurs_sales)
fri_sales = int(fri_sales)

#Adding the days sales to a total_sales variables
total_sales = (mon_sales + tues_sales + wed_sales + thurs_sales + fri_sales)

# Printing it with a string
print("This week\'s total sales:",total_sales)