f = open('person.csv')
persons = f.readlines()
f.close()

f2 = open('survey.csv')
surveys = f2.readlines()
f2.close()

for person in persons:
    person = person.split('|')
    for survey in list(surveys):
        survey = survey.split('|')
        if person[0] == survey[1]:
            print person[0], survey[1]
            
