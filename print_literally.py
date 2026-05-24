import time
import win32print
import os

def literal_print(text, show_progress=False):
    """
    check im os is windows if so,
    encode the string so that its printable,
    after which start printing.
    """
    # Hehe my first time using raise
    if os.name == 'nt':
        starting_time = time.time()
        text = text.encode("utf-8") # For some reason even though I specified for it to be text win32print still wants me to encode it...
        if show_progress:
            print("*----Printing----*")
            print(text.decode("utf-8"))
            print("*--Printer-logs--*")
        try:
            printer_name = win32print.GetDefaultPrinter()
        except Exception as e:
            raise OSError(f"No default printer found: {e}")
        open_printer = win32print.OpenPrinter(printer_name)

        if show_progress:
            print("Default printer used:", printer_name)
            print("Opening printer: ", open_printer)

        win32print.StartDocPrinter(open_printer, 1, ("Test", None, "TEXT"))
        win32print.StartPagePrinter(open_printer)

        if show_progress:
            print("Starting print")
        try: # If there's an error close the printer yea
            win32print.WritePrinter(open_printer, text)
        except Exception as e:
            win32print.EndPagePrinter(open_printer)
            win32print.EndDocPrinter(open_printer)
            win32print.ClosePrinter(open_printer)
            raise OSError(f"Could not write to printer: {e}")
        win32print.EndPagePrinter(open_printer)
        win32print.EndDocPrinter(open_printer)
        win32print.ClosePrinter(open_printer)

        if show_progress:
            print("Time took for windows to accept: ", time.time() - starting_time)
    else: # TODO add support for linux/macOS someday
        raise OSError("Literal_print currently only works on Windows")

def bin_print(text, show_progress=False):
    """
    So I made like an old project that makes my printer print my image's pure binary (well the 1's and 0's at least aka the human-readable version),
    uhh lets remake a small version of it!!!

    I just copied and pasted literal_print's code but turned the text to bin before encoding.
    """
    if os.name == 'nt':
        starting_time = time.time()
        text = ' '.join(format(ord(char), '08b') for char in text)
        text = text.encode("utf-8")
        if show_progress:
            print("*----Printing----*")
            print(text.decode("utf-8"))
            print("*--Printer-logs--*")
        try:
            printer_name = win32print.GetDefaultPrinter()
        except Exception as e:
            raise OSError(f"No default printer found: {e}")
        open_printer = win32print.OpenPrinter(printer_name)

        if show_progress:
            print("Default printer used:", printer_name)
            print("Opening printer: ", open_printer)

        win32print.StartDocPrinter(open_printer, 1, ("Test", None, "TEXT"))
        win32print.StartPagePrinter(open_printer)

        if show_progress:
            print("Starting print")
        try: # If there's an error close the printer yea
            win32print.WritePrinter(open_printer, text)
        except Exception as e:
            win32print.EndPagePrinter(open_printer)
            win32print.EndDocPrinter(open_printer)
            win32print.ClosePrinter(open_printer)
            raise OSError(f"Could not write to printer: {e}")
        win32print.EndPagePrinter(open_printer)
        win32print.EndDocPrinter(open_printer)
        win32print.ClosePrinter(open_printer)

        if show_progress:
            print("Time took for windows to accept: ", time.time() - starting_time)
    else: # TODO add support for linux/macOS someday
        raise OSError("Literal_print currently only works on Windows")
