from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_blue, ft_green, ft_grey


test = input("Type a number to test the respective function:\n"
             "1 - ft_invert\n"
             "2 - ft_red\n"
             "3 - ft_green\n"
             "4 - ft_brue\n"
             "5 - ft_grey\n")
try:
    test = int(test)
    assert 1 <= test <= 5
except Exception:
    print("Only numbers from 1 to 5 accepted")
    exit(1)

dic = {1: ft_invert,
       2: ft_red,
       3: ft_green,
       4: ft_blue,
       5: ft_grey}

array = ft_load("landscape.jpg")

dic[test](array)
print(dic[test].__doc__)

# ft_invert(array)
# print(ft_invert.__doc__)

# ft_red(array)
# print(ft_red.__doc__)

# ft_green(array)
# print(ft_green.__doc__)

# ft_blue(array)
# print(ft_blue.__doc__)

# ft_grey(array)
# print(ft_grey.__doc__)
