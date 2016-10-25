

p = "horses have joined a select group of animals that can communicate by pointing at symbols.scientists trained horses, by offering slices of carrot as an incentive, to touch a board with their muzzle to indicate if they wanted to wear a rug.the horses' requests matched the weather, suggesting it wasn't a random choice.a few other animals, including apes and dolphins, appear, like us, to express preferences by pointing at thing"
s = p.split('.')
for num in range(0,len(s)):
	print(s[num].capitalize())

p2 = "I have 1 son and 1 daughter. We have 1 house and 1 car."
p2.replace('1','one')
print(p2.replace('1','one'))

p3=[3,9,27]
for num in range(0,len(p3)):
	p3[num] = p3[num]*p3[num]*p3[num];
print(p3)