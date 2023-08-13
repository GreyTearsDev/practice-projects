class Student:
    '''Model a student
    Attributes: name, age, year, class_name'''
    
    def __init__(self, name, year, classroom):
        '''Initialize the attributes'''
        self.name = name
        self.year = year
        self.classroom = classroom
        
    def describe_student(self):
        '''Describe the student info.'''
        print(f'Name: {self.name} \nYear: {self.year} \nClassroom: {self.classroom}')
    

class Grades:
    '''Model the grades
    Attributes: all subjects'''
    def __init__(self, pt, eng, math, geo, bio, chem, his, phy, ph_ed, ed_lab, evp, emc):
        self.pt = pt
        self.eng = eng
        self.math = math
        self.geo = geo
        self.bio = bio
        self.chem = chem
        self.his = his
        self.phy = phy
        self.ph_ed = ph_ed
        self.ed_lab = ed_lab
        self.evp = evp
        self.emc = emc
        
        
    def subject_grade_combo(self):
        '''Create a dictionary with {subject:grade} pairs'''
        grades = [self.pt, self.eng, self.math, 
                   self.geo, self.bio, self.chem, 
                   self.his, self.phy, self.ph_ed,  
                   self.ed_lab, self.evp, self.emc]
    
        subjects = ['Portuguese', 'English', 
                     'Mathematics', 'Geography', 
                     'Biology', 'Chemistry', 
                     'History', 'Physics', 
                     'Physical Education',  
                     'Technical Drawing', 
                     'Arts', 'Civil and Moral Education']

        combo = {subjects[i]: grades[i] for i in range(len(subjects))}
        return combo
        
        
    def get_grade_average(self):
        '''Get the average of the grades'''
        grades = []
        
        average = sum (self.subject_grade_combo) / 12
        return ('Grade average', round(average, 1))
        
        
    def show_all_grades(self):
        '''Display all grades-subject combinations'''
        for key in self.subject_grade_combo:
            return (f'{key}: {self.subject_grade_combo[key]}')
        
    
    def show_bad_grades(self):
        '''Show all grades bellow 9.5'''
        for subject, grade in self.subject_grade_combo.items():
            if grade < 9.5:
                return (f'{subject}: {grade}')   
        
        
    def show_good_grades(self):
        '''Show all grades above 9.5'''
        for subject, grade in self.subject_grade_combo.items():
            if grade >= 9.5:
                return (f'{subject}: {grade}')

    def count_bad_grades(self):
        '''Count the number of low grades'''
        count = 0
        for grade in self.subject_grade_combo.value():
            if grade < 9.5:
                count += 1
        return count
        
        
    def nuclear_grades_results(self):
        '''Decide if the student passes or not'''
        if self.pt in self.show_bad_grades() and self.math in self.show_bad_grades():
            print('The student failed the year because of unsatisfactory \
                grades in both nuclear subjects (Portuguese and Mathematics).')
            print(f'Portuguese: {self.pt} \n Mathematics: {self.math}')
        
        elif self.pt in self.show_bad_grades() and self.math not in self.show_bad_grades():
            print(f'The student failed the year because of an unsatisfactory \
                grade in Portuguese, which is one of the nuclear subjects.')
            print(f'Portuguese: {self.pt}')
            
        else:
            self.pt not in self.show_bad_grades() and self.math in self.show_bad_grades()
            print(f'The student failed the year because of an unsatisfactory \
                grade in Mathematics, which is one of the nuclear subjects.')
            print(f'Mathematics: {self.math}')
            
    def pass_or_fail(self):
        if self.pt < 9.5 or self.math < 9.5:
            self.nuclear_grades_results()
        elif self.count_bad_grades() > 2:
            print('The student failed the year because he/she exceeded the \
                minimum number of low grades allowed to pass.')
        else:
            print('The student passed.')
            

student1 = Student('Tirso Samalungo', 9, 'A')
student1.describe_student()
        
student1 = Grades(16, 14, 13, 18, 10, 9, 5, 14, 19, 20, 20, 20)

student1.show_all_grades()

student1.pass_or_fail()

