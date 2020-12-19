# Code your solution here
month = input()

month_dict  = {"january": 31, "february": 28, 
                      "march": 31, "april": 30,
                      "may": 31, "june": 30, 
                      "july": 31, "august": 31,
                      "september": 30, "october": 31,
                      "november": 30, "december": 31}

if month in month_dict.keys():
    data = month_dict[month]

print(data)