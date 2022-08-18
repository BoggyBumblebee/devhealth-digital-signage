# Development Health Digital Signage

A Development Health (GitHub, SonarQube, ...) digital signage project for the Adafruit MatrixPortal M4 and a 64x32 Matrix Display

## Antecedents & Acknowledgments

This project uses the Adafruit MatrixPortal M4 portal, a unified set of chips on a board, which in Adafruit's own words provides:

>The Matrix Portal uses an ATMEL (Microchip) ATSAMD51J19, and an Espressif ESP32 Wi-Fi coprocessor with TLS/SSL support built-in. The M4 and ESP32 are a great couple - and each bring their own strengths to this board. The SAMD51 M4 has native USB, so it can show up like a disk drive, act as a MIDI or HID keyboard/mouse, and of course bootload and debug over a serial port. It also has DACs, ADC, PWM, and tons of GPIO, so it can handle the high speed updating of the RGB matrix.
Meanwhile, the ESP32 has secure WiFi capabilities, and plenty of Flash and RAM to buffer sockets. By letting the ESP32 focus on the complex TLS/SSL computation and socket buffering, it frees up the SAMD51 to act as the user interface. You get a great programming experience thanks to the native USB with files available for drag-n-drop, and you don't have to spend a ton of processor time and memory to do SSL encryption/decryption and certificate management. It's the best of both worlds!

[Adafruit MatrixPortal M4](https://learn.adafruit.com/adafruit-matrixportal-m4)

I'm also going to base the code (at least the organziation and core structure) on the 'Moon Phase Clock' example Phillip
Burgess for Adafruit Industries, copyright 2020, under the MIT License.  This project is also copyright, 2022, under the
MIT License

[Adafruit Moon Phase Clock](https://learn.adafruit.com/moon-phase-clock-for-adafruit-matrixportal)

## Dependencies

I've not made these libraries available in this repository, but they can be downloaded from the link below, dependent on
the version of CircuitPython (7.x or 8.x) you are using. I am using the 7.x libraries at the present time, to test and
run this.

[CircuitPython Libraries](https://circuitpython.org/libraries)

- adafruit_matrixportal - this library is the main library used with the MatrixPortal
- adafruit_bitmap_font - we have fancy font support, and it's easy to make new fonts. This library reads and parses font files
- adafruit_display_text - not surprisingly, it displays text on the screen
- adafruit_lis3dh.mpy - this library is used for the onboard accelerometer to detect the orientation of the MatrixPortal

## Installation

To use with CircuitPython, you need to first install the above libraries, into the lib folder on your CIRCUITPY drive.
Ensure that you have also copied (and updated with your secrets) the `secrets.py`. Finally, you need to update
`code.py` with the code from this repository.

## Technical Debt Badges

Yes, this is kind of circular, as these are the stats that the Digital Signage will show.  Here they are for the stats
for the project itself!

[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=devhealth-digital-signage&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=devhealth-digital-signage)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=devhealth-digital-signage&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=devhealth-digital-signage)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=devhealth-digital-signage&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=devhealth-digital-signage)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=devhealth-digital-signage&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=devhealth-digital-signage)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=devhealth-digital-signage&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=devhealth-digital-signage)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=devhealth-digital-signage&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=devhealth-digital-signage)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=devhealth-digital-signage&metric=coverage)](https://sonarcloud.io/summary/new_code?id=devhealth-digital-signage)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=devhealth-digital-signage&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=devhealth-digital-signage)
