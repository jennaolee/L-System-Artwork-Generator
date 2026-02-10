from pathlib import Path
from lsystem import LSystem

parameters = [
    {
        "axiom": "X",
        "rules": [
            ("F", "FF"),
            ("X", "F+[-F-XF-X][+FF][--XF[+X]][++F-X]"),
        ],
    },
    {
        "axiom": "FX",
        "rules": [
            ("F", "FF+[+F-F-F]-[-F+F+F]"),
        ],
    },
    {
        "axiom": "X",
        "rules": [
            ("F", "FX[FX[+XF]]"),
            ("X", "FF[+XZ++X-F[+ZX]][-X++F-X]"),
            ("Z", "[+F-X-F][++ZX]"),
        ],
    },
    {
        "axiom": "F",
        "rules": [
            ("F", "F+F-F-F+F")
        ],
    },
    {
        "axiom": "X",
        "rules": [
            ("F", "FFFX[FFX[+FXX]]"),
            ("X", "XFF[+FFFFX-X-F-X][F+X+FX]")
        ]
    }
]


def main():
    params1 = parameters[0]
    params2 = parameters[1]
    params3 = parameters[2]
    params4 = parameters[3]
    params5 = parameters[4]

    results_path = Path("results")

    try:
        results_path.mkdir(parents=True, exist_ok=True)
        print(f"Directory '{results_path}' created or already exists.")
    except OSError as e:
        print(f"Error creating directory: {e}")

    # LSystem 1
    LSystem(
        axiom=params1["axiom"],
        rules=params1["rules"],
        iterations=5,
        branch_length=80,
        branch_width=3,
        branch_angle=25,
        branch_length_falloff=0.65,
        leaf_length=6,
        leaf_width=3,
        leaf_color="green",
        branch_color="#5b3a29",
        filename=f"{results_path}/lsystem1.svg",
        size=(500, 500),
    )

    # LSystem 2
    LSystem(
        axiom=params2["axiom"],
        rules=params2["rules"],
        iterations=5,
        branch_length=100,
        branch_width=4,
        branch_angle=20,
        branch_length_falloff=0.7,
        leaf_length=20,
        leaf_width=10,
        leaf_color="pink",
        branch_color="green",
        filename=f"{results_path}/lsystem2.svg",
        size=(500, 500),
    )
    
    # LSystem 3
    LSystem(
        axiom=params3["axiom"],
        rules=params3["rules"],
        iterations=5,
        branch_length=120,
        branch_width=2,
        branch_angle=60,
        branch_length_falloff=0.6,
        leaf_length=5,
        leaf_width=6,
        leaf_color="red",
        branch_color="blue",
        filename=f"{results_path}/lsystem3.svg",
        size=(500, 500),
    )

    # LSystem 4 
    LSystem(
        axiom=params4["axiom"],
        rules=params4["rules"],
        iterations=4,
        branch_length=9,
        branch_width=4,
        branch_angle=90,
        branch_length_falloff=0.9,
        leaf_length=5,
        leaf_width=6,
        leaf_color="red",
        branch_color="blue",
        filename=f"{results_path}/lsystem4.svg",
        size=(500, 500),
    )

    # Lsystem 5
    LSystem(
        axiom=params5["axiom"],
        rules=params5["rules"],
        iterations=5,
        branch_length=10,
        branch_width=4,
        branch_angle=130,
        branch_length_falloff=0.6,
        leaf_length=2,
        leaf_width=2,
        leaf_color="purple",
        branch_color="orange",
        filename=f"{results_path}/lsystem5.svg",
        size=(500, 500),
    )





if __name__ == "__main__":
    main()


