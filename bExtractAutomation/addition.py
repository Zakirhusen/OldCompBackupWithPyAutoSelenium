import tkinter as tk
import win32print

def print_receipt():
    receipt_text = receipt_text_widget.get("1.0", "end-1c")
    with open("receipt.txt", "w") as f:
        f.write(receipt_text)
    printer_name = win32print.GetDefaultPrinter()
    hPrinter = win32print.OpenPrinter(printer_name)
    try:
        win32print.StartDocPrinter(hPrinter, 1, ("Receipt", None, "RAW"))
        win32print.StartPagePrinter(hPrinter)
        with open("receipt.txt", "rb") as f:
            win32print.WritePrinter(hPrinter, f.read())
        win32print.EndPagePrinter(hPrinter)
        win32print.EndDocPrinter(hPrinter)
    finally:
        win32print.ClosePrinter(hPrinter)

root = tk.Tk()

receipt_text_widget = tk.Text(root)
receipt_text_widget.pack()

print_button = tk.Button(root, text="Print", command=print_receipt)
print_button.pack()

root.mainloop()
