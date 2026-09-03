import pandas as pd

try:
    a = pd.read_csv("MP04_articulacion.csv")
    n = len(a)
    print(f"Objetivos del PGD analizados            : {n}")
    print(f"Declaran articulación con el PEI        : {(a.iloc[:,1]=='Sí').sum()} ({(a.iloc[:,1]=='Sí').mean():.0%})")
    print(f"Articulación VERIFICABLE en el texto    : {(a.iloc[:,3]=='Sí').sum()} ({(a.iloc[:,3]=='Sí').mean():.0%})")
    print(f"Con indicador                           : {(a.iloc[:,4]=='Sí').sum()}")
    print(f"Con línea base                          : {(a.iloc[:,5]=='Sí').sum()}")
    print(f"Con meta anual                          : {(a.iloc[:,6]=='Sí').sum()}")
    print(f"Con proyectos asociados                 : {a.iloc[:,7].notna().sum()}")

    completos = a[(a.iloc[:,3]=='Sí') & (a.iloc[:,4]=='Sí') & (a.iloc[:,5]=='Sí') & (a.iloc[:,6]=='Sí')]
    print(f"\nObjetivos COMPLETOS (articulados, con indicador, línea base y meta): "
          f"{len(completos)} de {n} ({len(completos)/n:.0%})")
    print("\nInterpretación: el porcentaje de objetivos completos es el mejor predictor")
    print("de que el plan pueda evaluarse al final del periodo.")
except FileNotFoundError:
    print("Archivo MP04_articulacion.csv no encontrado.")
