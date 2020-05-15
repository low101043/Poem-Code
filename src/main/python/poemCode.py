import random
import math

def main():
    print("This is the UI")
    print("THIS DOES NOT WORK")
    print(encrypt("Hello my name is nat meet at nine oclock"))


def transpositonEncrypt(input, numbers):

    input_no_spaces = input.replace(" ", "")
    length_of_numbers = len(numbers)
    

    length_of_input = len(input_no_spaces)


    if (length_of_input % length_of_numbers == 0):
        number_of_columns = (length_of_input // length_of_numbers)
    else:
        number_of_columns = (length_of_input // length_of_numbers)  + 1

    output = []
    for i in range(number_of_columns):
        row = []
        for j in range(length_of_numbers):

            index_for_letter = (i * length_of_numbers) + j

            if (index_for_letter < length_of_input):
           
                letter = input_no_spaces[index_for_letter]
            else:
                random_number = random.randint(0,25)

                letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

                letter = letters[random_number]


            row.append(letter)

        output.append(row)

    finalOutput = ""
    for number in numbers:
        index = int(number) -1
    
        for row in output:
            finalOutput += row[index]

    return finalOutput

def transpositonDecrypt(input, numbers):
    
    input_no_space = input.replace(" ", "")
    input_length = len(input_no_space)
    numbers_length = len(numbers)

    if (input_length % numbers_length == 0):
        number_of_columns = (input_length // numbers_length)
    else:
        number_of_columns = (input_length // numbers_length)  + 1


    output = []
    final_output = []

    for i in range((input_length // number_of_columns)):
        row = []
        for j in range(number_of_columns):
            
            index = (i * number_of_columns) + j

            letter = input_no_space[index]
            row.append(letter)
        output.append(row)
        final_output.append(None)


    
    for i in range(len(output)):
        number = numbers[i]
        index = int(number) -1
    
        row = output[i]
        final_output[index] = row

        

    string_output = ""
    for i in range(number_of_columns):
        for row in final_output:
            letter_to_remove = row[i]
            string_output += letter_to_remove
    
    return string_output

def keyGeneration(poem_string):
    output = ""
    letters_to_append = ""
    poem = poem_string.split(" ")

    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    
    for i in range(5):
        place_in_list = random.randint(0, len(poem) - 1)
        word = poem[place_in_list]
        output = output + word
        
        letters_to_append += letters[place_in_list % 26]

    print(output)

    
    #print(output_array)
    
    output_array = convertToNumbers(output)
    
    #print(output_array, letters_to_append)
    return letters_to_append, output_array

def convertToNumbers(output):
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    index = 1
    output_array = list(output)
    for letter in letters:
        if output.find(letter) == output.rfind(letter) and output.find != -1:
            output_array[output.find(letter)] = index
            index += 1
        elif (output.find(letter) != output.rfind(letter)):
            for i in range(len(output)):
                if output_array[i] == letter:
                    output_array[i] = index
                    index += 1

    return output_array
def keyMaker(letters_at_start, poem):
   
    possible_outputs = [[],[],[],[],[]]
    index_list = []
    
    for letter in letters_at_start:
        letter_to_index = {"a": 0, "b":1, "c": 2, "d":3, "e":4, "f": 5, "g":6, "h":7, "i":8, "j":9, "k":10, "l":11, "m":12, "n": 13, "o":14, "p":15, "q":16, "r":17, "s":18, "t":19, "u":20, "v":21, "w":22, "x":23, "y":24, "z":25}
        index = letter_to_index[letter]
        index_list.append(index)
        
    poem_list = poem.split(" ")

    length_of_poem = len(poem_list)

    i = 0
    while (i < length_of_poem):
        
        if (i + index_list[0] < length_of_poem):
            possible_outputs[0].append(poem_list[i +index_list[0]])

        if (i + index_list[1] < length_of_poem):
            possible_outputs[1].append(poem_list[i +index_list[1]])

        if (i + index_list[2] < length_of_poem):
            possible_outputs[2].append(poem_list[i +index_list[2]])

        if (i + index_list[3] < length_of_poem):
            possible_outputs[3].append(poem_list[i +index_list[3]])

        if (i + index_list[4] < length_of_poem):
            possible_outputs[4].append(poem_list[i +index_list[4]])
        i = i + 26

    #print(possible_outputs)

    max = 0
    for row in possible_outputs:
        if (len(row)> max):
            max = len(row)

    if (len(possible_outputs[0]) < max):
        possible_outputs[0].append(None)

    if (len(possible_outputs[1]) < max):
        possible_outputs[1].append(None)

    if (len(possible_outputs[2]) < max):
        possible_outputs[2].append(None)

    if (len(possible_outputs[3]) < max):
        possible_outputs[3].append(None)

    if (len(possible_outputs[4]) < max):
        possible_outputs[4].append(None)
    

  #  print(possible_outputs)

    final_output_array = []

    i = 0
    j = 0
    k = 0
    l = 0
    p = 0
    for c in range (max**5):
        data = []
        data.append(possible_outputs[0][i])
        data.append(possible_outputs[1][j])
        data.append(possible_outputs[2][k])
        data.append(possible_outputs[3][l])
        data.append(possible_outputs[4][p])
        final_output_array.append(data)
        
        p += 1
        if (p >= max):
            l += 1
            p = 0

            if (l >= max):
                k += 1
                l = 0
                p = 0

                if (k >= max):
                    j += 1
                    k = 0
                    l = 0
                    p = 0

                    if (j >= max):
                        i += 1
                        j = 0
                        k = 0
                        l = 0
                        p = 0


#    print(final_output_array)  ##HAS ALL POSSIBLE SOLUTIONS  REMOVE ALL WITH NONE IN IT

 #   print("\n\n")

    places_to_remove = []

    for i in range(len(final_output_array)):
        row = final_output_array[i]

        if None in row:
            places_to_remove.append(i)

   
    
    for place in range(len(places_to_remove)):

        index = places_to_remove[len(places_to_remove) - 1- place]
        final_output_array.pop(index)

    #print(final_output_array)


    final_output_strings = []
    output_numbers = []
    for row in final_output_array:
        output = ""
        for word in row:
            output += word 
        output_number = convertToNumbers(output)
        output_numbers.append(output_number)

    return output_numbers

def encrypt(input):
    
    poem = "the Beginning of the good news about jesus the messiah the son of god as it is written in isaiah the prophet i will"
    poem = poem.lower()
    input = input.lower()

    identifiers, key = keyGeneration(poem)

    print(identifiers, key)
    transposed_once = transpositonEncrypt(input, key)
    transposed_twice = transpositonEncrypt(transposed_once, key)

    final_output = identifiers + transposed_twice

    return final_output


def decryt(input):
    pass


main()
