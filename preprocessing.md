# Dokumentacja prac nad projektem

## Eksploracja i korekta zbioru danych
Dostarczone datasety zostały przejrzane, zeby zapoznać się z ich strukturą. Zostało odnalezione wiele błędów związanych m.in. ze spójnością i sensownością danych. Część danych (zarówno na wejściu, jak i na wyjściu) została poddana korekcie. Szczegóły opisano w pliku dataset.md. Poprawione dane znajdują się w plikach data_1.txt (pełne dane) i data_2.txt

## Reanotacja danych
Po wielu nieudanych próbach zrównoleglenia danych z plików data_1.txt i data_2.txt dane zostały częściowo zreanotowane ręcznie za pomocą narzędzia https://arunmozhi.in/ner-annotator/. Następnie wyeksportowane dane zostały przekształcone przy uzyciu skryptu sample_data_transformation.py w format odpowiedni do późniejszego trenowania modelu.

## Trening danych
Proces trenowania jest udokumentowany w pliku training.py. Za pomocą skryptu testing.py została przeprowadzona wstępna inspekcja jakości na fragmencie, który nie został zaanotowany w poprzedniej części.
Finalne dane output_blahaj6c.txt zostały przetworzone za pomocą skryptu anonymizer.py aby spełniać warunki oczekiwanego formatu.
