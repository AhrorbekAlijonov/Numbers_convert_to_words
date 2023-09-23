def num_to_uzbek_convert(num):
    units = ("", "bir ", "ikki ", "uch ", "to'rt ","besh ", "olti ", "yetti ","sakkiz ", "to'qqiz ", "o'n ", "o'n bir ", "o'n ikki ", "o'n uch ", "o'n to'rt ", "o'n besh ","o'n olti ", "o'n yetti ", "o'n sakkiz ", "o'n to'qqiz ")
    tens =("", "", "yigizma ", "o'ttiz ", "qiriq ", "ellik ","oltmish ","yetmush ","sakson ","to'qson ")

    if num < 0:
        return "minus "+num_to_uzbek_convert(-num)

    if num<20:
        return  units[num] 

    if num<100:

        return  tens[num // 10]  +units[int(num % 10)] 

    if num<1000:
        return units[num // 100]  +"yuz " +num_to_uzbek_convert(int(num % 100))

    if num<1000000: 
        return  num_to_uzbek_convert(num // 1000) + "ming " + num_to_uzbek_convert(int(num % 1000))

    if num < 1000000000:    
        return num_to_uzbek_convert(num // 1000000) + "milion " + num_to_uzbek_convert(int(num % 1000000))

    return num_to_uzbek_convert(num // 1000000000)+ "miliard "+ num_to_uzbek_convert(int(num % 1000000000))
