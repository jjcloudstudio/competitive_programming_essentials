month_conversion = {
    "jan": "January",
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

#print(month_conversion["aug"])
#print(month_conversion.get("aug"))
print(month_conversion.get("abc", "not a valid key"))
print(month_conversion.get("lower.Jan", "not a valid key"))
