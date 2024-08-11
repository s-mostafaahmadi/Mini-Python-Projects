This program can lock any files

in current situation:

When encryption.py is run, all files with the extension .txt will be encoded in this directory
Every file that is coded contains a token that is specific to that file and a key that is for all the txt files in this directory.

It opens text files, encrypts the contents and saves each file's special token in a new file with the same name  with the extension .Keylogger.

The key of the encrypted files is stored in a file called key_Files.txt

If you do not have the token of each file and the key, you cannot decrypt any file.

decrypt requires two things :
1. token : Each file has its own token
2. The key that is the same for all encrypted files

If you want to encode other formats such as photos, videos, and zip, you must change the desired_format inside the codes.