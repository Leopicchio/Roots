EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
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
L Device:L L1
U 1 1 5F61174B
P 5350 5800
F 0 "L1" H 5402 5846 50  0000 L CNN
F 1 "1m" H 5402 5755 50  0000 L CNN
F 2 "Inductor_SMD:L_1008_2520Metric" H 5350 5800 50  0001 C CNN
F 3 "~" H 5350 5800 50  0001 C CNN
	1    5350 5800
	1    0    0    -1  
$EndComp
$Comp
L Device:C C1
U 1 1 5F611C3C
P 5350 6200
F 0 "C1" H 5465 6246 50  0000 L CNN
F 1 "10p" H 5465 6155 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 5388 6050 50  0001 C CNN
F 3 "~" H 5350 6200 50  0001 C CNN
	1    5350 6200
	1    0    0    -1  
$EndComp
Wire Wire Line
	5350 5450 5900 5450
$Comp
L Amplifier_Buffer:BUF602xD U1
U 1 1 5F614228
P 6200 5450
F 0 "U1" H 6544 5496 50  0000 L CNN
F 1 "BUF602xD" H 6544 5405 50  0000 L CNN
F 2 "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" H 6200 5150 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/buf602.pdf" H 6200 5450 50  0001 C CNN
	1    6200 5450
	1    0    0    -1  
$EndComp
$Comp
L power:+3.3V #PWR010
U 1 1 5F6150C6
P 6100 5150
F 0 "#PWR010" H 6100 5000 50  0001 C CNN
F 1 "+3.3V" H 6115 5323 50  0000 C CNN
F 2 "" H 6100 5150 50  0001 C CNN
F 3 "" H 6100 5150 50  0001 C CNN
	1    6100 5150
	1    0    0    -1  
$EndComp
$Comp
L Device:R R2
U 1 1 5F615997
P 7450 5600
F 0 "R2" H 7520 5646 50  0000 L CNN
F 1 "510k" H 7520 5555 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 7380 5600 50  0001 C CNN
F 3 "~" H 7450 5600 50  0001 C CNN
	1    7450 5600
	1    0    0    -1  
$EndComp
$Comp
L Device:C C2
U 1 1 5F615DD6
P 7850 5600
F 0 "C2" H 7965 5646 50  0000 L CNN
F 1 "470p" H 7965 5555 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 7888 5450 50  0001 C CNN
F 3 "~" H 7850 5600 50  0001 C CNN
	1    7850 5600
	1    0    0    -1  
$EndComp
Wire Wire Line
	6500 5450 7000 5450
Wire Wire Line
	7850 5450 7450 5450
Connection ~ 7450 5450
Wire Wire Line
	7450 5750 7850 5750
$Comp
L Device:R R1
U 1 1 5F60FA22
P 5350 5300
F 0 "R1" H 5280 5254 50  0000 R CNN
F 1 "1k" H 5280 5345 50  0000 R CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 5280 5300 50  0001 C CNN
F 3 "~" H 5350 5300 50  0001 C CNN
	1    5350 5300
	-1   0    0    1   
$EndComp
Connection ~ 5350 5450
Wire Wire Line
	5350 5450 5350 5650
Wire Wire Line
	5350 5950 5350 6050
$Comp
L Diode:1N914 D1
U 1 1 5F61BA3C
P 7150 5450
F 0 "D1" H 7150 5234 50  0000 C CNN
F 1 "1N914" H 7150 5325 50  0000 C CNN
F 2 "Diode_SMD:D_SOD-523" H 7150 5275 50  0001 C CNN
F 3 "http://www.vishay.com/docs/85622/1n914.pdf" H 7150 5450 50  0001 C CNN
	1    7150 5450
	-1   0    0    1   
$EndComp
Wire Wire Line
	7300 5450 7450 5450
Connection ~ 7850 5450
Wire Notes Line
	7000 4950 7000 6050
Wire Notes Line
	7000 6050 8250 6050
Wire Notes Line
	8250 6050 8250 4950
Wire Notes Line
	8250 4950 7000 4950
Wire Notes Line
	5000 6650 5700 6650
Wire Notes Line
	5700 6650 5700 4900
Wire Notes Line
	5700 4900 5000 4900
Text Notes 5050 7200 0    50   ~ 0
Resonant circuit. \n\nThe frequency of oscillation (where the peak is)\n depends on L1 and C1 according to the \nformula f_peak = 1/(2*pi*sqrt(L1*C1)).  \nIncreasing R1 makes the peak wider
Text Notes 7300 6200 0    50   ~ 0
Envelope detector.\n
Wire Notes Line
	5000 4900 5000 6650
$Comp
L AD5932_Ultralibrarian:AD5932YRUZ U2
U 1 1 5F6290CA
P 2400 2250
F 0 "U2" H 4000 2637 60  0000 C CNN
F 1 "AD5932YRUZ" H 4000 2531 60  0000 C CNN
F 2 "AD5932YRUZ:AD5932YRUZ" H 4000 2490 60  0001 C CNN
F 3 "" H 2400 2250 60  0000 C CNN
	1    2400 2250
	1    0    0    -1  
$EndComp
Text Notes 5150 4550 0    50   ~ 0
Connector used to test \nthe circuit with an external \nWaveform Generator.
Text Notes 3700 3300 0    50   ~ 0
Signal generator
Wire Wire Line
	5600 2350 6100 2350
Text GLabel 5600 2450 2    50   Input ~ 0
STANDBY
Text GLabel 5600 2850 2    50   Input ~ 0
CTRL
Text GLabel 5600 2950 2    50   Input ~ 0
INTERRUPT
$Comp
L Device:C C5
U 1 1 5F63D74D
P 1850 2550
F 0 "C5" V 1900 2300 50  0000 C CNN
F 1 "100nF" V 1800 2350 50  0000 C CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 1888 2400 50  0001 C CNN
F 3 "~" H 1850 2550 50  0001 C CNN
	1    1850 2550
	0    1    1    0   
$EndComp
Text GLabel 2400 2750 0    50   Input ~ 0
MCLK
Text GLabel 2400 2850 0    50   Input ~ 0
SYNCOUT
Text GLabel 2400 2950 0    50   Input ~ 0
MSBOUT
Wire Wire Line
	1450 2650 1700 2650
Wire Wire Line
	1700 2550 1700 2650
Connection ~ 1700 2650
Wire Wire Line
	1700 2650 2400 2650
Wire Wire Line
	2000 2550 2400 2550
Text GLabel 5600 2550 2    50   Input ~ 0
FSYNC
Text GLabel 5600 2650 2    50   Input ~ 0
SCLK
Text GLabel 5600 2750 2    50   Input ~ 0
SDATA
Wire Wire Line
	2400 2350 2050 2350
Wire Wire Line
	2050 2350 2050 2250
Wire Wire Line
	2400 2450 1750 2450
$Comp
L Device:C C7
U 1 1 5F65D5C2
P 2250 2250
F 0 "C7" V 1998 2250 50  0000 C CNN
F 1 "10nF" V 2089 2250 50  0000 C CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 2288 2100 50  0001 C CNN
F 3 "~" H 2250 2250 50  0001 C CNN
	1    2250 2250
	0    1    1    0   
$EndComp
Wire Wire Line
	2100 2250 2050 2250
$Comp
L Device:C C3
U 1 1 5F6614C5
P 850 1350
F 0 "C3" H 965 1396 50  0000 L CNN
F 1 "100nF" H 965 1305 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 888 1200 50  0001 C CNN
F 3 "~" H 850 1350 50  0001 C CNN
	1    850  1350
	-1   0    0    1   
$EndComp
$Comp
L Device:C C4
U 1 1 5F6614CB
P 1250 1350
F 0 "C4" H 1365 1396 50  0000 L CNN
F 1 "10uF" H 1365 1305 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 1288 1200 50  0001 C CNN
F 3 "~" H 1250 1350 50  0001 C CNN
	1    1250 1350
	-1   0    0    1   
$EndComp
Wire Wire Line
	850  1500 1250 1500
Wire Wire Line
	850  1200 1250 1200
Connection ~ 1250 1200
Wire Wire Line
	1250 1200 1750 1200
$Comp
L power:GNDD #PWR02
U 1 1 5F6614DB
P 850 1500
F 0 "#PWR02" H 850 1250 50  0001 C CNN
F 1 "GNDD" H 854 1345 50  0000 C CNN
F 2 "" H 850 1500 50  0001 C CNN
F 3 "" H 850 1500 50  0001 C CNN
	1    850  1500
	1    0    0    -1  
$EndComp
Connection ~ 850  1500
$Comp
L Device:Ferrite_Bead FB1
U 1 1 5F669A8F
P 1900 1200
F 0 "FB1" V 1626 1200 50  0000 C CNN
F 1 "Ferrite_Bead" V 1717 1200 50  0000 C CNN
F 2 "Inductor_SMD:L_0603_1608Metric" V 1830 1200 50  0001 C CNN
F 3 "~" H 1900 1200 50  0001 C CNN
	1    1900 1200
	0    1    1    0   
$EndComp
$Comp
L Device:C C9
U 1 1 5F66C798
P 3100 1350
F 0 "C9" H 3215 1396 50  0000 L CNN
F 1 "100nF" H 3215 1305 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 3138 1200 50  0001 C CNN
F 3 "~" H 3100 1350 50  0001 C CNN
	1    3100 1350
	1    0    0    -1  
$EndComp
$Comp
L Device:C C6
U 1 1 5F66C79E
P 2650 1350
F 0 "C6" H 2765 1396 50  0000 L CNN
F 1 "10uF" H 2765 1305 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 2688 1200 50  0001 C CNN
F 3 "~" H 2650 1350 50  0001 C CNN
	1    2650 1350
	1    0    0    -1  
$EndComp
Connection ~ 2650 1200
Wire Wire Line
	2650 1200 2050 1200
Wire Wire Line
	3100 1500 2650 1500
$Comp
L power:GNDA #PWR05
U 1 1 5F6701D8
P 3100 1500
F 0 "#PWR05" H 3100 1250 50  0001 C CNN
F 1 "GNDA" H 3105 1327 50  0000 C CNN
F 2 "" H 3100 1500 50  0001 C CNN
F 3 "" H 3100 1500 50  0001 C CNN
	1    3100 1500
	1    0    0    -1  
$EndComp
Connection ~ 3100 1500
Connection ~ 2050 2250
$Comp
L power:GNDD #PWR03
U 1 1 5F67B5AA
P 1450 2650
F 0 "#PWR03" H 1450 2400 50  0001 C CNN
F 1 "GNDD" H 1454 2495 50  0000 C CNN
F 2 "" H 1450 2650 50  0001 C CNN
F 3 "" H 1450 2650 50  0001 C CNN
	1    1450 2650
	1    0    0    -1  
$EndComp
Text GLabel 9050 1500 2    50   Input ~ 0
CTRL
Text GLabel 9050 1300 2    50   Input ~ 0
SCLK
Text GLabel 9050 1400 2    50   Input ~ 0
SDATA
Text GLabel 9050 1200 2    50   Input ~ 0
FSYNC
$Comp
L Connector:Conn_01x01_Male J4
U 1 1 5F73220D
P 6100 6600
F 0 "J4" H 6072 6532 50  0000 R CNN
F 1 "Conn_01x01_Male" H 6072 6623 50  0000 R CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x01_P2.54mm_Vertical" H 6100 6600 50  0001 C CNN
F 3 "~" H 6100 6600 50  0001 C CNN
	1    6100 6600
	-1   0    0    1   
$EndComp
Connection ~ 3100 1200
$Comp
L Connector:Conn_01x02_Male J5
U 1 1 5F7500B1
P 3650 1300
F 0 "J5" H 3622 1182 50  0000 R CNN
F 1 "Conn_01x02_Male" H 3622 1273 50  0000 R CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical" H 3650 1300 50  0001 C CNN
F 3 "~" H 3650 1300 50  0001 C CNN
	1    3650 1300
	-1   0    0    1   
$EndComp
Wire Wire Line
	3450 1300 3450 1500
Wire Wire Line
	3450 1500 3100 1500
$Comp
L power:GNDA #PWR0101
U 1 1 5F758B99
P 6100 2350
F 0 "#PWR0101" H 6100 2100 50  0001 C CNN
F 1 "GNDA" H 6105 2177 50  0000 C CNN
F 2 "" H 6100 2350 50  0001 C CNN
F 3 "" H 6100 2350 50  0001 C CNN
	1    6100 2350
	1    0    0    -1  
$EndComp
$Comp
L power:GNDA #PWR0102
U 1 1 5F75A0CE
P 1150 3650
F 0 "#PWR0102" H 1150 3400 50  0001 C CNN
F 1 "GNDA" H 1155 3477 50  0000 C CNN
F 2 "" H 1150 3650 50  0001 C CNN
F 3 "" H 1150 3650 50  0001 C CNN
	1    1150 3650
	1    0    0    -1  
$EndComp
$Comp
L power:GNDD #PWR0103
U 1 1 5F75B75E
P 1550 3650
F 0 "#PWR0103" H 1550 3400 50  0001 C CNN
F 1 "GNDD" H 1554 3495 50  0000 C CNN
F 2 "" H 1550 3650 50  0001 C CNN
F 3 "" H 1550 3650 50  0001 C CNN
	1    1550 3650
	1    0    0    -1  
$EndComp
$Comp
L power:GNDA #PWR0104
U 1 1 5F75FEA1
P 5350 6350
F 0 "#PWR0104" H 5350 6100 50  0001 C CNN
F 1 "GNDA" H 5355 6177 50  0000 C CNN
F 2 "" H 5350 6350 50  0001 C CNN
F 3 "" H 5350 6350 50  0001 C CNN
	1    5350 6350
	1    0    0    -1  
$EndComp
$Comp
L power:GNDA #PWR0105
U 1 1 5F7614E4
P 6100 5750
F 0 "#PWR0105" H 6100 5500 50  0001 C CNN
F 1 "GNDA" H 6105 5577 50  0000 C CNN
F 2 "" H 6100 5750 50  0001 C CNN
F 3 "" H 6100 5750 50  0001 C CNN
	1    6100 5750
	1    0    0    -1  
$EndComp
$Comp
L power:GNDA #PWR0106
U 1 1 5F762BB7
P 7850 5750
F 0 "#PWR0106" H 7850 5500 50  0001 C CNN
F 1 "GNDA" H 7855 5577 50  0000 C CNN
F 2 "" H 7850 5750 50  0001 C CNN
F 3 "" H 7850 5750 50  0001 C CNN
	1    7850 5750
	1    0    0    -1  
$EndComp
Connection ~ 2050 1200
Wire Wire Line
	2050 1200 2050 2250
Connection ~ 1750 1200
Wire Wire Line
	1750 1200 1750 2450
$Comp
L power:+3.3V #PWR0107
U 1 1 5F778124
P 3100 900
F 0 "#PWR0107" H 3100 750 50  0001 C CNN
F 1 "+3.3V" H 3115 1073 50  0000 C CNN
F 2 "" H 3100 900 50  0001 C CNN
F 3 "" H 3100 900 50  0001 C CNN
	1    3100 900 
	1    0    0    -1  
$EndComp
$Comp
L Device:Net-Tie_2 NT1
U 1 1 5F780D55
P 1350 3650
F 0 "NT1" H 1350 3831 50  0000 C CNN
F 1 "Net-Tie_2" H 1350 3740 50  0000 C CNN
F 2 "NetTie:NetTie-2_SMD_Pad2.0mm" H 1350 3650 50  0001 C CNN
F 3 "~" H 1350 3650 50  0001 C CNN
	1    1350 3650
	1    0    0    -1  
$EndComp
Wire Wire Line
	1250 3650 1150 3650
Wire Wire Line
	1450 3650 1550 3650
Wire Wire Line
	5900 6600 5900 6350
Wire Wire Line
	5900 6350 6000 6350
Wire Wire Line
	5900 6350 5900 6050
Wire Wire Line
	5900 6050 5350 6050
Connection ~ 5900 6350
Connection ~ 5350 6050
Text GLabel 6000 6350 2    50   Input ~ 0
ELECTRODE
Text GLabel 1250 1200 1    50   Input ~ 0
DVDD
Text GLabel 5600 2250 2    50   Input ~ 0
SIGNAL
$Comp
L Device:R R4
U 1 1 5F65210F
P 8550 1650
F 0 "R4" H 8600 1700 50  0000 L CNN
F 1 "10k" H 8600 1600 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 8480 1650 50  0001 C CNN
F 3 "~" H 8550 1650 50  0001 C CNN
	1    8550 1650
	1    0    0    -1  
$EndComp
$Comp
L power:GNDD #PWR06
U 1 1 5F67DB29
P 8550 1800
F 0 "#PWR06" H 8550 1550 50  0001 C CNN
F 1 "GNDD" H 8554 1645 50  0000 C CNN
F 2 "" H 8550 1800 50  0001 C CNN
F 3 "" H 8550 1800 50  0001 C CNN
	1    8550 1800
	1    0    0    -1  
$EndComp
Connection ~ 7850 5750
Wire Wire Line
	3100 1200 2650 1200
Wire Wire Line
	3100 1200 3450 1200
$Comp
L OPA322:OPA322AIDBVR U3
U 1 1 5FB1959F
P 2300 5100
F 0 "U3" H 2750 5450 60  0000 L CNN
F 1 "OPA322AIDBVR" H 2500 5550 60  0000 L CNN
F 2 "OPA322:OPA322AIDBVR" H 3400 5340 60  0001 C CNN
F 3 "" H 2300 5100 60  0000 C CNN
	1    2300 5100
	1    0    0    -1  
$EndComp
$Comp
L power:+3.3V #PWR09
U 1 1 5FB1BD22
P 2300 4850
F 0 "#PWR09" H 2300 4700 50  0001 C CNN
F 1 "+3.3V" H 2300 5000 50  0000 C CNN
F 2 "" H 2300 4850 50  0001 C CNN
F 3 "" H 2300 4850 50  0001 C CNN
	1    2300 4850
	1    0    0    -1  
$EndComp
$Comp
L power:GNDA #PWR011
U 1 1 5FB517C0
P 2300 5350
F 0 "#PWR011" H 2300 5100 50  0001 C CNN
F 1 "GNDA" H 2300 5200 50  0000 C CNN
F 2 "" H 2300 5350 50  0001 C CNN
F 3 "" H 2300 5350 50  0001 C CNN
	1    2300 5350
	1    0    0    -1  
$EndComp
$Comp
L Device:R R8
U 1 1 5FB580F0
P 2050 6050
F 0 "R8" V 1843 6050 50  0000 C CNN
F 1 "22k" V 1934 6050 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 1980 6050 50  0001 C CNN
F 3 "~" H 2050 6050 50  0001 C CNN
	1    2050 6050
	0    1    1    0   
$EndComp
$Comp
L Device:R R7
U 1 1 5FB59078
P 1350 6050
F 0 "R7" V 1143 6050 50  0000 C CNN
F 1 "6k" V 1234 6050 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 1280 6050 50  0001 C CNN
F 3 "~" H 1350 6050 50  0001 C CNN
	1    1350 6050
	0    1    1    0   
$EndComp
$Comp
L power:GNDA #PWR08
U 1 1 5FB63E6B
P 1200 6250
F 0 "#PWR08" H 1200 6000 50  0001 C CNN
F 1 "GNDA" H 1200 6100 50  0000 C CNN
F 2 "" H 1200 6250 50  0001 C CNN
F 3 "" H 1200 6250 50  0001 C CNN
	1    1200 6250
	1    0    0    -1  
$EndComp
Wire Wire Line
	1200 6250 1200 6050
$Comp
L Device:R R6
U 1 1 5FB67C42
P 1200 5050
F 0 "R6" V 993 5050 50  0000 C CNN
F 1 "100" V 1084 5050 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 1130 5050 50  0001 C CNN
F 3 "~" H 1200 5050 50  0001 C CNN
	1    1200 5050
	0    1    1    0   
$EndComp
$Comp
L Device:C C11
U 1 1 5FB68504
P 1450 5200
F 0 "C11" H 1200 5150 50  0000 L CNN
F 1 "330p" H 1200 5050 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 1488 5050 50  0001 C CNN
F 3 "~" H 1450 5200 50  0001 C CNN
	1    1450 5200
	1    0    0    -1  
$EndComp
Wire Wire Line
	1350 5050 1450 5050
Connection ~ 1450 5050
$Comp
L power:GNDA #PWR07
U 1 1 5FB6AEA7
P 1450 5350
F 0 "#PWR07" H 1450 5100 50  0001 C CNN
F 1 "GNDA" H 1450 5200 50  0000 C CNN
F 2 "" H 1450 5350 50  0001 C CNN
F 3 "" H 1450 5350 50  0001 C CNN
	1    1450 5350
	1    0    0    -1  
$EndComp
$Comp
L Device:C C12
U 1 1 5FB6EEC6
P 4200 5000
F 0 "C12" V 3948 5000 50  0000 C CNN
F 1 "22n" V 4039 5000 50  0000 C CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 4238 4850 50  0001 C CNN
F 3 "~" H 4200 5000 50  0001 C CNN
	1    4200 5000
	0    1    1    0   
$EndComp
$Comp
L Device:R R9
U 1 1 5FB6F775
P 4450 5250
F 0 "R9" H 4520 5296 50  0000 L CNN
F 1 "1k" H 4520 5205 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 4380 5250 50  0001 C CNN
F 3 "~" H 4450 5250 50  0001 C CNN
	1    4450 5250
	1    0    0    -1  
$EndComp
$Comp
L power:GNDA #PWR012
U 1 1 5FB700B6
P 4450 5400
F 0 "#PWR012" H 4450 5150 50  0001 C CNN
F 1 "GNDA" H 4450 5250 50  0000 C CNN
F 2 "" H 4450 5400 50  0001 C CNN
F 3 "" H 4450 5400 50  0001 C CNN
	1    4450 5400
	1    0    0    -1  
$EndComp
$Comp
L power:GNDD #PWR013
U 1 1 5FB7EEAA
P 9100 3950
F 0 "#PWR013" H 9100 3700 50  0001 C CNN
F 1 "GNDD" H 9104 3795 50  0000 C CNN
F 2 "" H 9100 3950 50  0001 C CNN
F 3 "" H 9100 3950 50  0001 C CNN
	1    9100 3950
	1    0    0    -1  
$EndComp
Text GLabel 9100 3150 1    50   Input ~ 0
DVDD
Text GLabel 9600 3600 2    50   Input ~ 0
MCLK
Text Notes 8050 4350 0    50   ~ 0
50 MHz clock generator. When the pin INH is low the circuit is stopped.
$Comp
L 0530480710:0530480710 J2
U 1 1 5FB94B00
P 8150 1600
F 0 "J2" H 8778 1346 50  0000 L CNN
F 1 "0530480710" H 8778 1255 50  0000 L CNN
F 2 "0530480710:0530480710" H 8800 1700 50  0001 L CNN
F 3 "https://www.molex.com/pdm_docs/sd/530480710_sd.pdf" H 8800 1600 50  0001 L CNN
F 4 "Conn Shrouded Header (4 Sides) HDR 7 POS 1.25mm Solder RA Thru-Hole PicoBlade Tray" H 8800 1500 50  0001 L CNN "Description"
F 5 "3.7" H 8800 1400 50  0001 L CNN "Height"
F 6 "Molex" H 8800 1300 50  0001 L CNN "Manufacturer_Name"
F 7 "0530480710" H 8800 1200 50  0001 L CNN "Manufacturer_Part_Number"
F 8 "" H 8800 1100 50  0001 L CNN "Arrow Part Number"
F 9 "" H 8800 1000 50  0001 L CNN "Arrow Price/Stock"
F 10 "" H 8800 900 50  0001 L CNN "Mouser Part Number"
F 11 "" H 8800 800 50  0001 L CNN "Mouser Price/Stock"
	1    8150 1600
	-1   0    0    1   
$EndComp
Wire Wire Line
	8150 1750 8150 1600
$Comp
L power:+3.3V #PWR014
U 1 1 5FBA73A7
P 8150 900
F 0 "#PWR014" H 8150 750 50  0001 C CNN
F 1 "+3.3V" H 8165 1073 50  0000 C CNN
F 2 "" H 8150 900 50  0001 C CNN
F 3 "" H 8150 900 50  0001 C CNN
	1    8150 900 
	1    0    0    -1  
$EndComp
$Comp
L power:PWR_FLAG #FLG01
U 1 1 5FBA73AE
P 8150 900
F 0 "#FLG01" H 8150 975 50  0001 C CNN
F 1 "PWR_FLAG" V 8150 1028 50  0000 L CNN
F 2 "" H 8150 900 50  0001 C CNN
F 3 "~" H 8150 900 50  0001 C CNN
	1    8150 900 
	0    1    1    0   
$EndComp
Wire Wire Line
	3100 900  3100 1200
Text GLabel 8500 5450 2    50   Input ~ 0
VOUT
Text GLabel 9050 1100 2    50   Input ~ 0
VOUT
Wire Wire Line
	8150 1100 9050 1100
Wire Wire Line
	8150 1200 9050 1200
Wire Wire Line
	9050 1300 8150 1300
Wire Wire Line
	8150 1400 9050 1400
$Comp
L power:GNDA #PWR0108
U 1 1 5FBBCFA9
P 8150 1750
F 0 "#PWR0108" H 8150 1500 50  0001 C CNN
F 1 "GNDA" H 8155 1577 50  0000 C CNN
F 2 "" H 8150 1750 50  0001 C CNN
F 3 "" H 8150 1750 50  0001 C CNN
	1    8150 1750
	1    0    0    -1  
$EndComp
Text Notes 8600 2150 0    50   ~ 0
Molex connector to the other board\n
Wire Wire Line
	1500 6050 1700 6050
Connection ~ 1700 6050
Wire Wire Line
	1700 6050 1900 6050
Wire Wire Line
	2200 6050 3900 6050
Wire Wire Line
	4050 5000 3900 5000
Wire Wire Line
	4350 5000 4450 5000
Wire Wire Line
	4450 5100 4450 5000
Connection ~ 4450 5000
Wire Wire Line
	4450 5000 5350 5000
Wire Wire Line
	5350 5000 5350 5150
Text GLabel 850  5050 0    50   Input ~ 0
SIGNAL
Wire Wire Line
	1450 5050 2050 5050
Wire Wire Line
	3900 6050 3900 5100
$Comp
L KC2016Z:KC2016Z U4
U 1 1 5FBF4D2C
P 9100 3600
F 0 "U4" H 9400 3900 50  0000 L CNN
F 1 "KC2016Z" H 9350 3800 50  0000 L CNN
F 2 "KC2016Z:KC2016Z" H 9130 3996 50  0001 C CNN
F 3 "" H 9130 3996 50  0001 C CNN
	1    9100 3600
	1    0    0    -1  
$EndComp
Wire Wire Line
	9400 3600 9600 3600
Wire Wire Line
	2050 5150 1700 5150
Wire Wire Line
	1700 5150 1700 6050
Wire Wire Line
	2650 5100 3900 5100
Connection ~ 3900 5100
Wire Wire Line
	3900 5100 3900 5000
$Comp
L Device:C C8
U 1 1 5FC1630F
P 8500 3400
F 0 "C8" H 8615 3446 50  0000 L CNN
F 1 "100nF" H 8615 3355 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 8538 3250 50  0001 C CNN
F 3 "~" H 8500 3400 50  0001 C CNN
	1    8500 3400
	-1   0    0    1   
$EndComp
$Comp
L power:GNDD #PWR0109
U 1 1 5FC19BEB
P 8500 3550
F 0 "#PWR0109" H 8500 3300 50  0001 C CNN
F 1 "GNDD" H 8504 3395 50  0000 C CNN
F 2 "" H 8500 3550 50  0001 C CNN
F 3 "" H 8500 3550 50  0001 C CNN
	1    8500 3550
	1    0    0    -1  
$EndComp
Wire Wire Line
	9100 3150 9100 3250
Wire Wire Line
	8500 3300 8500 3250
Wire Wire Line
	8500 3250 9100 3250
Connection ~ 8500 3250
Connection ~ 9100 3250
Wire Wire Line
	7850 5450 8500 5450
$Comp
L Connector:Conn_01x01_Male J1
U 1 1 5FC4936B
P 5350 4800
F 0 "J1" V 5412 4844 50  0000 L CNN
F 1 "Conn_01x01_Male" V 5250 4500 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x01_P2.54mm_Vertical" H 5350 4800 50  0001 C CNN
F 3 "~" H 5350 4800 50  0001 C CNN
	1    5350 4800
	0    1    1    0   
$EndComp
Connection ~ 5350 5000
Wire Wire Line
	8150 1500 8550 1500
Connection ~ 8550 1500
Wire Wire Line
	8550 1500 9050 1500
Wire Wire Line
	8150 900  8150 1000
Connection ~ 8150 900 
Wire Wire Line
	1050 5050 850  5050
Wire Notes Line
	1000 5600 1000 4650
Wire Notes Line
	1000 4650 1600 4650
Wire Notes Line
	1600 4650 1600 5600
Wire Notes Line
	1600 5600 1000 5600
Wire Notes Line
	4050 4600 4050 5700
Wire Notes Line
	4050 5700 4700 5700
Wire Notes Line
	4700 5700 4700 4600
Wire Notes Line
	4700 4600 4050 4600
Text Notes 4050 4550 0    50   ~ 0
High Pass Filter\n
Text Notes 1050 4600 0    50   ~ 0
Low Pass Filter\n
$EndSCHEMATC
