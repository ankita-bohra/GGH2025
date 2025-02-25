# Pharmacist Assistant AI Chatbot

## Overview

This project implements an AI chatbot designed to assist pharmacists with common tasks, such as medication refills, dosage checks, and providing basic information. The chatbot uses Natural Language Understanding (NLU) to interpret user input, a knowledge base to store relevant data, and a graphical user interface (GUI) for interaction.

## Features

*   **Text-Based Chat Interface:** A simple Tkinter-based interface for interacting.
*   **Intent Recognition:** Identifies the patient's intent (e.g., "refill medication," "check dosage").
*   **Entity Extraction:** Extracts relevant information from user/patient input (e.g., medication name).
*   **Medication Refill:** Simulates medication refills based on available inventory.
*   **Dosage Check:** Provides typical dosage information (from knowledge base).
*   **OCR Support:** Extracts text from prescription images using PaddleOCR.

## Prerequisites

*   **Python 3.7 - 3.10:** A supported version of Python is required.
*   **Virtual Environment (Recommended):** Using a virtual environment is highly recommended to manage dependencies.
*   **Tkinter:** Tkinter should be included with your Python installation.
*   **PaddlePaddle:** For OCR functionality (optional), PaddlePaddle is required.
*   **PaddleOCR:** For OCR functionality (optional), PaddleOCR is required.

## Installation

1.  **Create a Virtual Environment:**

    ```bash
    python3.10 -m venv myenv  # Or python, py, depending on your system
    ```

2.  **Activate the Virtual Environment:**

    *   **Windows:**

        ```bash
        myenv\Scripts\activate
        ```

    *   **macOS/Linux:**

        ```bash
        source myenv/bin/activate
        ```

3.  **Upgrade pip:**

    ```bash
    pip install --upgrade pip
    ```

4.  **Install PaddlePaddle (If Using OCR):**

    *   **CPU Version:**

        ```bash
        pip install paddlepaddle
        ```

    *   **GPU Version (Example - Find the Correct Command on PaddlePaddle Website):**

        ```bash
        pip install paddlepaddle-gpu==<version> -f <index_url>
        ```

        *   Replace `<version>` and `<index_url>` with the appropriate values from the PaddlePaddle installation page: [https://www.paddlepaddle.org.cn/en/install/quick](https://www.paddlepaddle.org.cn/en/install/quick)

5.  **Install PaddleOCR (If Using OCR):**

    ```bash
    pip install paddleocr
    ```

6.  **Install Other Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Download the Code:** Download the project code and extract it to a directory.
2.  **Navigate to the Project Directory:** Open a terminal or command prompt and navigate to the directory where you extracted the code.
3.  **Activate the Virtual Environment:** (If you haven't already)
4.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5.  **Run the Chatbot:**

    ```bash
    python src/gui.py
    ```

6.  **Interact with the Chatbot:** The chatbot window will appear. Type your messages in the input box and click "Send".

## Code Structure

*   **`src/chatbot.py`:** Contains the core chatbot logic, including:
    *   `PharmacistChatbot` class: Handles NLU, dialog management, and knowledge base interactions.
    *   `process_message` function: Processes user input and generates a response.
    *   `understand_intent` function: Uses NLU to understand the user's intent and extract entities.
    *   `generate_response` function: Generates a response based on the intent and entities.
    *   `process_image` function: (If using OCR) Extracts text from prescription images using OCR.
*   **`src/gui.py`:** Contains the GUI implementation using Tkinter:
    *   `ChatbotGUI` class: Implements the chat interface.
    *   `send_message` function: Sends the message to the chatbot and displays the response.
*   **`src/nlu/`:** Contains the NLU components:
    *   `intent_classifier.py`: Classifies the intent of the message.
    *   `entity_extractor.py`: Extracts entities from the message.
*   **`src/knowledge_base/`:** Contains the knowledge base data and logic:
    *   `knowledge_base.py`: Class that defines the knowledge base.
    *   `medications.csv`: CSV file containing medication information.
    *   `patients.csv`: CSV file containing patient records.
*   **`src/ocr/`:** Contains the OCR engine integration and image preprocessing:
    *   `ocr_engine.py`: Abstract Class for implementation of OCR engines.
    *   `image_preprocessor.py`: (Optional) Functions for preprocessing images before OCR.
*   **`data/`:** Contains training data, sample images, and other resources.
*   **`requirements.txt`:** Lists all the project dependencies.
*   **`config.py`:** Stores configuration settings (API keys, database connections, etc.).

## Customization

*   **NLU:** The NLU components (`intent_classifier.py`, `entity_extractor.py`) can be replaced with more sophisticated NLU frameworks like Rasa or Dialogflow.
*   **Knowledge Base:** The knowledge base can be extended by adding more data to the `medications.csv` and `patients.csv` files, or by connecting to a database.
*   **OCR:** The OCR engine can be replaced with a different engine (e.g., Google Cloud Vision API) by implementing a new class that inherits from the `OCREngine` abstract class.
*   **GUI:** The GUI can be customized by modifying the Tkinter code in `src/gui.py`.


