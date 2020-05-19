class Student:
    Scores = {}

    # initializing the constructor method

    def _init_(self, name, grade):
        self.name = name
        self.grade = grade

    @property
    def getScores(self):

        answer_key = []
        # read into answer_key list, the answer key from file
        answer_key = [line.strip() for line in open("answers.txt", 'r')]
        student_answers = []
        total_score = 100
        # read into student_answers list, student answers from file
        student_answers = [line.strip().split(',')
                           for line in open("data.txt", 'r')]
        i = 0

        print('--' * 10, "Evaluating Scores : ", self.getName(), '--' * 10)
        try:
            while self.getName() != student_answers[i][0]:
                i = i + 1
            if self.getName() == (student_answers[i][0]):
                k, j = 0, 1
                while k < len(answer_key):
                    if answer_key[k] == student_answers[i][j]:
                        print("Question Number ", k + 1, ": 10 out of 10 ")
                        k = k + 1
                        j = j + 1
                    else:
                        print("Question Number ", k + 1, ": 0 out of 10 ")
                        total_score = total_score - 10
                        k = k + 1
                        j = j + 1
                Student.Scores[self.getName()] = total_score
                oldscore = student_objs[index].grade
                newscore = Student.Scores[self.getName()]
                range = abs(oldscore - newscore)
                average = abs(oldscore + newscore) / 2
                print('-' * 20, "Performance of student", self.getName(), '-' * 20)
                print(" Old score : ", oldscore, "\n New score : ", newscore, "\n Grade Range : ", range,
                      "\n Average Grade : ", format(average, '.1f'))

        except IndexError:
            print("Student mismatch")
            Student.Scores[self.getName()] = "Can't Evaluate"
        return (range, average)

    def getName(self):
        return self.name

    @staticmethod
    def sortDict():
        return sorted(Student.Scores.items())


student_objs = [

    Student('Sammy Student', 65),
    Student('Betty sanchez', 45),
    Student('Alice brown', 100),
    Student('tom Schulz', 50),
    Student('Anusha Satish', 80)
]
overall_range, overall_average = 0.0, 0.0
for index in range(len(student_objs)):
    range, average = student_objs[index].getScores
    overall_average = overall_average + average
    overall_range = overall_range + range

sortList = Student.sortDict()
overall_average = overall_average / len(student_objs)
overall_range = overall_range / len(student_objs)

print('+' * 25, "Class Performance ", '+' * 25)
for k, v in sortList:
    print(str(k).title(), "has scored:", v)
print('-' * 50)
print(" Overall Grade Range : ", format(overall_range, '.1f'), "\n Overall Average Grade: ",
      format(overall_average, '.1f'))
print('*+' * 50)