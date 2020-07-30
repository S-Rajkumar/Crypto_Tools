#!/usr/bin/env python3

'''
author : udmnxpdu
date   : July 2020
'''

class Crypto_Tools :
    """ This Class contains cryptographics tools ( decoder and encoder )
    1.decode_phone_code(cipherText)
        cipherText -> <string>
        returns => uncipher_text <string>
        Example :
            cipherText : 8836 66997388
            unCipherText : udm nxpdu
    """
    
    phone_pad = {"2":"a","22":"b","222":"c","3":"d","33":"e","333":"f","4":"g","44":"h","444":"i","5":"j","55":"k","555":"l","6":"m","66":"n", "666":"o","7":"p","77":"q","777":"r","7777":"s","8":"t","88":"u","888":"v","9":"w","99":"x","999":"y","9999":"z","0":" ","1":"."," ":" "}
    
    def decode_phone_code(self,cipherText) :
        n = len(cipherText)
        tmp = ""
        result = ""
        for i in range(0,n) :
            tmp += cipherText[i]
            if i + 1 == n :
                try :
                    result += self.phone_pad[tmp]
                except :
                    result += tmp
            elif cipherText[i] == cipherText[i+1] :
                pass
            else :
                try :
                    result += self.phone_pad[tmp]
                except :
                    result += tmp
                tmp = ""
        return result
