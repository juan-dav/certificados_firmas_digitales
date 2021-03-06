
import sys
import time
import io
start_time = time.time()


def menu():
    args = sys.argv
    args = args[1:]  # First element of args is the file name

    if len(args) == 0:
        print(
            '------------------------------------------------------------------------------')
        print(
            '|                     Universidad Autónoma de Occidente                      |')
        print(
            '|                 Especialización en seguridad informática                   |')
        print(
            '|                      Certificados y firmas digitales                       |')
        print(
            '|                                                                            |')
        print(
            '|          No pasate ninguna bandera, para obtener la ayuda ejecuta:         |')
        print(
            '|                            python args.py -h                               |')
        print(
            '------------------------------------------------------------------------------')
    else:
        if args[0] == '-h' or args[0] == '--ayuda' or args[0] == '--help':
            print(
                '------------------------------------------------------------------------------------------')
            print(
                '|                            Universidad Autónoma de Occidente                           |')
            print(
                '|                        Especialización en seguridad informática                        |')
            print(
                '|                            Certificados y firmas digitales                             |')
            print(
                '|                                                                                        |')
            print(
                '|                        Banderas para el uso correcto de args.py                        |')
            print(
                '------------------------------------------------------------------------------------------')
            print(
                '|  Opciones:                                                                             |')
            print(
                '|    -h, --ayuda       muestra la ayuda basica.                                          |')
            print(
                '|                                                                                        |')
            print(
                '|    -d, --decifrar    criptoanaliza un mensaje dado un archivo, automaticamente muestra |')
            print(
                '|                      por consola la salida de todo el analisis junto a su clave        |')
            print(
                '|                      tanto en posición del alfabeto como el letra                      |')
            print(
                '|                         python criptoanalisis_cesar.py -d mensaje_en_texto_cifrado.cif |')
            print(
                '|                                                                                        |')
            print(
                '|  Estudiantes:                                                                          |')
            print(
                '|    Juan David Garcia Reyes                                                             |')
            print(
                '|    Juan Camilo Tamayo Molina                                                           |')
            print(
                '|                                                                                        |')
            print(
                '|  Profesor:                                                                             |')
            print(
                '|    Siler Amador Donado                                                                 |')
            print(
                '------------------------------------------------------------------------------------------')
        elif args[0] == '-d' or args[0] == '--descifrar':
            if args[1] == '':
                messageError(args[0], args)
                exit
            else:
                    print((args[1]))
                    decrypted(args[1])


def initialAlphabet():
    return 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZÏÀ]«3ÙÜ_[%\n'
    # return u"!\"#$%&'()*+-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~ÇüéâäàåçêëèïîìÄÅÉæÆôöòûùÿÖÜø£Ø×ƒáíóúñÑªº¿®¬½¼¡«»░▒▓│┤ÁÂÀ©╣║╗╝¢¥┐└┴┬├─┼ãÃ╚╔╩╦╠═╬¤ðÐÊËÈıÍÎÏ┘┌█▄¦Ì▀ÓßÔÒõÕµþÞÚÛÙýÝ¯´≡±‗¾¶§÷¸°¨·¹³²■"
    # return u"!#$%&'()*+-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~ÇüéâäàåçêëèïîìÄÅÉæÆôöòûùÿÖÜø£Ø×ƒáíóúñÑªº¿®¬½¼¡«»░▒▓│┤ÁÂÀ©╣║╗╝¢¥┐└┴┬├─┼ãÃ╚╔╩╦╠═╬¤ðÐÊËÈıÍÎÏ┘┌█▄¦Ì▀ÓßÔÒõÕµþÞÚÛÙýÝ¯´≡±‗¾¶§÷¸°¨·¹³²■"


def fileContent(file):
    f = open(file, "r")
    message = f.read()
    f.close()

    return message


def countAndSortLetters(encryptedMessage):
    lettersInMessage = []

    for indexLetterMessage, letterMessage in enumerate(encryptedMessage):
        isLetterInMessage = 0
        indexCounterLetterInMessage = 0
        for indexCounterLetter, counterLetter in enumerate(lettersInMessage):
            if letterMessage == counterLetter['letter']:
                isLetterInMessage = 1
                indexCounterLetterInMessage = indexCounterLetter
        if isLetterInMessage:
            lettersInMessage[indexCounterLetterInMessage]['quantity'] += 1
        else:
            lettersInMessage.append({'letter': letterMessage, 'quantity': 1})

    lettersInMessage = sorted(
        lettersInMessage, key=lambda i: i['quantity'], reverse=True)

    return lettersInMessage


def decrypted(file):
    name = file.split('.')[0]
    key = 0
    alphabet = initialAlphabet()
    module = len(alphabet)
    decriptedMessage = ''
    alphabetFrequency = [
        {'letter': 'E', 'index': 4},
        {'letter': 'A', 'index': 0},
        {'letter': 'S', 'index': 19},
        {'letter': 'O', 'index': 15},
        {'letter': 'I', 'index': 8},
        {'letter': 'N', 'index': 13},
        {'letter': 'R', 'index': 18},
        {'letter': 'D', 'index': 3},
        {'letter': 'T', 'index': 20},
        {'letter': 'C', 'index': 2},
        {'letter': 'L', 'index': 11},
        {'letter': 'U', 'index': 21},
        {'letter': 'M', 'index': 12},
        {'letter': 'P', 'index': 16},
        {'letter': 'G', 'index': 6},
        {'letter': 'B', 'index': 1},
        {'letter': 'F', 'index': 5},
        {'letter': 'V', 'index': 22},
        {'letter': 'Y', 'index': 25},
        {'letter': 'Q', 'index': 17},
        {'letter': 'H', 'index': 7},
        {'letter': 'Z', 'index': 26},
        {'letter': 'J', 'index': 9},
        {'letter': 'X', 'index': 24},
        {'letter': 'W', 'index': 23},
        {'letter': 'K', 'index': 10},
        {'letter': 'Ñ', 'index': 14},
    ]

    # se realiza el llamado a la función que me obtiene el contenido del archivo
    encryptedMessage = fileContent(file)

    # se realiza el llamado a la función que cuenta y ordena las letras de mayor a menor
    # del texto cifrado
    lettersInMessage = countAndSortLetters(encryptedMessage)

    # Asignación de la propiedad index en la lista de las letras que más se repiten en el mensaje para facilitar
    # el cripto analisis
    for letterMessage in lettersInMessage:
        for letterInAlphabetFrequency in alphabetFrequency:
            if letterMessage['letter'] == letterInAlphabetFrequency['letter']:
                letterMessage['index'] = letterInAlphabetFrequency['index']

    # ciclo para recorer el alfabeto de freciencia para el idioma español o ingles
    for indexLetterInAlphabetFrequency, letterInAlphabetFrequency in enumerate(alphabetFrequency):
        # validación para verificar que el indice de la frecuencia del alfabeto mas uno no vaya a superar el limite del arreglo
        if indexLetterInAlphabetFrequency+1 < len(alphabetFrequency):
            # inicialización de las hipotesis
            K11 = 0
            K12 = 0
            K21 = 0
            K22 = 0
            # ciclo para recorer las letras que se encuentran en el mensaje cifrado
            for firstIndexLetterMessage, firstLetterMessage in enumerate(lettersInMessage):
                # validación para verificar que el indice del mensaje cifrado mas uno no vaya a superar el limite del arreglo
                if firstIndexLetterMessage+1 < len(lettersInMessage):
                    # ciclo para recorer las letras que se encuentran en el mensaje cifrado por segunda vez para realizar
                    # la operación de las hipotesis
                    for secondIndexLetterMessage, secondLetterMessage in enumerate(lettersInMessage):
                        # validación para verificar que el indice del mensaje cifrado mas el indice en que se encuentra el primer ciclo
                        # del mensaje cifrado mas uno no vaya a superar el limite del arreglo
                        if secondIndexLetterMessage+firstIndexLetterMessage+1 < len(lettersInMessage):
                            # se obtienen el par de letras a las cuales se les va a realizar las hipotesis
                            firtsLetter = lettersInMessage[firstIndexLetterMessage]
                            secondLetter = lettersInMessage[secondIndexLetterMessage + firstIndexLetterMessage+1]
                            # Se filtran los caracteres que no se encuentren en la tabla de frecuencias, para que encuentren su 
                            # Indice correspondiente en el alfabeto
                            if len(firtsLetter) < 3 or firtsLetter['letter'] != "\n":
                               firtsLetter['index'] = alphabet.index(str(firtsLetter['letter']))
                            if len(secondLetter) < 3  or secondLetter['letter'] != "\n":
                               secondLetter['index'] = alphabet.index(str(secondLetter['letter']))
                            # se realiza el calculo de las hipotesis para el par de letras, ejemplo par de letras A, B
                            K11 = (firtsLetter['index'] - alphabetFrequency[indexLetterInAlphabetFrequency]['index']) % module
                            K12 = (secondLetter['index'] - alphabetFrequency[indexLetterInAlphabetFrequency+1]['index']) % module
                            # se realiza el calculo de las hipotesis para el par de letras de manera inversa,
                            # ejemplo par de letras B, A
                            K21 = (secondLetter['index'] - alphabetFrequency[indexLetterInAlphabetFrequency]['index']) % module
                            K22 = (firtsLetter['index'] - alphabetFrequency[indexLetterInAlphabetFrequency+1]['index']) % module
                            # validación en cascada si el resultado de las hipotesis 1 o 2 da el mismo resultado,
                            # si esto pasa quiere decir que la llave utilizada para cifrado el mensaje fue encontrada
                            if K11 == K12:
                                break
                            if K21 == K22:
                                break
                    if K11 == K12:
                        break
                    if K21 == K22:
                        break
            if K11 == K12:
                key = K11
                break
            if K21 == K22:
                key = K21
                break

    for letterMessage in lettersInMessage:
        cube=""
        print(("letra "+letterMessage['letter']+" tiene " +
               str(letterMessage['quantity'])+" repeticiones"))
        for x in range(letterMessage['quantity']):
            cube += """[|]"""
        print(cube)
    print('')
    print(('La llave que se utilizo fue el numero: ' +
           str(key)+', '+alphabet[key]))


def messageError(indexArg, args):
    print('------------------------------------------------------------------------------')
    print('|                     Universidad Autónoma de Occidente                      |')
    print('|                 Especialización en seguridad informática                   |')
    print('|                      Certificados y firmas digitales                       |')
    print('|                                                                            |')
    print('|     Error en el uso de las banderas, Por favor ver la ayuda ejecutando:    |')
    print('|                            python args.py -h                               |')
    print('------------------------------------------------------------------------------')


if __name__ == '__main__':
    menu()
    print(("--- %s segundos ---" % (time.time() - start_time)))
