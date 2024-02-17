from caesar import caesar
from colorama import Fore

# Your code goes here

print(Fore.YELLOW + """
                                                        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                                                        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                                                        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                                                        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                                                        ░░░░░░░░░░░░░░░░░░▒▓████████▓▒░░░░░░░░░░░░░░░░░░░░
                                                        ░░░░░░░░░░░░░░░░▓██▓▒▒▒▒▒▒▒▒▓██▓░░░░░░░░░░░░░░░░░░
                                                        ░░░░░░░░░░░░░░░▓██░░░░░░░░░░░░▓██░░░░░░░░░░░░░░░░░
                                                        ░░░░░░░░░░░░░░▒██▒░░░░░░░░░░░░░██▓░░░░░░░░░░░░░░░░
                                                        ░░░░░░░░░░░░░░▒██░░░░░░░░░░░░░░██▓░░░░░░░░░░░░░░░░
                                                        ░░░░░░░░░░░░░░▒██░░░░░░░░░░░░░░██▓░░░░░░░░░░░░░░░░
                                                        ░░░░░░░░░░░░░▒▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓███▓░░░░░░░░░░░░░░░
                                                        ░░░░░░░░░░░░▓███████████████████████▒░░░░░░░░░░░░░
                                                        ░░░░░░░░░░░░███████████▓▒▓██████████▒░░░░░░░░░░░░░
                                                        ░░░░░░░░░░░░█████████▒░░░░░▓████████▒░░░░░░░░░░░░░
                                                        ░░░░░░░░░░░░█████████▒░░░░░▒████████▒░░░░░░░░░░░░░
                                                        ░░░░░░░░░░░░██████████▓░░░▓█████████▒░░░░░░░░░░░░░
                                                        ░░░░░░░░░░░░███████████░░▒██████████▒░░░░░░░░░░░░░
                                                        ░░░░░░░░░░░░███████████▒░▒██████████▒░░░░░░░░░░░░░
                                                        ░░░░░░░░░░░░████████████████████████▒░░░░░░░░░░░░░
                                                        ░░░░░░░░░░░░▓███████████████████████░░░░░░░░░░░░░░
                                                        ░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░
                                                        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                                                        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                                                        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
      """)
print(Fore.YELLOW + """                                                                                  
                                             ___                                        ___              _                  
                                            (  _`\                                     (  _`\  _        ( )                 
                                            | ( (_)   _ _    __    ___    _ _  _ __    | ( (_)(_) _ _   | |__     __   _ __ 
                                            | |  _  /'_` ) /'__`\/',__) /'_` )( '__)   | |  _ | |( '_`\ |  _ `\ /'__`\( '__)
                                            | (_( )( (_| |(  ___/\__, \( (_| || |      | (_( )| || (_) )| | | |(  ___/| |   
                                            (____/'`\__,_)`\____)(____/`\__,_)(_)      (____/'(_)| ,__/'(_) (_)`\____)(_)   
                                                                                                | |                        
                                                                                                (_)                        

      """)

while True:
    operation = input(Fore.RED + "Type 'e' 🔐 to encrypt, type 'd' 🔓 to decrypt : ")
    print("\n")
    text = input(Fore.GREEN + "Type your message 🗣️  💬 📝 : ")
    print("\n")
    shift = input(Fore.RED + "Type the shift number  1️⃣  2️⃣  3️⃣  : ")
    print("\n")
    result = caesar(text, shift, operation)

    print(Fore.GREEN + f"📜🗝️  Your {operation} message is {result}  📜 🗝️ ")
    print("\n")

    restart = input(Fore.RED + "do you want to restart the application? (y/n) (👌/⛔) : ")
    if restart == "y":
        print("\n")
        continue
       
    else:
        exit()