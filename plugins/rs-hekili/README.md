# RS Hekili - Asistente de Rotación de Combate (RuneScape 3)

Inspirado en el mítico addon **Hekili** de World of Warcraft, este plugin proyecta sobre el área de juego una cola visual con las próximas habilidades óptimas que debes lanzar según tus recursos, enfriamientos (cooldowns) y nivel actual.

---

## 🧙‍♂️ Habilidades Soportadas (Magia)
Se adapta automáticamente a tu nivel de Magia actual:
* **Nivel 1: Wrack** (Tecla `[1]`): Habilidad de relleno rápido (3s cooldown). Inflige 188% de daño si el objetivo está aturdido.
* **Nivel 12: Sonic Wave** (Tecla `[2]`): Daño sólido y +6% de puntería en el próximo ataque.
* **Nivel 15: Impact** (Tecla `[3]`): Aturde e inmoviliza al enemigo. **¡Prepara el combo para duplicar el daño de Wrack!**
* **Nivel 18: Dragon Breath** (Tecla `[4]`): Ataque masivo en área (188% daño). Se activa automáticamente en cuanto subas a nivel 18.
* **Nivel 34: Combust** (Tecla `[5]`): Daño de sangrado prolongado.
* **Nivel 45: Asphyxiate** (Tecla `[Q]`): Umbral de alto daño canalizado.

---

## 🖥️ El HUD en Pantalla
* **Ranura 1 (Grande con borde dorado)**: La habilidad óptima que debes presionar **YA**. Muestra el nombre y la tecla asignada (ej: `[3]` para Impact).
* **Ranuras 2 y 3 (Menores)**: Las siguientes habilidades en la cola para los próximos ticks de combate.

---

## 🎮 Cómo Probarlo en RuneScape Beta
1. Sincroniza desde Git Bash:
   ```bash
   ./rs.sh sync rs-hekili
   ```
2. En la consola del juego (**`ALT` + `` ` ``**):
   ```text
   prf
   pon rs-hekili
   ```
3. Verás aparecer el HUD sobre el centro inferior de tu pantalla recomendando tu combo óptimo (`Impact` -> `Wrack` -> `Sonic Wave`).
