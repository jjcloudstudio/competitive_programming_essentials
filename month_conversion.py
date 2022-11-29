month_conversion = {
    "JAN": "January",
    "feb": "February",
    "mar": "March",
    "apr": "April",
    "may": "May",
    "jun": "June",
    "jul": "July",
    "aug": "August",
    "sep": "September",
    "oct": "October",
    "nov": "November",
    "dec": "December",
}

dict((k.lower(), v) for k,v in {'My Key':'My Value'}.items())

print(month_conversion["aug"])
print(month_conversion.get("aug", "not a valid key"))
print(month_conversion.get("abc", "not a valid key"))
print(month_conversion.get("jan", "not a valid key"))
