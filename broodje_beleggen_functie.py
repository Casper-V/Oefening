def broodje_beleggen(grootte, *broodbeleg):
	"""print een overzicht van een of meer items beleg die zijn besteld voor een broodje"""
    print(broodbeleg)
    print(f"Je hebt een {grootte} broodje besteld met:")
    for beleg in broodbeleg:
        print(f"- {beleg}")