DESCRIPTION:
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !


def pig_it(text):
    pigged_words = []
    for word in text.split():
        pigged_words.append(word if word in ',.!?:' else word[1:] + word[0] + 'ay')
            
    pigged_text = ' '.join(pigged_words)
    
    
    return pigged_text    

