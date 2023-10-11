results, links, collection, grade = scrape(["MP5-SD | Kitbash", "Tec-9 | Brother", "Galil AR | Connexion",
                        "MAG-7 | Monster Call", "MAC-10 | Allure"], 0.093)

ev_calc(results[0]['x_sum'], results[0]['y_mean'], collection, grade)
#email(results,links)
