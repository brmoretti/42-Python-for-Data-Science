ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

###
### CODE
###

#List
ft_list[-1] = "World!"

#Tuple
tmp = list(ft_tuple)
tmp[1] = "Brazil!"
ft_tuple = tuple(tmp)

#Set
ft_set.discard("tutu!")
ft_set.add("Sao Paulo!")

#Dictionary
ft_dict["Hello"] = "42SP!"

###
### END
###

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
