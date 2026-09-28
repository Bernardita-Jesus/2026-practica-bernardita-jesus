"""Suma las horas semanales de la tabla del README y actualiza la fila Total."""
import re
from pathlib import Path

readme = Path(__file__).resolve().parents[2] / "README.md"
lineas = readme.read_text(encoding="utf-8").splitlines()

fila_semana = re.compile(r"^\|.*\|\s*(\d+)\s*/\s*\d+\s*\|\s*$")
total = 0
ultima_fila = None
fila_total = None

for i, linea in enumerate(lineas):
    if linea.startswith("| **Total**"):
        fila_total = i
        continue
    m = fila_semana.match(linea)
    if m:
        total += int(m.group(1))
        ultima_fila = i

nueva = f"| **Total**          |            |                                              | **{total:03d}**                |"

if fila_total is not None:
    lineas[fila_total] = nueva
elif ultima_fila is not None:
    lineas.insert(ultima_fila + 1, nueva)

readme.write_text("\n".join(lineas) + "\n", encoding="utf-8")
print(f"Total de horas: {total}")
