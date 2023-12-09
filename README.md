intlang jest interpreterem prostego języka programowania o nazwie intlang. Język ten został stworzony przez Kamila Malickiego. Interpreter umożliwia wykonywanie prostych operacji arytmetycznych, manipulację rejestrami i wykonywanie podstawowych operacji na nich.

Obsługiwane operacje:

PRINT: Wypisuje podane argumenty do konsoli.

SKŁADNIA:

a) PRINT 'co chcesz napisać'

b) PRINT $RAX

c) PRINT $RAY

SET: Ustawia wartość rejestru RAX. 

SKŁADNIA: 

SET {LICZBA PRZNIESIONA DO RAX}

INC: Inkrementuje wartość rejestru RAX.

SKŁADNIA: 

INC => {RAX+=1} 

STORE: Zapisuje wartość w danym rejestrze RAR.

SKŁADNIA: 

STORE {BIT NUMBER} {LICZBA PRZNIESIONA DO RAR}

DATA: Wyświetla wartość z danego rejestru RAR.

SKŁADNIA: 

DATA {BIT NUMBER} => { PYTHON = print(RAR[bit number])}

DOUBLE: Mnoży wartość rejestru RAX przez 2.

SKŁADNIA: DOUBLE => {RAX*=2} 

MOV: Przenosi wartość z jednego rejestru do drugiego.

SKŁADNIA:

a) MOV Y => {RAY<--RAX}  

b) MOV X => {RAX<--RAY} 

ITOA: Konwertuje wartość rejestru na odpowiedni znak.

SKŁADNIA:

a) ITOA $RAX => { PYTHON = print(chr(RAX))}  

b) ITOA $RAY => { PYTHON = print(chr(RAX))}  

c) ITOA $RAR[bit number]= {PYTHON = print(chr(RAR[bit number]))}
  
ATOI: Konwertuje znak na odpowiadającą mu wartość liczbową.

SKŁADNIA:

a) ATOI $RAX => {RAX -= 48}

b) ATOI $RAY => {RAY -= 48}

c) ATOI $RAR[bit number] => {RAR[bit number] -= 48}

SUM: Dodaje wartości rejestrów RAX i RAY.

SKŁADNIA: SUM => {RAX += RAY}

SUB: Odejmuje wartość rejestru RAY od RAX.

SKŁADNIA: SUB => {RAX -= RAY}

NINC: Dekrementuje wartość rejestru RAX.

SKŁADNIA: NINC => {RAX-=1} 

GOTO: Przechodzi do konkretnej linii kodu.

SKŁADNIA: GOTO {SKOK DO JAKIEJŚ LINIKI KODU}

PASS: Pomija aktualną instrukcję.

SKŁADNIA: PASS

CMP: Porównuje wartość rejestru RAX z podanym warunkiem i podejmuje akcję na podstawie wyniku porównania.

SKŁADNIA: CMP {WARTOŚĆ PORÓWNANA Z RAX} GOTO {SKOK DO JAKIEJŚ LINIKI KODU}

RARCMP: Porównuje wartości w dwóch rejestrach RAR i podejmuje akcję na podstawie wyniku porównania.

SKŁADNIA: RARCMP {JAKIŚ BIT DO PORÓWNANIA Z REJESTRU RAR} {JAKIŚ BIT DO PORÓWNANIA Z REJESTRU RAR} GOTO {SKOK DO JAKIEJŚ LINIKI KODU}

INPUT: Pobiera wartość od użytkownika i zapisuje ją w rejestrze RAX.

SKŁADNIA: INPUT

EXIT: Kończy działanie programu.

SKŁADNIA: EXIT

Instrukcje uruchomienia:
Aby uruchomić interpreter intlang, użyj polecenia w terminalu:

python intlang.py <file.il>

Gdzie <file.il> to ścieżka do pliku zawierającego kod w języku intlang.

Przykładowy kod  w języku intlang:

PRINT 'Hello, world!'

SET 10

INC

NINC

PRINT $RAX

Uwaga!
Język intlang jest prostym językiem interpretowanym i nie posiada obsługi złożonych operacji. Proszę upewnić się, że kod napisany w tym języku jest zgodny z dokumentacją dostarczoną przez Kamila Malickiego czyli przez autora języka intLang.

Niniejszy README ma na celu zapewnienie informacji o tym, jak korzystać z interpretera intlang oraz jakie operacje są obsługiwane. Proszę pamiętać, że niniejszy program jest chroniony prawem autorskim Kamila Malickiego.

Aktualizacje oprogramowania:

1.1.0: dodanie nowego rejestru RAR który posiada podział na 8 bitów (0,1,2,3,4,5,6,7).

1.0.5: dodanie nowego rejestru RAY który można używać jako pamięć dodatkowa do rejestru RAX.
