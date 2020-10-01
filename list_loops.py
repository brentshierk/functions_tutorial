#Q1
songs = ["ROCKSTAR", "Do It", "For The Night"]

#Q2
print(songs[0:1])
print(songs[-1:])

#Q3
songs[2] = "The moon"
# print the list
print(songs)

#Q4

songs.append('Day Without End')
songs.append('Pontiac 87')
songs.append('Worm In Heaven')
print(songs)
del songs[0]
print(songs)



# 1. Create another list called animals and fill it with 3 animal strings of your choice such as "Cat", "Dog", and "Bird"
# 2. Add another animal to your list
# 3. print out the 3rd animal in the list
# 4. Delete the first animal in the list
# 5. Use a loop to print out all the animals in you

#step 1 
animals = ['dog','cat','bird']
#step 2
animals.append('alligator')
#step 3
print(animals[2])
#step 4
animals.pop(0)
#step 5 
for animal in animals:
  print(animal)