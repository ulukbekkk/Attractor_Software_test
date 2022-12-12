class CesarCipher:
    _alphabet = None
    _shift = None
    
    def set_alphabet(self, value):
        self._alphabet = value

    def set_shift(self, value):
        self._shift = value

    def encode(self, plain_text):
        encoded = ''
        max_ind = len(self._alphabet) - 1
        
        for i in plain_text:
            place_ind = self._alphabet.find(i)
            ind = place_ind + self._shift

            if i not in self._alphabet:
                encoded += i
                continue

            if ind > max_ind:
                last_ind = ind - max_ind -1
                res = self._alphabet[last_ind]
                encoded += res
            else:
                encoded += self._alphabet[ind]
        return encoded


cesar = CesarCipher()
cesar.set_alphabet('abcdefghijklmnopqrstuvwxyz')
cesar.set_shift(3)
res = cesar.encode('The quick brown fox jumps over the lazy dog')
print(res)

test_answer = 'Tkh txlfn eurzq ira mxpsv ryhu wkh odcb grj'
if res == test_answer:
    print(True)



