# intlang-interpreter
Interpreter intlang jest prostym interpreterem języka skryptowego stworzonym przez Kamil Malickiego. Pozwala on na wykonywanie prostych instrukcji oraz operacji arytmetycznych.

Uruchamianie
Aby uruchomić interpreter intlang, należy użyć terminala i wpisać następującą komendę:

python intlang.py <file.il>
Gdzie <file.il> to ścieżka do pliku zawierającego kod w języku intlang. Pamiętaj, że plik musi mieć rozszerzenie .il.

Instrukcje języka intlang
Interpreter obsługuje następujące instrukcje:

PRINT: Wypisuje na ekranie podane argumenty.
SET: Ustawia wartość rejestru RAX na podaną liczbę.
INC: Inkrementuje wartość rejestru RAX o 1.
DOUBLE: Podwaja wartość rejestru RAX.
MOV: Przenosi wartość między rejestrami RAX i RAY.
SUM: Dodaje wartości rejestrów RAX i RAY, wynik zapisuje w RAX.
SUB: Odejmuje wartość rejestru RAY od RAX, wynik zapisuje w RAX.
NINC: Dekrementuje wartość rejestru RAX o 1.
GOTO: Przechodzi do określonej linii w kodzie.
PASS: Przechodzi do następnej linii kodu.
CMP: Porównuje wartość rejestru RAX z określoną liczbą i wykonuje skok do podanej linii zależnie od warunku.
INPUT: Pobiera wartość od użytkownika i zapisuje ją do rejestru RAX.
EXIT: Kończy działanie interpretera.

Przykładowy kod:

Oto przykładowy kod w języku intlang:

SET 5
INC
PRINT $RAX
PRINT "KONIEC"
Ten kod ustawi wartość RAX na 5, zwiększy ją o 1 i wyświetli wynik (6) na ekranie.
A na samym końcu wyświetla napis KONIEC przed zakończeniem programu.

Autor
Ten interpreter został stworzony przez Kamil Malickiego. Wszelkie prawa zastrzeżone.

