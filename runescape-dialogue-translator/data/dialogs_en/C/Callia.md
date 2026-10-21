# Callia

- **Original Wiki Page**: [Transcript:Callia](https://runescape.wiki/w/Transcript%3ACallia)
- **Letter**: `C`

---

## Dialogue Transcript


### Upon entering the farm after Callia has attempted to store a new animal


#### With sufficient space in her storage

- One of your farmhands has a new unchecked animal for you.

#### Without sufficient space in her storage


##### Due to the egg being a different species

- Your breeding pen is full and your collector farmhand couldn't hold this particular species: [species name]. Collect your pen or collector to breed that species again.

##### Due to her already holding ten eggs

- Your breeding pen is full and your collector farmhand couldn't hold any more of: [species name]. Collect your pen or collector to breed that species again.

### Collect

- (Condition: If the player has inventory space:)
  - (receives=animals)
- (Condition: If the player does not have inventory space:)
  - **Callia:** You don't have enough space in your backpack to collect these beauties, come back when you've got more space.
- (Condition: If Callia does not have animals:)
  - **Callia:** I've got nothing new for you currently.

### Check

- (Condition: If Callia has animals:)
  - Callia holds the following for you:
  - [Type of animal] (unchecked): [number].
- (Condition: If Callia does not have animals:)
  - Callia is not currently holding any animals for you.
