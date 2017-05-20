import csv
# open the file - and read all of the lines.
changes_file = 'changes_python.log.txt'
# use strip to strip out spaces and trim the line.

my_file = open(changes_file, 'r')
data = my_file.readlines()

data = [line.strip() for line in open(changes_file, 'r')]

# print the number of lines read
print(len(data))

sep = 72*'-'

# create the commit class to hold each of the elements - I am hoping there will be 422
# otherwise I have messed up.
class Commit:
    "'class for commits'"
   
    def __init__(self, revision = None, author = None, date = None, comment_line_count = None, changes = None, comment = None):
        self.revision = revision
        self.author = author
        self.date = date
        self.comment_line_count = comment_line_count
        self.changes = changes
        self.comment = comment
       
       
    def get_commit_comment(self):
        return self.revision,self.author,self.date,self.comment_line_count
        #return  self.revision + "-" + self.author + "-" + self.date + "-"  + self.comment_line_count
		
		#'svn merge -r' + str(self.revision-1) + ':' + str(self.revision) + ' by ' \
         #       + self.author + ' with the comment ' + ','.join(self.comment) \
          #      + ' and the changes ' + ','.join(self.changes), self.year

commits = []
current_commit = None
index = 0

author = {}
while True:
    try:
       
        # parse each of the commits and put them into a list of commits
        current_commit = Commit()
        details = data[index + 1].split('|')
        current_commit.revision = int(details[0].strip().strip('r'))
        
        current_commit.author = details[1].strip()
        current_commit.date = details[2].strip()
        
        current_commit.comment_line_count = int(details[3].strip().split(' ')[0])
        current_commit.changes = data[index+2:data.index('',index+1)]
        #print(current_commit.changes)
        index = data.index(sep, index + 1)
        #current_commit.comment = data[index-current_commit.comment_line_count:index]
        commits.append(current_commit)
        
    except IndexError:
        break


#csv list 
my_listCsv = [] 
for index, commit in enumerate(commits):
	sublist = []
	sublist.append(commit.get_commit_comment())
	my_listCsv.append(sublist)

with open("My_Result.csv", 'wb') as csvfile:
	spamwriter = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
	spamwriter.writerow([])
	for i in my_listCsv:
		spamwriter.writerow(i) 

print "My_Result.csv was created!"






#writer.writerow(['Revision ', 'Authors ', 'Date ', 'number_of_lines '])
#index = 0	

#for commit in commits:
#	out.write(commits[index]['revision'])#
#	out.write(';')
#	print(commits[index]['revision'])
#	out.write(commits[index]['author'])
#	out.write(';')
#	print(commits[index]['author'])
#	out.write(commits[index]['date'])
#	out.write(';')
#	print(commits[index]['date'])
#	out.write(commits[index]['number_of_lines'])
#	out.write(';')
#	print(commits[index]['number_of_lines'])
#	out.write(str(commits[index]['comment']))
#	out.write(';')
#	out.write(str(commits[index]['changes']))
#	out.write('\n')
#	index = index +1
#out.close()	
