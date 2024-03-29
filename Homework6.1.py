люди = [{"ім'я": "Макс", "вік": 15}, {"ім'я": "Оля", "вік": 18}, {"ім'я": "Ігор", "вік": 45}, {"ім'я": "Галя", "вік": 15}, {"ім'я": "Володя", "вік": 22}]

мін_вік = min(люди, key=lambda особа: особа["вік"])["вік"]

наймолодші_імена = [особа["ім'я"] for особа in люди if особа["вік"] == мін_вік]

макс_довжина = len(max(люди, key=lambda особа: len(особа["ім'я"]))["ім'я"])

найдовші_імена = [особа["ім'я"] for особа in люди if len(особа["ім'я"]) == макс_довжина]

загальний_вік = sum(особа["вік"] for особа in люди)
середній_вік = загальний_вік / len(люди)

print(f"Наймолодші люди у цьому списку: {наймолодші_імена}")
print(f"Найдовші імена у цьому списку: {найдовші_імена}")
print(f"Середній вік усіх у цьому списку: {середній_вік}")
