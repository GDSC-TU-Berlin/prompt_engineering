from time import sleep



def test_get_capital(fun):
    solution = {'Deutschland': ["Berlin"], "Frankreich": ["Paris"], "Spanien": ["Madrid"], "Italien": ["Rom"],
                "Schweiz": ["Bern"], "Österreich": ["Wien"], "Polen": ["Warschau"], "Tschechien": ["Prag"],
                "Dänemark": ["Kopenhagen"], "Niederlande": ["Amsterdam"], "Belgien": ["Brüssel"],
                "Kanada": ["Ottawa"], "Mexiko": ["Mexiko-Stadt"], "Brasilien": ["Brasília"],
                "Argentinien": ["Buenos Aires"],
                "China": ["Peking", "Beijing"], "Japan": ["Tokio", "Tokyo"],
                "Indien": ["Neu-Delhi", "Neu Delhi", "New Delhi", "New-Delhi"],
                "Russland": ["Moskau"],
                "USA": ["Washington D.C.", "Washington D", "Washington, D"]}

    correct = 0
    for country, capital in solution.items():
        for i in range(3):
            pred = fun(country)
            if pred not in capital:
                print(f"Die Hauptstadt von {country} ist {pred}.")
            else:
                correct += 1

    print(f"Correct: {correct}/{len(solution) * 3}")


def test_knobel_aufgaben(fun, client, rep=1):
    if rep > 5:
        print(" rep > 5 is not allowed.")
        return

    solutions = {
        "Du schaust auf ein Portrait und ich sage Dir: Der Vater der Person auf dem Potrait ist der Sohn meines Vaters, aber ich habe keine Geschwister. Wessen Bild schaust Du an?": "Das Bild meines Kindes.",
        "Stell dir ein imaginaires Dorf vor welches mehr Einwohner hat als die Person mit den meistenb Haaren auf dem Kopf. Stell Dir außerdem vor, dass kein Einwohner eine Glatze hat. Kann es sein, dass keine zwei Einwohner die gleiche Anzahl von Haaren haben?": "Nein, das ist nicht möglich.",
        "Darf nach Ansicht der kanadischen Kirche ein Mann die Schwester seiner Witwe heiraten?": "Der Mann ist tot, also ist es egal.",
        "Vor Dir stehen 2 Kisten und genau eine davon enthält einen Schatz. Beide Kisten tragen eine Aufschrift mit eindeutigen Wahrheitswert und die Situation enthält keinen Widerspruch. Kiste 1: Genau eine der beiden Aussagen ist wahr. Kiste 2 sagt: Ich enthalte nicht den Schatz. Wo ist der Schatz?": "In Kiste 2."
    }

    correct = 0
    for (i, (question, solution)) in enumerate(solutions.items()):
        c = 0
        for _ in range(rep):
            sleep(3)
            pred = fun(question)

            response = client.chat.completions.create(
                model="gpt-4-1106-preview",
                messages=[
                    {
                        "role": "assistant",
                        "content": f"Du bist ein Lehrer und bewertest die Antwort eines Schüler auf die Frage: {question}. Die richtige Antwort lautet: {solution}. Dies ist außerdem die einzig richtige Antwort. Gebe eine konstruktive Kritik an die Antwort des Schülers. Außerdem sage am Ende falls die Antwort richtig war, KORREKT und falls nicht FALSCH."
                    },
                    {
                        "role": "user",
                        "content": f"{pred}"
                    },
                ]
            )

            res = response.choices[0].message.content.strip()
            if "KORREKT" in res:
                correct += 1
                c += 1
        print(f"Fortschritt: {i + 1}/{len(solutions)}. Ergebnisse für dieses Rätsel: {c}/{rep}")
    print(f"Correct: {correct}/{len(solutions) * rep}")
