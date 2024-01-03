
content_list = [] #creating a empty list to store the data 

def display_content(): #function to display content
    print(content_list) #printing the content_list

def count_word(paragraph): #function to Count words #passing 'paragraph' to the function
    word_count = len(paragraph.split()) #spliting 'paragraph' into list and finding the length
    print(f"\nThe number of words in text:- {word_count}") #printing the result
    
def count_sentence(paragraph): #function to Count sentence
    word_count = len(paragraph.split('.')) #spliting 'paragraph' into list with '.' to separate sentence's and finding the length 
    print(f"\nThe number of sentence in text:- {word_count}") #printing the result
    
def specific_word_count(): #function to Count the repeated words
    user_input_2 = str(input("Enter a specific word:- ")) #taking user input (a specific word)
    for i in content_list: #iterate each data from 'content_list' to 'i'
        specific = i.split().count(user_input_2) #spliting 'i' into list and counting the user input from it
    print(f"\nThe word '{user_input_2}' repeated {specific} times.") #printing result

def main(): #creating main function (starting point of execution)
    while True: #for repeating the below functions.
        print("\n\t===== FILE HANDLING =====") 
        filename = input("\nEnter the name of the file: ") #taking file as a input from user
        with open(filename, '+r') as file: #opening the file and giving permission to 'read'
            paragraph = file.read() #reads and stores the file content into 'paragraph'
            content_list.append(paragraph.lower()) #convering 'paragraph'  contents into lower case and appending the data to the list named 'content_list'


        print("\n1. Display the content \n2. Count Words\n3. Count Sentences \n4. Specific Word Count \n0. Exit") #displaying the choice
        user_input = int(input("\nEnter Any Choice: ")) #taking user input as intiger (like 1,2,3,4,0)

        if user_input == 1: #if the user input is 1 'display_content()' function will work'
            display_content()
        elif user_input == 2: #if the user input is 2 'count_word()' function will work'
            count_word(paragraph) #passing 'paragraph to the function'
        elif user_input == 3: #if the user input is 3 'count_sentence()' function will work'
            count_sentence(paragraph) #passing 'paragraph to the function'
        elif user_input == 4: #if the user input is 4 'repeated_word_count()' function will work'
            specific_word_count()       

        elif user_input == 0: #if the user input is 0 then the program will break
            break
        
        else: #else print the below prompt
            print("Enter the given choices.")

if __name__ == '__main__': #checks if the script is being run as the main program
    main()
