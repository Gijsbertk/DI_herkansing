import subprocess, re

def snpeff(snpeff_output_files):
    """
    Snpeff kan via deze functie aangeroepen worden.
    Dit werkt alleen als het script vanuit een Linux Terminal aangeroepen wordt
    :param output_files: Een list met alle namen van de output files die gemaakt moeten worden
    :type output_files: list
    """
    for bestand in snpeff_output_files:
        nummer = re.findall(r"00..", bestand) #vindt het participantnummer in elk meegegeven bestand
        with open(bestand, "w") as snpeff_output: #schrijft naar een nieuw bestand als output file
            completed_process = subprocess.run(
                [
                    "conda", "run", "snpEff", "-Xmx8g", "GRCh37.75", "-no-downstream", "-no-intergenic",
                    "-no-intron", "-no-upstream", "-no-utr", "-verbose", "-noStats",
                    "files/PGPC_" + "".join(nummer) + "_S1.flt.vcf21",
                ], #het snpeff-commando met alle bijbehorende variabelen
                stdout=snpeff_output
            )

def main():
    snpeff_output_files = ["files/PGPC_0006.chr21.snpEff.vcf", "files/PGPC_0052.chr21.snpEff.vcf"]
    snpeff(snpeff_output_files)
main()
