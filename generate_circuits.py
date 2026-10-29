import schemdraw
import schemdraw.elements as elm

def generate_m1_schematic():
    d = schemdraw.Drawing(backend='matplotlib')
    d.config(fontsize=10.5, font='sans-serif')

    # Top Section Headers
    d += elm.Label().label('ESP32 TRANSMITTER', color='#1a73e8', fontsize=12).at((2.0, 5.8))
    d += elm.Label().label('M1: TUNED LC TANK', color='#1a73e8', fontsize=12).at((10.5, 5.8))
    d += elm.Label().label('M1: ENVELOPE DETECTOR', color='#1a73e8', fontsize=12).at((20.5, 5.8))

    # --- 1. Transmitter ---
    source = elm.SourceSin().up().length(2.8).at((1.2, 1.6))
    d += source
    d += elm.Label().label('ESP32 DAC1\n(GPIO 25)\n700 kHz AM', color='#1f2937', fontsize=9.5).at((-0.1, 3.0))
    d += elm.Ground().at((1.2, 1.6))
    d += elm.Label().label('GND 1\n(Transmitter)', color='#4b5563', fontsize=9).at((1.2, 0.8))

    # Primary 5t loop
    d += elm.Line().right().length(2.0).at(source.end)
    l_prim = elm.Inductor().down().length(2.8).at((3.2, 4.4))
    d += l_prim
    d += elm.Label().label('L1: 5 turns\n(Driver Loop)', color='#1f2937', fontsize=9.5).at((4.2, 3.0))
    d += elm.Line().left().length(2.0).at(l_prim.end)

    # --- 2. Magnetic Coupling (Air Gap) ---
    d += elm.Label().label('Air Gap (2-5 cm)\nMagnetic Coupling (M)', color='#d97706', fontsize=9.5).at((6.3, 3.6))
    d += elm.Line().right().length(1.2).linestyle('--').color('#d97706').at((5.1, 3.0))
    d += elm.Arrow().right().length(1.2).color('#d97706').at((6.4, 3.0))

    # --- 3. Receiver Tuned Tank ---
    # Secondary 75t coil
    l_sec = elm.Inductor().down().length(2.8).at((8.5, 4.4))
    d += l_sec
    d += elm.Label().label('L2: 75 turns\n(50mm PVC)\nL ≈ 292 µH', color='#1f2937', fontsize=9.5).at((9.7, 3.0))
    d += elm.Dot().at((8.5, 4.4))
    d += elm.Dot().at((8.5, 1.6))

    # Tank top rail
    d += elm.Line().right().length(3.8).at((8.5, 4.4))
    d += elm.Dot().at((12.3, 4.4))

    # Variable tuning capacitor
    c_var = elm.CapacitorVar().down().length(2.8).at((12.3, 4.4))
    d += c_var
    d += elm.Label().label('C_tune\n20–280 pF', color='#1f2937', fontsize=9.5).at((13.4, 3.0))
    d += elm.Dot().at((12.3, 1.6))

    # Tank bottom rail
    d += elm.Line().right().length(3.8).at((8.5, 1.6))
    
    # Ground 2 (Isolated)
    d += elm.Ground().at((10.4, 1.6))
    d += elm.Label().label('GND 2 (Receiver)\n[ISOLATED FROM GND 1!]', color='#16a34a', fontsize=9).at((10.4, 0.8))

    # --- 4. Test Point 1 (TP1) & Diode ---
    d += elm.Line().right().length(2.2).at((12.3, 4.4))
    tp1 = elm.Dot().at((14.5, 4.4))
    d += tp1
    d += elm.Label().label('TP1', color='#dc2626', fontsize=11).at((14.5, 5.0))
    d += elm.Label().label('(RF Peak)', color='#dc2626', fontsize=8.5).at((14.5, 4.7))

    # Diode 1N60P
    d += elm.Line().right().length(0.8).at((14.5, 4.4))
    diode = elm.Diode().right().length(2.0).at((15.3, 4.4))
    d += diode
    d += elm.Label().label('1N60P', color='#1f2937', fontsize=10).at((16.3, 5.0))
    d += elm.Label().label('(Germanium)', color='#4b5563', fontsize=8.5).at((16.3, 4.7))
    d += elm.Line().right().length(0.8).at(diode.end)

    # Test Point 3 (TP3)
    tp3 = elm.Dot().at((18.1, 4.4))
    d += tp3
    d += elm.Label().label('TP3', color='#dc2626', fontsize=11).at((18.1, 5.0))
    d += elm.Label().label('(Audio Out)', color='#dc2626', fontsize=8.5).at((18.1, 4.7))

    # --- 5. Detector Load: R = 15k and C = 3.3nF ---
    # 15 kOhm Resistor
    d += elm.Line().right().length(2.2).at((18.1, 4.4))
    d += elm.Dot().at((20.3, 4.4))
    r_load = elm.Resistor().down().length(2.8).at((20.3, 4.4))
    d += r_load
    d += elm.Label().label('R = 15 kΩ', color='#1f2937', fontsize=9.5).at((21.4, 3.0))
    d += elm.Dot().at((20.3, 1.6))

    # 3.3 nF Capacitor
    d += elm.Line().right().length(2.8).at((20.3, 4.4))
    d += elm.Dot().at((23.1, 4.4))
    c_load = elm.Capacitor().down().length(2.8).at((23.1, 4.4))
    d += c_load
    d += elm.Label().label('C = 3.3 nF\n(RC ≈ 50 µs)', color='#1f2937', fontsize=9.5).at((24.4, 3.0))
    d += elm.Dot().at((23.1, 1.6))

    # Bottom rail to GND 2
    d += elm.Line().right().length(10.8).at((12.3, 1.6))

    # --- 6. Audio Stage Interface ---
    d += elm.Line().right().length(2.2).at((23.1, 4.4))
    d += elm.Dot().at((25.3, 4.4))
    d += elm.Label().label('Audio Out\n(to IC Amp + Speaker)', color='#7c3aed', fontsize=9.5).at((27.1, 4.4))

    d += elm.Line().right().length(2.2).at((23.1, 1.6))
    d += elm.Dot().at((25.3, 1.6))
    d += elm.Label().label('GND 2 Reference', color='#16a34a', fontsize=9.5).at((26.7, 1.6))

    d.save('m1_circuit_diagram.png', dpi=300)
    d.save('m1_circuit_diagram.svg')
    print("m1_circuit_diagram generated successfully.")

def generate_ground_loop_diagram():
    d = schemdraw.Drawing(backend='matplotlib')
    d.config(fontsize=10.5, font='sans-serif')

    d += elm.Label().label('THE DAY 1 MISTAKE: ACCIDENTAL COMMON GROUND LOOP', color='#dc2626', fontsize=12.5).at((8.5, 5.8))

    # Transmitter
    source = elm.SourceSin().up().length(2.5).at((1.2, 1.6))
    d += source
    d += elm.Label().label('ESP32 DAC', color='#1f2937', fontsize=9.5).at((-0.1, 2.85))
    d += elm.Ground().at((1.2, 1.6))
    d += elm.Label().label('GND 1', color='#4b5563', fontsize=9).at((1.2, 0.9))

    # Primary
    d += elm.Line().right().length(2.0).at(source.end)
    l_prim = elm.Inductor().down().length(2.5).at((3.2, 4.1))
    d += l_prim
    d += elm.Label().label('5t loop', color='#1f2937', fontsize=9.5).at((4.0, 2.85))
    d += elm.Line().left().length(2.0).at(l_prim.end)

    # Receiver Tank
    l_sec = elm.Inductor().down().length(2.5).at((7.5, 4.1))
    d += l_sec
    d += elm.Label().label('75t coil', color='#1f2937', fontsize=9.5).at((6.4, 2.85))
    d += elm.Dot().at((7.5, 4.1))
    d += elm.Dot().at((7.5, 1.6))

    d += elm.Line().right().length(2.8).at((7.5, 4.1))
    c_var = elm.CapacitorVar().down().length(2.5).at((10.3, 4.1))
    d += c_var
    d += elm.Label().label('VarCap', color='#1f2937', fontsize=9.5).at((11.3, 2.85))
    d += elm.Dot().at((10.3, 4.1))
    d += elm.Dot().at((10.3, 1.6))

    d += elm.Line().right().length(2.8).at((7.5, 1.6))

    # Diode + Load
    d += elm.Line().right().length(1.8).at((10.3, 4.1))
    diode = elm.Diode().right().length(2.0).at((12.1, 4.1))
    d += diode
    d += elm.Label().label('1N60P', color='#1f2937', fontsize=10).at((13.1, 4.8))
    d += elm.Dot().at(diode.end)
    d += elm.Line().right().length(1.0).at(diode.end)
    
    r_load = elm.Resistor().down().length(2.5).at((15.1, 4.1))
    d += r_load
    d += elm.Label().label('15 kΩ || 3.3 nF\nDetector Load', color='#1f2937', fontsize=9.5).at((16.6, 2.85))
    d += elm.Dot().at(r_load.end)
    d += elm.Line().left().length(4.8).at(r_load.end)

    # Fatal Common Ground Connection
    d += elm.Line().right().length(13.9).at((1.2, 1.6)).color('#dc2626').linestyle('--').linewidth(2.8)
    d += elm.Label().label('ACCIDENTAL COMMON GROUND CONNECTION (THE MISTAKE)\nShorts the floating induced EMF straight back to source ground!\nResult: Signal across tank and detector collapses to ZERO.', 
                           color='#dc2626', fontsize=10.5).at((8.0, 0.4))

    d.save('ground_loop_fault.png', dpi=300)
    d.save('ground_loop_fault.svg')
    print("ground_loop_fault generated successfully.")

generate_m1_schematic()
generate_ground_loop_diagram()
