import des
import argparse
import abc
import enum
from abc import ABC, abstractmethod
from pathlib import Path
from enum import Enum
from des import DesKey
import argparse
import os
import ast

"""
Submitted
By: Saksham Bhardwaj, A01185352
    Prerna Prerna, A01195525

"""


class CryptoMode(Enum):
    # Encryption mode
    EN = "en"
    # Decryption Mode
    DE = "de"


class Request:
    """
    The request object represents a request to either encrypt or decrypt
    certain data. The request object comes with certain accompanying
    configuration options as well as a field that holds the result. The
    attributes are:
        - encryption_state: 'en' for encrypt, 'de' for decrypt
        - data_input: This is the string data that needs to be encrypted or
        decrypted. This is None if the data is coming in from a file.
        - input_file: The text file that contains the string to be encrypted or
        decrypted. This is None if the data is not coming from a file and is
        provided directly.
        - output: This is the method of output that is requested. At this
        moment the program supports printing to the console or writing to
        another text file.
        - key: The Key value to use for encryption or decryption.
        - result: Placeholder value to hold the result of the encryption or
        decryption. This does not usually come in with the request.

    """

    def __init__(self):
        self.encryption_state = None
        self.data_input = None
        self.input_file = None
        self.output = None
        self.key = None
        self.result = None

    def __str__(self):
        return f"Request: State: {self.encryption_state}\n " \
               f"Data: {self.data_input}\n" \
               f"Input file: {self.input_file}\n" \
               f"Output: {self.output}\n" \
               f"Key: {self.key}"


def setup_request_commandline() -> Request:

    parser = argparse.ArgumentParser()
    parser.add_argument("key", help="The key to use when encrypting or "
                                    "decrypting. This needs to be of "
                                    "length 8, 16 or 24")
    parser.add_argument("-s", "--string", help="The string that needs to "
                                               "be "
                                               "encrypted or decrypted")
    parser.add_argument("-f", "--file", help="The text file that needs to be"
                                             "encrypted or decrypted")
    parser.add_argument("-o", "--output", default="print",
                        help="The output of the program. This is 'print' by "
                             "default, but can be set to a file name as well.")
    parser.add_argument("-m", "--mode", default="en",
                        help="The mode to run the program in. If 'en' (default)"
                             " then the program will encrypt, 'de' will cause "
                             "the program to decrypt")
    try:
        args = parser.parse_args()
        print(f"args: {args}")
        request = Request()
        print(f"args.mode: {args.mode}")
        request.encryption_state = CryptoMode(args.mode)
        request.data_input = args.string
        request.input_file = args.file
        request.output = args.output
        request.key = args.key
        return request
    except Exception as e:
        print(f"Error! Could not read arguments.\n{e}")
        quit()


class KeyLengthError(Exception):
    def __init__(self, length):
        super().__init__(f"Keys must be 8, 16, or 24 characters long."
                         f"Your key is {length} characters long.")
        self.length = length


class EmptyStringError(Exception):
    def __init__(self):
        super().__init__(f"You cannot use cryptography on an empty string.")


class MultipleInputSourceError(Exception):
    def __init__(self, string, file):
        super().__init__(f"You have multiple sources of input. String '"
                         f"{string}' and file path '{file}' were detected.")
        self.string = string
        self.file = file


class NoInputSourceError(Exception):
    def __init__(self):
        super().__init__(f"No input source detected.")


class FileExtensionError(Exception):
    def __init__(self, path):
        super().__init__(f"Your file path '{path}' does not end with the "
                         f".txt file extension.")
        self.path = path


class BaseCryptographyHandler(ABC):
    def __init__(self, next_handler=None) -> None:
        """
        Initialises a CryptographyHandler and sets up the next Handler.
        :param next_handler: CryptographyHandler
        """
        self._next_handler = next_handler

    @abstractmethod
    def handle_request(self, request) -> bool:
        pass

    @property
    def next_handler(self):
        return self._next_handler

    @next_handler.setter
    def next_handler(self, next_handler):
        self._next_handler = next_handler


class KeyCryptographyValidator(BaseCryptographyHandler):
    def handle_request(self, request) -> None:
        print("KeyCryptography running...")
        if len(request.key) in [8, 16, 24]:
            if not self.next_handler:
                return

            return self.next_handler.handle_request(request)
        else:
            raise KeyLengthError(len(request.key))


class InputCryptographyValidator(BaseCryptographyHandler):
    def handle_request(self, request) -> None:
        print("Input validator running...")

        # If there are two input sources
        if request.data_input and request.input_file:
            raise MultipleInputSourceError(request.data_input,
                                           request.input_file)

        # If there are no input sources
        if request.data_input is None and not request.input_file:
            raise NoInputSourceError

        # If there is only a raw string
        if request.data_input is not None:
            # Check that data has at least 1 character
            if len(request.data_input) > 0:
                if not self.next_handler:
                    return
                return self.next_handler.handle_request(request)
            else:
                raise EmptyStringError
        # If there is a file path
        else:
            # Check if extension is correct
            if not request.input_file.endswith(".txt"):
                raise FileExtensionError(request.input_file)
            # Check if the file is empty
            elif os.stat(request.input_file).st_size == 0:
                raise EmptyStringError
            # If there are no errors
            else:
                if not self.next_handler:
                    return
                return self.next_handler.handle_request(request)


class OutputCryptographyValidator(BaseCryptographyHandler):

    def handle_request(self, request) -> None:
        print("Output validator running...")
        if request.output.lower() == "print":
            if not self.next_handler:
                return
            return self.next_handler.handle_request(request)

        # Check if output path is valid
        if not request.output.endswith(".txt"):
            raise FileExtensionError(request.output)
        else:
            if not self.next_handler:
                return
            return self.next_handler.handle_request(request)


class EncryptionCryptographyHandler(BaseCryptographyHandler):
    def handle_request(self, request) -> None:
        print("Encryption handler running")
        # Set up encryption key
        bytes_key = request.key.encode()
        key0 = DesKey(bytes_key)

        # Encrypting from direct string
        if request.data_input:
            print("Encrypting request from direct string... ...")
            bytes_str = request.data_input.encode()
            request.result = key0.encrypt(bytes_str, padding=True)
        else:
            print("Encrypting from input file... ...")
            with open(request.input_file) as file:
                # bytes_str = request.input_file.encode()
                bytes_str = file.read().encode()
                request.result = key0.encrypt(bytes_str, padding=True)

        if self.next_handler:
            self.next_handler.handle_request(request)
        else:
            return


class DecryptionCryptographyHandler(BaseCryptographyHandler):
    def handle_request(self, request) -> None:
        # Set up decryption key
        bytes_key = request.key.encode()
        key0 = DesKey(bytes_key)

        if request.data_input:
            print("Decrypting request from direct string... ...")
            request.result = ast.literal_eval(r"{0}".format(
                request.data_input))
        else:
            with open(request.input_file, "rb+") as input_file:
                request.result = input_file.read()

        request.result = key0.decrypt(request.result, padding=True).decode(
            'utf-8')

        if self.next_handler:
            self.next_handler.handle_request(request)
        else:
            return


class PrintCryptographyHandler(BaseCryptographyHandler):
    def handle_request(self, request) -> None:
        print("Print handler running...")
        if request.output.lower() == "print":
            print(request.result)
        else:
            with open(request.output, "w+") as output_file:
                output_file.write(request.result)


class Crypto:

    def __init__(self):
        en_key = KeyCryptographyValidator()

        en_input = InputCryptographyValidator()

        en_output = OutputCryptographyValidator()
        en_handler = EncryptionCryptographyHandler()
        en_print = PrintCryptographyHandler()
        en_key.next_handler = en_input
        en_input.next_handler = en_output
        en_output.next_handler = en_handler
        en_handler.next_handler = en_print

        # Chain for decrypting data
        de_key = KeyCryptographyValidator()
        de_input = InputCryptographyValidator()
        de_output = OutputCryptographyValidator()
        de_handler = DecryptionCryptographyHandler()
        de_print = PrintCryptographyHandler()
        de_key.next_handler = de_input
        de_input.next_handler = de_output
        de_output.next_handler = de_handler
        de_handler.next_handler = de_print

        self.encryption_start_handler = en_key
        self.decryption_start_handler = de_key

    def execute_request(self, request: Request):
        if request.encryption_state is CryptoMode.EN:
            return self.encryption_start_handler.handle_request(request)
        elif request.encryption_state is CryptoMode.DE:
            return self.decryption_start_handler.handle_request(request)


def main(request: Request):
    driver = Crypto()
    try:
        driver.execute_request(request)
    except FileNotFoundError as e:
        print(e)


if __name__ == '__main__':
    request = setup_request_commandline()
    main(request)
