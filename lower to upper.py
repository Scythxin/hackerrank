def swap_case(s):
    x=""
    for i in s:
        if i.islower()== True:
            x=x+(i.upper())
        elif i.isupper()== True:
            x=x+(i.lower())
        else:
            x=x+i     

    return x



s = "Happy Birthday"
result = swap_case(s)
print(result)