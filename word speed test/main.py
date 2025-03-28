import time

def typing_speed_test():
    print("Typing Speed Test")
    test_sentence = "This is a python test."
    print(f"\nType the following sentence:\n{test_sentence}\n")

    input("Press Enter to start...")
    start_time = time.time()

    user_input = input("\nStart typing: ")
    elapsed_time = time.time() - start_time

    if user_input == test_sentence:
        print("\nGreat job! You typed the sentence correctly.")
    else:
        print("\nYou made some mistakes in typing the sentence.")

    speed = len(test_sentence.split()) / (elapsed_time / 60)
    print(f"\nTyping Speed: {speed:.2f} WPM")
    print(f"Time Taken: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    typing_speed_test()