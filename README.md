# Chip-8-Emulator

A chip8 emulator built using pygame.

## Requirements

* Python 3
* pygame 2.0.1

## Setup

* Clone the repository to a folder

    ```bash
    git clone https://github.com/shree-vidya/Chip-8-Emulator.git
    ```

* `cd` into folder and create virtual environment and activate.

    ```bash
    python3 -m venv env
    . env/bin/activate
    ```

* Install all required modules

    ```bash
    pip3 install -r requirements.txt
    ```

* To run the application:

    ```bash
    python3 main.py
    ```

* If it works fine then deploy on AWS lambda using
  
    ```bash
    chalice deploy
    ```

## References

* http://devernay.free.fr/hacks/chip8/C8TECH10.HTM#0.0
