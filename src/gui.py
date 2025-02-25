import tkinter as tk
from tkinter import scrolledtext, filedialog
from PIL import Image, ImageTk  # Import Pillow for image handling
from src.chatbot import PharmacistChatbot  # Import the chatbot class
from src.ocr.ocr_engine import OCROptions


class ChatbotGUI:
    def __init__(self, chatbot: PharmacistChatbot):
        self.chatbot = chatbot
        self.root = tk.Tk()
        self.root.title("Pharmacist Assistant Chatbot")

        self.text_area = scrolledtext.ScrolledText(self.root, width=60, height=20)
        self.text_area.pack(padx=10, pady=10)
        self.text_area.config(state=tk.DISABLED)

        self.input_box = tk.Entry(self.root, width=60)
        self.input_box.pack(padx=10, pady=5)

        self.send_button = tk.Button(self.root, text="Send", command=self.send_message)
        self.send_button.pack(pady=5)

        self.upload_button = tk.Button(self.root, text="Upload Prescription Image",
                                        command=self.upload_image)  # Add upload button
        self.upload_button.pack(pady=5)

    def upload_image(self):
        """Opens a file dialog to select an image and processes it."""
        filename = filedialog.askopenfilename(
            initialdir=".",
            title="Select an Image",
            filetypes=(("Image files", "*.png;*.jpg;*.jpeg"), ("all files", "*.*"))
        )
        if filename:
            # Process the image using the chatbot's OCR engine
            extracted_text = self.chatbot.process_image(filename)

            # Display the extracted text in the chat area
            self.text_area.config(state=tk.NORMAL)
            self.text_area.insert(tk.END, "Chatbot (from image): " + extracted_text + "\n")
            self.text_area.config(state=tk.DISABLED)
            self.text_area.see(tk.END)  # Scroll to the end

    def send_message(self):
        message = self.input_box.get()
        self.input_box.delete(0, tk.END)

        # Display user message
        self.text_area.config(state=tk.NORMAL)
        self.text_area.insert(tk.END, "You: " + message + "\n")
        self.text_area.config(state=tk.DISABLED)

        # Get chatbot response
        response = self.chatbot.process_message(message)

        # Display chatbot response
        self.text_area.config(state=tk.NORMAL)
        self.text_area.insert(tk.END, "Chatbot: " + response + "\n")
        self.text_area.config(state=tk.DISABLED)

        self.text_area.see(tk.END)  # Scroll to the end

    def run(self):
        self.root.mainloop()


# Main Function
if __name__ == "__main__":
    ocr_options = OCROptions()
    chatbot = PharmacistChatbot(ocr_options)
    gui = ChatbotGUI(chatbot)
    gui.run()
