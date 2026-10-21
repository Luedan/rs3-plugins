local Dictionary = {}

-- Frases exactas de diálogos de NPCs, opciones de respuesta y mensajes del juego
Dictionary.exact = {
    -- Diálogo específico de Hans (capturas del usuario)
    ["You are in Lumbridge Castle."] = "Estás en Lumbridge Castle.",
    ["You're in Lumbridge Castle."] = "Estás en Lumbridge Castle.",
    ["Hello. What are you doing here?"] = "Hola. ¿Qué estás haciendo aquí?",
    ["What are you doing here?"] = "¿Qué estás haciendo aquí?",
    ["I'm looking for whoever is in charge of this place."] = "Estoy buscando a quien esté a cargo de este lugar.",
    ["I have come to kill everyone in this castle!"] = "¡He venido a matar a todos en este castillo!",
    ["I don't know. I'm lost. Where am I?"] = "No lo sé. Estoy perdido. ¿Dónde estoy?",
    ["Can you tell me how long I've been playing?"] = "¿Puedes decirme cuánto tiempo he estado jugando?",
    ["This is Lumbridge Castle."] = "Este es el castillo de Lumbridge.",
    ["Who is in charge of this place?"] = "¿Quién está a cargo de este lugar?",
    ["I'm in charge of supervising this castle."] = "Estoy a cargo de supervisar este castillo.",
    ["I have been here for a long time."] = "He estado aquí durante mucho tiempo.",

    -- Botones de diálogo
    ["Click here to continue"] = "Haz clic aquí para continuar",
    ["Press Space to continue"] = "Presiona Espacio para continuar",
    ["Select an option"] = "Selecciona una opción",
    ["Choose an option"] = "Elige una opción",
    ["Please wait..."] = "Por favor espera...",

    -- Saludos y aperturas de diálogo
    ["Greetings, adventurer!"] = "¡Saludos, aventurero!",
    ["Greetings, adventurer."] = "Saludos, aventurero.",
    ["Greetings!"] = "¡Saludos!",
    ["Hello there!"] = "¡Hola!",
    ["Hello there."] = "Hola.",
    ["Hello, adventurer."] = "Hola, aventurero.",
    ["Hello."] = "Hola.",
    ["Welcome, traveller."] = "Bienvenido, viajero.",
    ["Welcome to Lumbridge!"] = "¡Bienvenido a Lumbridge!",
    ["How can I help you today?"] = "¿Cómo puedo ayudarte hoy?",
    ["What can I do for you today?"] = "¿Qué puedo hacer por ti hoy?",
    ["What can I do for you?"] = "¿Qué puedo hacer por ti?",
    ["What brings you here?"] = "¿Qué te trae por aquí?",
    ["What would you like to know?"] = "¿Qué te gustaría saber?",
    ["Can I help you with something?"] = "¿Puedo ayudarte en algo?",
    ["Is there something you need?"] = "¿Hay algo que necesites?",
    ["Good day to you."] = "Buen día tengas.",
    ["Good day, adventurer."] = "Buen día, aventurero.",

    -- Opciones del jugador (menús de respuesta)
    ["I am looking for a quest."] = "Estoy buscando una misión.",
    ["I'm looking for a quest."] = "Estoy buscando una misión.",
    ["Do you have any quests for me?"] = "¿Tienes alguna misión para mí?",
    ["What is this place?"] = "¿Qué es este lugar?",
    ["Can you tell me about this place?"] = "¿Puedes hablarme sobre este lugar?",
    ["Who are you?"] = "¿Quién eres?",
    ["What do you do here?"] = "¿A qué te dedicas aquí?",
    ["Can you help me?"] = "¿Puedes ayudarme?",
    ["I'd like to ask you something."] = "Me gustaría preguntarte algo.",
    ["I have a question."] = "Tengo una pregunta.",
    ["Tell me more."] = "Cuéntame más.",
    ["Let's talk about something else."] = "Hablemos de otra cosa.",
    ["Goodbye."] = "Adiós.",
    ["Farewell."] = "Hasta luego.",
    ["I must be going."] = "Debo marcharme.",
    ["I have to go now."] = "Tengo que irme ahora.",
    ["Yes, please."] = "Sí, por favor.",
    ["No, thank you."] = "No, gracias.",
    ["No, thanks."] = "No, gracias.",
    ["Yes."] = "Sí.",
    ["No."] = "No.",
    ["Sure."] = "Seguro.",
    ["Never mind."] = "Olvídalo.",
    ["Thank you."] = "Gracias.",
    ["Thanks."] = "Gracias.",
    ["Thank you for your help."] = "Gracias por tu ayuda.",
    ["I'm fine, thanks."] = "Estoy bien, gracias.",

    -- Diálogos de Lumbridge Sage
    ["I am the Lumbridge Sage. How may I guide you?"] = "Soy el Lumbridge Sage. ¿Cómo puedo guiarte?",
    ["Where should I start my adventures?"] = "¿Dónde debería comenzar mis aventuras?",
    ["What should I do?"] = "¿Qué debería hacer?",
    ["Can you teach me the basics?"] = "¿Puedes enseñarme lo básico?",

    -- Mensajes del sistema y acciones comunes
    ["Nothing interesting happens."] = "No sucede nada interesante.",
    ["The door is locked."] = "La puerta está cerrada con llave.",
    ["It's locked."] = "Está cerrado con llave.",
    ["You cannot reach that."] = "No puedes alcanzar eso.",
    ["You can't reach that."] = "No puedes alcanzar eso.",
    ["Your inventory is too full to hold any more."] = "Tu inventario está demasiado lleno para guardar más.",
    ["Your inventory is full."] = "Tu inventario está lleno.",
    ["You don't have enough inventory space."] = "No tienes suficiente espacio en el inventario.",
    ["You don't have enough energy to run."] = "No tienes suficiente energía para correr.",
    ["You are too tired to run."] = "Estás demasiado cansado para correr.",
    ["It heals some health."] = "Restaura algo de salud.",
    ["You eat the food."] = "Te comes la comida.",
    ["It tastes delicious."] = "Sabe delicioso.",
    ["You're already in combat!"] = "¡Ya estás en combate!",
    ["You are already in combat."] = "Ya estás en combate.",
    ["You cannot do that right now."] = "No puedes hacer eso en este momento.",
    ["You need to be out of combat to do that."] = "Necesitas estar fuera de combate para hacer eso.",
    ["I can't reach that!"] = "¡No puedo alcanzar eso!",
    ["There is nothing here to see."] = "No hay nada que ver aquí.",
    ["You attempt to pick the lock."] = "Intentas forzar la cerradura.",
    ["You manage to pick the lock."] = "Consigues forzar la cerradura.",
    ["You fail to pick the lock."] = "Fallas al forzar la cerradura."
}

-- Patrones dinámicos (sustituciones con comodines)
Dictionary.patterns = {
    -- Diálogos y explicaciones de NPCs
    { pat = "^You are in (.-)%.$", rep = "Estás en %1." },
    { pat = "^You're in (.-)%.$", rep = "Estás en %1." },
    { pat = "^You are at (.-)%.$", rep = "Estás en %1." },
    { pat = "^This is (.-)%.$", rep = "Este es %1." },
    { pat = "^Welcome to (.-)!$", rep = "¡Bienvenido a %1!" },
    { pat = "^Welcome to (.-)%.$", rep = "Bienvenido a %1." },
    { pat = "^I am (.-)%.$", rep = "Soy %1." },
    { pat = "^I'm (.-)%.$", rep = "Soy %1." },

    -- Acciones sobre objetos del entorno
    { pat = "^You search the (.-) and find nothing%.$", rep = "Registras el %1 y no encuentras nada." },
    { pat = "^You search the (.-) and find (.-)%.$", rep = "Registras el %1 y encuentras %2." },
    { pat = "^You search the (.-)%.$", rep = "Registras el %1." },
    { pat = "^You open the (.-)%.$", rep = "Abres el %1." },
    { pat = "^You close the (.-)%.$", rep = "Cierras el %1." },
    { pat = "^You unlock the (.-)%.$", rep = "Abres con llave el %1." },
    { pat = "^The (.-) is locked%.$", rep = "El %1 está cerrado con llave." },

    -- Habilidades y profesiones
    { pat = "^You swing your pickaxe at the (.-)%.$", rep = "Golpeas con tu pico la %1." },
    { pat = "^You mine some (.-)%.$", rep = "Extraes algo de %1." },
    { pat = "^You manage to mine some (.-)%.$", rep = "Consigues extraer algo de %1." },
    { pat = "^You chop down the (.-)%.$", rep = "Talas el %1." },
    { pat = "^You get some (.-)%.$", rep = "Obtienes algo de %1." },
    { pat = "^You catch a (.-)%.$", rep = "Atrapas un %1." },
    { pat = "^You catch some (.-)%.$", rep = "Atrapas algo de %1." },
    { pat = "^You successfully cook the (.-)%.$", rep = "Cocinas con éxito el %1." },
    { pat = "^You accidentally burn the (.-)%.$", rep = "Quemas accidentalmente el %1." },
    { pat = "^You eat the (.-)%.$", rep = "Te comes el %1." },
    { pat = "^You drink a dose of (.-)%.$", rep = "Bebes una dosis de %1." },
    { pat = "^You light the (.-)%.$", rep = "Enciendes el %1." },
    { pat = "^The fire catches and the (.-) begins? to burn%.$", rep = "El fuego prende y el %1 comienza a arder." },

    -- Requisitos y bloqueos
    { pat = "^You need a (.-) to do that%.$", rep = "Necesitas un %1 para hacer eso." },
    { pat = "^You need a (.-) to cut this tree%.$", rep = "Necesitas un %1 para talar este árbol." },
    { pat = "^You don't have enough (.-)%.$", rep = "No tienes suficiente %1." },
    { pat = "^You need level (%d+) (.-) to do that%.$", rep = "Necesitas nivel %1 en %2 para hacer eso." },
    { pat = "^You need a level of (%d+) in (.-) to do this%.$", rep = "Necesitas nivel %1 en %2 para hacer esto." },

    -- Preguntas y opciones de diálogo
    { pat = "^Can you teach me about (.-)%?$", rep = "¿Puedes enseñarme acerca de %1?" },
    { pat = "^Can you tell me about (.-)%?$", rep = "¿Puedes hablarme acerca de %1?" },
    { pat = "^Tell me about (.-)%.$", rep = "Háblame sobre %1." },
    { pat = "^Talk to me about (.-)%.$", rep = "Háblame acerca de %1." },
    { pat = "^I need help with (.-)%.$", rep = "Necesito ayuda con %1." },
    { pat = "^What can you tell me about (.-)%?$", rep = "¿Qué puedes decirme sobre %1?" },

    -- Diálogos dinámicos de Hans (tiempo jugado)
    { pat = "^You've spent (%d+) days?, (%d+) hours?, (%d+) minutes? in the world since you arrived (%d+) days? ago%.$", rep = "Has pasado %1 días, %2 horas, %3 minutos en el mundo desde que llegaste hace %4 días." },
    { pat = "^You've spent (%d+) hours?, (%d+) minutes? in the world since you arrived (%d+) days? ago%.$", rep = "Has pasado %1 horas, %2 minutos en el mundo desde que llegaste hace %3 días." },
    { pat = "^You've spent (%d+) days?, (%d+) hours? in the world since you arrived (%d+) days? ago%.$", rep = "Has pasado %1 días, %2 horas en el mundo desde que llegaste hace %3 días." },
    { pat = "^You've spent (%d+) days? in the world since you arrived (%d+) days? ago%.$", rep = "Has pasado %1 días en el mundo desde que llegaste hace %2 días." },

    -- Descripciones de examinar (Examines)
    { pat = "^A sturdy (.-)%.$", rep = "Un resistente %1." },
    { pat = "^A large (.-)%.$", rep = "Un gran %1." },
    { pat = "^A small (.-)%.$", rep = "Un pequeño %1." },
    { pat = "^An ancient (.-)%.$", rep = "Un antiguo %1." }
}

return Dictionary
