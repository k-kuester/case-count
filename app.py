from shiny import App, Inputs, Outputs, Session, render, ui, reactive

app_ui = ui.page_fluid(
    ui.tags.style(
        """
        body {
            font-family: Times
            }
        """
    ),
    ui.input_text_area("x", "Input Text", placeholder="Enter text"),
    ui.output_text("txt")
)

def count(inp):
    case_dict = {
        ' ': 400,
        'e': 400,
        'n': 336,
        'o': 336,
        'i': 304,
        'a': 304,
        't': 304,
        's': 304,
        'r': 304,
        'l': 200,
        'h': 200,
        'd': 176,
        'm': 160,
        'c': 160,
        'f': 160,
        'u': 160,
        '.': 160,
        ',': 160,
        'b': 128,
        'p': 120,
        'g': 120,
        'y': 120,
        'w': 120,
        'j': 72,
        'v': 72,
        'k': 72,
        'q': 48,
        'x': 48,
        'z': 48,
        '\'': 48,
        '\'': 48,
        '-': 40,
        'fi': 32,
        'ff': 32,
        'fl':24,
        'ffl': 24,
        'ffi': 24,
        'st': 24,
        'ct': 24,
        '"': 24,
        '"': 24,
        '?': 24,
        ']': 24,
        '[': 24,
        ')': 24,
        '(': 24,
        '!': 24,
        ';': 24,
        ':': 24,
        '&': 24,
        'A': 28,
        'B': 15,
        'C': 18,
        'D': 19,
        'E': 38,
        'F': 20,
        'G': 18,
        'H': 20,
        'I': 28,
        'K': 12,
        'L': 23,
        'M': 16,
        'N': 31,
        'O': 30,
        'P': 20,
        'Q': 7,
        'R': 20,
        'S': 20,
        'T': 38,
        'V': 13,
        'W': 12,
        'X': 6,
        'Y': 15,
        'Z': 8,
        'J': 10,
        'U': 15
    }
    count_dict = {}
    minus_dict = {}
    count = 0
    #convert string to list
    char_list = list(inp)

    #count up each sort in string
    for char in char_list:
        if char in count_dict.keys():
            x = count_dict[char]
            count_dict[char] =  x + 1
        else:
            count_dict[char] = 1

    for key in count_dict:
        x = case_dict[key]
        minus_dict[key] = x - count_dict[key]

    return count_dict, minus_dict

def server(input: Inputs, output: Outputs, session: Session):
    @output
    @render.text
    def txt():
        if (input.x()):
            return count(input.x())

app = App(app_ui, server)
