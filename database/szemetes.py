





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


# def query_all_igel_to_list(self):
#     self.list_query_igel.clear()
#     m = session.query(Igel).all()
#     for i in m:
#         self.list_query_igel.addItem(i.name)


# now = datetime.now()
# dt_string = now.strftime("%d_%m_%Y_%H_%M")
# name = self.list_query_igel.currentItem().text()
# igel = session.query(Igel).filter_by(name=name).first()
# can = canvas.Canvas(f"pdf\igel{igel.name}_{dt_string}.pdf")
# can.drawString(100, 750, f"{igel.name} Profil")
# can.drawString(100, 650, f"Name: {igel.name}")
# can.drawString(100, 600, f"Geschlecht: {igel.sex}")
# can.drawString(100, 550, f"Alter: {igel.age} Jahre alt")
# can.drawString(100, 500, f"Gewicht: {igel.weight} Gramm")
# can.drawString(100, 450, f"Kontaktperson: {igel.contacts}")
# can.drawString(100, 400, f"Fundort: {igel.local}")
# can.save()
# webbrowser.open_new(rf"pdf\igel{igel.name}_{dt_string}.pdf")
# # packet = io.BytesIO()
# # can = canvas.Canvas(packet, pagesize=letter)
# # can.drawString(10, 100, "Hello world")
# # can.save()
# #
# # # move to the beginning of the StringIO buffer
# # packet.seek(0)
# #
# # # create a new PDF with Reportlab
# # new_pdf = PdfFileReader(packet)
# # # read your existing PDF
# # existing_pdf = PdfFileReader(open("pdf\igelBubuka_04_12_2022_23_00.pdf", "rb"))
# # output = PdfFileWriter()
# # # add the "watermark" (which is the new pdf) on the existing page
# # page = existing_pdf.getPage(0)
# # page.mergePage(new_pdf.getPage(0))
# # output.addPage(page)
# # # finally, write "output" to a real file
# # outputStream = open("destination.pdf", "wb")
# # output.write(outputStream)
# # outputStream.close()