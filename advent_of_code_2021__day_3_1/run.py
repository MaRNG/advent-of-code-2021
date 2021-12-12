import os
from energy_diagnostic import EnergyDiagnostic


def run():
    with open(os.path.join(os.path.dirname(__file__), 'data/input.txt'), 'r') as f:
        lines = f.readlines()

        energy_diagnostic = EnergyDiagnostic()
        energy_diagnostic.load_log(lines)

        energy_diagnostic.process_log()

        print(energy_diagnostic.get_energy_consumption())


run()
