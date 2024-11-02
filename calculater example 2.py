Rate = 30

hours = int(input(' projected number of hours'))
materials = float(input('wholesale cost of materials'))

CostOne = (hours * Rate)
CostTwo = (materials * 1.2)
CostThree = (CostOne + CostTwo)

print(CostThree)
print('End of program')
