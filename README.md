    # ASR Tool – Automatic Speech Recognition System

## 📌 Project Description

ASR Tool is a Python-based Automatic Speech Recognition application that converts human speech into written text.

The application captures audio from the user's microphone, processes the speech using a speech recognition service, and displays the converted text on the screen.

The recognized text can also be saved into a text file for future reference.

## 🎯 Objectives

* Capture speech using a microphone
* Convert speech into text
* Display the recognized text
* Handle recognition and connection errors
* Save recognized text into a file
* Provide a simple graphical user interface

## 🛠️ Technologies Used

* Python 3
* SpeechRecognition
* PyAudio
* Google Speech Recognition API
* Tkinter
* Git
* GitHub

## 📂 Project Structure

```text
ASR-Tool/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── output/
    └── recognized_text.txt
```

## ⚙️ Requirements

Before running the project, make sure Python 3 is installed.

A working microphone and internet connection are required for speech recognition.

## 🚀 Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/ASR-Tool.git
```

### Step 2: Open the project

```bash
cd ASR-Tool
```

### Step 3: Create a virtual environment

```bash
python -m venv venv
```

### Step 4: Activate the virtual environment

For Windows:

```bash
venv\Scripts\activate
```

For Linux/macOS:

```bash
source venv/bin/activate
```

### Step 5: Install dependencies

```bash
pip install -r requirements.txt
```

If PyAudio installation fails on Windows, install it using:

```bash
pip install pipwin
pipwin install pyaudio
```

Then install SpeechRecognition:

```bash
pip install SpeechRecognition
```

## ▶️ Run the Project

Execute:

```bash
python app.py
```

The ASR application window will open.

## 🎤 How to Use

1. Open the ASR application.
2. Click **Start Recording**.
3. Speak clearly into the microphone.
4. Wait while the speech is processed.
5. The recognized speech will appear in the text box.
6. Click **Save Text** to save the recognized text.
7. Click **Clear** to remove the current text.

## 🧪 Testing

The following test cases can be used to test the application.

| Test Case | Input                | Expected Output                      |
| --------- | -------------------- | ------------------------------------ |
| TC01      | Clear speech         | Correct text should be displayed     |
| TC02      | Long sentence        | Sentence should be converted to text |
| TC03      | No speech            | Recognition warning should appear    |
| TC04      | Background noise     | System should attempt recognition    |
| TC05      | No internet          | Connection error should be displayed |
| TC06      | Save recognized text | Text should be saved successfully    |
| TC07      | Clear button         | Text box should become empty         |

## ✅ Expected Result

The system successfully captures speech through the microphone and converts the speech into text. The recognized text is displayed in the application and can be stored in a text file.

## 🔮 Future Enhancements

* Offline speech recognition
* Multiple language support
* Voice command functionality
* Audio file upload
* Automatic punctuation
* Text-to-speech functionality
* Speaker identification
* Real-time speech transcription

## 👩‍💻 Author

Student Project – ASR Tool Implementation

## 📄 License

This project is developed for academic and educational purposes.
