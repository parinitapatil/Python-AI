from datetime import datetime
import random
# Perfect. A **personal chat assistant** is actually a better learning project than an expense tracker because it introduces concepts you'll use in AI applications.

# But let's build it the way a software engineer thinks—not by jumping into code.

# ---

# # Step 0: Don't think about Python.

# Imagine you're explaining your assistant to a friend.

# Ask yourself:

# > **What should my assistant be able to do?**

# For Version 1, let's keep it simple.

# ```
# You: Hello
# Assistant: Hi!

# You: What is your name?
# Assistant: I'm your assistant.

# You: Time
# Assistant: Current time is ...

# You: Exit
# Assistant: Goodbye!
# ```

# Notice we haven't written a single line of code yet.

# We've only defined the **requirements**.

# ---

# # ✅Step 1: What happens first?

# When the program starts, what should happen?

# Maybe:

# ```
# Welcome to Personal Assistant!
# ```
print("Welcome to Personal Assistant!")
jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did the computer get cold? Because it left its Windows open!",
    "Why do Python programmers wear glasses? Because they can't C!"
]

# List of motivational quotes
quotes = [
    "Keep learning. Every expert was once a beginner.",
    "Consistency beats motivation.",
    "Small progress every day leads to big results.",
    "Practice is what turns knowledge into skill."
]

print("=" * 40)
print("🤖 Welcome to Your Personal Chat Assistant!")
print("Type 'help' to see available commands.")
print("Type 'exit' to quit.")
print("=" * 40)
# Then...

# Should it stop immediately?

# No.

# It should keep talking.

# So ask yourself:

# > Which Python concept repeats something until we decide to stop?

# Answer:

# ```python
# while
# ```

# Notice how the problem led us to the solution.

# ---

# # Step 2: Inside the loop
while True:
    
    # Get user input
    user = input("\nYou:").strip().lower()
    
    #Exit
    if user == 'exit' or user == 'bye' or user == 'stop' or user == 'quit':
        print("Assistant: Goodbye! Have a great day!")
        break
    
    #conditions
    elif user == 'hello' or user == 'hi':
        print("Assistant: Hi! How can I assist you today?")
    
    # time
    elif user == 'time':
        print(f"Assistant: Current Time is {datetime.now().strftime('%H:%M:%S')}")
        
    # Date
    elif user == 'date':
        print(f"Assistant: Today's Date is {datetime.now().strftime('%d-%m-%Y')}")
    
    # Joke
    elif user == 'joke':
        print(f"Assistant: {random.choice(jokes)}")
    
    # Motivational Quote
    elif user == 'quote':
        print(f"Assistant: {random.choice(quotes)}")
    
    # Calculator
    elif user.startswith('calculate'):
        try:
            expression = user.replace('calculate', '').strip()
            result = eval(expression)
            print(f"Assistant: The result of '{expression}' is {result}")   
        except Exception as e:
            print(f"Assistant: Sorry, I couldn't calculate that. Please check your expression.")        
            
    # Help
    elif user == 'help':
        print("Assistant: Here are the commands you can use:")
        print("  - hello / hi : Greet the assistant")
        print("  - time : Get current time")
        print("  - date : Get today's date")
        print("  - joke : Hear a joke")
        print("  - quote : Get a motivational quote")
        print("  - calculate <expression> : Perform a calculation (e.g., calculate 2 + 2)")
        print("  - exit / bye / stop / quit : Exit the assistant")
    else:
        print("Assistant: Sorry, I don't understand that. Type 'help' to see available commands.")
        
    
    
# Every conversation follows the same pattern.

# ```
# User types something

# ↓

# Assistant understands it

# ↓

# Assistant replies

# ↓

# Wait for next message
# ```

# So inside the loop we need:

# ```
# Get input

# ↓

# Check what user typed

# ↓

# Respond
# ```

# ---

# # Step 3: How do we get the user's message?

# Think like a human.

# The assistant has to **listen**.

# In Python, "listening" means:

# ```python
# input()
# ```

# Now we have the user's message.

# Example:

# ```
# You: hello
# ```

# ---

# # Step 4: How does the assistant decide what to say?

# Imagine you're the assistant.

# If someone says:

# ```
# hello
# ```

# You reply:

# ```
# Hi!
# ```

# If someone says:

# ```
# time
# ```

# You show the time.

# If someone says:

# ```
# bye
# ```

# You exit.

# That's simply **decision making**.

# Which Python concept makes decisions?

# ```
# if
# elif
# else
# ```

# ---

# # Step 5: What if the user types something unknown?

# Example:

# ```
# What's your favorite movie?
# ```

# Our assistant doesn't know.

# So we need a default response.

# ```
# Sorry, I don't understand.
# ```

# This becomes the `else` case.

# ---

# # Step 6: When should the loop stop?

# If the user types:

# ```
# exit
# ```

# or

# ```
# bye
# ```

# The assistant should stop.

# Which keyword stops a loop?

# ```
# break
# ```

# ---

# # At this point, our program's logic looks like this:

# ```
# Start

# ↓

# Print Welcome

# ↓

# Loop forever

# ↓

# Get user input

# ↓

# Is it "hello"?

# ↓

# Yes → Reply

# ↓

# No

# ↓

# Is it "time"?

# ↓

# Yes → Reply

# ↓

# No

# ↓

# Is it "exit"?

# ↓

# Yes → break

# ↓

# No

# ↓

# Default reply

# ↓

# Repeat
# ```

# This is called an **algorithm**.

# Notice we still haven't worried about syntax.

# ---

# # Version 1 Features

# We'll implement these one by one:

# * ✅ Greeting
# * ✅ Name
# * ✅ Current time
# * ✅ Current date
# * ✅ Basic calculator
# * ✅ Tell a joke
# * ✅ Random motivational quote
# * ✅ Exit

# Later we'll add:

# * Memory
# * Notes
# * To-do list
# * Weather
# * AI responses
# * Voice input
# * Voice output

# ---

# # Before writing code, answer this

# **Question 1:**

# Your assistant needs to keep chatting until the user decides to exit.

# Which Python structure would you choose?

# A. `for` loop

# B. `while` loop

# C. `if` statement

# Don't guess—tell me **why** you chose it. That's how you'll build the reasoning skill that makes projects much easier.
