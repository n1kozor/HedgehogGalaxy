





"""
igel = session.query(Igel).filter_by(name="Sonic").first()
igel_id = igel.id
take_time = session.query(MedicsIgelHistroy).order_by(MedicsIgelHistroy.igel_id).all()

medic_id_list= []
for k in take_time:
    medic_id_list.append(k.medics_id)



igel_name = session.query(Igel).filter_by(id=igel_id).first()

medic_list = []
for j in medic_id_list:
    medic_name = session.query(Medics).filter_by(id=j).first()
    medic_list.append(medic_name.name)

print(f"{igel.name} hat bis jetzt folgende Medikamenten eingenommen: {medic_list}")


"""


