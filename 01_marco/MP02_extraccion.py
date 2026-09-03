import pdfplumber, re, pandas as pd

def estructura(ruta, patron_titulo=r"^\s*(\d+(?:\.\d+)*)\s+([A-ZÁÉÍÓÚÑ][^\n]{4,90})$"):
    """Extrae el índice real del documento a partir de sus encabezados numerados."""
    filas = []
    try:
        with pdfplumber.open(ruta) as pdf:
            for n, pagina in enumerate(pdf.pages, 1):
                texto = pagina.extract_text() or ""
                for linea in texto.split("\n"):
                    m = re.match(patron_titulo, linea.strip())
                    if m:
                        filas.append({"pagina": n, "numeral": m.group(1),
                                      "titulo": m.group(2).strip(),
                                      "nivel": m.group(1).count(".") + 1})
        return pd.DataFrame(filas).drop_duplicates(subset=["numeral","titulo"])
    except FileNotFoundError:
        print(f"Archivo no encontrado: {ruta}")
        return pd.DataFrame()

if __name__ == "__main__":
    pei = estructura("../anexo-000395-2025.pdf")
    pgd = estructura("../anexo-000301-2024.pdf")
    if not pei.empty: pei.to_csv("MP02_estructura_pei.csv", index=False)
    if not pgd.empty: pgd.to_csv("MP02_estructura_pgd.csv", index=False)
    print("Extracción completada.")
