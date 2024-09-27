import random
import pyautogui as pgui
import time
import os

from error_list import error_letters

# Function to dynamically calculate error_rate, pause_rate, and char_pause based on speed
def calculate_typing_parameters(speed: str):
    if speed == "slow":
        char_pause = (0.3, 0.5)  # Slow typing speed
        error_rate = 0.1         # Lower chance of error
        pause_rate = 10          # More frequent pauses
    elif speed == "fast":
        char_pause = (0.01, 0.1)  # Fast typing speed
        error_rate = 0.1         # Fewer mistakes
        pause_rate = 3            # Less frequent pauses
    else:  # Default is "medium"
        char_pause = (0.1, 0.3)  # Medium typing speed
        error_rate = 0.2         # Normal error chance
        pause_rate = 5           # Medium pauses
    return char_pause, error_rate, pause_rate

def get_paragraph_from_file(file_path: str):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return file.read().strip()
    return "Hello! This is the default paragraph."  

def main(file_path: str = '', speed: str = 'medium'):
    # Get the paragraph either from the file or use default text
    paragraph = get_paragraph_from_file(file_path)
    
    # Get typing parameters based on speed
    char_pause, error_rate, pause_rate = calculate_typing_parameters(speed)
    
    char_list = list(paragraph)
    i = 0
    while i < len(char_list):
        char = char_list[i]
        
        # Random pause to simulate human pause
        if random.randint(0, 100) < pause_rate:
            time.sleep(random.uniform(0.5, 2))  # Simulate a longer pause
        
        # Simulate typing a wrong character occasionally
        if random.random() < error_rate and char.lower() in error_letters:
            wrong_char = random.choice(error_letters[char.lower()])
            pgui.write(wrong_char)
            time.sleep(random.uniform(*char_pause))  # Simulate human typing speed
            pgui.press('backspace')  # Correct the error
            time.sleep(0.1)  # Slight pause for backspacing
        
        # Type the correct character
        pgui.write(char)
        time.sleep(random.uniform(*char_pause))  # Simulate human typing speed
        
        i += 1

if __name__ == '__main__':
    time.sleep(5)  # Wait for 5 seconds before starting, for user to naviagte to the typing area
    main(file_path='paragraph.txt', speed='fast')
