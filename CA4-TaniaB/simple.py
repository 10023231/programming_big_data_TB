
# open the file - and read all of the lines.
changes_file = 'changes_python.log'
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
    'class for commits'
   
    def __init__(self, revision = None, author = None, date = None, comment_line_count = None, changes = None, comment = None):
        self.revision = revision
        self.author = author
        self.date = date
        self.comment_line_count = comment_line_count
        self.changes = changes
        self.comment = comment

    def get_commit_comment(self):
        return 'svn merge -r' + str(self.revision-1) + ':' + str(self.revision) + ' by ' \
                + self.author + ' with the comment ' + ','.join(self.comment) \
                + ' and the changes ' + ','.join(self.changes)

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
        current_commit.comment = data[index-current_commit.comment_line_count:index]
        commits.append(current_commit)
    except IndexError:
        break

print(len(commits))

commits.reverse()

for index, commit in enumerate(commits):
    print(commit.get_commit_comment())

#####################################################
def read_file(changes_file):
    # use strip to strip out spaces and trim the line.
    data = [line.strip() for line in open(changes_file, 'r')]
    return data

def get_commits(data):
    sep = 72*'-'
    commits = []
    current_commit = None
    index = 0
    while index < len(data):
        try:
            # parse each of the commits and put them into a list of commits
            details = data[index + 1].split('|')
            # the author with spaces at end removed.
            commit = {'revision': details[0].strip(),
                'author': details[1].strip(),
                'date': details[2].strip(),
                'number_of_lines': details[3].strip().split(' ')[1]
            }
            # add details to the list of commits.
            commits.append(commit)
            index = data.index(sep, index + 1)
        except IndexError:
            break
    return commits

date_view = []
author_view = []
day_view = []	
name_check = 0
if __name__ == '__main__':
    # open the file - and read all of the lines.
    changes_file = 'changes_python.log'
    data = read_file(changes_file)
    commits = get_commits(data)
	date_view = get_date(commits)
	author_view = get_authors(commits)
	day_view = get_days(commits)

    # print the number of lines read
    print(len(data))
    #print(commits)
    print(commits[0])
    print(commits[1]['author'])
    print(len(commits))
	
	#analysis of dates
	print (date_view[0])
	print (date_view[-1])
	
	#viewing the author names
	print (author_view[0])
	#finding total commits by names
	name_check = get_names(get_authors)
	
	#viewing days
	print (day_view)
	
	#trying to create csv file...hope will work, this time
	import csv
	
	day = [day.split(' ',1)[0] for day in date_view]
	
	with open('days.csv','wb'0 as my_result_file:
		writer = csv.writer(my_result_file, distinct=' ')
		writer.writerows(day)
		
	with open('all_days.csv','wb') as my_result_file:
		writer = csv.writer(my_result_file, distinct=' ')
		writer.writerows(day_view)
	
	my_result_file.close()
	
	
	
	
	#will continue....	
	#ex:import csv
 
#ifile  = open('test.csv', "rb")
#reader = csv.reader(ifile)
#ofile  = open('ttest.csv', "wb")
#writer = csv.writer(ofile, delimiter='', quotechar='"', quoting=csv.QUOTE_ALL)
 
#for row in reader:
#    writer.writerow(row)
 
#ifile.close()
#ofile.close()