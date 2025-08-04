import random

print("QUIZ APP".center(100))

points = 0

def templet(question, correctAnswer, options, count):
    print(f"\n\n\nQUES: {count} {question} \t Points : {10**count}\n")

    random.shuffle(options)

    for i in range(4):
        print(f"{i+1} : {options[i]}")

    ans = int(input("\n\nEnter Your Choice : "))

    if(options[ans-1] == correctAnswer):
        print("Correct")
        return True
    else:
        print("Wrong")
        return False
    

if __name__ == "__main__":

    questions = {
        "Which planet is known as the Red Planet?" : ["Mars", "Earth", "Jupiter", "Saturn"],
        "What is the square root of 144?" : ["12", "14", "10", "16"],
        "Who was the first Prime Minister of India?" : ["Jawaharlal Nehru", "Mahatma Gandhi", "Subhas Chandra Bose", "Sardar Patel"],
        "Which gas do plants absorb from the atmosphere?" : ["Carbon Dioxide", "Oxygen", "Nitrogen", "Helium"],
        "What is the chemical symbol for Gold?" : ["Au", "Ag", "Gd", "Go"],
        "Which organ is responsible for pumping blood?" : ["Heart", "Lungs", "Kidney", "Liver"],
        "What is the capital of Australia?" : ["Canberra", "Sydney", "Melbourne", "Perth"],
        "Who invented the telephone?" : ["Alexander Graham Bell", "Thomas Edison", "Nikola Tesla", "Isaac Newton"],
        "Which is the largest continent?" : ["Asia", "Africa", "Europe", "North America"],
        "Which is the hardest natural substance?" : ["Diamond", "Gold", "Iron", "Quartz"],
        "In which year did India gain independence?" : ["1947", "1950", "1945", "1942"],
        "What is the boiling point of water in Celsius?" : ["100", "90", "80", "120"],
        "Who painted the Mona Lisa?" : ["Leonardo da Vinci", "Vincent Van Gogh", "Pablo Picasso", "Michelangelo"],
        "Which Indian cricketer is known as the 'Master Blaster'?" : ["Sachin Tendulkar", "Virat Kohli", "M.S. Dhoni", "Kapil Dev"],
        "Which element has the atomic number 1?" : ["Hydrogen", "Oxygen", "Helium", "Carbon"],
        "Which country is known for the Great Wall?" : ["China", "Japan", "India", "Egypt"],
        "Which blood group is a universal donor?" : ["O Negative", "O Positive", "AB Positive", "A Negative"],
        "Who discovered gravity?" : ["Isaac Newton", "Albert Einstein", "Galileo", "Stephen Hawking"],
        "Which bird is the fastest in the world?" : ["Peregrine Falcon", "Eagle", "Ostrich", "Hawk"],
        "Which Indian festival is known as the Festival of Lights?" : ["Diwali", "Holi", "Eid", "Navratri"],
        "What is the main ingredient in bread?" : ["Flour", "Rice", "Corn", "Sugar"],
        "What does CPU stand for?" : ["Central Processing Unit", "Central Program Unit", "Computer Processing Unit", "Central Print Unit"],
        "Who is the author of 'Harry Potter'?" : ["J.K. Rowling", "Stephen King", "J.R.R. Tolkien", "Agatha Christie"],
        "Which metal is liquid at room temperature?" : ["Mercury", "Lead", "Zinc", "Aluminum"],
        "Which ocean is the largest?" : ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"],
        "How many players are there in a football (soccer) team?" : ["11", "10", "9", "12"],
        "Which Indian city is known as the Pink City?" : ["Jaipur", "Udaipur", "Jodhpur", "Delhi"],
        "Which is the smallest prime number?" : ["2", "1", "3", "5"],
        "Who is known as the Missile Man of India?" : ["Dr. A.P.J. Abdul Kalam", "Homi Bhabha", "Vikram Sarabhai", "C.V. Raman"],
        "What is the currency of Japan?" : ["Yen", "Won", "Dollar", "Ruble"]
    }


    count = 1
    
    questions = list(questions.items())
    random.shuffle(questions)
    questions = dict(questions)
    
    for question in questions:
        answer = questions[question][0]
        options = questions[question]

        result = templet(question, answer, options, count)

        if(result == False):
            print(f"Correct Answer is: {answer}") 
            break
        
        if(count == 10):
            print("\nWell Done!, You answered all questions correctly")
            break

        points = 10**count
        print("\nCurrent Score: ", points)

        count += 1

    print(f"\n\nYour Final Score: {points}".center(100))