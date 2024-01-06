from jproperties import Properties

"""
initialises a set that contains all the swears in the text file defined in the properties file
"""
def initSwearSet() -> set[str]:
    configs = Properties()
    file_name = "pulled from properties file"
    swear_set = set()
    
    
    with open("../properties.properties", "rb") as config_file:
        configs.load(config_file)    
        file_name = configs.get("SWEARFILE")[0]
    
    with open(f"../{file_name}", "r") as swear_file:
        for line in swear_file:
            swear_set.add(line.strip("\r\n"))
    
    return swear_set