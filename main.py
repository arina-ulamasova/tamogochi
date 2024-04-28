from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
import random

class ReactionLabel(Label):
    pass

class ProgrammerSimulator(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hunger = 6.0
        self.energy = 2.0
        self.leisure = 4.0
        self.motivation = 3.0
        self.max_stat = 10.0
        self.min_stat = 0.0
        self.running = False
        self.money = 0
        self.goal = 60
        self.earning_paused = False

    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20)

        top_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        self.earning_label = Label(text=f'Заработано: {self.money}$, Цель: {self.goal}$', size_hint=(1, None), height=30, halign='right', valign='middle')
        top_layout.add_widget(self.earning_label)
        layout.add_widget(top_layout)

        main_layout = BoxLayout(orientation='horizontal')
        self.programmer_layout = BoxLayout(orientation='horizontal')
        self.programmer_image = Image(source='img1.png')
        self.programmer_layout.add_widget(self.programmer_image)
        main_layout.add_widget(self.programmer_layout)

        self.reaction_label = ReactionLabel(text='', halign='center', valign='middle', size_hint=(0.6, 1), color=(0.4, 0.4, 1, 1))  # синий цвет (R, G, B, A)
        main_layout.add_widget(self.reaction_label)

        self.stats_layout = BoxLayout(orientation='vertical', size_hint=(0.3, None), height=150)
        self.hunger_label = Label(text=f'Голод: {self.hunger:.1f}', size_hint=(1, None), height=30)
        self.energy_label = Label(text=f'Бодрость: {self.energy:.1f}', size_hint=(1, None), height=30)
        self.leisure_label = Label(text=f'Досуг: {self.leisure:.1f}', size_hint=(1, None), height=30)
        self.motivation_label = Label(text=f'Мотивация: {self.motivation:.1f}', size_hint=(1, None), height=30)
        self.stats_layout.add_widget(self.hunger_label)
        self.stats_layout.add_widget(self.energy_label)
        self.stats_layout.add_widget(self.leisure_label)
        self.stats_layout.add_widget(self.motivation_label)
        main_layout.add_widget(self.stats_layout)

        layout.add_widget(main_layout)

        self.buttons_layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        self.send_lunch_button = Button(text='Отправить на обед', size_hint=(1, None), height=40, on_press=self.send_lunch)
        self.offer_coffee_button = Button(text='Предложить кофе', size_hint=(1, None), height=40, on_press=self.offer_coffee)
        self.send_break_button = Button(text='Отправить на перекур', size_hint=(1, None), height=40, on_press=self.send_break)
        self.promise_bonus_button = Button(text='Пообещать премию', size_hint=(1, None), height=40, on_press=self.promise_bonus)
        self.buttons_layout.add_widget(self.send_lunch_button)
        self.buttons_layout.add_widget(self.offer_coffee_button)
        self.buttons_layout.add_widget(self.send_break_button)
        self.buttons_layout.add_widget(self.promise_bonus_button)
        layout.add_widget(self.buttons_layout)

        self.update_stats()
        self.start_game()

        return layout

    def start_game(self):
        self.running = True
        Clock.schedule_interval(self.update, 1)
        Clock.schedule_interval(self.earn_money, 1)

    def update(self, dt):
        if self.running:
            self.hunger -= 1/45
            self.energy -= 1/30
            self.leisure -= 1/95
            self.motivation -= 1/60
            self.check_game_over()
            self.update_stats()
            if self.money >= self.goal:
                self.end_game()

    def earn_money(self, dt):
        if not self.earning_paused:
            self.money += 1
            self.earning_label.text = f'Заработано: {self.money}$, Цель: {self.goal}$'

    def update_stats(self):
        self.hunger = max(self.min_stat, min(self.max_stat, self.hunger))
        self.energy = max(self.min_stat, min(self.max_stat, self.energy))
        self.leisure = max(self.min_stat, min(self.max_stat, self.leisure))
        self.motivation = max(self.min_stat, min(self.max_stat, self.motivation))
        self.hunger_label.text = f'Голод: {self.hunger:.1f}'
        self.energy_label.text = f'Бодрость: {self.energy:.1f}'
        self.leisure_label.text = f'Досуг: {self.leisure:.1f}'
        self.motivation_label.text = f'Мотивация: {self.motivation:.1f}'

    def send_lunch(self, instance):
        self.earning_paused = True
        Clock.schedule_once(self.resume_earning, 3)

        reactions = [
            "охх... я так объелся",
            "хотите пообедать со мной, босс?",
            "Уже обед? Я и не заметил",
            "Омномном, было вкусно"
        ]
        self.reaction_label.text = random.choice(reactions)
        self.hunger += 1
        self.update_stats()

    def offer_coffee(self, instance):
        self.earning_paused = True
        Clock.schedule_once(self.resume_earning, 10)

        reactions = [
            "мм, латте с соленной карамелью...",
            "вам тоже купить кофе, босс?",
            "Беспокоитесь о моих синяках под глазами, босс?",
            "В этот раз я выпил энергетик, хе-хе..."
        ]
        self.reaction_label.text = random.choice(reactions)
        self.energy += 1
        self.update_stats()

    def send_break(self, instance):
        self.earning_paused = True
        Clock.schedule_once(self.resume_earning, 10)

        reactions = [
            "Оо, свежий воздух!",
            "Хоть отдохну 5 минут...",
            "Оу, мои глаза болят от солнечного света",
            "Спасибо, стрельнуть вам сигаретку, босс?"
        ]
        self.reaction_label.text = random.choice(reactions)
        self.leisure += 1
        self.update_stats()

    def promise_bonus(self, instance):
        self.earning_paused = True
        Clock.schedule_once(self.resume_earning, 3)

        reactions = [
            "О, реально? Спасибо, босс",
            "Вы не врете, босс?...",
            "О деньги, деньги... Ээ, какие цветы вы любите, босс?",
            "Оу, денюжки. Закажу сегодня доставку суши"
        ]
        self.reaction_label.text = random.choice(reactions)
        self.motivation += 1
        self.update_stats()

    def resume_earning(self, dt):
        self.earning_paused = False

    def end_game(self):
        self.reaction_label.text = "Рабочий день закончился! Программист позвал вас на свидание"
        self.running = False
        Clock.unschedule(self.update)
        Clock.unschedule(self.earn_money)

    def check_game_over(self):
        if self.hunger <= self.min_stat or self.energy <= self.min_stat or self.leisure <= self.min_stat or self.motivation <= self.min_stat:
            self.reaction_label.text = "Ой-ой, ваш программист уволился!"
            self.running = False
            Clock.unschedule(self.update)
            Clock.unschedule(self.earn_money)

if __name__ == '__main__':
    ProgrammerSimulator().run()
