import Gui
import speak
import model

if __name__ == "__main__":
    Gui.AudioSelectorGUI()
    assis = speak.Model()
    answer = model.Model("vanshika\\assests\\question.json")

    while True:
        response = assis.commands()
        ans = answer.get_answer(response)
        assis.speak(ans)
