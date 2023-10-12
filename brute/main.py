from nuts_and_bolts import brutemain, encryptiondecryptionmain
#from nuts_and_bolts import encryptiondecryptionmain
from nuts_and_bolts.brutemain import bruteforce
from nuts_and_bolts.encryptiondecryptionmain import encryptdecrypt

print(" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ " +
	"_ _ _ _ _ _ _ _ _ _ _ _")
print("|Would you like to encrypt/ decrypt text?\t\t\t\t\t    |")
print("|Or would you like to brute-force text (necessary for decrypting" +
	" when no key matrix |")
print("|is available)?\t\t\t\t\t\t\t\t\t    |")
print("|_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ " +
	"_ _ _ _ _ _ _ _ _ _ _ _|")
	
inpt = input("\n\tEnter 0 for encrypt/ decrypt. Enter 1 for " +
	"brute-force: ")

while str(inpt) != '0' and str(inpt) != '1':
	print("\n\tERROR")
	
	inpt = input("\n\tEnter '0' for encrypt/ decrypt. Enter '1' for " +
		"brute-force: ")

if str(inpt) == '0':
	encryptdecrypt()
else:
	bruteforce()
	
