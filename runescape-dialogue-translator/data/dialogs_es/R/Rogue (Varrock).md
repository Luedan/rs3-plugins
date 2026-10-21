# Rogue (Varrock)

- **Original Wiki Page**: [Transcript:Rogue (Varrock)](https://runescape.wiki/w/Transcript%3ARogue%20%28Varrock%29)
- **Letter**: `R`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In the Rogues' Castle

- **Pícaro:** ¿Has venido a sacarme de aquí?
- Seleccione una opción
  - ¿Por qué estás encerrado aquí?
    - **Player:** ¿Por qué estás encerrado aquí?
    - **Pícaro:** Solía ser parte del grupo de pícaros aquí, hasta que me acusaron de haber robado el oro que le habíamos robado a personas que previamente se lo habían robado a otra persona.
    - **Player:** ¿Entonces te encerraron?
    - **Pícaro:** Sí, seguí diciéndoles que no robé nada, pero simplemente se negaron a creerme.
    - **Player:** Entonces, ¿lo robaste?
    - **Pícaro:** ¡Ese no es el punto! Lo importante es que dije que no.
    - **Player:** Eh... ya veo.
    - **Pícaro:** Entonces, ¿has venido a liberarme o qué?
    - Seleccione una opción
      - Sí, lo tengo.
        - (continue|Yes)
      - No, no lo he hecho.
        - (continue|No)
  - Sí, lo tengo.
    - **Player:** Sí, lo he hecho. Las puertas estaban cerradas pero usé este anillo mágico para viajar a un reino paralelo donde todos los cambios recientes son opuestos al otro lado. Entonces, al cerrar las puertas allí, abrí las puertas que él-
    - **Pícaro:** Hombre, ¿rompiste las puertas con la cabeza o qué? De todos modos, agradezco la ayuda, hombre. Si alguna vez necesitas algo, ven a verme a mi casa en Varrock. Tengo un negocio que podría interesarte.
    - **Player:** ¿Dónde está Varrock?
    - **Pícaro:** Suponiendo que no haya sido ocupado por ninguno de los atracadores, tengo un lugar en las partes no tan agradables de la ciudad, justo detrás de la tienda de tiro con arco. Ven a verme allí. De todos modos, tengo que correr ahora antes de que mis supuestos compañeros se den cuenta de lo que tú y tu cabeza dura habéis hecho.
    - El prisionero se escapa del castillo y se dirige al sur hacia Varrock.
    - (Action: La pantalla se vuelve negra y luego vuelve a aparecer; el pícaro se ha ido.)
  - No, no lo he hecho.
    - **Player:** No, no lo he hecho. Sólo estoy aquí para asegurarme de que no hayas conseguido nada para comer.
    - **Pícaro:** Oh, hombre, te lo sigo diciendo, yo no robé el oro. Sólo déjame salir.
    - **Player:** Eh...no.

### In Varrock


#### Hablando con el pícaro

- **Pícaro:** Bienvenido a mi humilde morada. ¿Qué puedo hacer por ti?
- Seleccione una opción
  - Mencionaste un negocio.
    - **Player:** Arriba en el Castillo de los Pícaros, mencionaste un negocio. ¿Qué fue eso?
    - **Pícaro:** Ah, sí, corro... ¿cómo se llama? Algo así como un pequeño negocio de joyería. Entonces, si te encuentras con alguna joya de oro no encantada, con mucho gusto te la quitaré por una suma decente de coins.
    - **Player:** ¿Solo joyas de oro?
    - **Pícaro:** Correcto. No compraré nada que no sea dorado hermoso y brillante. Mis... eh... los clientes son exigentes con eso.
    - Seleccione una opción
      - Tengo algunos aquí.
        - **Player:** Tengo algunos aquí.
        - **Pícaro:** Bien, bien, solo entrégalo y veré qué puedo dar por él.
      - Muy bien, lo recordaré.
        - **Player:** Muy bien, lo recordaré.
  - Nada.
    - **Player:** Nada.

#### Vender artículos


##### Usar un artículo en el pícaro que no compra

- **Pícaro:** Lo siento, pero no me ocupo de eso. Sólo vendo joyas de oro no encantadas, nada más. Trae notas si quieres, pero prefiero el trato real.

##### Vender un solo artículo

- **Pícaro:** Te daré [price] coins por ese [item]. ¿Tenemos un trato?
- Seleccione una opción
  - Sí, lo hacemos.
    - (removes=the piece of gold jewellery used on the rogue) (receives=the number of gold coins stated above)
    - **Rogue:** Fue un placer hacer negocios contigo. Vuelve si tienes más joyas para vender.
  - No, no lo hacemos.
    - **Player:** No, no lo hacemos.

##### Vender varios artículos


##### Si hay más de 10,000 elementos en la pila

- **Pícaro:** ¡Vaya, qué joyas tienes ahí! Intente mantenerlo en cantidades inferiores a 10.000. Los grandes números me duelen la cabeza.

##### Si hay 10,000 o menos elementos en la pila


##### Si el player no tiene 100.000.000 coins

- **Pícaro:** Qué buen [item] tienes ahí. Te daré [price] por el grupo. ¿Tenemos un trato?
- Seleccione una opción
  - Sí, lo hacemos.
    - (removes=all pieces of the type of gold jewellery used on the rogue) (receives=the number of gold coins stated above)
    - **Rogue:** Fue un placer hacer negocios contigo. Vuelve si tienes más joyas para vender.
  - No, no lo hacemos.
    - **Player:** No, no lo hacemos.

##### Si el player tiene al menos 100.000.000 coins

- **Pícaro:** Ya tienes suficiente dinero. Normalmente no me molesta, pero ahora estás siendo absurdo.
