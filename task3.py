from collections import Counter
'''
You are given a list of sentences. Create a word tree from each sentence and find how many times the word is appeared in other word trees.
 Input:
sentences = [“My name is Ram”, “”He is a good person”, “You should be careful while coding”, “He can do better”, “The person is mysterious”, “Jay Shree Ram”, “It is my pen.”]
 Output:
word_trees = [[“My”, “name”, “is”, “Ram”], [“He”, “is”, “a”, “good”, “person”], [“You”, “should”, “be”, “careful”, “while”, “coding”], [“He”, “can”, “do”, “better”], [“The”, “person”, “is”, “mysterious”], [“Jay”, “Shree”, “Ram”], [“It”, “is”, “my”, “pen”]]
Number of time each word appears:
{“My”: 1, “name”: 1, “is”: 4, “Ram”: 2, “He”: 2, “good”: 1, “person”: 2, “You”: 1 ......} Likewise all word should be covered.'''


sentences = ["My name is Ram", "He is a good person", "You should be careful while coding", "He can do better", "The person is mysterious", "Jay Shree Ram", "It is my pen."]

#word_trees
word_trees = []
for i in sentences:
    word_trees.append(i.split())
print("word_trees =",word_trees)

#Number of time each word appears:
word_tree = []
split_sentence=[words for list_tree in sentences for words in list_tree.split()]
counts = Counter(split_sentence)
print("Number of time each word appears:",dict(counts))