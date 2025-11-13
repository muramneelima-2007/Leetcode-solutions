class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        rotation=0
        while (len(students)!=0):
            if(students[0]==sandwiches[0]):
                students=students[1:]
                sandwiches=sandwiches[1:]
                rotation=0
            else:
                students=students[1:]+[students[0]]
                rotation+=1
                if(rotation>len(students)):
                    return len(students)
        return 0
        


                
