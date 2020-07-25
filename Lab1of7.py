#Using concatenation and the len() function to find the length of a certain movie star's actual full name. The length is stored in the name_length variable.

given_name = "William"
middle_names = "Bradley"
family_name =  "Pitt"

name_length = len(given_name + " " + middle_names + " " + family_name)


# The name fits within the driving license character limit

driving_license_character_limit = 28
print(name_length <= driving_license_character_limit)