def calendar(m):
    date = "january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"

    for i in range (0, len(date)):
        if m == date[i]:
            return i + 1
    return m + " is not a munth"

print (calendar("march"))