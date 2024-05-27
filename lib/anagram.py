# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()  
    def match(self, possible_anagrams):
        correct_anagrams = []

        for candidate in possible_anagrams:
            candidate_lower = candidate.lower()

            if candidate_lower != self.word:
                if sorted(list(candidate_lower)) == sorted(list(self.word)):
                    correct_anagrams.append(candidate)

        return correct_anagrams

# Example
if __name__ == "__main__":
    listen = Anagram("listen")
    possible_anagrams = ['enlists', 'google', 'inlets', 'banana']
    result = listen.match(possible_anagrams)
    print(result)  # Output: ['inlets']
