from matplotlib import pyplot as plt
import string

"""
This is a comment.
Example of filename:
filename = "./texts/anne_frank_diary.txt"
filename = "./texts/adventure_of_tom_sawyer.txt"
filename = "./texts/alice_in_wonderland.txt"
filename = "./texts/crime_and_punishment.txt"
filename = "./texts/jane_eyre.txt"
filename = "./texts/pride_and_prejudice.txt"
filename = "./texts/sense_and_sensibility.txt"
"""

filename = "./texts/pride_and_prejudice.txt" # can modify

character_list = {}
for i in range(26):
    character_list[string.ascii_uppercase[i]] = 0

with open(filename, "r", encoding="utf-8") as file:
    file_read = file.readlines()
    for i in file_read:
        i = i.strip().upper()
        character_list["A"] += i.count("A")
        character_list["B"] += i.count("B")
        character_list["C"] += i.count("C")
        character_list["D"] += i.count("D")
        character_list["E"] += i.count("E")
        character_list["F"] += i.count("F")
        character_list["G"] += i.count("G")
        character_list["H"] += i.count("H")
        character_list["I"] += i.count("I")
        character_list["J"] += i.count("J")
        character_list["K"] += i.count("K")
        character_list["L"] += i.count("L")
        character_list["M"] += i.count("M")
        character_list["N"] += i.count("N")
        character_list["O"] += i.count("O")
        character_list["P"] += i.count("P")
        character_list["Q"] += i.count("Q")
        character_list["R"] += i.count("R")
        character_list["S"] += i.count("S")
        character_list["T"] += i.count("T")
        character_list["U"] += i.count("U")
        character_list["V"] += i.count("V")
        character_list["W"] += i.count("W")
        character_list["X"] += i.count("X")
        character_list["Y"] += i.count("Y")
        character_list["Z"] += i.count("Z")


if __name__ == "__main__":
    plt.bar(character_list.keys(), character_list.values())

    plt.title(f"Character frequency in {filename[8:]}")
    plt.xlabel("List of characters")
    plt.ylabel("Occurrence")

    for index, value in enumerate(character_list.values()):
        plt.text(index - 0.55, value, str(value))

    plt.show()
