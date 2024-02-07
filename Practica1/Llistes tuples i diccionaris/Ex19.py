areas_pis = ["Menjador", 10.15, "Rebedor", 9.56, "Habitació1", 12.34, "Terrassa", 15.55, "Lavabo", 7.98, "Cuina", 12, "Habitació2", 12.23]

print(f"El segon element: {areas_pis[1]}")

print(f"L' ultim element: {areas_pis[-1]}")

index_terrassa = areas_pis.index("Terrassa")
area_terrassa = areas_pis[index_terrassa + 1] 
print(f"La terrassa: {area_terrassa}")

print(f"Del primer al tercer element: {areas_pis[:3]}")

print(f"Del tercer element a l'últim: {areas_pis[2:]}")

area_habitacion1 = areas_pis[areas_pis.index("Habitació1") + 1]
area_habitacion2 = areas_pis[areas_pis.index("Habitació2") + 1]
total_area_habitaciones = area_habitacion1 + area_habitacion2
print(f"Total de l'àrea de les dues habitacions: {total_area_habitaciones}")

areas_pis[areas_pis.index("Lavabo") + 1] = 8.5
print(f"Nova list area amb l'àrea modificada del lavabo: {areas_pis}")

areas_pis.extend(["pati interior", 2.78])
print(f"Nova list area amb l'àrea de 'pati interior' i 2.78 afegides: {areas_pis}")

total_area_pis = sum([areas_pis[i + 1] for i in range(0, len(areas_pis), 2)])
print(f"Total de l'àrea del pis: {total_area_pis}")
