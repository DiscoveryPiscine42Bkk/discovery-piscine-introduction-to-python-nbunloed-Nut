def find_the_redheads(family_dict):
    redheads = list(filter(lambda name: family_dict[name].lower() == "red", family_dict))
    return redheads

if __name__ == "__main__":
    family ={
        "alice": "blonde",
        "bob": "red",
        "charlie": "brown",
        "daisy": "red" }
    redhead_list = find_the_redheads(family)
    print(redhead_list)