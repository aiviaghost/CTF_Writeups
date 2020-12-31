from enigma.machine import EnigmaMachine # https://py-enigma.readthedocs.io/en/latest/overview.html
from itertools import product
from string import ascii_uppercase

'''
Given the name and the description mentioning an old cipher I figured they were using an enigma machine. 
Everything except the initial ring positions was given so I googled for an enigma simulator. 
Conveniently one of the first results was a simulator specifically for the wehrmacht model. 
Then it was just a simple bruteforce (26^3 possible configurations) to find the correct starting positions. 
'''

with open("wehrmacht.txt", "r") as f:
    ciphertext = ''.join(f.readlines()).replace("\n", "").replace(" ", "")

machine = EnigmaMachine.from_key_sheet(
       rotors='I II III',
       reflector='B',
       ring_settings=[1, 2, 3],
       plugboard_settings='AQ BJ')

for p in product(ascii_uppercase, ascii_uppercase, ascii_uppercase):
    # print(''.join(p))
    machine.set_display(''.join(p))
    plaintext = machine.process_text(ciphertext)
    if "ICECTF" in plaintext:
        print("Starting positions: " + ''.join(p))
        print(plaintext)
        break

'''
deciphered: 
ICECTFTURINGMACHFAWGHADEOACZYYPRPXGXFZHKYKTICHOSENISKNOWNASQWERTZUORQERXTHEDIAGRAMSHOWSTHECONNXCTIONSWHENTHEKEYQISDEPRESYEDANDSUPPOSINGTHATCISCONNLCTEDTOCTHROUGHTHEWHEELSXTQEONLYOUTLETFORTHEPOSITIVEYFTHEBATTERYISTHROUGHTHEQKFYTOGHENCETOCANDTHENTHROUGFTHEEBULBXTHERESULTISTHATTWEEBULBLIGHTSXMOREGENERALLOWECANSAYIFTWOCONTACTSCZZDMFTHEEINTRITTSWALZARECONNEUTEDTHROUGHTHEWHEELSTHENTHORESULTOFENCIPHERINGTHELETNERASSOCIATEDWITHCISTHELETTERASSOCIATEDWITHDXNOTICETIATIFPISTHERESULTOFENCIPHEHINGGZZTHENGISTHERESULTOFEYCIPHERINGPATTHESAMEPLACEZIALSOTHATTHERESULTOFENCIPHHRINGGCANNEVERBEGXONTHEWHELLSARERINGSORTYRESCARRYINGKLPHABETSZZANDROTATABLEWITPRESPECTTOTHERESTOFTHEWHEEHQRRJMFPKQTHGYZMBWLCJTGZMBNWXWHENTHEMACHINEISBEINGUSXDTHREEOFTHEWHEELSAREPUTINUETWEENTHEUXKXWXANDTHEEXWXUNSOMEPRESCRIBEDORDERXTHEWPYTHATTHECURRENTMIGHTFLOWFJOMTHEEXWXTHROUGHTHEWHEELSKNDBACKISSHOWNBELOWXVERYNIJEWORKXTHECODEISICECTFTURIYGMACHINEX

Flag: ICECTF{TURINGMACHINE}
'''
