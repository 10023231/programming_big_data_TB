
import unittest

from simple import Commit

class TestCommits(unittest.TestCase):
        data = [line.strip() for line in open(changes_file, 'r')]
        sep = 72*'-'
    def setUp(self):
        self.data = read_file('changes_python.log.txt')
        changes_file = 'changes_python.log.txt'
        
    def test_number_of_lines(self):
        self.assertEqual(5255, len(self.data))

    def test_number_of_commits(self):
        commits = get_commits(self.data)
        self.assertEqual(422, len(commits))

    def test_first_commit(self):
        commits = get_commits(self.data)
        self.assertEqual('Vincent', commits[0]['author'])
        self.assertEqual('r155192', commits[0]['revision'])
        
    def test_last_commit(self):
        commits = get_commits(self.data)
        self.assertEqual('Vincent', commits[421]['author'])
        self.assertEqual('r155192', commits[421]['revision'])
        
        
if __name__ == '__main__':
    unittest.main()
