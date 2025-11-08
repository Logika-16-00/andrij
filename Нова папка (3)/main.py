import os
import json
import time
import random
import threading

import numpy as np
import customtkinter as ctk

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset

# Переклад
from deep_translator import GoogleTranslator

# ======================= Модель =======================
class ChatbotModel(nn.Module):
    def __init__(self, input_size, output_size):
        super(ChatbotModel, self).__init__()
        self.fc1 = nn.Linear(input_size, 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, output_size)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.5)

    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.relu(self.fc2(x))
        x = self.dropout(x)
        x = self.fc3(x)
        return x

# ======================= Асистент =======================
class ChatbotAssistant:
    def __init__(self, intents_path, function_mappings=None):
        self.model = None
        self.intents_path = intents_path
        self.documents = []
        self.vocabulary = []
        self.intents = []
        self.intents_responses = {}
        self.function_mappings = function_mappings
        self.X = None
        self.y = None

    # ======= Український токенайзер =======
    @staticmethod
    def tokenize_and_lemmatize(text):
        text = text.lower()
        tokens = [word.strip(".,!?;:()[]{}\"'") for word in text.split()]
        return [t for t in tokens if t]

    def bag_of_words(self, words):
        return [1 if word in words else 0 for word in self.vocabulary]

    def parse_intents(self):
        if os.path.exists(self.intents_path):
            with open(self.intents_path, 'r', encoding='utf-8') as f:
                intents_data = json.load(f)

            for intent in intents_data['intents']:
                if intent['tag'] not in self.intents:
                    self.intents.append(intent['tag'])
                    self.intents_responses[intent['tag']] = intent['responses']

                for pattern in intent['patterns']:
                    pattern_words = self.tokenize_and_lemmatize(pattern)
                    self.vocabulary.extend(pattern_words)
                    self.documents.append((pattern_words, intent['tag']))

            self.vocabulary = sorted(set(self.vocabulary))

    def prepare_data(self):
        bags, indices = [], []
        for document in self.documents:
            words = document[0]
            bag = self.bag_of_words(words)
            intent_index = self.intents.index(document[1])
            bags.append(bag)
            indices.append(intent_index)

        self.X = np.array(bags)
        self.y = np.array(indices)

    def train_model(self, batch_size, lr, epochs):
        X_tensor = torch.tensor(self.X, dtype=torch.float32)
        y_tensor = torch.tensor(self.y, dtype=torch.long)
        dataset = TensorDataset(X_tensor, y_tensor)
        loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)
        self.model = ChatbotModel(self.X.shape[1], len(self.intents))
        criterion = nn.CrossEntropyLoss()
        optimizer = optim.Adam(self.model.parameters(), lr=lr)

        for epoch in range(epochs):
            running_loss = 0.0
            for batch_X, batch_y in loader:
                optimizer.zero_grad()
                outputs = self.model(batch_X)
                loss = criterion(outputs, batch_y)
                loss.backward()
                optimizer.step()
                running_loss += loss.item()
            print(f"Епоха {epoch + 1}/{epochs}: Втрата: {running_loss / len(loader):.4f}")

    def save_model(self, model_path, dimensions_path):
        torch.save(self.model.state_dict(), model_path)
        with open(dimensions_path, 'w', encoding='utf-8') as f:
            json.dump({'input_size': self.X.shape[1], 'output_size': len(self.intents)}, f, ensure_ascii=False)

    def load_model(self, model_path, dimensions_path):
        if not os.path.exists(model_path) or not os.path.exists(dimensions_path):
            print("[!] Модель не знайдена, створюю нову...")
            self.prepare_data()
            self.model = ChatbotModel(self.X.shape[1], len(self.intents))
            return

        with open(dimensions_path, 'r', encoding='utf-8') as f:
            dimensions = json.load(f)
        self.model = ChatbotModel(dimensions['input_size'], dimensions['output_size'])
        self.model.load_state_dict(torch.load(model_path))
        print("[✅] Модель успішно завантажено.")

    # ======= Анімація друкування =======
    @staticmethod
    def typing_animation(widget, text, speed=0.03):
        for char in text:
            widget.insert(ctk.END, char)
            widget.update_idletasks()
            time.sleep(speed)
        widget.insert(ctk.END, "\n\n")
        widget.see(ctk.END)

    # ======= Обробка повідомлення з перекладом =======
    def process_message(self, input_message):
        # Визначаємо мову користувача
        try:
            detected_lang = GoogleTranslator(source='auto', target='en').detect(input_message)  # детекція через deep-translator
        except:
            detected_lang = 'uk'

        # Переклад на українську для моделі
        translated_input = GoogleTranslator(source='auto', target='uk').translate(input_message)

        words = self.tokenize_and_lemmatize(translated_input)
        bag = self.bag_of_words(words)
        bag_tensor = torch.tensor([bag], dtype=torch.float32)
        self.model.eval()
        with torch.no_grad():
            predictions = self.model(bag_tensor)
        predicted_class_index = torch.argmax(predictions, dim=1).item()
        predicted_intent = self.intents[predicted_class_index]

        if self.function_mappings and predicted_intent in self.function_mappings:
            self.function_mappings[predicted_intent]()

        # Відповідь українською
        response = random.choice(self.intents_responses.get(predicted_intent, ["Вибач, я не розумію."]))

        # Перекладаємо назад на мову користувача
        if detected_lang != 'uk':
            try:
                response = GoogleTranslator(source='uk', target=detected_lang).translate(response)
            except:
                pass

        return response

# ======================= Функції =======================
def get_stocks():
    stocks = ['AAPL', 'META', 'NVDA', 'GS', 'MSFT']
    print("📊 Твої випадкові акції:", random.sample(stocks, 3))

# ======================= Інтерфейс =======================
class ChatUI(ctk.CTk):
    def __init__(self, assistant):
        super().__init__()
        self.assistant = assistant
        self.title("🤖 GPT Асистент")
        self.geometry("600x600")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.chat_box = ctk.CTkTextbox(self, width=560, height=450, wrap="word", font=("Consolas", 14))
        self.chat_box.pack(pady=20)
        self.chat_box.insert(ctk.END, "🤖 Привіт! Я твій асистент. Напиши щось нижче.\n\n")
        self.chat_box.configure(state="disabled")

        self.entry = ctk.CTkEntry(self, width=460, placeholder_text="Введи повідомлення...")
        self.entry.pack(side="left", padx=(20, 10), pady=(0, 20))
        self.entry.bind("<Return>", lambda event: self.send_message())

        self.send_button = ctk.CTkButton(self, text="Надіслати", command=self.send_message)
        self.send_button.pack(side="right", padx=(0, 20), pady=(0, 20))

    def send_message(self):
        message = self.entry.get().strip()
        if not message:
            return
        self.entry.delete(0, ctk.END)

        self.chat_box.configure(state="normal")
        self.chat_box.insert(ctk.END, f"🧠 Ви: {message}\n")
        self.chat_box.configure(state="disabled")

        threading.Thread(target=self.reply_message, args=(message,)).start()

    def reply_message(self, message):
        response = self.assistant.process_message(message)
        self.chat_box.configure(state="normal")
        self.chat_box.insert(ctk.END, "🤖 Асистент: ")
        ChatbotAssistant.typing_animation(self.chat_box, response, speed=0.03)
        self.chat_box.configure(state="disabled")

# ======================= Головна логіка =======================
if __name__ == '__main__':

    assistant = ChatbotAssistant('intents.json', function_mappings={'stocks': get_stocks})
    assistant.parse_intents()
    assistant.prepare_data()
    assistant.train_model(batch_size=8, lr=0.001, epochs=100)
    assistant.save_model('chatbot_model.pth', 'dimensions.json')
    assistant.load_model('chatbot_model.pth', 'dimensions.json')

    app = ChatUI(assistant)
    app.mainloop()
