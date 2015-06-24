#dog_program.py
#something about how old our dog is

age_of_dog = input('Enter age of dog: ')
if age_of_dog <= 0:
    print"Hold on! Say what"
elif age_of_dog == 1:
    print"about 14 human years"
elif age_of_dog ==2:
    print "about 22 human years"
elif age_of_dog > 2:
    human_years = 22 + (age_of_dog - 2) * 5
    print "about ", human_years," human years"