def compare_subjects_within_student(subj1_all_students,
                                    subj2_all_students):
    """
    Compare the two subjects with their students and print out the "preferred"
    subject for each student. Single-subject students shouldn't be printed.

    Choice for the data structure of the function's arguments is up to you.
    """
    set1=set(subj1_all_students.keys())
    set2 = set(subj2_all_students.keys())
    set2.intersection_update(set1)
    for student in set2:
        list1=max(subj1_all_students[student])
        list2=max(subj2_all_students[student])
        if list1 < list2:
            print('preferred subject for',str(student),'is subject2')
        else:
            print('preferred subject for', str(student), 'is subject1')

math={'Yossi':[70,79], 'Dana': [60, 99], 'Sima':[95,15],'Benni': [49, 95],'Donkey':[86,85]}
science={'Yossi':[56,100],'Sima':[8,55],'Dana':[77, 63],'Benni':[98,89]}
compare_subjects_within_student(math,science)
