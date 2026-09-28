import os, importlib, sys
sys.path.insert(0, os.path.dirname(__file__))
from common import page
ROOT = "/home/claude/site/melrakki-main"
mods = ["p_off_grid_power","p_surveillance","p_critical_infrastructure","p_drone_dock","p_telecoms","p_oil_gas","p_defence"]
for m in mods:
    M = importlib.import_module(m).META
    out = page(**M)
    d = os.path.join(ROOT, M["slug"]); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w").write(out)
    print(M["slug"], len(out))
