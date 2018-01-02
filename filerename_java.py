import os,shutil
os.chdir('c:\\Users\Shantanu1395\Documents\GitHub\Hackerrank\Java')
for filename in os.listdir():
    if filename.endswith('.txt'):
        file = open('c:\\Users\Shantanu1395\Documents\GitHub\Hackerrank\Java\\'+filename, "r")
        line=file.readline()[2:]                   # As I have used '//' as first line
        line="_".join(line.split(" "))[:-1]+".java"           #[:-1] for \n
        file.close()
        shutil.move('c:\\Users\Shantanu1395\Documents\GitHub\Hackerrank\Java\\'+filename,'c:\\Users\Shantanu1395\Documents\GitHub\Hackerrank\Java\\'+line)
