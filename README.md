# devhealth-digital-signage
A Development Health (GitHub, SonarQube, ...) digital signage project for the Adafruit MatrixPortal M4 and a 64x32 Matrix Display

# Antecedents & Acknowledgments 
This project uses the Adafruit MatrixPortal M4 portal, a unfied set of chips on a board, which in Adafruit's own words provides:

>The Matrix Portal uses an ATMEL (Microchip) ATSAMD51J19, and an Espressif ESP32 Wi-Fi coprocessor with TLS/SSL support built-in. The M4 and ESP32 are a great couple - and each bring their own strengths to this board. The SAMD51 M4 has native USB, so it can show up like a disk drive, act as a MIDI or HID keyboard/mouse, and of course bootload and debug over a serial port. It also has DACs, ADC, PWM, and tons of GPIO, so it can handle the high speed updating of the RGB matrix.

>Meanwhile, the ESP32 has secure WiFi capabilities, and plenty of Flash and RAM to buffer sockets. By letting the ESP32 focus on the complex TLS/SSL computation and socket buffering, it frees up the SAMD51 to act as the user interface. You get a great programming experience thanks to the native USB with files available for drag-n-drop, and you don't have to spend a ton of processor time and memory to do SSL encryption/decryption and certificate management. It's the best of both worlds!

https://learn.adafruit.com/adafruit-matrixportal-m4

I'm also going to base the code (at least the organziation a core structure) on the 'Moon Phase Clock' example Phillip Burgess for Adafruit Industries, copyright 2020, under the MIT License.  This project is also copyright, 2022, under the MIT License

https://learn.adafruit.com/moon-phase-clock-for-adafruit-matrixportal
