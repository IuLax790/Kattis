for i in range(int(input())):
    name,studyStart,age,courses = input().split(' ')
    status = 'ineligible'
    if int(studyStart.split('/')[0])>=2010 or int(age.split('/')[0])>=1991:
        status = 'eligible'
    elif int(courses)<=40:
        status = 'coach petitions'
    print(name,status)
