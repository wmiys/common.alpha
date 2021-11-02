import json
import uuid
from datetime import datetime

SECONDS_PER_HOUR = 3600

#------------------------------------------------------
# return the data from the specified json file
#------------------------------------------------------
def readJsonFile(file_name_path: str) -> dict:
    with open(file_name_path) as configFile:
        configData = json.loads(configFile.read())
        return configData

# ------------------------------------------------------
# Returns a UUID
#-------------------------------------------------------
def getUUID(as_string: bool=True):
    new_uuid = uuid.uuid4()
    
    if as_string == True:
        return str(new_uuid)
    else:
        return new_uuid

# ------------------------------------------------------
# Prints an object to the console between the specified number of line breaks
#-------------------------------------------------------
def printWithSpaces(output='', num_spaces: int = 20):
    lineBreak(num_spaces)
    print(output)
    lineBreak(num_spaces)

# ------------------------------------------------------
# Prints a specified number of line breaks to the console
#-------------------------------------------------------
def lineBreak(num_lines: int=1):
    print("\n" * num_lines)

# ------------------------------------------------------
# Checks if any of the fields contained in the dict are valid properties of the given object
#
# returns a boolean:
#   true - all dict fields are valid
#   false - the dict contains a field that is not a property of the object
#-------------------------------------------------------
def areAllKeysValidProperties(test_dict: dict, the_object: object) -> bool:
    for key in test_dict:
        if not hasattr(the_object, key):
            return False
    
    return True


#------------------------------------------------------
# Set's the object's properties given a dict
#------------------------------------------------------
def setPropertyValuesFromDict(new_property_values: dict, the_object):
    # set the object properties
    for key in new_property_values:
        if new_property_values[key]:
            setattr(the_object, key, new_property_values.get(key, None))
        else:
            setattr(the_object, key, None)
        
    
def intTryParse(value):
    try:
        return int(value), True
    except ValueError:
        return value, False


def getDurationHours(date_start: datetime, date_end: datetime):
    then = date_start        
    now  = date_end                             # Now
    duration = now - then                         # For build-in functions
    duration_in_s = duration.total_seconds()      # Total number of seconds between dates

    hours = divmod(duration_in_s, SECONDS_PER_HOUR)[0] 

    return hours