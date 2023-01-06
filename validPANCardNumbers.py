import re
 
def get_valid_pan_number(par):
    re_exp = r"[A-Z]{3}[ABCFGHLJPTK]{1}[A-Z]{1}[0-9]{4}[A-Z]{1}"
    return re.findall(re_exp, par)

par = "AABZA1111A AABAA1111AxMKOFM5336A"
print(set(get_valid_pan_number(par)))
