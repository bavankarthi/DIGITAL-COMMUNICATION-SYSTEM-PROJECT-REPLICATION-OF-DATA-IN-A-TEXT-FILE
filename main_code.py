# open both files
f = open('second.txt', 'r+')
f.truncate(0)
with open('first.txt','r') as firstfile,open('second.txt','a') as secondfile:

    #secondfile.close() #to change file access modes
    
    # read content from first file	
    for line in firstfile:
        
        # append content to second file
        secondfile.write(line)
	
