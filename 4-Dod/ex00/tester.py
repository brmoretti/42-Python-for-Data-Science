from statistics import ft_statistics
ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
print("-----")
ft_statistics(toto="mean", tutu="median", tata="quartile")

# My tests
print("\n-------MY TESTS-------")
ft_statistics("a", "b", "c", toto="mean")
print("-----")
ft_statistics(1, 42, 360, 11, 64)
print("-----")
ft_statistics()
print("-----")
ft_statistics(toto="mean")
