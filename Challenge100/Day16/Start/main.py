# from turtle import Turtle, Screen

# my_screen = Screen()
# eylul = Turtle()
# eylul.shape("turtle")
# eylul.color("coral")
# eylul.forward(100)

# my_screen.exitonclick()


from prettytable import PrettyTable


x = PrettyTable()

x.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
x.add_rows(
    [
        ["Adelaide", 1295, 1158259, 600.5],
        ["Brisbane", 5905, 1857594, 1146.4],
        ["Darwin", 112, 120900, 1714.7],
        ["Hobart", 1357, 205556, 619.5],
        ["Sydney", 2058, 4336374, 1214.8],
        ["Melbourne", 1566, 3806092, 646.9],
        ["Perth", 5386, 1554769, 869.4],
    ]
)

x.align = "c"
print(x.align)
print(x)
print(x.get_string(fields=["City name", "Population"]))
