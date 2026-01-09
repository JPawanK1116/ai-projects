# AI Voice Assistant (VA)

## 📌 Project Overview
A smart desktop voice assistant designed to automate daily tasks on a PC. This assistant can perform system operations, retrieve information, and provide a conversational interface.

## 🎯 Objectives
- To build a personalized AI assistant.
- To automate tasks like opening applications, playing music, and web searching.
- To implement a GUI for better user interaction.

## 🧠 Concepts & Tech Stack
- **Natural Language Processing:** Speech Recognition
- **Deep Learning:** TensorFlow/Keras (for custom intent classification models)
- **GUI:** PyQt5 / Tkinter
- **Libraries:** SpeechRecognition, Pyttsx3, TensorFlow, PyQt5

## 📂 Architecture
- **src/run.py:** Main entry point of the application.
- **src/scifi.ui:** The graphical user interface design.
- **models/model.h5:** Pre-trained Keras model for intent recognition.

## 🚀 How to Run
1.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2.  Run the assistant:
    ```bash
    python src/run.py
    ```

## 🔮 Future Improvements
- Integrate LLMs (like Gemini/GPT) for more natural conversations.
- Add IoT control capabilities.
