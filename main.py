from Mini_Project_Library import Library, permit, commands

Abhinav_library_books = ["Programming Hero", "CR7", "Let us python", "Let us C", "Let us Java", "First head Python",
                         "AIML", "OOPs", "Harry potter", "Discord API", "Core Microprocessor", "Joy to hack",
                         "Penetration Tester", "Alok Feels", "Ghost Story", "Fence Room mate", "Game Champs",
                         "Sports",
                         "Auto-Bio Graphi"]
Abhinav_library = Library(Abhinav_library_books, "Abhinav's Library")
Abhinav_library.log_file()

while True:
    print(f"\n\n\nWelcome to the library name 'Abhinav'\nYou can Lead the book and also Donate the books here\n\n")
    name = input("Please Enter your Name : \t")
    if name == "Abhinav":
        permit(Abhinav_library)
    else:
        commands("Abhinav", Abhinav_library, name)
