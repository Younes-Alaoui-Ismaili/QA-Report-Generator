import pandas as pd
from fpdf import FPDF

# Charger les données Excel
def load_excel(file_name):
    return pd.read_excel(file_name)

# Analyser les résultats des tests
def analyze_results(df):
    total = len(df)
    passed = len(df[df['Statut'] == 'Réussi'])
    failed = len(df[df['Statut'] == 'Échoué'])
    return total, passed, failed

# Générer un rapport Excel mis à jour
def update_excel(file_name, df, total, passed, failed):
    summary = {
        "Total Tests": total,
        "Tests Réussis": passed,
        "Tests Échoués": failed
    }
    summary_df = pd.DataFrame([summary])
    with pd.ExcelWriter(file_name, mode='a', engine='openpyxl') as writer:
        summary_df.to_excel(writer, sheet_name="Résumé", index=False)

# Générer un rapport PDF
def generate_pdf(total, passed, failed):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Rapport de Tests", ln=True, align='C')
    pdf.cell(200, 10, txt=f"Total Tests : {total}", ln=True)
    pdf.cell(200, 10, txt=f"Tests Réussis : {passed}", ln=True)
    pdf.cell(200, 10, txt=f"Tests Échoués : {failed}", ln=True)
    pdf.output("rapport_de_tests.pdf")

# Exécution principale
if __name__ == "__main__":
    file_name = "test_cases.xlsx"  # Assure-toi que ce fichier est dans le même dossier
    df = load_excel(file_name)
    total, passed, failed = analyze_results(df)
    update_excel(file_name, df, total, passed, failed)
    generate_pdf(total, passed, failed)
    print("Rapport généré avec succès !")
