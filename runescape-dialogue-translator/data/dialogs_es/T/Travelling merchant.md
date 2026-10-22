# Travelling merchant

- **Original Wiki Page**: [Transcript:Travelling merchant](https://runescape.wiki/w/Transcript%3ATravelling%20merchant)
- **Letter**: `T`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Arriving

- ¡El travelling merchant ha llegado al centro!

### Talk to normally

- El comerciante está demasiado ocupado para hablar ahora.

### Talk to with Travelling Merchant Coupon

- **Travelling merchant:** Ah, veo que tienes uno de mis cupones. Entrégalo y puedo buscar algunas acciones recientes para ti.
- El comerciante sólo realiza un seguimiento de sus existencias de los últimos 30 días. ¿Para qué fecha le gustaría ver las acciones?
- ([runedate 30 days ago]-[runedate yesterday])
- ((If a too early runedate is input:))
  - **Travelling merchant:** No hago un seguimiento de mis existencias desde hace tanto tiempo, lo siento.
- ((If a valid runedate is input:))
  - **CONFIRMACIÓN**
  - Está a punto de cambiar el stock disponible a runedate [runedate] que contiene lo siguiente:
  - - Mapa de la isla inexplorada
  - - [Random item 1]
  - - [Random item 2]
  - - [Random item 3]
  - ¿Quieres continuar?
    - Cancelar
      - (end)
    - OK
      - (Se utiliza un cupón y la tienda de Travelling Merchant se abre con la fecha de ejecución seleccionada).
- ((If the current runedate is input:))
  - **Travelling merchant:** Ya les estoy mostrando el stock de ese día.
- ((If a too late runedate is input:))
  - **Travelling merchant:** Estos cupones no te dan acceso a mis existencias futuras, lo siento.

### Talk to after changing the stock with Travelling Merchant Coupon

- **Travelling merchant:** ¿Tienes todo lo que necesitas? ¿Quieres volver a ver las acciones de hoy?
- {{Colour|#FF0000|Advertencia:}} Esto revertirá las acciones a la fecha actual. Para ver las existencias recientes se necesitará otro cupón.
- **¿VER LAS ACCIONES DE HOY?**
  - Sí.
    - (La tienda de Travelling Merchant se abre con la fecha actual).
  - No.
    - (end)

### Using magical feather on them


#### Sin pergamino antiguo

- **Travelling merchant:** Interesante... ¡Tíralo aquí y te daré algo a cambio!
- El comerciante toma la pluma y, a cambio, te da un pergamino antiguo.
- **Travelling merchant:** Quizás puedas hacer un mejor uso de esta basura.

#### Con pergamino antiguo

- **Travelling merchant:** No necesito otro de esos ahora.

### Leaving

- El travelling merchant ha partido...
