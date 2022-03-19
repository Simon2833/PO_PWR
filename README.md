# PO_PWR
**Plemiona**\
    Symulacja plemion zaczyna się od stworzenia proceduralnie generowanej mapy. Całość skupia się na życiu poszczególnych plemion (ich ilość jest dobrana przez użytkownika), które wraz z biegiem czasu zaczynają ze sobą walczyć lub zakładać sojusze (poprzez scalenie). W ich środowisku losowo występują zasoby naturalne (pokarm szczególnie ważny w obliczu panującego głodu, który zagraża życiu) i czyhające w cieniu niebezpieczeństwa (wrogo nastwione stworzenia). W osadach można odnaleźć różne klasy jednostek (np. wojownicy, łucznicy).
    
 
WERSJA ROZSZERZONA

•	Ilość plemion - Ustalana przez użytkownika (min. 2)
 
•	Wrogie/Przyjazne plemiona - Plemie będzie generowane losowo ze statusem przyjaznego lub wrogiego
Przyjazny - Może zawierać sojusze z innymi przyjaznymi plemionami
Wrogie - Agresywne dla wszystkich bonusy do statystyk z uwagi na brak możliwości sojuszy
 
•	Wielkość mapy - Podawana przez użytkownika (min. 10x10, max.?)
 
•	Rodzaje jednostek :
- Wojownik - słaby zasięg ataku, średnia siła ataku, duży pancerz
- Pikinier - średni zasięg ataku, duża siła ataku, średni pancerz
- Łucznik - duży zasięg ataku, mała siła ataku, blisko zerowy pancerz
 
•	Losowe Wielkie stwory nieprzyjazne - Będą to prehistoryczne stworzenia (np. Smok wawelski ;) ) krótki zasięg a reszta statystyk duża, po zneutralizowaniu generuje dużo jedzenia
 
•	Morale - Są to bonusy lub minusy do statystyk zależne od ilości populacji plemienia. Jeżeli do plemienia dochodzi kolejny osadnik morale zostają zwiększone, a przy utracie jednego z nich - zmniejszone. (zaimplementujemy rozwiązanie które zapobiegnie wzrostowi morali do nieskonczonosci przy zerowym wzroscie popuacji na dluzszej przestrzeni czasu)
 
•	Zniszczenie bazy plemiennej - Wszyscy przynależni do tego plemienia osadnicy stają się bezimiennymi włóczęgami tułającymi się po mapie z minimalną szansą dołączenia do innego plemienia (podczas interakcji z członkiem napotkanego plemienia)
 
•	Surowce naturalne  - Będzie to uznawane za jedzenie które pozwala powiększyć populację o jedną osobę. Członek osady musi napotkać ten owoc w zasięgu swojej interakcji i automatycznie jest on zbierany co aktywuje funkcję zwiększenia populacji. Jeżeli osada nie znajdzie przez długi okres czasu żadnego jedzenia to następuje głód. Jeżeli dalej nie znajdą żadnego pożywienia co jakiś czas losowy osadnik ginie (Okres głodu zmniejsza także morale na czas jego trwania).
 
•	Wojna/Sojusze :

Wojna - Rozpoczyna się jeżeli np. jakaś jednostka umrze podczas walki, będzie trwała aż do zniszczenia bazy jednego z plemion (jeżeli zostaną pokonani wszyscy osadnicy baza autmatycznie znika razem z plemieniem), jeżeli wojna będzie trwała za długo z każdą rundą zwiększa się szansa na nastanie pokoju między nimi.
Sojusz - Dalej planujemy możliwości sojuszu, może to być mała szansa podczas interakcji między ich osadnikami jednak to jest jeszcze do zmiany
 
•	Menu z ustawieniami - Będzie to ekran główny z możliwością rozpoczęcia symulacji, wyjścia z niej, oraz ustawienia zasad gry:
- liczba plemion
- Ilość generowanego jedzenia
- Wielkość mapy
- Stosunek przyjaznych plemion do wrogich
- Przycisk do ustawień losowych
 	


W przyszłości będziemy dodawać funkcje lub je usuwać jeżeli będą zbyt problematyczne/ambitne.
Dalej myślimy nad rodzajem poruszania się postaci("sztuczna" inteligencja np. podczas wojny będą bardziej skupiać się na przeciwnikach niż podróży po świecie)
 
 
 
 
 
 

