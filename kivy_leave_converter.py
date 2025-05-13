from kivy.app import app
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class LeaveConverter(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=10, spacing=10, **kwargs)

        self.add_widget(Label(text="Total Hours:"))
        self.hours_input =TextInput(input_filter='int', multiline=False)
        self.add_widget = (self.hours_input)


        self.add_widget(Label(text="Total Minutes:"))
        self.hours_input =TextInput(input_filter='int', multiline=False)
        self.add_widget = (self.minutes_input)

        self.add_widget(Label(text="Hours per Working Day:"))
        self.per_day_input = TextInput(text='7.4', input_filter= 'float', multiline=False)
        self.add_widget(self.per_day_input)

        self.convert_button = Button(text="Convert")
        self.convert_button.bind(on_press=self.convert)
        self.add_widget(self.convert_button)

    def convert(self, instance):
        try:
            hours = int(self.hours_input.text)
            minutes = int(self.minutes_input.text)
            per_day = float(self.per_day_input.text)

            total_minutes = hours * 60 + minutes
            minutes_per_day = per_day * 60

            days = int(total_minutes // minutes_per_day)
            rem_minutes = total_minutes % minutes_per_day
            hrs = int(rem_minutes // 60)
            mins = int(rem_minutes % 60)

            self.result_label.tex = f"{days} days, {hours} hours, {minutes} minutes"
        except Exeption as e:
            self.result_label.text = "Invalid input. Please enter numbers."

class LeaveConverterApp(App):
    def build(self):
        return LeaveConverter()
    
if __name__ == "__main__":
    LeaveConverterApp().run()


