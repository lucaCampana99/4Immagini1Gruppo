# 4Immagini1Gruppo
image reverse search engine made by Luca Campana, Edoardo Maines, Alan Cesaro, Mario Sorrentino

# Implementazione ed applicazione algoritmi

In questo paragrafo spiegheremo la parte di background dell’applicazione, abbiamo deciso di suddividere questa parte in 2 programmi separati ed indipendenti, salvo poi, come vedremo in seguito, unire le 2 parti per avere delle maggiori performance nella ricerca per contorni.
Entrambi i programmi sono divisi in 2 macrosegmenti concettuali:
Composto dall’algoritmo scelto ed adattato alle nostre esigenze e da una classe che estrae le features da ogni immagine e le trascrive su un file.
Composto da una classe che implementa le funzioni di comparazione delle features e infine dall’applicazione finale.
Ora vedremo più in dettaglio ogni classe scelta:

# CONFRONTO TRAMITE COLORI

## Istogramma.py

In questa parte del programma viene implementata la classe Istogramma che si compone di 3 funzioni:
1. La funzione di inizializzazione
2. La funzione “histogram”: funzione che calcola l’istogramma 3D di una maschera data in input, in seguito l’output viene appiattito per facilitarne la scrittura su file e soprattutto l’estrazione in seguito
3. La funzione “describe”: in questa funzione l’immagine data in input viene convertita in formato “HSV” e viene suddivisa in 4 maschere, ed ad ognuna viene applicata la funzione histogram. I risultati vengono salvati in un array features. Inizialmente la nostra scelta era di suddividere l’immagine in 9 maschere, che teoricamente ne avrebbe aumentato la precisione. In fase di testing abbiamo però notato delle maggiori performance della versione a 4 maschere nel nostro Dataset.                                                                                                                                

## EstrazioneFeaturesIsto.py

In questa parte del programma viene applicata la funzione “describe” a tutte le immagini del dataset scelto. I risultati vengono convertiti in stringa e trascritti in un file di tipo csv. Questa nostra scelta è data dalla precedente esperienza nel corso di Programmazione 2, in cui abbiamo brevemente trattato la scrittura su file di tipo csv.
Il Dataset e l’index file viene dato in input grazie ad un Parser.

## ComparatoreIsto.py

In questa parte del programma viene implementata la classe Comparatore che si compone di 3 funzioni:
1. La funzione di inizializzazione
2. La funzione “chi2_distance”: funzione pensata proprio per confrontare istogrammi di colore
3. La funzione “compara”: che prende in input la features dell’immagine query. Questa funzione apre l’index file in lettura, e converte ogni riga (limitata dal carattere “,”) da stringa a float, in modo che le features possano essere confrontate con quelle della query. Le features verranno poi confrontate proprio tramite la funzione “chi2_distance” e i risultati vengono salvati nell’array associativo (tipo dict) “results”.

## Applicazione.py

In questa parte del programma avviene il confronto vero e proprio tra le features e avviene la stampa dei risultati.
L’immagine query viene descritta tramite la funzione “describe” della classe Istogramma e le features ricavate vengono comparate tramite la funzione “compara” della classe “Comparatore”.
I risultati vengono riordinati e limitati e in seguito stampati a video.

# CONFRONTO TRAMITE CONTORNI

## Sift.py

In questa parte del programma viene implementato l’algoritmo Sift. Questa nostra scelta è data in primis dalla semplicità di utilizzo di questo algoritmo ( inizialmente abbiamo avuto difficoltà nell’installazione della libreria xfeatures2d, che ci avrebbe reso possibile implementare funzioni come surf o brief) e inoltre dalle maggiori prestazioni, almeno sulla carta, rispetto all’algoritmo orb.
L’algoritmo è stato poi modificato rispetto alla forma originale per adattarlo alle nostre esigenze.
Si compone di una sola funzione:
1. La funzione “describe”: prende in input un’immagine, la descrive in modo standard tramite l’algoritmo sift. Abbiamo deciso in fase di testing di prendere i migliori 20 keypoints e relativi descrittori in quanto si è rivelato un buon compromesso tra velocità e precisione.                        I descrittori in seguito sono stati “appiattiti” in un’unica grande matrice (128*20 valori), il perché lo vedremo in seguito nella funzione “ComparatoreSift.py”.                                           In seguito abbiamo aggiunto degli zeri alla matrice, in quanto Sift, in caso i keypoints abbiano uguale importanza, ritorna entrambi. Nel nostro Dataset un’immagine ritornava addirittura 22 keypoints, quindi 128*22 valori. Per questo abbiamo reso la dimensione massima pari a 128*23 valori. Nel confronto è importante che ogni matrice abbia la stessa dimensione.

## EstrazioneSift.py

Questa parte del programma è concettualmente uguale a quella precedentemente spiegata nel confronto tramite colore. Abbiamo dovuto però cambiare tipologia di index file per salvare le nostre features: il file di tipo csv non ci permetteva di ripristinare matrici nel processo di confronto,  Quindi abbiamo utilizzato file di tipo “json”. Oltre alle differenze di scrittura dei 2 file, Nell’ EstrazioneSift.py viene applicato un resize all’immagine prima dell’estrazione delle features. Questo perché il metodo di confronto che vedremo in seguito si basa sulla distanza euclidea, quindi immagini di differenti dimensioni ma uguale contenuto avrebbero dato risultati assai diversi.

## ComparatoreSift.py

In questa parte del programma viene implementata la classe ComparatoreSift che si compone di 3 funzioni:
1. La funzione di inizializzazione
2. La funzione “euclidea”, che prende in input le features della query e le features dell’immagine da confrontare, ritornando in output la distanza euclidea delle nostre 2 matrici.                          Di norma con l’algoritmo sift si usano altri metodi di match, il più diffuso è sicuramente il brutal force matcher, che prende un singolo descrittore e lo confronta con tutti gli altri descrittori della seconda immagine. Questo però, oltre a rendere la scrittura su file assai più laboriosa ( sarebbe servito un index file per ogni immagine, complicato da gestire anche nella parte di interfaccia) rende la ricerca estremamente lenta, a volte superando i 10 secondi con il dataset usato come test (230 immagini, quindi molto piccolo). Questo dato, unito alle performance non proprio ottimali dell’algoritmo stesso ci ha fatto virare sulla soluzione descritta in precedenza, che durante i testing ha mostrato prestazioni non inferiori al B.F.M e velocità assai superiore.
3. La funzione “comparaSift”: fino alla fase di testing, questa funzione era concettualmente identica a quella sviluppata per la ricerca tramite colori. A farci modificare la struttura sono stati i molteplici bug in fase di testing, dove immagini apparentemente diverse comparivano in mezzo ai risultati attesi con buona frequenza, lavorare sul dataset sarebbe stato sicuramente efficace, però avrebbe avuto come risultato un’applicazione con buone prestazioni solo nel nostro dataset. Abbiamo notato che queste immagini avevano keypoints in posizioni e differenze di contrasto simili a quelle della query, e quindi avevano distanze euclidee poco minori delle immagini che ci saremmo aspettati in output. La nostra idea a quel punto è stata quella di usare qualcosa che avevamo già sviluppato per eliminare questi bug e rendere la ricerca estremamente precisa. Proprio per questo nella funzione “comparaSift” i risultati non vengono limitati, ma vengono direttamente passati all’applicazione.

## Mixer.py

Concettualmente identica all’ "Applicazione.py” della ricerca tramite colori. Qui però è presente un ciclo for in più, in cui le distanze euclidee e le distanze chi-squared con lo stesso imageID sono sommate, con apporto in media circa del 20% da parte della funzione Istogrammi e 80% da parte della funzione sift (per molte query del dataset sarebbe stato possibile abbassare molto sotto il 20%, ma per avere un buon funzionamento totale su tutte le immagini siamo arrivati a questa soglia). In seguito i risultati totali vengono riordinati e limitati, per poi essere stampati a video.

# CONSIDERAZIONI FINALI    

Abbiamo deciso di presentare 2 metodi di ricerca, quello per Istogrammi e la soluzione mista. Non abbiamo deciso di presentare una soluzione con solo sift in quanto le prestazioni non erano soddisfacenti, e dal punto di vista dello user poco importa l’algoritmo utilizzato e l’implementazionei, l’utente vuole un programma che offra una prestazioni adeguate sia in termini di qualità che di velocità. Le soluzioni che abbiamo presentato soddisfano, a nostro parere, questi requisiti
