import random
def foo(x,y,z):
    return 6*x**3 + 9*y**2 + 90*z -25

def fitness(x,y,z): #score the fitness high as it gets closer to 0
    ans = foo(x,y,z)
    if ans == 0:
        return 99999
    else:
        return abs(1/ans)
    
solution = []
for s in range(1000):
    solution.append((random.uniform(0,10000), #x
                    random.uniform(0,10000), #y
                    random.uniform(0,10000))) #z as a tuple
    
# print(solution[:5])
#lets use gen algo for 10000 gnerations 
for i in range(10000):
    rankedsolutions = []
    for s in solution:
        rankedsolutions.append( (fitness(s[0], s[1], s[2]), s))
    rankedsolutions.sort()
    rankedsolutions.reverse()
    
    print(f"=== Gen {i} best solutions ===")
    print(rankedsolutions[0])
    
    # THRESHOLD to stop
    if rankedsolutions[0][0] > 990:
        break
    
    bestsolutions = rankedsolutions[:100]
    
    elements = []
    for s in bestsolutions:
        elements.append(s[1][0])
        elements.append(s[1][1])
        elements.append(s[1][2])
        
    newGen = []
    for _ in range(1000):
        e1 = random.choice(elements) + random.uniform(0.99, 1.01)
        e2 = random.choice(elements) + random.uniform(0.99, 1.01)
        e3 = random.choice(elements) + random.uniform(0.99, 1.01)
        newGen.append((e1,e2,e3))
        
    solutions = newGen