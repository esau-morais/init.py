def grades(*nums, sit=False):
    """
    Analysis of grades and situation of a student:
    nums is the grade of the student (accepts multiple notes)
    sit (optional) is the situation of the student
    returns various information about class situation
    """
    g = dict()
    g["Total"] = len(nums)
    g["Highest"] = max(nums)
    g["Smaller"] = min(nums)
    g["Mean"] = sum(nums) / len(nums)
    if sit == True:
        if g["Mean"] >= 7:
            g["Situation"] = "Good"
        elif g["Mean"] >= 5:
            g["Situation"] = "Reasonable"
        else:
            g["Situation"] = "Bad" 
    return g


answer = grades(10, 7, 9, sit=True)
print(answer)

help(grades)
