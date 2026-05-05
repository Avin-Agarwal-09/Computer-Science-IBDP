class Assessment:
    
    def __init__(self, assessment_name, score):
        self.assessment_name = assessment_name
        self.score = score

    def get_score(self):
        return self.score

    def __str__(self):
        return f"{self.assessment_name}: {self.score}"


class Student:
    
    def __init__(self, student_name):
        self.student_name = student_name
        self.assessments = []
        
        self.grade_boundaries = [90, 80, 70, 60, 50]
        self.grades = ['A', 'B', 'C', 'D', 'E', 'F']
        self.current_grade = None

    def add_assessment(self, assessment):
        self.assessments.append(assessment)

    def get_average_score(self):
        if len(self.assessments) == 0:
            return 0
        
        total = 0
        for assessment in self.assessments:
            total += assessment.get_score()
        
        return total / len(self.assessments)

    def calculate_grade(self):
        average = self.get_average_score()
        
        for i in range(len(self.grade_boundaries)):
            if average >= self.grade_boundaries[i]:
                self.current_grade = self.grades[i]
                return
        
        self.current_grade = self.grades[-1]  # F

    def __str__(self):
        self.calculate_grade()
        return (f"Name: {self.student_name}\n"
                f"Average: {self.get_average_score()}\n"
                f"Grade: {self.current_grade}")
    
Student.add_assessment(Assessment("test 1",75))

print(Student)