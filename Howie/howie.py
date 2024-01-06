from jproperties import Properties

"""
initialises a set that contains all the swears in the text file defined in the properties file
"""
def initSwearSet() -> set[str]:
    configs = Properties()
    file_name = "pulled from properties file"
    swear_set = set()
    