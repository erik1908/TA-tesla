import teslapy
def solve_captcha(svg):
    with open('captcha.svg', 'wb') as f:
        f.write(svg)
    return input('Captcha: ')