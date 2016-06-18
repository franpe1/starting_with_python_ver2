def main():

# List with the good answers
    answers = ['B','D','A','A','C',
                'A','B','A','C','D',
                'B','C','D','A','D',
                'C','C','B','D','A']

# enter the file name and get the score in a list
    file = str(input("enter the file name with the score: "))
    
    exam = readexam(file)

    results = compare(answers,exam)

#Print the results ( good, wrong + list of wrongs )
    print(results)

# if score is > 15 PASSED else FAILED
# Display the total of correct and incorrect answers
# Show the question number of the incorrect ones

def readexam(filename):
    with open('data/'+filename, 'r') as f:
        reader = f.readlines()

        # remove the \n from each element
        i = 0
        while i < len(reader):
            reader[i] = reader[i].rstrip('\n')
            i += 1
        return reader


# comapre the exam list with the answers
def compare(answers,exam):
    i = 0
    q = 0
    good = 0
    bad = 0
    badlist = [ ]
    
    for i in range(20):
        if answers[i] == exam[i]:
            good += 1
        else:
            bad += 1
            q = i + 1             # get the question number
            badlist.append(q)
        i += 1

    result = [good , bad]
        
    return result,badlist


main()
