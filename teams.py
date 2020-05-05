file = open("teams.txt", "w")
file.write("Manchester United" '\n' "Arsenal"
            '\n' "Chelsea" '\n' "Tottenham" '\n'
            "West Ham")
file.close()
read_file = open("teams.txt", "r")

print(read_file.readline())
read_file.readline()
read_file.readline()
print(read_file.readline())
read_file.readline()

file.close()