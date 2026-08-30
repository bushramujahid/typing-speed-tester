import time # time module is used for time-related functions
import random #random module is used for generating random numbers

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "A journey of a thousand miles begins with a single step.",
    "To be or not to be, that is the question.",
]

def measure_accuracy(user_input, test_sentence):
    correct_chars = sum(1 for a, b in zip(user_input, test_sentence) if a == b)
    accuracy = (correct_chars / len(test_sentence)) * 100 if test_sentence else 0
    return accuracy
    

    

def typing_test():
    test_sentence = random.choice(sentences) # randomly select a sentence from the list
    print("Type the following sentence as fast as you can:")
    print(test_sentence)
    input("Press Enter when you're ready...")
    start_time = time.time() # record the start time
    user_input = input("\nstart typing:\n") # get user input
    end_time = time.time() # record the end time
    time_taken = end_time - start_time # calculate the time taken
    word_count = len(test_sentence.split(" ")) # count the number of words in the sentence

    print("results:")
    print(f"Time taken: {time_taken} seconds")
    print(f"Words typed: {word_count}")
    print(f"Typing speed: {word_count / (time_taken/60):.2f} words per minute")
    print(f"Accuracy: {measure_accuracy(user_input, test_sentence):.2f}%")

typing_test()

