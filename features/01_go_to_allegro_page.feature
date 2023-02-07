# Created by paulina at 04/02/2023
Feature: Otwarcie przeglądarki Chrome, przejście na stronę Allegro

  Scenario: Otwarcie przeglądarki Chrome
    Given Komunikat o przetwarzaniu danych jest widoczny
    When Użytkownik wybierze przycisk Zamknij
    Then Strona Google jest widoczna

  Scenario: Wyszukiwanie w Google - brak frazy wyszikiwania
    Given Strona Google jest widoczna
    When Użytkownik wybierze przycisk Szukaj w Google
    But Wyszukiwana fraza nie jest uzupełniona
    Then Strona Google jest widoczna

  Scenario: Wyszukanie Allegro za pomocą Google
    Given Strona Google jest widoczna
    When Użytkownik wyszuka frazę Allegro
    Then Wyniki wyszukiwania są widoczne

  Scenario: Przejście z wyników wyszukiwania na stronę główną Allegro
    Given Wyniki wyszukiwania są widoczne
    When Użytkownik wybierze jeden z wyników wyszukiwania
    Then Komunikat RODO na stronie Allegro jest widoczny