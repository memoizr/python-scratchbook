class Anagram:
    def are_anagrams(self, reference, comparable):
        reference_list = list(reference)
        comparable_list = list(comparable)

        anagrams = True
        for ref_char in reference_list:
            ref_match = 0
            for comp_char in comparable_list:
                if ref_char == comp_char:
                    ref_match = ref_match + 1

            if ref_match == 0:
                anagrams = False

        return anagrams

    def are_anagrams2(self, reference, comparable):
        comparable_list = list(comparable)
        i = 0
        anagram = True

        while i < len(reference) and anagram:
            j = 0
            found = False
            while j < len(comparable_list) and not found:
                if reference[i] == comparable_list[j]:
                    found = True
                else:
                    j = j + 1
            if found:
                comparable_list[j] = None
            else:
                anagram = False

            i = i + 1

        return anagram

    def are_anagrams3(self, reference, comparable):
        dict_one = {}
        dict_two = {}

        for i in reference:
            if dict_one.get(i) != None:
                dict_one[i] = dict_one[i] + 1
            else:
                dict_one[i] = 1

        for i in comparable:
            if dict_two.get(i) != None:
                dict_two[i] = dict_two[i] + 1
            else:
                dict_two[i] = 1

        print dict_one,  dict_two
        return dict_one ==  dict_two


#match = Anagram.are_anagrams(Anagram(),"abcd", "dcba")
#match = Anagram.are_anagrams2(Anagram(),"boon", "noob")
match = Anagram.are_anagrams3(Anagram(),"asdfgll", "lfgasdl")

print match




