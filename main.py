from pyscript import display, document

def studentClassification (e):
    document.getElementById('output').innerHTML = ""

    classification = float(document.getElementById('input1').value)

    if classification >= 95 and classification == 100:
        display("bergamo 1", target ='output')
    elif classification >= 90 and classification <= 94:
        display("bergamo 2.", target ='output')
    elif classification >= 80 and classification <= 89:
        display("bergamo 3.", target ='output')
    elif classification > 75 and classification < 79:
        display("perugia 1.", target ='output')
    elif classification >= 70 and classification <= 75:
        display("perugia 2.", target ='output')
    else:
        display("invalid.", target ='output')