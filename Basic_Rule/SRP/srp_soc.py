class Journal:
    def __init__(self):
        self.enteries=[]
        self.count=0

    def add(self,txt):
        self.enteries.append(txt)
        self.count+=1
    
    def remove(self,pos):
        del self.enteries[pos]
    
    def __str__(self):
        return '\n'.join(self.enteries)

class Persistance:
    @staticmethod
    def save_to_a_file(journal,filepath):
        file=open(filepath,'w')
        file.write(str(journal))
        file.close()

j1=Journal()
j1.add("Hello")
j1.add("World")
print(j1)
filepath='/home/dram/design_pattern/Basic_Rule/SRP/journal.txt'
Persistance.save_to_a_file(j1,filepath)
with open(filepath) as insidefile:
    a=insidefile.read()
    print(a)


'''Instead of making the Journal Function to take more responsibility
we made the persistance class to take care of saving the journal to a particular
path hence this is called Single responsiblity/Seperation of Concern principle'''




    