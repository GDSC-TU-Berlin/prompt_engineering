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
