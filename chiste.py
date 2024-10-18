import random

chistes = [
    "¿Por qué los pájaros no usan Facebook? ¡Porque ya tienen Twitter!",
    "¿Qué le dice una iguana a su hermana gemela? ¡Iguanita!",
    "¿Cómo maldice un pollito a otro pollito? ¡¡¡Que te pongan en la olla!!!",
    "¿Qué le dice un jardinero a otro? ¡Disfrutemos mientras podamos!",
    "¿Por qué los esqueletos no pelean entre ellos? Porque no tienen agallas.",
    "¿Qué hace una abeja en el gimnasio? ¡Zum-ba!",
    "¿Cómo se despiden los químicos? ¡Ácido un placer!",
    "¿Qué hace una vaca en un terremoto? ¡Leche agitada!",
]

def contar_chistes():
    while True:
        chiste_aleatorio = random.choice(chistes)
        print(chiste_aleatorio)
        
        respuesta = input("¿Quieres escuchar otro chiste? (si/no): ").strip().lower()
        if respuesta != 'si':
            print("¡Hasta luego! Espero que te hayas reído.")
            break

contar_chistes()
