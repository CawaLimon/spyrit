EESchema Schematic File Version 2
LIBS:power
LIBS:device
LIBS:stm32
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
LIBS:Oscillators
LIBS:pyBoard-cache
EELAYER 25 0
EELAYER END
$Descr A1 33110 23386
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L STM32F405RGTx U?
U 1 1 5810CE81
P 11350 8400
F 0 "U?" H 7150 10325 50  0000 C CNN
F 1 "STM32F405RGTx" H 15550 10325 50  0000 R BNN
F 2 "LQFP64" H 15550 10275 50  0000 R TNN
F 3 "" H 11350 8400 50  0000 C CNN
	1    11350 8400
	1    0    0    -1  
$EndComp
$Comp
L STM32F405RGTx U?
U 1 1 5810CFA4
P 11350 8400
F 0 "U?" H 7150 10325 50  0000 C CNN
F 1 "STM32F405RGTx" H 15550 10325 50  0000 R BNN
F 2 "LQFP64" H 15550 10275 50  0000 R TNN
F 3 "" H 11350 8400 50  0000 C CNN
	1    11350 8400
	1    0    0    -1  
$EndComp
Text GLabel 15650 6800 2    60   Input ~ 0
PA0-X1
Text GLabel 15650 6900 2    60   Input ~ 0
PA1-X2
Text GLabel 15650 7000 2    60   Input ~ 0
PA2-X3
Text GLabel 15650 7200 2    60   Input ~ 0
PA4-X5
Text GLabel 15650 7100 2    60   Input ~ 0
PA3-X4
Text GLabel 15650 7400 2    60   Input ~ 0
PA6-X7
Text GLabel 15650 7300 2    60   Input ~ 0
PA5-X6
Text GLabel 16550 7800 2    60   Input ~ 0
PA10-ID
Text GLabel 15650 7900 2    60   Input ~ 0
PA11-DM
Text GLabel 15650 8100 2    60   Input ~ 0
PA13-RED-P5
Text GLabel 15650 8000 2    60   Input ~ 0
PA12-DP
Text GLabel 15650 8200 2    60   Input ~ 0
PA14-GRN-P4
Text GLabel 15650 8300 2    60   Input ~ 0
PA15-YEL-P3
Text GLabel 15650 8500 2    60   Input ~ 0
PB0-Y11
Text GLabel 15650 8600 2    60   Input ~ 0
PB1-Y12
Text GLabel 16700 8700 2    60   Input ~ 0
PB2-BOOT1-MMA-INT
Text GLabel 15650 8800 2    60   Input ~ 0
PB3-SW-X17
Text GLabel 15650 8900 2    60   Input ~ 0
PB4-BLU-P2
Text GLabel 17200 9000 2    60   Input ~ 0
PB5-MMA_AVDD
Text GLabel 19000 9100 2    60   Input ~ 0
PB6-SCL-X9
Text GLabel 19000 9200 2    60   Input ~ 0
PB7-SDA-X10
Text GLabel 15650 9300 2    60   Input ~ 0
PB8-Y3
Text GLabel 15650 9400 2    60   Input ~ 0
PB9-Y4
Text GLabel 19000 9500 2    60   Input ~ 0
PB10-Y9
Text GLabel 19000 9600 2    60   Input ~ 0
PB11-Y10
Text GLabel 15650 9700 2    60   Input ~ 0
PB12-Y5
Text GLabel 15650 9800 2    60   Input ~ 0
PB13-Y6
Text GLabel 15650 9900 2    60   Input ~ 0
PB14-Y7
Text GLabel 15650 10000 2    60   Input ~ 0
PB15-Y8
$Comp
L R R9]
U 1 1 5810DD9C
P 18050 8650
F 0 "R9]" V 18130 8650 50  0000 C CNN
F 1 "4k7" V 18050 8650 50  0000 C CNN
F 2 "" V 17980 8650 50  0000 C CNN
F 3 "" H 18050 8650 50  0000 C CNN
	1    18050 8650
	1    0    0    -1  
$EndComp
$Comp
L R R10
U 1 1 5810DEC1
P 18300 8650
F 0 "R10" V 18380 8650 50  0000 C CNN
F 1 "4k7" V 18300 8650 50  0000 C CNN
F 2 "" V 18230 8650 50  0000 C CNN
F 3 "" H 18300 8650 50  0000 C CNN
	1    18300 8650
	1    0    0    -1  
$EndComp
$Comp
L R R11
U 1 1 5810DEE4
P 18550 8650
F 0 "R11" V 18630 8650 50  0000 C CNN
F 1 "4k7" V 18550 8650 50  0000 C CNN
F 2 "" V 18480 8650 50  0000 C CNN
F 3 "" H 18550 8650 50  0000 C CNN
	1    18550 8650
	1    0    0    -1  
$EndComp
$Comp
L R R12
U 1 1 5810DF03
P 18800 8650
F 0 "R12" V 18880 8650 50  0000 C CNN
F 1 "4k7" V 18800 8650 50  0000 C CNN
F 2 "" V 18730 8650 50  0000 C CNN
F 3 "" H 18800 8650 50  0000 C CNN
	1    18800 8650
	1    0    0    -1  
$EndComp
$Comp
L R R20
U 1 1 5810DF36
P 16600 9850
F 0 "R20" V 16680 9850 50  0000 C CNN
F 1 "100k" V 16600 9850 50  0000 C CNN
F 2 "" V 16530 9850 50  0000 C CNN
F 3 "" H 16600 9850 50  0000 C CNN
	1    16600 9850
	1    0    0    -1  
$EndComp
$Comp
L R R20
U 1 1 5810DF59
P 16950 9850
F 0 "R20" V 17030 9850 50  0000 C CNN
F 1 "R" V 16950 9850 50  0000 C CNN
F 2 "" V 16880 9850 50  0000 C CNN
F 3 "" H 16950 9850 50  0000 C CNN
	1    16950 9850
	1    0    0    -1  
$EndComp
$Comp
L +3V3 #PWR?
U 1 1 5810E2CF
P 19400 8400
F 0 "#PWR?" H 19400 8250 50  0001 C CNN
F 1 "+3V3" H 19400 8540 50  0000 C CNN
F 2 "" H 19400 8400 50  0000 C CNN
F 3 "" H 19400 8400 50  0000 C CNN
	1    19400 8400
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR?
U 1 1 5810E47A
P 17100 10100
F 0 "#PWR?" H 17100 9850 50  0001 C CNN
F 1 "GND" H 17100 9950 50  0000 C CNN
F 2 "" H 17100 10100 50  0000 C CNN
F 3 "" H 17100 10100 50  0000 C CNN
	1    17100 10100
	1    0    0    -1  
$EndComp
Text GLabel 15650 7700 2    60   Input ~ 0
PA9-VBUS
Text GLabel 15650 7500 2    60   Input ~ 0
PA7-X8
$Comp
L R R21
U 1 1 5810F084
P 16500 7400
F 0 "R21" V 16580 7400 50  0000 C CNN
F 1 "100k" V 16500 7400 50  0000 C CNN
F 2 "" V 16430 7400 50  0000 C CNN
F 3 "" H 16500 7400 50  0000 C CNN
	1    16500 7400
	1    0    0    -1  
$EndComp
$Comp
L +3V3 #PWR?
U 1 1 5810F0BD
P 16500 7100
F 0 "#PWR?" H 16500 6950 50  0001 C CNN
F 1 "+3V3" H 16500 7240 50  0000 C CNN
F 2 "" H 16500 7100 50  0000 C CNN
F 3 "" H 16500 7100 50  0000 C CNN
	1    16500 7100
	1    0    0    -1  
$EndComp
NoConn ~ 7050 9300
NoConn ~ 7050 9400
NoConn ~ 7050 9500
NoConn ~ 7050 9600
NoConn ~ 7050 9700
Text GLabel 7050 9800 0    60   Input ~ 0
PC13-X18
NoConn ~ 7050 9900
NoConn ~ 7050 10000
Text GLabel 7050 8500 0    60   Input ~ 0
PC0-X19
Text GLabel 7050 8600 0    60   Input ~ 0
PC1-X20
Text GLabel 7050 8700 0    60   Input ~ 0
PC2-X21
Text GLabel 7050 8800 0    60   Input ~ 0
PC3-X22
Text GLabel 7050 8900 0    60   Input ~ 0
PC4-X11
Text GLabel 7050 9000 0    60   Input ~ 0
PC5-X12
Text GLabel 7050 9100 0    60   Input ~ 0
PC6-Y1
Text GLabel 7050 9200 0    60   Input ~ 0
PC7-Y2
NoConn ~ 7050 8300
Text GLabel 1100 6800 0    60   Input ~ 0
RST#
Text GLabel 3350 7000 0    60   Input ~ 0
BOOT0-P1
Text GLabel 3350 7300 0    60   Input ~ 0
VCAP1
Text GLabel 3350 7400 0    60   Input ~ 0
VCAP2
$Comp
L R R15
U 1 1 5810FB4E
P 3600 7600
F 0 "R15" V 3680 7600 50  0000 C CNN
F 1 "100k" V 3600 7600 50  0000 C CNN
F 2 "" V 3530 7600 50  0000 C CNN
F 3 "" H 3600 7600 50  0000 C CNN
	1    3600 7600
	0    1    1    0   
$EndComp
$Comp
L C C19
U 1 1 5810FBAB
P 3600 7850
F 0 "C19" H 3625 7950 50  0000 L CNN
F 1 "2u2" H 3625 7750 50  0000 L CNN
F 2 "" H 3638 7700 50  0000 C CNN
F 3 "" H 3600 7850 50  0000 C CNN
	1    3600 7850
	0    1    1    0   
$EndComp
$Comp
L C C20
U 1 1 5810FBEA
P 3600 8100
F 0 "C20" H 3625 8200 50  0000 L CNN
F 1 "2u2" H 3625 8000 50  0000 L CNN
F 2 "" H 3638 7950 50  0000 C CNN
F 3 "" H 3600 8100 50  0000 C CNN
	1    3600 8100
	0    1    1    0   
$EndComp
$Comp
L GND #PWR?
U 1 1 5810FEA3
P 3250 8250
F 0 "#PWR?" H 3250 8000 50  0001 C CNN
F 1 "GND" H 3250 8100 50  0000 C CNN
F 2 "" H 3250 8250 50  0000 C CNN
F 3 "" H 3250 8250 50  0000 C CNN
	1    3250 8250
	1    0    0    -1  
$EndComp
NoConn ~ 15650 7600
$Comp
L +3V3 #PWR?
U 1 1 58111019
P 1850 6450
F 0 "#PWR?" H 1850 6300 50  0001 C CNN
F 1 "+3V3" H 1850 6590 50  0000 C CNN
F 2 "" H 1850 6450 50  0000 C CNN
F 3 "" H 1850 6450 50  0000 C CNN
	1    1850 6450
	1    0    0    -1  
$EndComp
$Comp
L R R3
U 1 1 58111045
P 1850 6650
F 0 "R3" V 1930 6650 50  0000 C CNN
F 1 "4k7" V 1850 6650 50  0000 C CNN
F 2 "" V 1780 6650 50  0000 C CNN
F 3 "" H 1850 6650 50  0000 C CNN
	1    1850 6650
	1    0    0    -1  
$EndComp
$Comp
L SPST SW1-RST
U 1 1 58112B0E
P 1850 7500
F 0 "SW1-RST" H 1850 7600 50  0000 C CNN
F 1 "SPST" H 1850 7400 50  0000 C CNN
F 2 "" H 1850 7500 50  0000 C CNN
F 3 "" H 1850 7500 50  0000 C CNN
	1    1850 7500
	0    1    1    0   
$EndComp
Text Notes 1000 8800 0    59   ~ 0
In the original schematic PYBv10b, \nthis is a four port switch with only \ntwo ports being active and default to open.
$Comp
L C C13
U 1 1 581130A0
P 2500 7550
F 0 "C13" H 2525 7650 50  0000 L CNN
F 1 "100n" H 2525 7450 50  0000 L CNN
F 2 "" H 2538 7400 50  0000 C CNN
F 3 "" H 2500 7550 50  0000 C CNN
	1    2500 7550
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR?
U 1 1 58113283
P 1850 8200
F 0 "#PWR?" H 1850 7950 50  0001 C CNN
F 1 "GND" H 1850 8050 50  0000 C CNN
F 2 "" H 1850 8200 50  0000 C CNN
F 3 "" H 1850 8200 50  0000 C CNN
	1    1850 8200
	1    0    0    -1  
$EndComp
Text Notes 4800 9700 0    60   ~ 0
These ports are related to the \nuSD. We have determined that\nthis is not required. See FIRECODE\ndocuments for more information
$Comp
L Crystal Y1
U 1 1 581156EC
P 5700 7800
F 0 "Y1" H 5700 7950 50  0000 C CNN
F 1 "8MHz" H 5700 7650 50  0000 C CNN
F 2 "" H 5700 7800 50  0000 C CNN
F 3 "" H 5700 7800 50  0000 C CNN
	1    5700 7800
	1    0    0    -1  
$EndComp
$Comp
L C C2
U 1 1 581158A3
P 5950 8400
F 0 "C2" H 5975 8500 50  0000 L CNN
F 1 "18p" H 5975 8300 50  0000 L CNN
F 2 "" H 5988 8250 50  0000 C CNN
F 3 "" H 5950 8400 50  0000 C CNN
	1    5950 8400
	1    0    0    -1  
$EndComp
$Comp
L C C1
U 1 1 5811595A
P 5400 8400
F 0 "C1" H 5425 8500 50  0000 L CNN
F 1 "18p" H 5425 8300 50  0000 L CNN
F 2 "" H 5438 8250 50  0000 C CNN
F 3 "" H 5400 8400 50  0000 C CNN
	1    5400 8400
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR?
U 1 1 581162C5
P 5400 8700
F 0 "#PWR?" H 5400 8450 50  0001 C CNN
F 1 "GND" H 5400 8550 50  0000 C CNN
F 2 "" H 5400 8700 50  0000 C CNN
F 3 "" H 5400 8700 50  0000 C CNN
	1    5400 8700
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR?
U 1 1 5811731F
P 11350 10700
F 0 "#PWR?" H 11350 10450 50  0001 C CNN
F 1 "GND" H 11350 10550 50  0000 C CNN
F 2 "" H 11350 10700 50  0000 C CNN
F 3 "" H 11350 10700 50  0000 C CNN
	1    11350 10700
	1    0    0    -1  
$EndComp
$Comp
L C C8
U 1 1 58118035
P 6000 5750
F 0 "C8" H 6025 5850 50  0000 L CNN
F 1 "100n" H 6025 5650 50  0000 L CNN
F 2 "" H 6038 5600 50  0000 C CNN
F 3 "" H 6000 5750 50  0000 C CNN
	1    6000 5750
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR?
U 1 1 581180C6
P 6000 6100
F 0 "#PWR?" H 6000 5850 50  0001 C CNN
F 1 "GND" H 6000 5950 50  0000 C CNN
F 2 "" H 6000 6100 50  0000 C CNN
F 3 "" H 6000 6100 50  0000 C CNN
	1    6000 6100
	1    0    0    -1  
$EndComp
Text GLabel 6000 5350 1    60   Input ~ 0
VBAT
$Comp
L C C?
U 1 1 58118FBE
P 9900 5650
F 0 "C?" H 9925 5750 50  0000 L CNN
F 1 "4u7" H 9925 5550 50  0000 L CNN
F 2 "" H 9938 5500 50  0000 C CNN
F 3 "" H 9900 5650 50  0000 C CNN
	1    9900 5650
	1    0    0    -1  
$EndComp
$Comp
L C C3
U 1 1 58119050
P 10200 5650
F 0 "C3" H 10225 5750 50  0000 L CNN
F 1 "100n" H 10225 5550 50  0000 L CNN
F 2 "" H 10238 5500 50  0000 C CNN
F 3 "" H 10200 5650 50  0000 C CNN
	1    10200 5650
	1    0    0    -1  
$EndComp
$Comp
L C C4
U 1 1 58119128
P 10500 5650
F 0 "C4" H 10525 5750 50  0000 L CNN
F 1 "100n" H 10525 5550 50  0000 L CNN
F 2 "" H 10538 5500 50  0000 C CNN
F 3 "" H 10500 5650 50  0000 C CNN
	1    10500 5650
	1    0    0    -1  
$EndComp
$Comp
L C C5
U 1 1 581191B5
P 10800 5650
F 0 "C5" H 10825 5750 50  0000 L CNN
F 1 "100n" H 10825 5550 50  0000 L CNN
F 2 "" H 10838 5500 50  0000 C CNN
F 3 "" H 10800 5650 50  0000 C CNN
	1    10800 5650
	1    0    0    -1  
$EndComp
$Comp
L C C6
U 1 1 58119262
P 11100 5650
F 0 "C6" H 11125 5750 50  0000 L CNN
F 1 "100n" H 11125 5550 50  0000 L CNN
F 2 "" H 11138 5500 50  0000 C CNN
F 3 "" H 11100 5650 50  0000 C CNN
	1    11100 5650
	1    0    0    -1  
$EndComp
Wire Wire Line
	15650 8700 16700 8700
Wire Wire Line
	15650 9000 17200 9000
Wire Wire Line
	15650 9100 19000 9100
Wire Wire Line
	15650 9200 19000 9200
Wire Wire Line
	15650 9500 19000 9500
Wire Wire Line
	15650 9600 19000 9600
Wire Wire Line
	18800 8800 18800 9600
Connection ~ 18800 9600
Wire Wire Line
	18550 8800 18550 9500
Connection ~ 18550 9500
Wire Wire Line
	18300 8800 18300 9200
Connection ~ 18300 9200
Wire Wire Line
	18050 8800 18050 9100
Connection ~ 18050 9100
Wire Wire Line
	18050 8400 19400 8400
Wire Wire Line
	18050 8400 18050 8500
Wire Wire Line
	18300 8400 18300 8500
Connection ~ 18300 8400
Wire Wire Line
	18550 8400 18550 8500
Connection ~ 18550 8400
Wire Wire Line
	18800 8400 18800 8500
Connection ~ 18800 8400
Wire Wire Line
	16600 9700 16600 8700
Connection ~ 16600 8700
Wire Wire Line
	16950 9700 16950 9000
Connection ~ 16950 9000
Wire Wire Line
	16600 10000 16600 10100
Wire Wire Line
	16600 10100 17100 10100
Wire Wire Line
	16950 10000 16950 10100
Connection ~ 16950 10100
Wire Wire Line
	16500 7100 16500 7250
Wire Wire Line
	16500 7550 16500 7800
Wire Wire Line
	15650 7800 16550 7800
Connection ~ 16500 7800
Wire Wire Line
	3350 7300 7050 7300
Wire Wire Line
	3350 7400 7050 7400
Wire Wire Line
	3350 7000 7050 7000
Wire Wire Line
	3850 7000 3850 7600
Wire Wire Line
	3850 7600 3750 7600
Connection ~ 3850 7000
Wire Wire Line
	4050 7300 4050 7850
Wire Wire Line
	4050 7850 3750 7850
Connection ~ 4050 7300
Wire Wire Line
	4250 7400 4250 8100
Wire Wire Line
	4250 8100 3750 8100
Connection ~ 4250 7400
Wire Wire Line
	3450 7600 3250 7600
Wire Wire Line
	3250 7600 3250 8250
Wire Wire Line
	3450 7850 3250 7850
Connection ~ 3250 7850
Wire Wire Line
	3450 8100 3250 8100
Connection ~ 3250 8100
Wire Wire Line
	1100 6800 7050 6800
Wire Wire Line
	1850 6450 1850 6500
Wire Wire Line
	1850 6800 1850 7000
Connection ~ 1850 6800
Wire Wire Line
	2500 6800 2500 7400
Connection ~ 2500 6800
Wire Wire Line
	2500 7700 2500 8000
Wire Wire Line
	2500 8000 1850 8000
Wire Wire Line
	1850 8000 1850 8200
Wire Wire Line
	7050 8000 6900 8000
Wire Wire Line
	6900 8000 6900 7800
Wire Wire Line
	5400 7800 5400 8250
Wire Wire Line
	5400 8550 5400 8700
Wire Wire Line
	7050 8100 5400 8100
Connection ~ 5400 8100
Wire Wire Line
	5400 7800 5550 7800
Wire Wire Line
	6900 7800 5850 7800
Wire Wire Line
	5950 7800 5950 8250
Connection ~ 5950 7800
Wire Wire Line
	5950 8550 5950 8600
Wire Wire Line
	5950 8600 5400 8600
Connection ~ 5400 8600
Wire Wire Line
	11250 10400 11250 10700
Wire Wire Line
	11250 10700 11450 10700
Wire Wire Line
	11350 10700 11350 10400
Wire Wire Line
	11450 10700 11450 10400
Connection ~ 11350 10700
Wire Wire Line
	7050 7200 6400 7200
Wire Wire Line
	6400 7200 6400 5500
Wire Wire Line
	6400 5500 6000 5500
Wire Wire Line
	6000 5350 6000 5600
Connection ~ 6000 5500
Wire Wire Line
	6000 5900 6000 6100
Wire Wire Line
	11450 6400 11450 5400
Wire Wire Line
	11150 6400 11150 6150
Wire Wire Line
	11150 6150 11450 6150
Connection ~ 11450 6150
Wire Wire Line
	11250 6400 11250 6150
Connection ~ 11250 6150
Wire Wire Line
	11350 6400 11350 6150
Connection ~ 11350 6150
Wire Wire Line
	11450 5400 9900 5400
Wire Wire Line
	9900 5400 9900 5500
Wire Wire Line
	10200 5500 10200 5400
Connection ~ 10200 5400
Wire Wire Line
	10500 4750 10500 5500
Connection ~ 10500 5400
Wire Wire Line
	10800 5500 10800 5400
Connection ~ 10800 5400
Wire Wire Line
	11100 5500 11100 5400
Connection ~ 11100 5400
$Comp
L GND #PWR?
U 1 1 5811990D
P 10500 6000
F 0 "#PWR?" H 10500 5750 50  0001 C CNN
F 1 "GND" H 10500 5850 50  0000 C CNN
F 2 "" H 10500 6000 50  0000 C CNN
F 3 "" H 10500 6000 50  0000 C CNN
	1    10500 6000
	1    0    0    -1  
$EndComp
Wire Wire Line
	9900 5800 9900 6000
Wire Wire Line
	9900 6000 11100 6000
Wire Wire Line
	11100 6000 11100 5800
Connection ~ 10500 6000
Wire Wire Line
	10800 5800 10800 6000
Wire Wire Line
	10800 6000 10850 6000
Connection ~ 10850 6000
Wire Wire Line
	10500 5800 10500 6000
Wire Wire Line
	10200 5800 10200 6000
Connection ~ 10200 6000
$Comp
L +3V3 #PWR?
U 1 1 58119C06
P 10500 4750
F 0 "#PWR?" H 10500 4600 50  0001 C CNN
F 1 "+3V3" H 10500 4890 50  0000 C CNN
F 2 "" H 10500 4750 50  0000 C CNN
F 3 "" H 10500 4750 50  0000 C CNN
	1    10500 4750
	1    0    0    -1  
$EndComp
Wire Wire Line
	11550 6400 11550 5700
Wire Wire Line
	11550 5700 12300 5700
$Comp
L C C10
U 1 1 58119D63
P 12000 5950
F 0 "C10" H 12025 6050 50  0000 L CNN
F 1 "100n" H 12025 5850 50  0000 L CNN
F 2 "" H 12038 5800 50  0000 C CNN
F 3 "" H 12000 5950 50  0000 C CNN
	1    12000 5950
	1    0    0    -1  
$EndComp
$Comp
L C C9
U 1 1 58119E20
P 12300 5950
F 0 "C9" H 12325 6050 50  0000 L CNN
F 1 "4u7" H 12325 5850 50  0000 L CNN
F 2 "" H 12338 5800 50  0000 C CNN
F 3 "" H 12300 5950 50  0000 C CNN
	1    12300 5950
	1    0    0    -1  
$EndComp
Text GLabel 12400 5600 2    60   Input ~ 0
A3V3
Wire Wire Line
	12300 5700 12300 5800
Wire Wire Line
	12000 5700 12000 5800
Connection ~ 12000 5700
$Comp
L GND #PWR?
U 1 1 5811A117
P 12150 6250
F 0 "#PWR?" H 12150 6000 50  0001 C CNN
F 1 "GND" H 12150 6100 50  0000 C CNN
F 2 "" H 12150 6250 50  0000 C CNN
F 3 "" H 12150 6250 50  0000 C CNN
	1    12150 6250
	1    0    0    -1  
$EndComp
Wire Wire Line
	12000 6100 12000 6250
Wire Wire Line
	12000 6250 12300 6250
Wire Wire Line
	12300 6250 12300 6100
Connection ~ 12150 6250
Wire Wire Line
	12150 5700 12150 5600
Connection ~ 12150 5700
$Comp
L INDUCTOR L1
U 1 1 5811A352
P 12150 5300
F 0 "L1" V 12100 5300 50  0000 C CNN
F 1 "1k" V 12250 5300 50  0000 C CNN
F 2 "" H 12150 5300 50  0000 C CNN
F 3 "" H 12150 5300 50  0000 C CNN
	1    12150 5300
	1    0    0    -1  
$EndComp
Text Notes 12450 5400 0    60   ~ 0
The symbol in PYBv10b\nis different but has name\nL1 with value 1k
Wire Wire Line
	12150 5600 12400 5600
Wire Wire Line
	12150 5000 10500 5000
Connection ~ 10500 5000
$EndSCHEMATC
