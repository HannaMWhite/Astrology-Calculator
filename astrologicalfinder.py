#Python Astrological Finder
#Finds a user's astrological sign when they input the month and date of birth. 

# Determine the astrological sign based on the provided day and month
month = input("What month were you born? eg. June, April, May")
month = month.lower()
day = int(input("What day were you born?"))
months = ["march", "april", "may", "june", "july", "august", "september", "october", "november", "december", "january", "february"]

# Determine the astrological sign based on the provided day and month
if month in months:
    if month == "march":
        sign = "Pisces" if (day < 21) else "Aries ♈️"
    elif month == "april":
        sign = "Aries" if (day < 20) else "Taurus ♉️"
    elif month == "may":
        sign = "Taurus" if (day < 21) else "Gemini ♊️"
    elif month == "june":
        sign = "Gemini" if (day < 21) else "Cancer ♋️"
    elif month == "july":
        sign = "Cancer" if (day < 23) else "Leo ♌️"
    elif month == "august":
        sign = "Leo" if (day < 23) else "Virgo ♍️"
    elif month == "september":
        sign = "Virgo" if (day < 23) else "Libra ♎️"
    elif month == "october":
        sign = "Libra" if (day < 23) else "Scorpio ♏️"
    elif month == "november":
        sign = "Scorpio" if (day < 22) else "Sagittarius ♐️"
    elif month == "december":
        sign = "Sagittarius" if (day < 22) else "Capricorn ♑️"
    elif month == "january":
        sign = "Capricorn" if (day < 20) else "Aquarius ♒️"
    elif month == "february":
        sign = "Aquarius" if (day < 19) else "Pisces ♓️"

print ("Your Astrological sign is a " + sign)