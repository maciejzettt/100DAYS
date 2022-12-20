from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Index", [])
table.add_column("Pokemon Name", [])
table.add_column("Type", [])
table.add_row(["1", "Pikachu", "Electric"])
table.add_rows([["2", "Squirtle", "Water"], ["3", "Charmander", "Fire"]])
table.align = 'c'
table.vertical_char = '│'
table.horizontal_char = '─'
table.junction_char = '┼'
table.bottom_junction_char = '┴'
table.top_junction_char = '┬'
table.bottom_left_junction_char = '╰'
table.bottom_right_junction_char = '╯'
table.top_left_junction_char = '╭'
table.top_right_junction_char = '╮'
table.left_junction_char = '├'
table.right_junction_char = '┤'
print(table)
