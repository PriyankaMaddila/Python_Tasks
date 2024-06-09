file = open('C:/Users/hp/Desktop/Internships/Cognifyz/LEVEL-2 TASKS/count.txt','r')
data = file.read()
print("Givem text file data is:",data)

occurrences = data.count('india')
print("Number of occurrences of the word :",occurrences)
occurrences = data.count('India')
print("Number of occurrences of the word :",occurrences)
occurrences = data.count('Hinduism')
print("Number of occurrences of the word :",occurrences)

