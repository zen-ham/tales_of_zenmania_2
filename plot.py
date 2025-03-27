from colorama import Fore

# scraped story line lol

# game = [
#     # Introduction Sequence
#     (0, f"Welcome, The year is 2084.", Fore.CYAN, (), ()),
#     (0, "In the megacity of Zenmania, code is controlled. Algorithms dictate life.", Fore.RED, (), ()),
#     (0, "\nYou're a freelance hacktivist, known in underground networks as 'The Compiler'.", Fore.GREEN, (), ()),
#     (0, "Your reputation for bypassing corporate firewalls precedes you.", Fore.YELLOW, (), ()),
#
#     # Initial Choice: Resistance Network Entry Point
#     (0, "\nA encrypted message flashes on your vintage terminal:", Fore.WHITE, (), ()),
#     (0, "'Urgent mission. Potential system breach. Are you in?'", Fore.CYAN, ('y', 'n'), (10, 5)),
#
#     # Negative Response (Path 1: Hesitation)
#     (5, "You hesitate. The resistance doesn't forgive weakness.", Fore.RED, (), ()),
#     (5, "Your network credentials are revoked. Game over.", Fore.RED, (), ()),
#
#     # Positive Response - First Major Mission (Path 2: Rainforest Relic)
#     (10, "Coordinates received: An abandoned research facility deep in the Amazon Techno-Preserve.", Fore.GREEN, (), ()),
#     (10, "Mist clings to advanced ruins, where nature and technology have become intertwined.", Fore.CYAN, (), ()),
#     (10, "Your mission: Retrieve experimental quantum decryption algorithms.", Fore.YELLOW, (), ()),
#     (10, "\nChoose your approach:", Fore.WHITE, ('s', 'h'), (11, 12)),
#
#     # Stealth Approach in Rainforest Relic
#     (11, "You move silently through the overgrown facility, bio-luminescent fungi lighting your path.", Fore.GREEN, (), ()),
#     (11, "Encrypted terminals flicker with forgotten data.", Fore.CYAN, (), ()),
#     (11, "\nYou need to choose a decryption method:", Fore.WHITE, ('b', 'r'), (13, 14)),
#
#     # Hacking Approach in Rainforest Relic
#     (12, "You trigger an alarm. Automated defense drones activate!", Fore.RED, (), ()),
#     (12, "Your hacktivist skills are put to the ultimate test.", Fore.YELLOW, ('c', 'd'), (15, 16)),
#
#     # Stealth Decryption Paths
#     (13, "Using Hashcat, you crack the quantum encryption in record time.", Fore.GREEN, (), ()),
#     (13, "The algorithms download. Success!", Fore.CYAN, (), ()),
#
#     # Factory Infiltration Mission (Path 3: Industrial Espionage)
#     (13, "New mission: Infiltrate the MegaCorp Automated Production Complex.", Fore.YELLOW, (), ()),
#     (13, "Steam pipes and robotic assembly lines create a labyrinth of industrial chaos.", Fore.CYAN, (), ()),
#     (13, "\nChoose your entry point:", Fore.WHITE, ('v', 'c'), (21, 22)),
#
#     (14, "John the Ripper struggles with the complex quantum hash.", Fore.RED, (), ()),
#     (14, "Time runs out. Mission failed.", Fore.RED, (), ()),
#
#     # Hacking Defense Scenarios
#     (15, "Your custom neural firewall overwhelms the drone network.", Fore.GREEN, (), ()),
#     (15, "Victory achieved through pure computational prowess.", Fore.CYAN, (), ()),
#
#     (16, "The drones adapt faster than your defenses.", Fore.RED, (), ()),
#     (16, "You're trapped. Mission compromised.", Fore.RED, (), ()),
#
#     # Ventilation System Infiltration
#     (21, "You crawl through narrow ventilation ducts, heat and condensation everywhere.", Fore.GREEN, (), ()),
#     (21, "Security protocols scan for intrusion.", Fore.RED, ('h', 'b'), (23, 24)),
#
#     # Cargo Infiltration
#     (22, "Disguised as a maintenance drone, you enter the complex.", Fore.CYAN, (), ()),
#     (22, "One wrong move could trigger total system lockdown.", Fore.YELLOW, ('s', 'a'), (25, 26)),
#
#     # Ventilation Hacking Attempts
#     (23, "Your custom Python exploit bypasses initial security!", Fore.GREEN, (), ()),
#     (23, "You're through the first layer of defenses.", Fore.CYAN, (), ()),
#
#     (24, "The system's AI detection is too advanced.", Fore.RED, (), ()),
#     (24, "Alarm triggered. Extraction impossible.", Fore.RED, (), ()),
#
#     # Cargo Infiltration Scenarios
#     (25, "Stealth pays off. You reach the central data core.", Fore.GREEN, (), ()),
#     (25, "Crucial corporate secrets are now yours.", Fore.CYAN, (), ()),
#
#     # Cybernetic Assassination Mission (Path 4)
#     (25, "Your target: A high-ranking corporate executive with forbidden open-source sympathies.", Fore.RED, (), ()),
#     (25, "Location: Annual Technocratic Gala, a heavily secured virtual-physical hybrid event.", Fore.CYAN, (), ()),
#     (25, "\nChoose your infiltration method:", Fore.WHITE, ('v', 'n'), (31, 32)),
#
#     (26, "Aggressive approach triggers total lockdown.", Fore.RED, (), ()),
#     (26, "You're trapped. Mission failed.", Fore.RED, (), ()),
#
#
#     # Virtual Network Infiltration
#     (31, "You begin hacking the event's neural network, creating a digital ghost identity.", Fore.GREEN, (), ()),
#     (31, "Biometric firewalls require precise social engineering.", Fore.CYAN, ('s', 'f'), (33, 34)),
#
#     # Neural Implant Approach
#     (32, "You've acquired a rare neural override chip on the black market.", Fore.YELLOW, (), ()),
#     (32, "Risky, but potentially undetectable.", Fore.RED, ('i', 'c'), (35, 36)),
#
#     # Virtual Infiltration Scenarios
#     (33, "Subtle social engineering bypasses initial security checks.", Fore.GREEN, (), ()),
#     (33, "You're now a ghost in the system.", Fore.CYAN, (), ()),
#
#     (34, "Your fake credentials are flagged. Immediate lockdown!", Fore.RED, (), ()),
#     (34, "Mission compromised.", Fore.RED, (), ()),
#
#     # Neural Implant Scenarios
#     (35, "The neural override works perfectly. Target is now vulnerable.", Fore.GREEN, (), ()),
#     (35, "Complete mission success.", Fore.CYAN, (), ()),
#
#     (36, "Neural countermeasures detect the intrusion.", Fore.RED, (), ()),
#     (36, "Your consciousness is trapped in digital limbo.", Fore.RED, (), ()),
#
#     # Deep Web Information Retrieval (Path 5)
#     (40, "A cryptic message from the resistance: 'Find the Forgotten Archive'.", Fore.CYAN, (), ()),
#     (40, "The deepest layers of the dark web hold a treasure trove of suppressed knowledge.", Fore.GREEN, (), ()),
#     (40, "\nChoose your entry point:", Fore.WHITE, ('t', 'o'), (41, 42)),
#
#     # Tor Network Approach
#     (41, "You route through multiple anonymous Tor nodes.", Fore.CYAN, (), ()),
#     (41, "Each connection is a potential trap.", Fore.RED, ('e', 'd'), (43, 44)),
#
#     # Onion Routing Alternative
#     (42, "Custom-built quantum encryption creates an unbreakable path.", Fore.GREEN, (), ()),
#     (42, "But detection risks are high.", Fore.YELLOW, ('s', 'a'), (45, 46)),
#
#     # Tor Network Scenarios
#     (43, "Advanced encryption reveals hidden data repositories.", Fore.GREEN, (), ()),
#     (43, "The Forgotten Archive begins to unravel.", Fore.CYAN, (), ()),
#
#     (44, "A honeypot trap! Your location is compromised.", Fore.RED, (), ()),
#     (44, "Resistance connection terminated.", Fore.RED, (), ()),
#
#     # Onion Routing Scenarios
#     (45, "Stealth pays off. Critical data downloaded.", Fore.GREEN, (), ()),
#     (45, "The resistance will be pleased.", Fore.CYAN, (), ()),
#
#     # Corporate Server Room Infiltration (Path 6)
#     (45, "Target: ZenCorp's most secure data center.", Fore.RED, (), ()),
#     (45, "Physical security matches its digital defenses.", Fore.CYAN, (), ()),
#     (45, "\nChoose your infiltration strategy:", Fore.WHITE, ('d', 'c'), (51, 52)),
#
#     (46, "Aggressive routing triggers network-wide lockdown.", Fore.RED, (), ()),
#     (46, "Your digital fingerprint is now everywhere.", Fore.RED, (), ()),
#
#     # Direct Infiltration
#     (51, "You've obtained a stolen employee keycard.", Fore.GREEN, (), ()),
#     (51, "One wrong move could trigger total lockdown.", Fore.YELLOW, ('s', 'q'), (53, 54)),
#
#     # Cyber-Physical Hack
#     (52, "Remotely manipulating building security systems.", Fore.CYAN, (), ()),
#     (52, "A delicate dance of digital and physical intrusion.", Fore.GREEN, ('h', 'b'), (55, 56)),
#
#     # Direct Infiltration Scenarios
#     (53, "Silent movement through restricted zones.", Fore.GREEN, (), ()),
#     (53, "Server room access imminent.", Fore.CYAN, (), ()),
#
#     (54, "Security AI detects micro-movements.", Fore.RED, (), ()),
#     (54, "Instant containment protocol activated.", Fore.RED, (), ()),
#
#     # Cyber-Physical Hack Scenarios
#     (55, "Hack succeeds. Critical data extracted.", Fore.GREEN, (), ()),
#     (55, "Another blow against corporate control.", Fore.CYAN, (), ()),
#
#     # Quantum Encryption Breaking Challenge (Path 7)
#     (55, "The ultimate hacktivist challenge: Break the ZenCorp Quantum Encryption.", Fore.CYAN, (), ()),
#     (55, "No one has ever successfully cracked this system.", Fore.RED, (), ()),
#     (55, "\nChoose your approach:", Fore.WHITE, ('q', 'b'), (61, 62)),
#
#     (56, "Backup systems overwhelm your intrusion.", Fore.RED, (), ()),
#     (56, "Mission failed, escape impossible.", Fore.RED, (), ()),
#
#     # Quantum Computing Approach
#     (61, "You've acquired a rare quantum processing unit.", Fore.GREEN, (), ()),
#     (61, "Experimental technology against an unbreakable system.", Fore.CYAN, ('o', 'r'), (63, 64)),
#
#     # Brute Force Alternative
#     (62, "Traditional computing meets pure computational power.", Fore.YELLOW, (), ()),
#     (62, "Millions of simultaneous attack vectors.", Fore.RED, ('m', 'p'), (65, 66)),
#
#     # Quantum Computing Scenarios
#     (63, "Quantum entanglement breaks the first encryption layer!", Fore.GREEN, (), ()),
#     (63, "Unprecedented breakthrough.", Fore.CYAN, (), ()),
#
#     (64, "Quantum instability causes system crash.", Fore.RED, (), ()),
#     (64, "Your expensive equipment is fried.", Fore.RED, (), ()),
#
#     # Brute Force Scenarios
#     (65, "Massive computational cluster overwhelms defenses.", Fore.GREEN, (), ()),
#     (65, "Encryption cracked after days of computation.", Fore.CYAN, (), ()),
#
#     (66, "Predictive AI anticipates and blocks your attack.", Fore.RED, (), ()),
#     (66, "Total computational defeat.", Fore.RED, (), ()),
# ]

title = r'''
########   ###    ####     #######   #####
## ## ##  ## ##    ##       ##   #  ##   ##
   ##    ##   ##   ##       ##      ##
   ##    ##   ##   ##       ####     #####
   ##    #######   ##       ##           ##
   ##    ##   ##   ##  ##   ##   #  ##   ##
  ####   ##   ##  #######  #######   #####


    ><<<<     ><<<<<<<<
  ><<    ><<  ><<
><<        ><<><<
><<        ><<><<<<<<
><<        ><<><<
  ><<     ><< ><<
    ><<<<     ><<



         ,----,                     ,--.           ____                            ,--.
       .'   .'|     ,---,.        ,--.'|         ,'  , '.    ,---,               ,--.'|    ,---,    ,---,
    .'   .'   ;   ,'  .' |    ,--,:  : |      ,-+-,.' _ |   '  .' \          ,--,:  : | ,'--.' |   '  .' \
  ,---, '    .' ,---.'   | ,'--.''|  ' :   ,-+-. ;   , ||  /  ;    '.     ,'--.''|  ' : |   :  :  /  ;    '.
  |   :     ./  |   |   .' |   :  :  | |  ,--.'|'   |  ;| :  :       \    |   :  :  | | :   |  ' :  :       \
  ;   | .'  /   :   :  |-, :   |   \ | : |   |  ,', |  ': :  |   /\   \   :   |   \ | : |   :  | :  |   /\   \
  '---' /  ;    :   |  ;/| |   : '  '; | |   | /  | |  || |  :  ' ;.   :  |   : '  '; | '   '  ; |  :  ' ;.   :
    /  ;  /     |   :   .' '   ' ;.    ; '   | :  | :  |, |  |  ;/  \   \ '   ' ;.    ; |   |  | |  |  ;/  \   \
   ;  /  /--,   |   |  |-, |   | | \   | ;   . |  ; |--'  '  :  | \  \ ,' |   | | \   | '   :  ; '  :  | \  \ ,'
  /  /  / .'|   '   :  ;/| '   : |  ; .' |   : |  | ,     |  |  '  '--'   '   : |  ; .' |   |  ' |  |  '  '--'
./__;       :   |   |    \ |   | ''--'   |   : '  |/      |  :  :         |   | ''--'   '   :  | |  :  :
|   :     .'    |   :   .' '   : |       ;   | |'-'       |  | ,'         '   : |       ;   |.'  |  | ,'
;   |  .'       |   | ,'   ;   |.'       |   ;/           '--''           ;   |.'       '---'    '--''
'---'           '----'     '---'         '---'                            '---'


    __o
  o/  v\
 /|    <\
 //    o/
      /v
     />
   o/
  /v
 /> __o__/_
'''

game = [
    # Introduction and Setting
    (0, f"Welcome, the year is 2084.", Fore.CYAN, (), ()),
    (0, "In the megacity of Zenmania, code is controlled. Algorithms dictate life.", Fore.RED, (), ()),
    (0, "\nYou're a rogue cybersecurity specialist, wanted by the corporate regime.", Fore.GREEN, (), ()),
    (0, "Your mission: Infiltrate Arasaka Corporation's most secure digital fortress.", Fore.YELLOW, (), ()),
    
    # Initial Choice: Approach to Infiltration
    (0, "\nChoose your initial approach:", Fore.WHITE, (), ()),
    (0, "Do you want to (N)etwork with underground hackers or (S)olo infiltrate?", Fore.YELLOW, ('n', 's'), (10, 20)),
    
    # Hacker Network Path (Sequence 10-19)
    (10, "You enter a dimly lit underground coding den. Rebel programmers surround you.", Fore.GREEN, (), ()),
    (10, "A veteran hacker approaches. 'We've been expecting you.'", Fore.CYAN, (), ()),
    (10, "Choose your collaborative strategy:", Fore.WHITE, (), ()),
    (10, "Will you focus on (D)istributed cracking or (I)ntelligence gathering?", Fore.YELLOW, ('d', 'i'), (30, 40)),
    
    # Solo Infiltration Path (Sequence 20-29)
    (20, "You decide to go lone wolf. Risky, but potentially more stealthy.", Fore.RED, (), ()),
    (20, "Your custom-built Linux rig hums with potential.", Fore.GREEN, (), ()),
    (20, "Choose your initial breach method:", Fore.WHITE, (), ()),
    (20, "Attempt (S)QL injection or (P)hishing reconnaissance?", Fore.YELLOW, ('s', 'p'), (50, 60)),
    
    # Distributed Cracking Route (Sequence 30-39)
    (30, "The hacker collective sets up a massive distributed computing network.", Fore.CYAN, (), ()),
    (30, "You'll need to choose your password cracking approach carefully.", Fore.WHITE, (), ()),
    (30, "Do you use (H)ashcat for GPU-accelerated cracking or (J)ohn the Ripper?", Fore.YELLOW, ('h', 'j'), (70, 80)),
    
    # Intelligence Gathering Route (Sequence 40-49)
    (40, "You dive deep into Arasaka's digital footprint.", Fore.GREEN, (), ()),
    (40, "Social engineering or deep web reconnaissance?", Fore.WHITE, (), ()),
    (40, "Choose between (O)SIRT tracking or (S)ocial media analysis", Fore.YELLOW, ('o', 's'), (90, 100)),
    
    # SQL Injection Path (Sequence 50-59)
    (50, "Your SQL injection script finds a vulnerability in Arasaka's outer firewall.", Fore.CYAN, (), ()),
    (50, "But the system is complex. One wrong move could trigger alarms.", Fore.RED, (), ()),
    (50, "Proceed with (B)lind injection or (P)recise targeted attack?", Fore.YELLOW, ('b', 'p'), (110, 120)),
    
    # Phishing Reconnaissance (Sequence 60-69)
    (60, "You craft a sophisticated phishing email targeting Arasaka's internal network.", Fore.GREEN, (), ()),
    (60, "The success depends on your social engineering skills.", Fore.WHITE, (), ()),
    (60, "Do you impersonate (I)T support or a (H)igh-level executive?", Fore.YELLOW, ('i', 'h'), (130, 140)),
    
    # Hashcat Cracking Path (Success Route) (Sequence 70-79)
    (70, "Hashcat's GPU-accelerated cracking tears through password hashes.", Fore.CYAN, (), ()),
    (70, "Millions of hashes processed per second. The corporate encryption crumbles.", Fore.GREEN, (), ()),
    (70, "You've breached the first layer of Arasaka's security!", Fore.CYAN, (), ()),
    (70, "Proceed to (D)eep system infiltration or (E)xfiltrate initial data?", Fore.YELLOW, ('d', 'e'), (150, 160)),
    
    # John the Ripper Path (Failure Route) (Sequence 80-89)
    (80, "John the Ripper struggles. CPU-based cracking is painfully slow.", Fore.RED, (), ()),
    (80, "Arasaka's security algorithms detect and begin tracking your attempt.", Fore.WHITE, (), ()),
    (80, "Your connection is compromised. Mission failed.", Fore.RED, (), (), (1, 'Bad Ending 1')),  # Bad Ending
    
    # OSIRT Tracking (Sequence 90-99)
    (90, "You leverage OSIRT (Open-Source Intelligence Reconnaissance) techniques.", Fore.GREEN, (), ()),
    (90, "Mapping Arasaka's digital infrastructure reveals potential entry points.", Fore.CYAN, (), ()),
    (90, "Choose your next move: (C)orrelate data or (E)xploit discovered weakness?", Fore.YELLOW, ('c', 'e'), (170, 180)),
    
    # Social Media Analysis (Sequence 100-109)
    (100, "Social media reveals unexpected vulnerabilities in Arasaka's employee network.", Fore.GREEN, (), ()),
    (100, "Potential insider information could be your key.", Fore.WHITE, (), ()),
    (100, "Attempt (D)irect contact or (A)nalyze communication patterns?", Fore.YELLOW, ('d', 'a'), (190, 200)),
    
    # Blind SQL Injection (Failure Route) (Sequence 110-119)
    (110, "Your blind SQL injection triggers aggressive security protocols.", Fore.RED, (), ()),
    (110, "Arasaka's cybersecurity team traces and blocks your connection.", Fore.WHITE, (), ()),
    (110, "Mission compromised. You've been detected.", Fore.RED, (), (), (2, 'Bad Ending 2')),  # Bad Ending
    
    # Precise SQL Injection (Sequence 120-129)
    (120, "Surgical precision in your SQL injection reveals critical system weaknesses.", Fore.CYAN, (), ()),
    (120, "You've gained a foothold in Arasaka's internal network.", Fore.GREEN, (), ()),
    (120, "Proceed with (P)enetration or (S)tealth reconnaissance?", Fore.YELLOW, ('p', 's'), (210, 220)),
    
    # IT Support Phishing (Failure Route) (Sequence 130-139)
    (130, "Your IT support impersonation fails. The target is too skeptical.", Fore.RED, (), ()),
    (130, "Security protocols lock you out permanently.", Fore.WHITE, (), ()),
    (130, "Mission failed. Your digital fingerprint is now flagged.", Fore.RED, (), (), (3, 'Bad Ending 3')),  # Bad Ending
    
    # Executive Phishing (Sequence 140-149)
    (140, "Impersonating a high-level executive grants unexpected access.", Fore.GREEN, (), ()),
    (140, "You're now inside Arasaka's internal communication channels.", Fore.CYAN, (), ()),
    (140, "Choose your next move: (I)nfiltrate or (D)isrupt communications?", Fore.YELLOW, ('i', 'd'), (230, 240)),
    
    # Deep System Infiltration (Sequence 150-159)
    (150, "You penetrate deeper into Arasaka's most secure systems.", Fore.CYAN, (), ()),
    (150, "The heart of their digital infrastructure is within reach.", Fore.WHITE, (), ()),
    (150, "Final objective: (E)xpose corporate secrets or (D)estroy critical infrastructure?", Fore.YELLOW, ('e', 'd'), (250, 260)),
    
    # Data Exfiltration (Sequence 160-169)
    (160, "Carefully extracting critical data without triggering alarms.", Fore.GREEN, (), ()),
    (160, "Each byte is a potential weapon against the corporate regime.", Fore.CYAN, (), ()),
    (160, "Mission accomplished. Corporate secrets are now yours.", Fore.CYAN, (), (1000,)),  # Good Ending
    
    # OSIRT Data Correlation (Sequence 170-179)
    (170, "Correlating OSIRT data reveals a complex network of corporate vulnerabilities.", Fore.CYAN, (), ()),
    (170, "You've mapped their digital ecosystem.", Fore.GREEN, (), ()),
    (170, "Prepare for final approach: (A)ttack or (S)tealth?", Fore.YELLOW, ('a', 's'), (270, 280)),
    
    # OSIRT Weakness Exploitation (Sequence 180-189)
    (180, "Exploiting the discovered weakness gives you unprecedented access.", Fore.CYAN, (), ()),
    (180, "Arasaka's defenses are crumbling.", Fore.GREEN, (), ()),
    (180, "Final objective: (R)evenge or (J)ustice?", Fore.YELLOW, ('r', 'j'), (290, 300)),
    
    # Direct Contact (Failure Route) (Sequence 190-199)
    (190, "Attempting direct contact backfires spectacularly.", Fore.RED, (), ()),
    (190, "Your identity is compromised. Extraction becomes impossible.", Fore.WHITE, (), ()),
    (190, "Mission failed. You are now a known threat.", Fore.RED, (), (), (4, 'Bad Ending 4')),  # Bad Ending
    
    # Communication Pattern Analysis (Sequence 200-209)
    (200, "Analyzing communication patterns reveals hidden communication channels.", Fore.GREEN, (), ()),
    (200, "You've found a potential backdoor into their systems.", Fore.CYAN, (), ()),
    (200, "Proceed with (I)nfiltration or (D)isruption?", Fore.YELLOW, ('i', 'd'), (310, 320)),
    
    # Penetration Path (Sequence 210-219)
    (210, "Full penetration of Arasaka's network begins.", Fore.CYAN, (), ()),
    (210, "Every firewall falls before your advanced techniques.", Fore.GREEN, (), ()),
    (210, "Final move: (E)xpose or (D)estroy?", Fore.YELLOW, ('e', 'd'), (330, 340)),
    
    # Stealth Reconnaissance (Sequence 220-229)
    (220, "Moving like a ghost through Arasaka's digital landscape.", Fore.CYAN, (), ()),
    (220, "Gathering intelligence without leaving a trace.", Fore.GREEN, (), ()),
    (220, "Objective: (I)nfiltrate or (S)abotage?", Fore.YELLOW, ('i', 's'), (350, 360)),
    
    # Communication Infiltration (Sequence 230-239)
    (230, "You've become a silent observer in Arasaka's internal networks.", Fore.CYAN, (), ()),
    (230, "Secrets flow through your hands like water.", Fore.GREEN, (), ()),
    (230, "Final choice: (E)xpose corruption or (B)lack out communications?", Fore.YELLOW, ('e', 'b'), (370, 380)),
    
    # Communication Disruption (Sequence 240-249)
    (240, "Disrupting Arasaka's communication networks creates chaos.", Fore.RED, (), ()),
    (240, "But chaos can be as dangerous as it is revealing.", Fore.WHITE, (), ()),
    (240, "Mission outcome uncertain.", Fore.YELLOW, (), (500,)),  # Ambiguous Ending
    
    # Expose Corporate Secrets (Sequence 250-259)
    (250, "The truth of Arasaka's dark operations comes to light.", Fore.CYAN, (), ()),
    (250, "Your hack will change everything.", Fore.GREEN, (), ()),
    (250, "Mission successful. The world will know the truth.", Fore.CYAN, (), (1000,)),  # Good Ending
    
    # Destroy Infrastructure (Sequence 260-269)
    (260, "You target Arasaka's critical infrastructure.", Fore.RED, (), ()),
    (260, "Entire digital systems begin to collapse.", Fore.WHITE, (), ()),
    (260, "Destruction complete, but at what cost?", Fore.YELLOW, (), (500,)),  # Morally Ambiguous Ending
    
    # Aggressive OSIRT Attack (Sequence 270-279)
    (270, "Your attack is swift and merciless.", Fore.RED, (), ()),
    (270, "Arasaka's defenses crumble under your onslaught.", Fore.CYAN, (), ()),
    (270, "Total digital warfare achieved.", Fore.CYAN, (), (500,)),  # Aggressive Good Ending
    
    # Stealth OSIRT Approach (Sequence 280-289)
    (280, "You move through their systems like a phantom.", Fore.GREEN, (), ()),
    (280, "No alarms, no traces, pure digital invisibility.", Fore.CYAN, (), ()),
    (280, "Mission accomplished with surgical precision.", Fore.CYAN, (), (1000,)),  # Stealthy Good Ending
    
    # Revenge Path (Sequence 290-299)
    (290, "Personal vendetta drives your every move.", Fore.RED, (), ()),
    (290, "Arasaka will pay for their past crimes.", Fore.WHITE, (), ()),
    (290, "Revenge is a dish best served through code.", Fore.CYAN, (), (500,)),  # Revenge Ending
    
    # Justice Path (Sequence 300-309)
    (300, "You choose the path of systemic accountability.", Fore.GREEN, (), ()),
    (300, "Exposing corruption, not seeking personal vengeance.", Fore.CYAN, (), ()),
    (300, "True justice through digital transparency.", Fore.CYAN, (), (1000,)),  # Idealistic Ending
    
    # Communication Backdoor Infiltration (Sequence 310-319)
    (310, "Silently moving through hidden communication channels.", Fore.GREEN, (), ()),
    (310, "Arasaka remains unaware of your presence.", Fore.CYAN, (), ()),
    (310, "Complete infiltration achieved.", Fore.CYAN, (), (1000,)),  # Stealthy Success Ending
    
    # Communication Disruption Path (Sequence 320-329)
    (320, "Communications go dark. Chaos ensues.", Fore.RED, (), ()),
    (320, "Arasaka's coordination is shattered.", Fore.WHITE, (), ()),
    (320, "A strategic digital strike.", Fore.CYAN, (), (500,)),  # Disruptive Ending
    
    # Full Network Exposure (Sequence 330-339)
    (330, "Every dark secret of Arasaka is now public.", Fore.GREEN, (), ()),
    (330, "The truth cannot be hidden anymore.", Fore.CYAN, (), ()),
    (330, "Your hack brings true transparency.", Fore.CYAN, (), (1000,)),  # Whistleblower Ending
    
    # Total Infrastructure Destruction (Sequence 340-349)
    (340, "Complete digital annihilation of Arasaka's systems.", Fore.RED, (), ()),
    (340, "Nothing remains of their digital empire.", Fore.WHITE, (), ()),
    (340, "Destruction as a form of revolution.", Fore.CYAN, (), (500,)),  # Radical Ending
    
    # Stealthy Infiltration (Sequence 350-359)
    (350, "You become a ghost in their machine.", Fore.GREEN, (), ()),
    (350, "Gathering intelligence without a trace.", Fore.CYAN, (), ()),
    (350, "Absolute digital stealth.", Fore.CYAN, (), (1000,)),  # Ultra-Stealthy Ending
    
    # Sabotage Path (Sequence 360-369)
    (360, "Strategic points of failure identified and exploited.", Fore.RED, (), ()),
    (360, "Arasaka's systems begin to crumble from within.", Fore.WHITE, (), ()),
    (360, "Surgical digital sabotage.", Fore.CYAN, (), (1000,)),  # Surgical Ending
    
    # Expose Corruption (Sequence 370-379)
    (370, "Corporate corruption laid bare for the world to see.", Fore.GREEN, (), ()),
    (370, "No secret can withstand the light of truth.", Fore.CYAN, (), ()),
    (370, "A victory for transparency.", Fore.CYAN, (), (1000,)),  # Idealistic Success Ending
    
    # Black Out Communications (Sequence 380-389)
    (380, "Total communication blackout for Arasaka.", Fore.RED, (), ()),
    (380, "They are blind, deaf, and mute.", Fore.WHITE, (), ()),
    (380, "Communication is power, and you've stripped it away.", Fore.CYAN, (), (500,)),  # Communication Warfare Ending
    
    #
    #
    #
    # Plot branch A
    #
    #
    #
    
    # Initial Situation - Aftermath of Infrastructure Destruction
    (500, f"Welcome back. The dust hasn't settled.", Fore.RED, (), ()),
    (500, "Arasaka's infrastructure lies in digital ruins, but the hunt is just beginning.", Fore.WHITE, (), ()),
    (500, "Government and corporate trackers are closing in. Your digital footprint is your greatest threat.", Fore.CYAN, (), ()),
    
    # Initial Decision Point
    (500, "\nChoose your primary survival strategy:", Fore.WHITE, (), ()),
    (500, "Do you (E)rase all evidence or (M)itigate your digital trail?", Fore.YELLOW, ('e', 'm'), (510, 520)),
    
    # Complete Erasure Path (Sequence 510-599)
    (510, "Total digital obliteration becomes your only option.", Fore.RED, (), ()),
    (510, "You'll need to systematically destroy every trace of your existence.", Fore.WHITE, (), ()),
    (510, "Choose your initial erasure approach:", Fore.GREEN, (), ()),
    (510, "Use (D)ata destruction tools or (F)orensic counter-techniques?", Fore.YELLOW, ('d', 'f'), (530, 540)),
    
    # Digital Trail Mitigation Path (Sequence 520-529)
    (520, "Carefully crafting a new digital identity becomes crucial.", Fore.CYAN, (), ()),
    (520, "Minimal traces, maximum anonymity.", Fore.GREEN, (), ()),
    (520, "Select your mitigation strategy:", Fore.WHITE, (), ()),
    (520, "Employ (S)tegonography or (C)ryptographic identity masking?", Fore.YELLOW, ('s', 'c'), (550, 560)),
    
    # Data Destruction Tools Route (Sequence 530-539)
    (530, "Specialized data destruction tools power up.", Fore.RED, (), ()),
    (530, "Secure erasure algorithms prepare to annihilate your digital existence.", Fore.CYAN, (), ()),
    (530, "Choose your destruction vector:", Fore.WHITE, (), ()),
    (530, "Use (S)ecure file deletion or (M)ultipass overwriting?", Fore.YELLOW, ('s', 'm'), (570, 580)),
    
    # Forensic Counter-Techniques (Sequence 540-549)
    (540, "Advanced forensic counter-measures activate.", Fore.GREEN, (), ()),
    (540, "You'll need to outsmart the most sophisticated tracking algorithms.", Fore.CYAN, (), ()),
    (540, "Select your forensic evasion method:", Fore.WHITE, (), ()),
    (540, "Implement (T)emporal data manipulation or (M)etadata poisoning?", Fore.YELLOW, ('t', 'm'), (590, 600)),
    
    # Steganography Path (Sequence 550-559)
    (550, "You begin embedding critical data within innocuous digital media.", Fore.GREEN, (), ()),
    (550, "Images, audio files become your hidden communication channels.", Fore.CYAN, (), ()),
    (550, "Choose your steganographic approach:", Fore.WHITE, (), ()),
    (550, "Use (I)mage LSB technique or (A)udio frequency encoding?", Fore.YELLOW, ('i', 'a'), (610, 620)),
    
    # Cryptographic Identity Masking (Sequence 560-569)
    (560, "Complex cryptographic techniques create a digital ghost.", Fore.CYAN, (), ()),
    (560, "Your true identity becomes a shifting, uncatchable phantom.", Fore.GREEN, (), ()),
    (560, "Select your masking strategy:", Fore.WHITE, (), ()),
    (560, "Implement (O)nion routing or (P)rivacy-focused blockchain identity?", Fore.YELLOW, ('o', 'p'), (630, 640)),
    
    # Secure File Deletion (Sequence 570-579)
    (570, "Specialized secure deletion tools engage.", Fore.RED, (), ()),
    (570, "Every bit of data becomes a potential vulnerability to eliminate.", Fore.WHITE, (), ()),
    (570, "Critical decision point approaches.", Fore.GREEN, (), ()),
    (570, "Proceed with (C)omplete system wipe or (S)elective erasure?", Fore.YELLOW, ('c', 's'), (650, 660)),
    
    # Multipass Overwriting (Sequence 580-589)
    (580, "Military-grade data destruction protocols activate.", Fore.CYAN, (), ()),
    (580, "Multiple overwrites ensure absolute data elimination.", Fore.RED, (), ()),
    (580, "Choose your overwrite strategy:", Fore.WHITE, (), ()),
    (580, "Use (R)andom data or (Z)ero-fill technique?", Fore.YELLOW, ('r', 'z'), (670, 680)),
    
    # Temporal Data Manipulation (Sequence 590-599)
    (590, "You begin manipulating digital timestamps and histories.", Fore.GREEN, (), ()),
    (590, "Creating false trails and erasing real ones.", Fore.CYAN, (), ()),
    (590, "Select your temporal manipulation method:", Fore.WHITE, (), ()),
    (590, "Implement (F)alse timeline or (A)nomaly injection?", Fore.YELLOW, ('f', 'a'), (690, 700)),
    
    # Metadata Poisoning (Sequence 600-609)
    (600, "Injecting false metadata into tracking systems.", Fore.RED, (), ()),
    (600, "Your digital signature becomes a deliberate mirage.", Fore.CYAN, (), ()),
    (600, "Choose your poisoning approach:", Fore.WHITE, (), ()),
    (600, "Use (G)eo-spoofing or (I)dentity scrambling?", Fore.YELLOW, ('g', 'i'), (710, 720)),
    
    # Image LSB Steganography (Sequence 610-619)
    (610, "Embedding critical data in image Least Significant Bits.", Fore.GREEN, (), ()),
    (610, "Invisible information hidden in plain sight.", Fore.CYAN, (), ()),
    (610, "Refine your steganographic technique:", Fore.WHITE, (), ()),
    (610, "Choose (H)igh-compression or (L)ow-detection method?", Fore.YELLOW, ('h', 'l'), (730, 740)),
    
    # Audio Frequency Encoding (Sequence 620-629)
    (620, "Encoding data within audio frequency ranges.", Fore.CYAN, (), ()),
    (620, "Sound becomes your ultimate encryption medium.", Fore.GREEN, (), ()),
    (620, "Select audio encoding strategy:", Fore.WHITE, (), ()),
    (620, "Use (U)ltrasonic or (H)uman-audible range?", Fore.YELLOW, ('u', 'h'), (750, 760)),
    
    # Onion Routing Identity Masking (Sequence 630-639)
    (630, "Implementing multi-layer anonymous routing.", Fore.GREEN, (), ()),
    (630, "Your digital presence becomes a labyrinth.", Fore.CYAN, (), ()),
    (630, "Choose routing complexity:", Fore.WHITE, (), ()),
    (630, "Select (M)aximum layers or (S)tealth optimization?", Fore.YELLOW, ('m', 's'), (770, 780)),
    
    # Blockchain Privacy Identity (Sequence 640-649)
    (640, "Creating a cryptographically secure digital identity.", Fore.CYAN, (), ()),
    (640, "Blockchain becomes your ultimate anonymity shield.", Fore.GREEN, (), ()),
    (640, "Determine identity strategy:", Fore.WHITE, (), ()),
    (640, "Choose (D)ecentralized or (P)rivacy-focused approach?", Fore.YELLOW, ('d', 'p'), (790, 800)),
    
    # Complete System Wipe (Sequence 650-659)
    (650, "Initiating total system destruction protocol.", Fore.RED, (), ()),
    (650, "Every digital trace will be annihilated.", Fore.WHITE, (), ()),
    (650, "Final wipe preparation:", Fore.GREEN, (), ()),
    (650, "Confirm (F)inal wipe or (C)autious removal?", Fore.YELLOW, ('f', 'c'), (810, 820)),
    
    # Selective Erasure (Sequence 660-669)
    (660, "Precision targeting of specific digital evidence.", Fore.CYAN, (), ()),
    (660, "Surgical removal of compromising data.", Fore.GREEN, (), ()),
    (660, "Choose erasure precision:", Fore.WHITE, (), ()),
    (660, "Use (T)argeted or (C)omprehensive method?", Fore.YELLOW, ('t', 'c'), (830, 840)),
    
    # Random Data Overwrite (Sequence 670-679)
    (670, "Generating cryptographically secure random data.", Fore.CYAN, (), ()),
    (670, "Each overwrite makes recovery increasingly impossible.", Fore.RED, (), ()),
    (670, "Determine overwrite intensity:", Fore.WHITE, (), ()),
    (670, "Choose (H)igh-entropy or (L)ow-detection overwrite?", Fore.YELLOW, ('h', 'l'), (850, 860)),
    
    # Zero-Fill Technique (Sequence 680-689)
    (680, "Implementing military-grade zero-filling protocol.", Fore.WHITE, (), ()),
    (680, "Absolute data elimination through systematic zeroing.", Fore.RED, (), ()),
    (680, "Select zero-fill strategy:", Fore.GREEN, (), ()),
    (680, "Use (M)ultiple passes or (S)ingle comprehensive pass?", Fore.YELLOW, ('m', 's'), (870, 880)),
    
    # False Timeline Creation (Sequence 690-699)
    (690, "Constructing an elaborate false digital history.", Fore.GREEN, (), ()),
    (690, "Misdirection becomes your primary survival tool.", Fore.CYAN, (), ()),
    (690, "Choose timeline complexity:", Fore.WHITE, (), ()),
    (690, "Implement (C)omplex or (S)imple false narrative?", Fore.YELLOW, ('c', 's'), (890, 900)),
    
    # Anomaly Injection (Sequence 700-709)
    (700, "Introducing controlled digital anomalies.", Fore.CYAN, (), ()),
    (700, "Disrupting potential forensic reconstruction.", Fore.RED, (), ()),
    (700, "Select anomaly injection method:", Fore.WHITE, (), ()),
    (700, "Use (T)emporal or (S)patial disruption?", Fore.YELLOW, ('t', 's'), (910, 920)),
    
    # Geo-Spoofing (Sequence 710-719)
    (710, "Generating false geographical data traces.", Fore.GREEN, (), ()),
    (710, "Your digital location becomes a deliberate illusion.", Fore.CYAN, (), ()),
    (710, "Choose spoofing complexity:", Fore.WHITE, (), ()),
    (710, "Implement (H)igh-detail or (M)inimal trace spoofing?", Fore.YELLOW, ('h', 'm'), (930, 940)),
    
    # Identity Scrambling (Sequence 720-729)
    (720, "Systematically destroying your digital fingerprint.", Fore.RED, (), ()),
    (720, "No consistent identity remains.", Fore.WHITE, (), ()),
    (720, "Select scrambling technique:", Fore.GREEN, (), ()),
    (720, "Use (A)lgorithmic or (R)andom identity mutation?", Fore.YELLOW, ('a', 'r'), (950, 960)),
    
    # High-Compression Steganography Endings (730-739)
    (730, "High-compression steganography successfully conceals critical data.", Fore.GREEN, (), ()),
    (730, "Minimal file size raises no suspicions.", Fore.CYAN, (), ()),
    (730, "Your digital traces have been masterfully hidden.", Fore.CYAN, (), (), (5, 'Successful Stealth Ending')),  # Successful Stealth Ending
    
    # Low-Detection Steganography Endings (740-749)
    (740, "Low-detection methods prove less effective.", Fore.RED, (), ()),
    (740, "Forensic analysts begin to unravel your hidden data.", Fore.WHITE, (), ()),
    (740, "Your carefully crafted anonymity starts to crack.", Fore.YELLOW, (), (), (6, 'Partial Failure Ending 1')),  # Partial Failure Ending
    
    # Ultrasonic Audio Encoding Endings (750-759)
    (750, "Ultrasonic frequencies perfectly mask your data transmission.", Fore.GREEN, (), ()),
    (750, "Undetectable communication beyond human hearing.", Fore.CYAN, (), ()),
    (750, "Complete audio-based stealth achieved.", Fore.CYAN, (), (), (7, 'Advanced Stealth Ending')),  # Advanced Stealth Ending
    
    # Human-Audible Range Audio Encoding Endings (760-769)
    (760, "Audio-encoded data risks detection.", Fore.RED, (), ()),
    (760, "Potential interception becomes a critical threat.", Fore.WHITE, (), ()),
    (760, "Your communication method is compromised.", Fore.YELLOW, (), (), (8, 'Risky Ending 1')),  # Risky Ending
    
    # Maximum Layers Onion Routing Endings (770-779)
    (770, "Absolute anonymity through maximum routing layers.", Fore.GREEN, (), ()),
    (770, "Your digital path becomes an impenetrable maze.", Fore.CYAN, (), ()),
    (770, "Tracking becomes mathematically impossible.", Fore.CYAN, (), (), (9, 'Ultimate Anonymity Ending')),  # Ultimate Anonymity Ending
    
    # Stealth Optimization Onion Routing Endings (780-789)
    (780, "Optimized routing reduces potential detection points.", Fore.GREEN, (), ()),
    (780, "Surgical precision in digital invisibility.", Fore.CYAN, (), ()),
    (780, "Minimal digital footprint established.", Fore.CYAN, (), (), (10, 'Efficient Stealth Ending')),  # Efficient Stealth Ending
    
    # Decentralized Blockchain Identity Endings (790-799)
    (790, "Fully decentralized identity becomes your ultimate shield.", Fore.GREEN, (), ()),
    (790, "No single point of digital identification remains.", Fore.CYAN, (), ()),
    (790, "You've become a true digital phantom.", Fore.CYAN, (), (), (11, 'Complete Anonymity Ending')),  # Complete Anonymity Ending
    
    # Privacy-Focused Blockchain Identity Endings (800-809)
    (800, "Privacy-focused blockchain creates a controlled digital presence.", Fore.GREEN, (), ()),
    (800, "Carefully managed digital identity emerges.", Fore.CYAN, (), ()),
    (800, "Strategic digital anonymity achieved.", Fore.CYAN, (), (), (12, 'Controlled Anonymity Ending')),  # Controlled Anonymity Ending
    
    # Final Wipe Endings (810-819)
    (810, "Total system destruction complete. No traces remain.", Fore.RED, (), ()),
    (810, "Your entire digital existence has been erased.", Fore.WHITE, (), ()),
    (810, "Absolute digital annihilation successful.", Fore.CYAN, (), (), (13, 'Total Erasure Ending')),  # Total Erasure Ending
    
    # Cautious Removal Endings (820-829)
    (820, "Selective, careful data removal minimizes risk.", Fore.GREEN, (), ()),
    (820, "Critical evidence systematically eliminated.", Fore.CYAN, (), ()),
    (820, "Precision in digital cleanup achieved.", Fore.CYAN, (), (), (14, 'Surgical Removal Ending')),  # Surgical Removal Ending
    
    # Targeted Erasure Endings (830-839)
    (830, "Precisely targeted data removal leaves no suspicious gaps.", Fore.GREEN, (), ()),
    (830, "Only the most critical evidence is eliminated.", Fore.CYAN, (), ()),
    (830, "Surgical digital cleanup successful.", Fore.CYAN, (), (), (15, 'Precise Elimination Ending')),  # Precise Elimination Ending
    
    # Comprehensive Erasure Endings (840-849)
    (840, "Comprehensive data removal triggers suspicion.", Fore.RED, (), ()),
    (840, "Extensive deletions raise forensic red flags.", Fore.WHITE, (), ()),
    (840, "Your attempts at total erasure become noticeable.", Fore.YELLOW, (), (), (16, 'Risky Ending 2')),  # Risky Ending 2
    
    # High-Entropy Overwrite Endings (850-859)
    (850, "High-entropy data overwrite creates perfect digital obfuscation.", Fore.GREEN, (), ()),
    (850, "Recovery becomes mathematically improbable.", Fore.CYAN, (), ()),
    (850, "Your data is now indistinguishable noise.", Fore.CYAN, (), (), (17, 'Ultimate Erasure Ending')),  # Ultimate Erasure Ending
    
    # Low-Detection Overwrite Endings (860-869)
    (860, "Low-detection overwrite leaves subtle traces.", Fore.RED, (), ()),
    (860, "Forensic analysts find potential recovery points.", Fore.WHITE, (), ()),
    (860, "Your digital erasure shows potential weaknesses.", Fore.YELLOW, (), (), (18, 'Partial Failure Ending 2')),  # Partial Failure Ending 2
    
    # Multiple Pass Overwrite Endings (870-879)
    (870, "Multiple overwrite passes ensure absolute data destruction.", Fore.GREEN, (), ()),
    (870, "Each pass makes previous data recovery impossible.", Fore.CYAN, (), ()),
    (870, "Military-grade data elimination achieved.", Fore.CYAN, (), (), (19, 'Comprehensive Erasure Ending')),  # Comprehensive Erasure Ending
    
    # Single Comprehensive Pass Endings (880-889)
    (880, "Single comprehensive pass leaves potential recovery vectors.", Fore.RED, (), ()),
    (880, "Incomplete data destruction raises forensic opportunities.", Fore.WHITE, (), ()),
    (880, "Your digital cleanup shows critical vulnerabilities.", Fore.YELLOW, (), (), (20, 'Risky Ending 3')),  # Risky Ending 3
    
    # Complex False Timeline Endings (890-899)
    (890, "Intricate false timeline completely misleads investigators.", Fore.GREEN, (), ()),
    (890, "Every digital breadcrumb tells a calculated lie.", Fore.CYAN, (), ()),
    (890, "Absolute misdirection achieved.", Fore.CYAN, (), (), (21, 'Ultimate Deception Ending')),  # Ultimate Deception Ending
    
    # Simple False Narrative Endings (900-909)
    (900, "Simple false narrative quickly unravels.", Fore.RED, (), ()),
    (900, "Investigators easily pierce through your cover story.", Fore.WHITE, (), ()),
    (900, "Your attempts at misdirection fail.", Fore.YELLOW, (), (), (22, 'Failure Ending')),  # Failure Ending
    
    # Temporal Disruption Endings (910-919)
    (910, "Temporal data manipulation creates perfect chronological confusion.", Fore.GREEN, (), ()),
    (910, "Historical records become impossibly complex.", Fore.CYAN, (), ()),
    (910, "Time itself becomes your alibi.", Fore.CYAN, (), (), (23, 'Advanced Misdirection Ending')),  # Advanced Misdirection Ending
    
    # Spatial Disruption Endings (920-929)
    (920, "Spatial data disruption fragments your digital presence.", Fore.RED, (), ()),
    (920, "Inconsistent location data raises immediate suspicions.", Fore.WHITE, (), ()),
    (920, "Your attempt at spatial misdirection backfires.", Fore.YELLOW, (), (), (24, 'Risky Ending 4')),  # Risky Ending 4
    
    # High-Detail Geo-Spoofing Endings (930-939)
    (930, "Extremely detailed geo-spoofing creates a perfect false trail.", Fore.GREEN, (), ()),
    (930, "Your digital location becomes an intricate illusion.", Fore.CYAN, (), ()),
    (930, "Investigators lose themselves in your fabricated geography.", Fore.CYAN, (), (), (25, 'Ultimate Deception Ending')),  # Ultimate Deception Ending
    
    # Minimal Trace Geo-Spoofing Endings (940-949)
    (940, "Minimal geo-spoofing provides basic misdirection.", Fore.RED, (), ()),
    (940, "Subtle location inconsistencies become apparent.", Fore.WHITE, (), ()),
    (940, "Your geographic camouflage shows clear weaknesses.", Fore.YELLOW, (), (), (26, 'Partial Failure Ending 3')),  # Partial Failure Ending
    
    # Algorithmic Identity Mutation Endings (950-959)
    (950, "Algorithmic identity mutation creates a perfect digital phantom.", Fore.GREEN, (), ()),
    (950, "Your digital identity becomes a constantly shifting entity.", Fore.CYAN, (), ()),
    (950, "Tracking becomes fundamentally impossible.", Fore.CYAN, (), (), (27, 'Ultimate Anonymity Ending')),  # Ultimate Anonymity Ending
    
    # Random Identity Mutation Endings (960-969)
    (960, "Random identity mutation creates chaotic digital presence.", Fore.RED, (), ()),
    (960, "Unpredictable changes raise immediate red flags.", Fore.WHITE, (), ()),
    (960, "Your identity mutation becomes suspiciously erratic.", Fore.YELLOW, (), (), (28, 'Risky Ending 5')),  # Risky Ending 5
    
    #
    #
    #
    # Plot branch B
    #
    #
    #
    
    # Introduction to New Job
    (1000, f"Welcome back. After your leak of Arasaka, your reputation as a digital vigilante has opened unexpected doors.", Fore.CYAN, (), ()),
    (1000, "A prestigious tech company offers you a remote blue team cybersecurity role.", Fore.GREEN, (), ()),
    (1000, "Your mission: Defend the corporate network from an imminent cyber threat.", Fore.WHITE, (), ()),
    
    # Initial Threat Detection
    (1000, "Anomalous network traffic triggers your intrusion detection systems.", Fore.RED, (), ()),
    (1000, "Choose your initial response:", Fore.WHITE, (), ()),
    (1000, "Do you (A)nalyze traffic patterns or (I)solate suspicious endpoints?", Fore.YELLOW, ('a', 'i'), (1010, 1020)),
    
    # Traffic Pattern Analysis Path
    (1010, "Deep packet inspection reveals complex network infiltration attempts.", Fore.CYAN, (), ()),
    (1010, "The attack methodology suggests a sophisticated threat actor.", Fore.GREEN, (), ()),
    (1010, "Choose your investigative approach:", Fore.WHITE, (), ()),
    (1010, "Perform (W)ireshark analysis or (N)etflow correlation?", Fore.YELLOW, ('w', 'n'), (1030, 1040)),
    
    # Endpoint Isolation Strategy
    (1020, "Quickly isolating potentially compromised network segments.", Fore.RED, (), ()),
    (1020, "But isolation might alert the attackers to your awareness.", Fore.WHITE, (), ()),
    (1020, "Next step: (F)orensic capture or (R)isk mitigation?", Fore.YELLOW, ('f', 'r'), (1050, 1060)),
    
    # Wireshark Deep Analysis
    (1030, "Wireshark reveals intricate attack signatures.", Fore.CYAN, (), ()),
    (1030, "Potential indicators of advanced persistent threat (APT).", Fore.GREEN, (), ()),
    (1030, "Choose your response:", Fore.WHITE, (), ()),
    (1030, "Initiate (T)hreat hunting or prepare (C)ounter-intrusion?", Fore.YELLOW, ('t', 'c'), (1070, 1080)),
    
    # Netflow Correlation
    (1040, "Netflow data uncovers unusual communication patterns.", Fore.GREEN, (), ()),
    (1040, "Geographical and temporal anomalies detected.", Fore.CYAN, (), ()),
    (1040, "Next investigative step:", Fore.WHITE, (), ()),
    (1040, "Conduct (G)eo-tracking or (B)otnet analysis?", Fore.YELLOW, ('g', 'b'), (1090, 1100)),
    
    # Forensic Capture
    (1050, "Capturing forensic evidence of potential breach.", Fore.CYAN, (), ()),
    (1050, "Detailed log analysis becomes critical.", Fore.WHITE, (), ()),
    (1050, "Proceed with (L)og correlation or (E)xtract artifacts?", Fore.YELLOW, ('l', 'e'), (1110, 1120)),
    
    # Risk Mitigation
    (1060, "Implementing comprehensive risk mitigation strategies.", Fore.RED, (), ()),
    (1060, "Defensive walls up, but at what cost to investigation?", Fore.WHITE, (), ()),
    (1060, "Focus on (P)reventive controls or (D)etection mechanisms?", Fore.YELLOW, ('p', 'd'), (1130, 1140)),
    
    # Threat Hunting
    (1070, "Active threat hunting reveals sophisticated attack vectors.", Fore.GREEN, (), ()),
    (1070, "You're closing in on the attacker's methodology.", Fore.CYAN, (), ()),
    (1070, "Next move:", Fore.WHITE, (), ()),
    (1070, "Pursue (I)ntrusion timeline or map (A)ttack infrastructure?", Fore.YELLOW, ('i', 'a'), (1150, 1160)),
    
    # Counter-Intrusion Preparation
    (1080, "Preparing advanced counter-intrusion techniques.", Fore.RED, (), ()),
    (1080, "Setting up honeypots and deception grids.", Fore.WHITE, (), ()),
    (1080, "Strategy: (L)ure and trace or (B)lock and analyze?", Fore.YELLOW, ('l', 'b'), (1170, 1180)),
    
    # Geo-Tracking
    (1090, "Tracking attack origins across global networks.", Fore.CYAN, (), ()),
    (1090, "Geolocation data points to multiple international sources.", Fore.GREEN, (), ()),
    (1090, "Investigative path:", Fore.WHITE, (), ()),
    (1090, "Pursue (O)rigin tracking or (C)orrelate infrastructure?", Fore.YELLOW, ('o', 'c'), (1190, 1200)),
    
    # Botnet Analysis
    (1100, "Complex botnet infrastructure detected.", Fore.RED, (), ()),
    (1100, "Massive distributed attack potential identified.", Fore.WHITE, (), ()),
    (1100, "Response strategy:", Fore.WHITE, (), ()),
    (1100, "Perform (S)ink-holing or (D)istributed takedown?", Fore.YELLOW, ('s', 'd'), (1210, 1220)),
    
    # Log Correlation
    (1110, "Correlating logs reveals intricate attack patterns.", Fore.GREEN, (), ()),
    (1110, "Each log entry a piece of a complex puzzle.", Fore.CYAN, (), ()),
    (1110, "Next analytical step:", Fore.WHITE, (), ()),
    (1110, "Use (E)LK stack or (S)iem correlation?", Fore.YELLOW, ('e', 's'), (1230, 1240)),
    
    # Artifact Extraction
    (1120, "Extracting critical forensic artifacts.", Fore.CYAN, (), ()),
    (1120, "Potential evidence of sophisticated cyber espionage.", Fore.WHITE, (), ()),
    (1120, "Proceed with (F)orensic analysis or (M)alware reverse engineering?", Fore.YELLOW, ('f', 'm'), (1250, 1260)),
    
    # Preventive Controls
    (1130, "Implementing robust preventive security controls.", Fore.RED, (), ()),
    (1130, "Strengthening network defenses at every layer.", Fore.WHITE, (), ()),
    (1130, "Focus on (F)irewall or (E)ndpoint protection?", Fore.YELLOW, ('f', 'e'), (1270, 1280)),
    
    # Detection Mechanisms
    (1140, "Advanced threat detection systems activated.", Fore.GREEN, (), ()),
    (1140, "Real-time monitoring at maximum sensitivity.", Fore.CYAN, (), ()),
    (1140, "Choose detection strategy:", Fore.WHITE, (), ()),
    (1140, "Implement (A)nomaly detection or (B)ehavioral analytics?", Fore.YELLOW, ('a', 'b'), (1290, 1300)),
    
    # Intrusion Timeline Path (1150-1159)
    (1150, "The digital forensics reveal a meticulously planned cyber attack.", Fore.GREEN, (), ()),
    (1150, "Each timestamp tells a story of calculated infiltration.", Fore.CYAN, (), ()),
    (1150, "You've reconstructed the entire attack methodology.", Fore.CYAN, (), ()),
    (1150, "Your comprehensive timeline becomes a weapon against future threats.", Fore.WHITE, (), ()),
    (1150, "A masterpiece of cyber investigation completed.", Fore.GREEN, (), (), (29, 'Investigative Success Ending')),  # Investigative Success Ending
    
    # Attack Infrastructure Mapping (1160-1169)
    (1160, "The attacker's entire digital infrastructure lies exposed.", Fore.RED, (), ()),
    (1160, "Servers, relay points, and command structures meticulously mapped.", Fore.CYAN, (), ()),
    (1160, "Your analysis could cripple entire cyber criminal networks.", Fore.CYAN, (), ()),
    (1160, "Raw intelligence becomes a strategic weapon.", Fore.GREEN, (), ()),
    (1160, "The digital landscape now bends to your understanding.", Fore.WHITE, (), (), (30, 'Infrastructure Intelligence Ending')),  # Infrastructure Intelligence Ending
    
    # Lure and Trace Path (1170-1179)
    (1170, "Your sophisticated honeypot successfully captures the attacker's techniques.", Fore.GREEN, (), ()),
    (1170, "Each interaction reveals more about the mysterious threat.", Fore.CYAN, (), ()),
    (1170, "Digital breadcrumbs lead deeper into the cyber rabbit hole.", Fore.CYAN, (), ()),
    (1170, "The hunter becomes the hunted in this digital chess match.", Fore.RED, (), ()),
    (1170, "A triumph of deception and cybersecurity strategy.", Fore.WHITE, (), (), (31, 'Honeypot Deception Ending')),  # Honeypot Deception Ending
    
    # Block and Analyze Path (1180-1189)
    (1180, "Aggressive defensive protocols neutralize the immediate threat.", Fore.RED, (), ()),
    (1180, "But victory comes at the cost of deeper investigation.", Fore.WHITE, (), ()),
    (1180, "The attacker's true identity remains shrouded in mystery.", Fore.CYAN, (), ()),
    (1180, "Survival, but not total understanding.", Fore.CYAN, (), ()),
    (1180, "A pyrrhic victory in the cyber warfare landscape.", Fore.GREEN, (), (), (32, 'Defensive Pyrrhic Victory Ending')),  # Defensive Pyrrhic Victory Ending
    
    # Origin Tracking (1190-1199)
    (1190, "The attack's geographical origins unravel like a complex tapestry.", Fore.GREEN, (), ()),
    (1190, "Multiple international nodes reveal a global cyber conspiracy.", Fore.CYAN, (), ()),
    (1190, "Each traced IP address tells a fragment of a larger story.", Fore.CYAN, (), ()),
    (1190, "Geopolitical cyber warfare mapped in exquisite detail.", Fore.RED, (), ()),
    (1190, "Your tracking becomes a critical intelligence breakthrough.", Fore.WHITE, (), (), (33, 'Global Threat Mapping Ending')),  # Global Threat Mapping Ending
    
    # Infrastructure Correlation (1200-1209)
    (1200, "Correlating infrastructure reveals interconnected threat networks.", Fore.CYAN, (), ()),
    (1200, "Each connection point a strategic vulnerability.", Fore.GREEN, (), ()),
    (1200, "The digital ecosystem of cyber threats laid bare.", Fore.CYAN, (), ()),
    (1200, "Your analysis could reshape cyber defense strategies globally.", Fore.WHITE, (), ()),
    (1200, "A comprehensive map of digital threat landscapes.", Fore.RED, (), (), (34, 'Infrastructure Intelligence Ending')),  # Infrastructure Intelligence Ending
    
    # Sink-Holing Path (1210-1219)
    (1210, "Strategic sink-holing neutralizes the botnet's communication channels.", Fore.RED, (), ()),
    (1210, "Infected nodes suddenly go silent, cut off from their master.", Fore.CYAN, (), ()),
    (1210, "A surgical strike against distributed cyber threats.", Fore.GREEN, (), ()),
    (1210, "The botnet's power dissipates like morning mist.", Fore.CYAN, (), ()),
    (1210, "Cyber defense achieved through precision intervention.", Fore.WHITE, (), (), (35, 'Botnet Neutralization Ending')),  # Botnet Neutralization Ending
    
    # Distributed Takedown (1220-1229)
    (1220, "Coordinated takedown operations cripple the attacking infrastructure.", Fore.GREEN, (), ()),
    (1220, "Multiple attack vectors systematically eliminated.", Fore.RED, (), ()),
    (1220, "A collaborative cyber defense effort bears fruit.", Fore.CYAN, (), ()),
    (1220, "The digital battlefield transformed by strategic action.", Fore.CYAN, (), ()),
    (1220, "Collective cyber resilience demonstrated.", Fore.WHITE, (), (), (36, 'Distributed Defense Success Ending')),  # Distributed Defense Success Ending
    
    # ELK Stack Analysis (1230-1239)
    (1230, "The ELK stack reveals intricate attack patterns.", Fore.GREEN, (), ()),
    (1230, "Log data transformed into actionable intelligence.", Fore.CYAN, (), ()),
    (1230, "Every log entry a piece of a complex puzzle.", Fore.CYAN, (), ()),
    (1230, "Advanced log correlation uncovers hidden threat mechanisms.", Fore.WHITE, (), ()),
    (1230, "Analytical power turned against cyber adversaries.", Fore.RED, (), (), (37, 'Log Intelligence Ending')),  # Log Intelligence Ending
    
    # SIEM Correlation (1240-1249)
    (1240, "SIEM correlation exposes the attack's sophisticated methodology.", Fore.CYAN, (), ()),
    (1240, "Security events interconnected, revealing deeper threats.", Fore.GREEN, (), ()),
    (1240, "Real-time threat intelligence at its pinnacle.", Fore.CYAN, (), ()),
    (1240, "The digital defense system operates with unprecedented precision.", Fore.WHITE, (), ()),
    (1240, "Cyber threats analyzed and neutralized in real-time.", Fore.RED, (), (), (38, 'SIEM Intelligence Ending')),  # SIEM Intelligence Ending
    
    # Forensic Analysis (1250-1259)
    (1250, "Forensic analysis unveils the attack's intricate details.", Fore.GREEN, (), ()),
    (1250, "Digital evidence reconstructs the entire cyber incident.", Fore.CYAN, (), ()),
    (1250, "Each artifact a testimony to the attacker's methodology.", Fore.CYAN, (), ()),
    (1250, "Forensic insights become a weapon of understanding.", Fore.WHITE, (), ()),
    (1250, "The science of digital investigation triumphs.", Fore.RED, (), (), (39, 'Forensic Investigation Ending')),  # Forensic Investigation Ending
    
    # Malware Reverse Engineering (1260-1269)
    (1260, "Reverse engineering reveals the malware's complex architecture.", Fore.RED, (), ()),
    (1260, "Each layer of code a window into the attacker's mind.", Fore.CYAN, (), ()),
    (1260, "Sophisticated obfuscation techniques systematically dismantled.", Fore.GREEN, (), ()),
    (1260, "The malware's secrets laid bare through technical prowess.", Fore.CYAN, (), ()),
    (1260, "A triumph of analytical cybersecurity techniques.", Fore.WHITE, (), (), (40, 'Malware Reverse Engineering Ending')),  # Malware Reverse Engineering Ending
    
    # Firewall Focus (1270-1279)
    (1270, "Advanced firewall configurations create an impenetrable digital fortress.", Fore.RED, (), ()),
    (1270, "Multiple layers of network protection deployed.", Fore.GREEN, (), ()),
    (1270, "Each packet scrutinized, each connection validated.", Fore.CYAN, (), ()),
    (1270, "The network transformed into a bastion of security.", Fore.CYAN, (), ()),
    (1270, "Defensive capabilities elevated to new heights.", Fore.WHITE, (), (), (41, 'Firewall Fortress Ending')),  # Firewall Fortress Ending
    
    # Endpoint Protection (1280-1289)
    (1280, "Comprehensive endpoint protection shields critical infrastructure.", Fore.GREEN, (), ()),
    (1280, "Every device becomes a defended stronghold.", Fore.CYAN, (), ()),
    (1280, "Advanced threat detection at the device level.", Fore.CYAN, (), ()),
    (1280, "Individual endpoints contribute to collective security.", Fore.RED, (), ()),
    (1280, "A holistic approach to cybersecurity realized.", Fore.WHITE, (), (), (42, 'Endpoint Defense Ending')),  # Endpoint Defense Ending
    
    # Anomaly Detection (1290-1299)
    (1290, "Anomaly detection algorithms uncover hidden threat patterns.", Fore.GREEN, (), ()),
    (1290, "Statistical models predict and prevent cyber incidents.", Fore.CYAN, (), ()),
    (1290, "Machine learning turns defense into a predictive science.", Fore.CYAN, (), ()),
    (1290, "Potential threats neutralized before they manifest.", Fore.RED, (), ()),
    (1290, "The future of proactive cyber defense.", Fore.WHITE, (), (), (43, 'Predictive Defense Ending')),  # Predictive Defense Ending
    
    # Behavioral Analytics (1300-1309)
    (1300, "Behavioral analytics expose the attacker's unique digital fingerprint.", Fore.CYAN, (), ()),
    (1300, "User and system behaviors analyzed with unprecedented depth.", Fore.GREEN, (), ()),
    (1300, "Deviations from normal patterns instantly flagged.", Fore.CYAN, (), ()),
    (1300, "Psychological profiling meets cybersecurity technology.", Fore.RED, (), ()),
    (1300, "A new frontier of adaptive cyber defense.", Fore.WHITE, (), (), (44, 'Behavioral Defense Ending')),  # Behavioral Defense Ending
]




























descriptions = {
    0: """Cybersecurity Specialist: A professional skilled in protecting systems from digital threats.""",
    
    10: """Distributed Cracking: A technique using multiple computers to break encryption faster.
Intelligence Gathering: The process of collecting data to uncover vulnerabilities.""",
    
    20: """Linux: Open-source Unix-like OS known for stability, security, and flexibility in IT environments.
Breach Method: A technique used to exploit vulnerabilities and gain unauthorized access to systems.
SQL Injection: Code injection attack that manipulates SQL queries to access or modify databases.
Phishing: Social engineering attack tricking users into revealing sensitive information via deceptive messages.""",
    
    30: """Hashcat: A powerful, GPU-accelerated password-cracking tool.
John the Ripper: A CPU-based password cracker used for security auditing.""",
    
    40: """OSINT (Open-Source Intelligence): Gathering publicly available information for analysis.
Social Media Analysis: Examining online interactions for security vulnerabilities.""",
    
    50: """Blind SQL Injection: A technique where attackers infer database information through responses.
Targeted SQL Attack: A precise exploitation of database vulnerabilities to gain access.""",
    
    60: """Phishing Email: A deceptive email designed to trick recipients into revealing sensitive data.
Social Engineering: Manipulating people into divulging confidential information.""",
    
    70: """GPU Cracking: Using graphics cards to accelerate password decryption.
Encryption: The process of converting data into a secure format unreadable without a key.""",
    
    90: """OSIRT: Open-Source Intelligence Reconnaissance, a method for analyzing digital footprints.""",
    
    100: """Social Media Exploitation: Using employees' online presence to identify security gaps.
Insider Information: Privileged data obtained from within an organization.""",
    
    120: """Penetration Testing: Simulated cyberattacks to evaluate system security.""",
    
    160: """Data Exfiltration: Stealthily extracting sensitive information from a system.
Corporate Espionage: Illegally acquiring trade secrets or confidential business data.""",
    
    170: """Network Vulnerability Mapping: Identifying weak points in a system’s security.
Cyber Attack: A deliberate attempt to damage, disrupt, or gain unauthorized access to systems.""",
    
    180: """Weakness Exploitation: Taking advantage of security flaws to infiltrate systems.""",
    #
    #
    #
    #
    200: """Communication Pattern Analysis: Examining message flows to uncover hidden channels.
Backdoor Access: An undetected entry point into a system.""",
    
    210: """Network Penetration: Gaining unauthorized access to a system’s core.
Firewall Breaching: Overcoming security barriers to enter a network.""",
    
    230: """Communication Infiltration: Tapping into internal networks without detection.""",
    
    250: """Hacktivism: Using hacking as a tool for social justice.""",
    
    270: """OSIRT: Open-Source Intelligence Reconnaissance, a method for analyzing digital footprints.""",
    
    280: """OSIRT: Open-Source Intelligence Reconnaissance, a method for analyzing digital footprints.""",
    
    310: """Backdoor Infiltration: Using covert access points to stay undetected.""",
    
    330: """Whistleblowing: Exposing unethical actions through leaks.""",
    
    380: """Blackout Attack: Shutting down all internal communications.""",
    #
    #
    #
    #
    #
    # 500


    
    500: """Digital footprint: Traces of online activity that can be tracked.
Corporate trackers: Systems used by organizations to monitor digital activities.""",

    510: """Erasure approach: Method chosen to remove digital traces.
Data destruction tools: Software designed to permanently delete information.
Forensic counter-techniques: Methods to prevent digital forensic analysis.""",

    520: """Digital identity: Online persona and associated data.
Anonymity: State of being untraceable or unidentified.
Steganography: Hiding data within other files or media.
Cryptographic masking: Using encryption to conceal identity.""",

    530: """Secure erasure: Permanent deletion of digital data.
Destruction vector: Specific method of data elimination.
Secure file deletion: Permanent removal of individual files.
Multipass overwriting: Repeated writing of data to ensure erasure.""",

    540: """Forensic counter-measures: Techniques to evade digital forensic analysis.
Tracking algorithms: Programs designed to follow digital activities.
Temporal manipulation: Altering time-related data.
Metadata poisoning: Corrupting or falsifying file metadata.""",

    550: """Steganographic approach: Method for hiding data within other files.
Digital media: Files like images, audio, or video used for hiding data.
LSB technique: Least Significant Bit method for hiding data in images.
Audio frequency encoding: Hiding data in sound wave patterns.""",

    560: """Cryptographic techniques: Mathematical methods for securing information.
Digital ghost: Untraceable online presence.
Onion routing: Layered encryption for anonymous communication.
Blockchain identity: Decentralized digital identity system.""",

    570: """System wipe: Complete erasure of all data on a system.
Selective erasure: Targeted deletion of specific data.
Vulnerability elimination: Removing potential points of compromise.""",

    580: """Overwrite strategy: Technique for writing over existing data.
Random data: Unpredictable patterns used in overwriting.
Zero-fill: Writing zeros to all storage locations.""",

    590: """Temporal manipulation: Altering time-related digital data.
Anomaly injection: Introducing irregularities to confuse analysis.""",

    600: """Metadata poisoning: Corrupting or falsifying file metadata.
Digital signature: Unique characteristics identifying digital content.
Geo-spoofing: Falsifying location data.
Identity scrambling: Randomizing personal identifiers.""",

    610: """LSB steganography: Hiding data in least significant bits of images.
High-compression: Method for hiding data in the exact algorithm you compress a file with.
Low-detection: Techniques minimizing chances of discovery.
Invisible information: Data hidden within other files.""",

    620: """Audio encoding: Converting data into sound-based formats.
Encryption medium: Carrier used for hidden data.
Ultrasonic range: Frequencies above human hearing.
Human-audible range: Sounds detectable by people.""",

    630: """Multi-layer routing: Multiple encryption hops for anonymity.
Maximum layers: Highest number of encryption hops.
Stealth optimization: Balancing anonymity and performance.""",

    640: """Cryptographically secure: Using strong mathematical protection.
Anonymity shield: System protecting identity.
Decentralized approach: Distributed identity management.
Privacy-focused: Designed to maximize user privacy.""",

    670: """Cryptographically secure: Mathematically strong random generation.
Overwrite intensity: Degree of data destruction certainty.
High-entropy: Highly unpredictable data patterns.""",

    680: """Zero-filling: Writing zeros to all storage locations.
Multiple passes: Repeated overwriting for security.
Single pass: One-time overwrite process.""",

    700: """Digital anomalies: Irregularities in data patterns.
Forensic disruption: Preventing evidence reconstruction.
Temporal disruption: Time-based irregularities.
Spatial disruption: Location-based inconsistencies.""",

    710: """High-detail spoofing: Complex false location data.""",

    720: """Digital fingerprint: Unique identifying characteristics.
Algorithmic mutation: Systematic identity changes.
Random mutation: Unpredictable identity alterations.""",

    730: """High-compression steganography: Data hiding with size reduction.
File size optimization: Balancing hidden data and file characteristics.""",



    # 730
    #
    #
    #
    #
    #
    #
    740: """Forensic analysts: Professionals who investigate digital systems to uncover and analyze evidence.""",

    750: """Ultrasonic frequencies: Sound waves above human hearing range, often used for covert data transmission.
Data transmission: The process of sending digital information from one system to another.
Audio-based stealth: Using sound waves to covertly transfer data without detection.""",

    760: """Audio-encoded data: Information converted into sound waves for transmission.
Interception: The unauthorized capture of data during transmission.
Compromised communication: When a secure channel is breached or becomes vulnerable.""",

    770: """Onion routing: Layered encryption technique that anonymizes internet traffic by routing through multiple nodes.
Digital path: The route taken by data through networks and systems.
Tracking: Monitoring or tracing digital activities or identities.""",

    780: """Digital footprint: The trail of data left by a user's online activity.
Detection points: Vulnerable moments or locations where activities could be noticed.""",

    790: """Decentralized identity: Digital identity not controlled by any single authority.
Digital identification: Methods used to recognize or verify online identities.""",

    800: """Privacy-focused blockchain: Distributed ledger technology designed to protect user anonymity.
Digital identity: The online representation of an individual or entity.
Strategic anonymity: Carefully planned methods to maintain untraceability.""",

    820: """Selective data removal: Carefully choosing which information to delete.
Digital cleanup: Process of removing incriminating or sensitive data.""",

    830: """Targeted data removal: Focused deletion of specific information.
Critical evidence: Key digital proof that could compromise security.""",

    840: """Forensic red flags: Indicators that alert investigators to suspicious activity.
Extensive deletions: Large-scale removal of data that may appear conspicuous.""",

    850: """High-entropy overwrite: Data destruction method using random patterns to prevent recovery.
Digital obfuscation: Making data incomprehensible or difficult to interpret.
Indistinguishable noise: Data that appears random and contains no recoverable information.""",

    860: """Overwrite traces: Residual data that remains after deletion attempts.
Forensic recovery: The process of retrieving supposedly erased data.""",

    870: """Multiple pass overwrite: Repeated data writing to ensure complete destruction.
Data recovery: Retrieving information from damaged or erased storage.""",

    880: """Single pass overwrite: One-time data writing that may leave recoverable traces.
Recovery vectors: Potential methods to retrieve deleted information.
Digital cleanup vulnerabilities: Weaknesses in data removal processes.""",

    920: """Location data: Information about physical or digital positions.""",

    930: """Geo-spoofing: Falsifying geographic location data.""",

    940: """Minimal geo-spoofing: Basic attempts to falsify location data.
Location inconsistencies: Discrepancies in position information.""",

    950: """Algorithmic mutation: Systematic, programmed changes to digital identity.""",

    960: """Random mutation: Unpredictable changes to digital identity.""",
    #
    #
    #
    #
    #
    #
    #
    #
    1000: """Digital vigilante: A hacker who exposes wrongdoing, often operating outside legal boundaries.
Blue team cybersecurity: Defensive security professionals who protect systems from attacks.
Corporate network: A company's interconnected computer systems and digital infrastructure.
Cyber threat: Potential danger to digital systems from malicious actors.""",

    1010: """Wireshark: Network protocol analyzer for deep traffic inspection.
Netflow: Network protocol for collecting IP traffic information.
Traffic pattern analysis: Examining network data flows to identify anomalies.
Intrusion detection systems: Security tools that monitor for malicious activities.
Suspicious endpoints: Devices or systems showing signs of compromise.
Deep packet inspection: Analyzing the contents of network traffic in detail.
Threat actor: An individual or group responsible for cyber attacks.""",

    1020: """Network segmentation: Dividing networks to limit breach impacts.
Forensic capture: Preserving digital evidence for investigation.
Risk mitigation: Strategies to reduce potential damage from threats.
Compromised segments: Parts of a network that have been breached.""",

    1030: """Wireshark: Network protocol analyzer for deep traffic inspection.
Attack signatures: Unique patterns identifying specific cyber threats.
Advanced Persistent Threat (APT): Sophisticated, long-term cyber attack campaigns.
Threat hunting: Proactively searching for signs of compromise in networks.""",

    1040: """Netflow: Network protocol for collecting IP traffic information.
Geographical anomalies: Suspicious location-based network activities.
Botnet analysis: Studying networks of compromised devices controlled by attackers.""",

    1050: """Log analysis: Examining system records for security insights.
Artifact extraction: Collecting digital evidence from systems.
Forensic evidence: Digital information preserved for legal or investigative purposes.""",

    1060: """Preventive controls: Security measures to stop attacks before they occur.
Detection mechanisms: Systems that identify ongoing security breaches.""",

    1070: """Attack vectors: Methods used to exploit system vulnerabilities.
Intrusion timeline: Chronological reconstruction of a cyber attack.
Attack infrastructure: Technical resources used by threat actors.""",

    1080: """Counter-intrusion: Defensive measures against active attacks.
Honeypots: Decoy systems designed to lure and study attackers.
Deception grids: Networks of traps to mislead and detect intruders.""",

    1090: """Geo-tracking: Following digital activities across locations.
Infrastructure correlation: Linking related systems in an attack.""",

    1100: """Botnet: Network of infected devices controlled remotely.
Sink-holing: Redirecting malicious traffic to controlled servers.
Distributed takedown: Coordinated effort to disable attack networks.""",

    1110: """ELK stack: Elasticsearch, Logstash, Kibana for log analysis.
SIEM: Security Information and Event Management systems.
Log correlation: Connecting events across different system records.""",

    1120: """Malware reverse engineering: Analyzing malicious code to understand it.
Cyber espionage: Stealing secrets through digital means.
Forensic artifacts: Digital remnants of system activities.""",

    1130: """Firewall: Network security system monitoring incoming/outgoing traffic.
Endpoint protection: Security software for individual devices.
Network defenses: Measures to protect digital infrastructure.""",

    1140: """Anomaly detection: Identifying deviations from normal system behavior.
Behavioral analytics: Studying patterns of user/system activities.
Real-time monitoring: Continuous observation of system activities.""",

    1150: """Digital forensics: Scientific investigation of digital evidence.
Cyber investigation: Process of examining digital crimes.""",

    1160: """Command structures: Hierarchical organization of attack systems.
Digital landscape: The interconnected realm of online systems.""",

    1170: """Honeypot deception: Using bait systems to study attackers.
Cyber rabbit hole: Complex investigation leading to deeper discoveries.""",

    1180: """Defensive protocols: Established procedures for system protection.
Pyrrhic victory: Success achieved at excessive cost.""",

    1190: """Geopolitical cyber warfare: Digital attacks with international implications.
International nodes: Connection points across country borders.""",

    1200: """Threat networks: Interconnected systems used for malicious purposes.
Digital ecosystem: The complex web of interconnected technologies."""
}
