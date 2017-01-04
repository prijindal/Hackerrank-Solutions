class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores
    
    def calculate(self):
    	sum = 0
    	for i in self.scores:
    		sum+=i
    	avg = sum/len(self.scores)
    	if avg >= 90:
    		return 'O'
    	elif avg >= 80:
    		return 'E'
    	elif avg >= 70:
    		return 'A'
    	elif avg >= 55:
    		return 'P'
    	elif avg >= 40:
    		return 'D'
    	else:
    		return 'T'