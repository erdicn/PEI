# Experiences 

## 1er essai porte ouverte 2 personnes 

 _____________________________
|							  P (when i say porte ouvert 
| C1		  C2		C3	 |	ou ferme sans ajouter 
F___P_						 |	quelque chose cest cette 
|	  |		TTTTTTTTTTTTTTTTT|	porte quze je parle)
|	  |			  E   R      |
|_____|______________________|

Legende 
	P   : porte 
	F   : fenetre
	T   : table
	C%d : capteur et son numero
	E   : moi(erdi) 
	R   : Raphael

### Initialisations
- 1er arduino 0 
- 2eme arduino 3 min 23 sec
- 3eme arduino 5 min 36 sec 
- A 1 heure 14 min 45 sec jai ouvert la fenetre 
- A 1 heure 51 min  30 sec raphael est promene entre les capteurs jusque a 2 heure 0 0 

void liberer(cell_t* liste){
	cell_t* temp;
	while(liste){
		temp = liste;
		liste = liste->suivant;
		free(temp);
	}
}