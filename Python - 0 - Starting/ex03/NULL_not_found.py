def NULL_not_found(object: any) -> int:
    the_type = type(object)
    if object is None:
        print(f"Nothing: None {the_type}")
        return 0
    if isinstance(object, float) and str(object) == 'nan':
        print(f"Cheese: nan {the_type}")
        return 0
    if object == 0 and the_type is int:
        print(f"Zero: 0 {the_type}")
        return 0
    if object == '' and the_type is str:
        print(f"Empty: {the_type}")
        return 0
    if object is False and the_type is bool:
        print(f"Fake: False {the_type}")
        return 0
    print("Type not Found")
    return 1
