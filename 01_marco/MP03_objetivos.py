import pdfplumber, re, pandas as pd

def objetivos(ruta, patrones):
    encontrados = []
    try:
        with pdfplumber.open(ruta) as pdf:
            for n, p in enumerate(pdf.pages, 1):
                t = p.extract_text() or ""
                for pat in patrones:
                    for m in re.finditer(pat, t):
                        encontrados.append({"pagina": n, "codigo": m.group(1).strip(),
                                            "texto": m.group(2).strip()[:180]})
        return pd.DataFrame(encontrados).drop_duplicates(subset=["codigo"])
    except FileNotFoundError:
        print(f"Archivo no encontrado: {ruta}")
        return pd.DataFrame()

PAT_PEI = [r"(OEI\s*\.?\s*\d+)\s*[:.\-]?\s*(.{20,200})",
           r"(AEI\s*\.?\s*[\d.]+)\s*[:.\-]?\s*(.{20,200})"]
PAT_PGD = [r"(O\.?\s?G\.?D\.?\s*\d+|OGD\s*\d+|Objetivo\s+\d+)\s*[:.\-]?\s*(.{20,200})"]

if __name__ == "__main__":
    obj_pei = objetivos("../anexo-000395-2025.pdf", PAT_PEI)
    obj_pgd = objetivos("../anexo-000301-2024.pdf", PAT_PGD)
    
    if not obj_pei.empty: obj_pei.to_csv("MP03_objetivos_pei.csv", index=False)
    if not obj_pgd.empty: obj_pgd.to_csv("MP03_objetivos_pgd.csv", index=False)
    print("Extracción de objetivos completada.")
