# 3. Произвольные именованные аргументы (**kwargs) - передаются как словарь
def person_info(**info):
    print("Last name is " + info["lname"])
person_info(fname = "Tobias", lname = "Refsnes")