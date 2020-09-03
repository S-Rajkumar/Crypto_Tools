#!/usr/bin/env python3

'''
author : udmnxpdu
date   : July 2020
'''

import base62
import base64
import base58

class Crypto_Tools :
    """ This Class contains cryptographics tools ( decoder and encoder )
    1.decode_phone_code(cipherText)
        cipherText -> <string>
        returns => plain_text <string>
        Example :
            cipherText : 8836 66997388
            plain_text : udm nxpdu
            
    2.decode_dna_bin_code(bin_code)
        bin_code -> <string>
        return => DNA_code <string>
        Example :
            bin_code : 010111000000000110
            DNA code : GGTAAAAGC
	    
    3.decode_dna_code(dna_code)
        dna_code -> <string>
        returns => plain_text <string>
        Example :
            dna_code : GGTAAAAGC
            plain_text : Raj
            
    4.encode_dna_code(plain_text)
        plain_text -> <string>
        returns => DNA_code <string>
        Example :
            plain_text : Raj
            DNA_code : GGTAAAAGC
            
    5.encode_dna_bin_code(dna_code)
        dna_code -> <string>
        returns => Binary_DNA_code <string>
        Example :
            DNA_code : GGTAAAAGC
            Binary_DNA_code : 010111000000000110
	    
    6.encode_base64(plain_text)
	plain_text -> <string>
	return => base64_encoded_text <string>
	Example :
	    plain_text : Raj
	    base64_encoded_text : UmFq
	    
    7.decode_base64(base64_encoded_text)
	base64_encoded_text -> <string>
	return => plain_text <string>
	Example :
	    base64_encoded_text : UmFq
	    plain_text : Raj
	    
    8.encode_base32(plain_text)
	plain_text -> <string>
	return => base32_encoded_text
	Example :
	    plain_text : Raj
	    base32_encoded_text : KJQWU===
	    
    9.decode_base32(base32_encoded_text)
	base32_encoded_text -> <string>
	return => plain_text <string>
	Example :
	    base32_encoded_text : KJQWU===
	    plain_text : Raj
	    
   10.encode_base58(plain_text)
	plain_text -> <string>
	return => base58_encoded_text <string>
	Example :
	    plain_text : Raj
	    base58_encoded_text : UfuK
	    
   11.decode_base58(base58_encoded_text)
	base58_encoded_text -> <string>
	return => plain_text <string>
	Example :
	    base58_encoded_text : UfuK
	    plain_text : Raj
	    
   12.encode_base36(plain_text)
	plain_text -> <string>
	return => base36_encoded_text <int>
	Example :
	    plain_text : Raj
	    base36_encoded_text : 35371
	    
   13.decode_base36(base36_encoded_text)
	base36_encoded_text -> <int>
	return => plain_text <string>
	Example :
	    base36_encoded_text : 35371
	    plain_text : Raj
	    
   14.encode_base62(plain_text)
	plain_text -> <string>
	return => base62_encoded_text <string>
	Example :
	    plain_text = : Raj
	    base62_encoded_text : MeUs
	    
   15.decode_base62(base62_encoded_text)
	base62_encoded_text -> <string>
	return => plain_text <string>
	Example :
	    base62_encoded_text : MeUs
	    plain_text : Raj
    """
    
    phone_pad_map = {
        "2":"a", "22":"b", "222":"c", "3":"d", "33":"e", "333":"f", "4":"g", "44":"h", "444":"i", "5":"j", "55":"k", "555":"l", "6":"m", "66":"n", "666":"o", "7":"p", "77":"q", "777":"r", "7777":"s", "8":"t", "88":"u", "888":"v", "9":"w", "99":"x", "999":"y", "9999":"z", "0":" ", "1":"."," ":" "
    }
    dna_code_map = {
        'AAA':'a', 'AAC':'b', 'AAG':'c', 'AAT':'d', 'ACA':'e', 'ACC':'f', 'ACG':'g', 'ACT':'h', 'AGA':'i', 'AGC':'j', 'AGG':'k', 'AGT':'l', 'ATA':'m', 'ATC':'n', 'ATG':'o', 'ATT':'p', 'CAA':'q', 'CAC':'r', 'CAG':'s', 'CAT':'t', 'CCA':'u', 'CCC':'v', 'CCG':'w', 'CCT':'x', 'CGA':'y', 'CGC':'z', 'CGG':'A', 'CGT':'B', 'CTA':'C', 'CTC':'D', 'CTG':'E', 'CTT':'F', 'GAA':'G', 'GAC':'H', 'GAG':'I', 'GAT':'J', 'GCA':'K', 'GCC':'L', 'GCG':'M', 'GCT':'N', 'GGA':'O', 'GGC':'P', 'GGG':'Q', 'GGT':'R', 'GTA':'S', 'GTC':'T', 'GTG':'U', 'GTT':'V', 'TAA':'W', 'TAC':'X', 'TAG':'Y', 'TAT':'Z', 'TCA':'1', 'TCC':'2', 'TCG':'3', 'TCT':'4', 'TGA':'5', 'TGC':'6', 'TGG':'7', 'TGT':'8', 'TTA':'9', 'TTC':'0', 'TTG':' ', 'TTT':'.'
    }
    dna_bin_code_map = {
        '00':'A', '10':'C', '01':'G', '11':'T'
    }

    def decode_phone_code(self,cipherText) :
        n = len(cipherText)
        tmp = ""
        result = ""
        for i in range(0,n) :
            tmp += cipherText[i]
            if i + 1 == n :
                try :
                    result += self.phone_pad_map[tmp]
                except :
                    result += tmp
            elif cipherText[i] == cipherText[i+1] :
                pass
            else :
                try :
                    result += self.phone_pad_map[tmp]
                except :
                    result += tmp
                tmp = ""
        return result
        
    def decode_dna_bin_code(self,bin_code) :
        bin_code = bin_code.replace(' ','')
        result = ""
        for i in range(0,len(bin_code),2) :
            result += self.dna_bin_code_map[bin_code[i:i+2]]
        return result
        
    def decode_dna_code(self,dna_code) :
        dna_code = dna_code.replace(' ','')
        result = ""
        for i in range(0,len(dna_code),3) :
            result += self.dna_code_map[dna_code[i:i+3]]
        return result
        
    def encode_dna_bin_code(self,dna_code) :
        dna_code = dna_code.replace(' ','')
        tmp_dna_bin_code_map = { value:key for key,value in self.dna_bin_code_map.items() }
        result = ""
        for i in range(0,len(dna_code)) :
            result += tmp_dna_bin_code_map[dna_code[i]]
        return result
        
    def encode_dna_code(self,plain_text) :
        tmp_dna_code_map = { value:key for key,value in self.dna_code_map.items() }
        result = ""
        for i in range(0,len(plain_text)) :
            result += tmp_dna_code_map[plain_text[i]]
        return result
	
    def encode_base64(self,plain_text) :
        return base64.b64encode(plain_text.encode('utf-8')).decode('utf-8')
	
    def decode_base64(self,b64_encoded_text) :
        return base64.b64decode(b64_encoded_text).decode('utf-8')
	
    def encode_base32(self,plain_text) :
        return base64.b32encode(plain_text.encode('utf-8')).decode('utf-8')
	
    def decode_base32(self,b32_encoded_text) :
        return base64.b32decode(b32_encoded_text).decode('utf-8')
	
    def encode_base58(self,plain_text) :
        return base58.b58encode(plain_text).decode('utf-8')
	
    def decode_base58(self,b58_encoded_text) :
        return base58.b58decode(b58_encoded_text).decode('utf-8')
	
    def encode_base36(self,plain_text) :
        return int(plain_text, 36)
	
    def decode_base36(self,b36_encoded_text) :
        base36_alpha = '0123456789abcdefghijklmnopqrstuvwxyz'
        result = ''
        while b36_encoded_text != 0 :
            b36_encoded_text, index = divmod(b36_encoded_text,36)
            result = base36_alpha[index] + result
        return result
	
    def encode_base62(self,plain_text) :
        return base62.encodebytes(plain_text.encode('ascii'))
	
    def decode_base62(self,b62_encoded_text) :
        return base62.decodebytes(b62_encoded_text).decode('ascii')
	
