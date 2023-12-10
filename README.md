# KURSA_DARBSSSS
VISS BEDIGI


## Sludinājumu Lietojumprogramma

### Galvenā informācija
Programma ar GUI , kas ļauj izveidot, rediģēt un dzēst sludinājumus par automašīnām.

### Funkcijas un to apraksti

#### `create_table()`
Funkcija, kas izveido datubāzes tabulu sludinājumiem, ja tāda neeksistē. Tā veic datubāzes inicializāciju.

#### `create_ad()`
Funkcija, kas izveido sākotnējo lietojumprogrammas logu un ļauj izveidot jaunu sludinājumu.

#### `open_create_ad_window()`
Funkcija, kas atver jaunu logu sludinājuma izveidei. Šajā logā lietotājs var ievadīt jaunā sludinājuma informāciju.

#### `save_ad(kategorija, marka, modelis, izlaiduma_gads, motors, motora_tilpums, atrumkarba, nobraukums, krasa, virsbuves_tips, tehniska_apskate, cena, apraksts)`
Funkcija, kas saglabā jauno sludinājumu datubāzē, pārbaudot un validējot ievadīto informāciju.

#### `edit_ad(ad_id)`
Funkcija, kas atver rediģēšanas logu un ļauj mainīt esošā sludinājuma informāciju, izmantojot sludinājuma ID.

#### `update_ads()`
Funkcija, kas atjauno sludinājumu sarakstu galvenajā logā, pārveidojot pogas sludinājumu parādīšanai.

#### `delete_ad(ad_id)`
Funkcija, kas nodzēš izvēlēto sludinājumu pēc tā ID.

#### `show_ad(ad)`
Funkcija, kas parāda detalizētu informāciju par konkrētu sludinājumu, to izmantojot kā parametru.

### Bibliotēkas un izmantojamās tehnoloģijas
- `tkinter`: Izmantots GUI izveidei
- `sqlite3`: Lietots datubāzes darbībām

### Kā lietot lietojumprogrammu
1. Palaist programmu
2. Izmantojiet pogas, lai izveidotu jaunus sludinājumus, rediģētu esošos vai dzēstu tos.

### Kļūdu apstrāde
Lietojumprogramma veic datu validāciju un informē lietotāju par iespējamām kļūdām, ja ievadītie dati neatbilst prasībām.

### Atbalstītie datu formāti un prasības
- Ievadlaukos pieņemti dažādi datu formāti, piemēram, teksti, cipari, teksta rindas, un tiek veikta atbilstoša validācija.

### Izvadīšana
Programma attēlo sludinājumu sarakstu un detalizētu informāciju par sludinājumu atsevišķā logā.

### Autors
- Izstrādātājs: OLEGS NEČIPARENKO
