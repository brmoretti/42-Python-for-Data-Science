def all_thing_is_obj(object: any) -> int:
	types = ("List", "Tuple", "Set", "Dict")

	the_type = type(object)
	if the_type is str:
		print(f"{object} is in the kictchen : {the_type}")
		return 42

	type_name = str(the_type).split(" ")[1][1:-2].capitalize()
	if (type_name in types):
		print(f"{type_name} : {the_type}")
		return 42

	print("Type not found")
	return 42
