import os
from oxygen_diagnostic import OxygenDiagnostic


def run():
    with open(os.path.join(os.path.dirname(__file__), 'data/input.txt'), 'r') as f:
        lines = f.readlines()

        energy_diagnostic = OxygenDiagnostic()
        energy_diagnostic.load_log(lines)

        energy_diagnostic.process_log()

        print(energy_diagnostic.get_life_support_rating())


run()
