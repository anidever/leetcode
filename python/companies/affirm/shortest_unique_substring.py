# can be solved using Trie data structure
'''Given an input list of names, for each name, find the shortest substring that only appears in that name.

Example:

Input: ["cheapair", "cheapoair", "peloton", "pelican"]
Output:
"cheapair": "pa"  // every other 1-2 length substring overlaps with cheapoair
"cheapoair": "po" // "oa" would also be acceptable
"pelican": "ca"   // "li", "ic", or "an" would also be acceptable
"peloton": "t"    // this single letter doesn't occur in any other string'''

'''Given an input list of strings, for each letter appearing anywhere
in the list, find the other letter(s) that appear in the most
number of words with that letter.

Example:
['abc', 'bcd', 'cde'] =>
  {
	a: [b, c],	# b appears in 1 word with a, c appears in 1 word with a
	b: [c], 	# c appears in 2 words with b, a and d each appear in only 1 word with b
	c: [b, d], 	# b appears in 2 words with c, d appears in 2 words with c. But a and e each
					  appear in only 1 word with c.
	d: [c],		# c appears in 2 words with d. But b and e each appear in only 1 word with d
	e: [c, d], 	# c appears in 1 word with e, d appears in 1 word with e

  }
'''

"""
This problem can be solved in O(N*L*L*L) complexity. The approach will be using suffix tries. Each node of the trie will be also storing the prefix count which will refer to the number of times the substring formed while traversing to that node from the root have appeared in all of the suffixes inserted till now.

We will be constructing N+1 tries. The first trie will be global and we will be inserting all the suffixes of all N string into it. The next N tries will be local for each of the N strings containing corresponding suffixes.

This preprocessing step of constructing tries will be done in O(N*L*L).

Now once the tries have been constructed, for each string, we can start quering the number of times a substring ( starting from minimum length) has occured in the global trie and the trie corresponding to that string. If it is same in both then it implies that it is not included in any other strings except itself. This can be achieved in O(N*L*L*L). The complexity can be explained as N for each string, L*L for considering each substring and L for performing query in the trie.
"""

from collections import Counter, defaultdict
from typing import List

class Component:
    def __init__(self, s):
        self.graph = defaultdict(list)
        count = Counter(s)

        for c1 in count:
            for c2 in count:
                if c1 != c2:
                    self.graph[c1].append(c2)
                    self.graph[c2].append(c1)


    def containsMember(self, u):
        return u in self.graph

    def members(self):
        return self.graph.keys()

def find_most_frequent_string_members(words: List[str]) -> dict:
    result = {}
    components = []
    chars = set()

    for word in words:
        components.append(Component(word))
        for c in word:
            chars.add(c)

    for ch in chars:
        current = defaultdict(int)
        for component in components:
            if component.containsMember(ch):
                for member in component.members():
                    if member != ch:
                        current[member] += 1

        c_max = max(current.values())
        final = []
        for item in current:
            if current[item] == c_max:
                final.append(item)
        result[ch] = final

    return result


input = ['abc', 'bcd', 'cde']
# find_most_frequent_string_members(input)


class TrieNode:
  def __init__(self):
    self.children = {}
    self.word = None  # Stores the complete word if it's an end node

class TrieNode:
  def __init__(self):
    self.children = {}
    self.word = None  # Stores the complete word if it's an end node

def find_unique_substring(names):
  """
  This function finds the shortest unique substring for each name in a list.

  Args:
      names: A list of strings.

  Returns:
      A dictionary where keys are the names in the input list and values are the shortest unique substrings of the corresponding key string.
  """
  result = {}
  for name in names:
    shortest_unique = None
    for i in range(1, len(name) + 1):
      for j in range(len(name) - i + 1):
        substring = name[j:j+i]
        # Check if substring appears in any other name
        if all(substring not in n for n in names if n != name):
          if not shortest_unique or len(substring) < len(shortest_unique):
            shortest_unique = substring
          break  # Break inner loop if a unique substring is found
    result[name] = shortest_unique
  return result

# Example usage
names = ["cheapair", "cheapoair", "peloton", "pelican"]
unique_substrings = find_unique_substring(names)
print(unique_substrings)





