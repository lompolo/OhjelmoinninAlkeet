import tulvatutkimus as t

planeetta = [
        [" ", "x", "x", " ", " ", "x", "x", " ", " ", " ", " ", " ", "x", " ", " ", " ", "x"], 
        [" ", "x", " ", "x", "x", " ", " ", "x", " ", "x", "x", " ", "x", " ", " ", " ", " "],
        [" ", "x", "x", " ", "x", " ", "x", "x", "x", " ", "x", " ", "x", " ", "x", " ", "x"],
        ["x", " ", " ", " ", " ", " ", " ", " ", " ", "x", "x", "x", " ", " ", "x", "x", "x"],
        [" ", " ", " ", " ", "x", " ", "x", " ", "x", "x", " ", "x", " ", " ", " ", " ", " "],
        ["x", " ", "x", "x", "x", " ", "x", "x", "x", "x", "x", "x", " ", " ", " ", " ", " "],
        [" ", " ", "x", "x", " ", " ", " ", "x", "x", " ", " ", "x", "x", "x", " ", "x", "x"],
        ["x", " ", "x", " ", "x", "x", "x", "x", " ", "x", "x", " ", " ", " ", " ", " ", " "],
        ["x", "x", " ", " ", "x", " ", "x", " ", "x", " ", "x", " ", "x", "x", " ", "x", "x"],
        [" ", "x", " ", "x", "x", "x", "x", "x", "x", "x", "x", " ", " ", " ", "x", " ", "x"],
        ["x", "x", "x", " ", " ", " ", "x", "x", "x", " ", "x", "x", "x", "x", " ", " ", "x"],
        ["x", "x", "x", "x", "x", "x", " ", "x", "x", " ", "x", " ", " ", " ", "x", " ", "x"],
    ]

t.tulvataytto(planeetta, 11, 7)
t.main(planeetta)