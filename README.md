# Proiect IOM - Aplicație de calendar

## Logica aplicatiei:

1. Selectare dată din calendar.
2. Pe baza datei din calendar se afiseaza 2 noi butoane: 
 
 - Insereaza eveniment
 - Rosteste evenimente din zi

## Descrierea functionalitatii:

- Insereaza eveniment: 
Atat vocal cat si text. Afisam 2 butoane prin care selectam modalitatea de inserare a evenimentului.
Se vor insera intr-un fisier (.csv, .txt) intr-o linie si va fi o problema pentru atunci cum ne jucam cu datele.

- Rosteste eveniment:
Cautam in CSV ziua respectiva, o aducem in piton si facem tts pe care il salvam + play cu tts.

- Alertare utilizator:
Cand se apeleaza `get_date` facem un loop care trece prin tooot .csv-ul si in cazul in care gaseste urmatoarea zi => un mesaj in UI
daca nu, scrie ca nu vor fi evenimente in ziua urmatoare.

                                                         
                                                         
