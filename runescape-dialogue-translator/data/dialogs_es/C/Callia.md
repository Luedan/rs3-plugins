# Callia

- **Original Wiki Page**: [Transcript:Callia](https://runescape.wiki/w/Transcript%3ACallia)
- **Letter**: `C`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Upon entering the farm after Callia has attempted to store a new animal


#### Con suficiente espacio en su almacenamiento.

- Uno de tus peones tiene un nuevo animal sin control para ti.

#### Sin suficiente espacio en su almacenamiento


##### Debido a que el huevo es de una especie diferente.

- Su corral de cría está lleno y su peón recolector no pudo contener esta especie en particular: [species name]. Recoge tu bolígrafo o coleccionista para volver a criar esa especie.

##### Debido a que ya tiene diez huevos.

- Su corral de cría está lleno y su peón coleccionista no pudo contener más de: [species name]. Recoge tu bolígrafo o coleccionista para volver a criar esa especie.

### Collect

- (Condition: If the player has inventory space:)
  - (receives=animals)
- (Condition: If the player does not have inventory space:)
  - **Callia:** No tienes suficiente espacio en tu backpack para coleccionar estas bellezas, regresa cuando tengas más espacio.
- (Condition: If Callia does not have animals:)
  - **Callia:** No tengo nada nuevo para ti actualmente.

### Check

- (Condition: If Callia has animals:)
  - Callia tiene lo siguiente para usted:
  - [Type of animal] (sin marcar): [número].
- (Condition: If Callia does not have animals:)
  - Callia actualmente no tiene ningún animal para usted.
