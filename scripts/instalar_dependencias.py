"""Instala as skills de que a marca-de-luxo depende, a partir de dependencias/skills.zip.

Uso:
    python instalar_dependencias.py              # instala só as que faltam em ~/.claude/skills
    python instalar_dependencias.py --verificar  # só lista o que falta, sem instalar
    python instalar_dependencias.py --forcar     # reinstala todas (sobrescreve as versões instaladas)
    python instalar_dependencias.py --destino <pasta>   # instala em outra pasta de skills

Nunca apaga nada: com --forcar, só sobrescreve os arquivos que vêm no pacote.
"""
import argparse
import json
import pathlib
import sys
import zipfile

AQUI = pathlib.Path(__file__).resolve().parent.parent
PACOTE = AQUI / "dependencias" / "skills.zip"
MANIFESTO = AQUI / "dependencias" / "manifesto.json"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--destino", default=str(pathlib.Path.home() / ".claude" / "skills"))
    ap.add_argument("--verificar", action="store_true")
    ap.add_argument("--forcar", action="store_true")
    a = ap.parse_args()

    destino = pathlib.Path(a.destino).expanduser()
    skills = [s["skill"] for s in json.loads(MANIFESTO.read_text(encoding="utf-8"))["skills"]]
    faltam = [s for s in skills if not (destino / s / "SKILL.md").exists()]
    alvo = skills if a.forcar else faltam

    print(f"Destino: {destino}")
    print(f"{len(skills)} skills no pacote; {len(faltam)} faltando: {', '.join(faltam) or 'nenhuma'}")
    if a.verificar or not alvo:
        return 0

    destino.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(PACOTE) as z:
        for nome in z.namelist():
            skill = nome.split("/", 1)[0]
            if skill not in alvo or nome.endswith("/"):
                continue
            caminho = (destino / nome).resolve()
            if destino.resolve() not in caminho.parents:  # proteção contra caminhos fora do destino
                print(f"Ignorado (fora do destino): {nome}")
                continue
            caminho.parent.mkdir(parents=True, exist_ok=True)
            caminho.write_bytes(z.read(nome))
    print(f"Instaladas: {', '.join(alvo)}")
    print("Reinicie a sessão do Claude para ele enxergar as skills novas.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
