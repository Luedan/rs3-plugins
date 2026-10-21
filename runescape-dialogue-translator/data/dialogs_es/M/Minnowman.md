# Minnowman

- **Original Wiki Page**: [Transcript:Minnowman](https://runescape.wiki/w/Transcript%3AMinnowman)
- **Letter**: `M`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Overhead

- ((Ocasionalmente se observa uno de los siguientes:))
  - **Minnowman:** {{RSChat|Any spare minnow going?}}
  - **Minnowman:** {{RSChat|I'm here to collect some minnow!}}
  - **Minnowman:** {{RSChat|Oi oi, give us your minnow!}}

### Talk-to

- **Minnowman:** ¿Tienes algún pececillo para mí? Necesito un montón para entregas.
- **Minnowman:** Necesito una pila de [número] para ser precisos.
- ((Sin el pececillo solicitado:))
  - El Minnowman requiere un pececillo magnético [número].
  - ((Repetido en una ventana emergente:))
    - El Minnowman requiere un pececillo magnético [número].
- ((Con el pececillo solicitado:))
  - ((Lo siguiente se muestra en una interfaz titulada "MINNOWMAN":))
    - ¿Quieres regalar el pececillo magnético Minnowman [número]?
      - CANCELAR
        - (end)
      - OK
        - (continue|Hand-in)

### Hand-in


#### Sin el pececillo solicitado

- El Minnowman requiere un pececillo magnético [número].
- ((Repetido en una ventana emergente:))
  - El Minnowman requiere un pececillo magnético [número].

#### Con el pececillo solicitado


##### Si no te han ayudado antes en este encuentro

- (removes=magnetic minnow)
- Ayudas al Minnowman con su situación de pececillo.
- ((Repetido en ventana emergente:))
  - Ayudas al Minnowman con su situación de pececillo.

##### Si ya ayudó antes en este encuentro

- Ya has ofrecido tu ayuda.
- ((Repetido en ventana emergente:))
  - Ya has ofrecido tu ayuda.

### Leaving

- ((Se ve uno de los siguientes y luego continúa a continuación:))
  - **Minnowman:** {{RSChat|I'll be off now, I've got minnow to deliver!}}
  - **Minnowman:** {{RSChat|Thanks for the minnow chaps}}
- ((Si el player ayudó:))
  - Serás recompensado por ayudar al muñeco pececillo: recibirás 1940 Fishing XP.
