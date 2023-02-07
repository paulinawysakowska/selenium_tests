# Created by paulina at 06/02/2023
Feature: Akceptacja zgód RODO, wyszukanie przedmiotu na stronie Allegro

  Scenario: Akceptacja zgód RODO
    Given Komunikat RODO na stronie Allegro jest widoczny
    When Użytkownik wyrazi zgodę na przetwarzanie danych
    Then Strona główna Allegro jest widoczna