import os,shutil
os.chdir('c:\\Users\Shantanu1395\Documents\GitHub\Hackerrank\Python')
for filename in os.listdir():
    if filename.endswith('.txt'):
        file = open('c:\\Users\Shantanu1395\Documents\GitHub\Hackerrank\Python\\'+filename, "r")
        line=file.readline()[1:]                                                                        # As I have used '#' as comment first line
        line="_".join(line.split(" "))[:-1]+".py"                                                       #[:-1] for \n
        file.close()
        shutil.move('c:\\Users\Shantanu1395\Documents\GitHub\Hackerrank\Python\\'+filename,'c:\\Users\Shantanu1395\Documents\GitHub\Hackerrank\Python\\'+line)
