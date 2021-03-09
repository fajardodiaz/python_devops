class Classy():
    def __init__(self):
        self.items = []

    def addItem(self,text):
         self.items.append(text)
        
    def getClassiness(self):
        return  self.items

# Test cases
me = Classy()
print(me.getClassiness())
# Should be 0

# # Should be 2
me.addItem("tophat")
print(me.getClassiness())

# me.addItem("bowtie")
# me.addItem("jacket")
# me.addItem("monocle")
# # Should be 11
# print me.getClassiness()

# me.addItem("bowtie")
# # Should be 15
# print me.getClassiness()