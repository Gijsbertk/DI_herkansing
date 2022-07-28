# DI_herkansing
herkansing van Data integratie github.
Deze applicatie fetcht data uit PDFs van patienten en annoteert VCF bestanden van patienten. Hierna vult de applicatie de opgehaalde informatie in, in een database. Als laatst haalt die concept IDs op, afkomend van Athena om deze weer te linken aan informatie opgehaald uit de PDFs en VCFs. 

# Hoe gebruik je deze applicatie?
In deze GITHUB of ZIP staan verschillenden mappen, in de DOCs map staat de logica uitgelegd van de mapping, deze is niet nodig voor het gebruik van de scripts. De enige mappen die nodig zijn is de data map en de map met de code. De code haal je allemaal op en open je stuk voor stuk  in een project in je IDE van keuze (Bijv. Pycharm), hetzelfde doe je met alle data. Dus de database_data en de SNP_eff_data, deze open je in hetzelfde project, om daarna het project te runnen, activeer je de workflow.py en alles doet het.  
