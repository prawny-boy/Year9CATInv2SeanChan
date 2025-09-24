from print_functions import *

def run_module(module:str):
    module_numbers = module.split(".")
    path = f"Part{module_numbers[0]}\\{module_numbers[1]}.{module_numbers[2]}.py"
    print_title(f"Running Part {module} Filename: {path}", title_words=False)
    file_to_run = open(path, "r").read()
    exec(file_to_run)

while True:
    print()
    selected_module = listed_input(
        choices={
            "1.1.1": "Integral of y=10",
            "1.1.2": "Integral of y=x^2",
            "1.1.3": "Integral of y=1/2*x+1 and (x-2)**2+0.5 for 0≤x≤4",
            "2.1.1": "Area of a bolt",
            "3.1.2": "Area of a target",
            "3.1.4": "Chance of scoring 10 or more on a target",
            "3.1.5": "Area of each colour on an irregular target",
            "4.1.1": "Trials until red in a probability distribution",
            "4.1.2": "Normal distribution of 4.1.1"
        },
        prompt="Choose a module to run:",
        return_key=True
    )
    run_module(selected_module)