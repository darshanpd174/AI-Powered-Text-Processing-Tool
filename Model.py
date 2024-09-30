
from textblob import TextBlob

class SpellCheckerModule:
    def __init__(self):
        self.spell_check = TextBlob("")
        self.corrections = []

    def correct_spell(self, text):

        words = text.split()
        corrected_words = []
        mistakes_found = []

        for word in words:
            corrected_word = str(TextBlob(word).correct())
            if corrected_word != word:
                self.corrections.append(f"{word} -> {corrected_word}")
                mistakes_found.append(word)
            corrected_words.append(corrected_word)

        corrected_text = " ".join(corrected_words)
        mistakes_string = ", ".join(mistakes_found)
         

        return corrected_text, mistakes_string

if __name__ == "__main__":
    # Create an instance of SpellCheckerModule
    spell_checker = SpellCheckerModule()

    # Example message
    message = "Hello worlld. my nami is joseephh. i like mashne learning. appple. bananana"

    # Correct spellings and get corrections
    corrected_spellings, mistakes_found = spell_checker.correct_spell(message)
    
    print("Original Message:")
    print(message)
    print("\nCorrected Message:")
    print(corrected_spellings)
    
    print("\nMistakes Found and Corrected:")
    print(mistakes_found)
    
