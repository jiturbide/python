class Text:

    def __init__(self,
                 text_or_file):
        """Method Constructor
        Parameters:
            text_or_file (str): Extract the text to be processed from a string or text file
        Returns:
            None

        """
        self.text = {}
        if text_or_file.find(".txt") > 0:
            text_file = open(text_or_file)
            lines = text_file.readlines()
        else:
            lines = text_or_file.split("\n")
        i = 1
        for line in lines:
            self.text[i] = line
            i += 1


    def find_words(self,
                   words):
        """Method to find the words in the lines of the text given

        Parameters:
            words (str): the word or words to be found in the text

        Returns:
            result (str): the lines of text where the word or words have been found
        """
        lines_to_show = []
        words_set = []
        words_set = words.split(",")
        result = ""
        for i in self.text:
            for j in words_set:
                word_to_find = j
                word_to_find_lower = j.lower()
                word_to_find_upper = j.upper()
                if self.text[i].find(word_to_find) >= 0 or \
                    self.text[i].find(word_to_find_lower) >= 0 or \
                        self.text[i].find(word_to_find_upper) >= 0:
                    lines_to_show.append(i)
        for k in lines_to_show:
            result += "Line " + str(k) + ": " + self.text[k] + "\n"

        return result

if __name__ == "__main__":
   print((999/1000))

   text = "In computer science, big O notation is used to classify algorithms according to how their run time or space requirements grow as the input size grows.\n"
   text += "In analytic number theory, big O notation is often used to express a bound on the difference between an arithmetical function and\n"
   text += "a better understood approximation; a famous example of such a difference is the remainder term in the prime number theorem.\n"
   text += "Big O notation is also used in many other fields to provide similar estimates"

   example = Text(text).find_words("")

   print('Output:', example)

