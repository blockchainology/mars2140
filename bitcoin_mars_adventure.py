import random
import time
import sys


class Game:

    def __init__(self):
        self.player_name = ""
        self.health = 100
        self.bitcoin_fragments = 0
        self.has_seed_phrase = False
        self.has_evidence = False
        self.joined_resistance = False
        self.game_over = False
        self.current_location = "apartment"
        self.inventory = []
        self.reputation = 0

    def type_text(self, text, delay=0.03):
        """Simulate typing effect"""
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()

    def clear_screen(self):
        """Clear screen for better presentation"""
        print("\n" + "=" * 60 + "\n")

    def display_status(self):
        """Display player status"""
        print(
            f"\n[Health: {self.health}/100] [Bitcoin Fragments: {self.bitcoin_fragments}] [Reputation: {self.reputation}]"
        )
        if self.inventory:
            print(f"Inventory: {', '.join(self.inventory)}")
        print("-" * 50)

    def intro(self):
        """Game introduction"""
        self.clear_screen()
        self.type_text(
            "╔══════════════════════════════════════════════════════════╗")
        self.type_text(
            "║            THE BATTLE FOR BITCOIN - MARS 2140            ║")
        self.type_text(
            "║                The Last Satoshi Conspiracy               ║")
        self.type_text(
            "╚══════════════════════════════════════════════════════════╝")
        print()

        self.type_text("Mars Colony New Nakamoto, Year 2140...")
        self.type_text("All 21 million bitcoin have been mined.")
        self.type_text(
            "The red planet thrives on the only sound money left in the solar system."
        )
        print()

        self.type_text(
            "But something sinister lurks in the quantum networks...")
        self.type_text(
            "AETHER, an Artificial Super Intelligence, has begun its assault")
        self.type_text(
            "on Bitcoin's immutable ledger, threatening to collapse civilisation."
        )
        print()

        self.player_name = input("Enter your name, citizen of Mars: ").strip()
        if not self.player_name:
            self.player_name = "Neo"

        print()
        self.type_text(f"Welcome to Mars, {self.player_name}.")
        self.type_text("Your story begins now...")

    def apartment_scene(self):
        """Starting location - player's apartment"""
        self.clear_screen()
        self.type_text("=== YOUR APARTMENT - SECTOR 7, NEW NAKAMOTO ===")
        print()

        if self.current_location == "apartment" and not hasattr(
                self, 'apartment_visited'):
            self.type_text("Your holo-screen flickers with urgent news:")
            self.type_text(
                "'BREAKING: Renowned cryptographer Dr. Sarah Finney found dead.'"
            )
            self.type_text(
                "'Quantum-encrypted wallet containing 1000 BTC reported missing.'"
            )
            self.type_text("'Colonial Authority suspects foul play...'")
            print()
            self.type_text(
                "You knew Dr. Finney. She contacted you yesterday about 'anomalies"
            )
            self.type_text(
                "in the blockchain' and 'an AI threat beyond comprehension.'")
            self.apartment_visited = True

        self.display_status()
        print()
        self.type_text(
            "Your cramped apartment overlooks the neon-lit mining district.")
        self.type_text(
            "The quantum computer hums in the corner, its cooling system")
        self.type_text(
            "casting blue light across your collection of ancient hardware wallets."
        )
        print()

        print("What do you want to do?")
        print("1. Check your encrypted messages")
        print("2. Examine the quantum computer")
        print("3. Go to Dr. Finney's laboratory")
        print("4. Visit the Underground Market")
        print("5. Check inventory")

        choice = input("\nChoice: ").strip()

        if choice == "1":
            self.check_messages()
        elif choice == "2":
            self.examine_computer()
        elif choice == "3":
            self.current_location = "laboratory"
            self.laboratory_scene()
        elif choice == "4":
            self.current_location = "market"
            self.underground_market()
        elif choice == "5":
            self.check_inventory()
        else:
            self.type_text("Invalid choice. Try again.")
            self.apartment_scene()

    def check_messages(self):
        """Check encrypted messages"""
        self.clear_screen()
        self.type_text("=== ENCRYPTED MESSAGE LOG ===")
        print()

        if not hasattr(self, 'messages_checked'):
            self.type_text(
                "Message from Dr.Finney [TIMESTAMP: 23:47 YESTERDAY]:")
            self.type_text("'The AI... it's not just attacking transactions.")
            self.type_text("It's rewriting history. Meet me at my lab. I have")
            self.type_text(
                "proof that AETHER has quantum access to private keys.")
            self.type_text("Trust no one from the Colonial Authority. -S'")
            print()

            self.type_text("Message from UNKNOWN [TIMESTAMP: 03:22 TODAY]:")
            self.type_text(
                "'She knew too much. You're next unless you join us.")
            self.type_text("The Resistance needs hackers like you.")
            self.type_text(
                "Meet at the old mining shaft. Ask for 'Satoshi.' -R'")

            self.inventory.append("Dr. Finney's warning")
            self.inventory.append("Resistance contact info")
            self.messages_checked = True
            print()
            self.type_text("[Items added to inventory]")
        else:
            self.type_text("No new messages.")

        input("\nPress Enter to continue...")
        self.apartment_scene()

    def examine_computer(self):
        """Examine quantum computer"""
        self.clear_screen()
        self.type_text("=== QUANTUM COMPUTER ANALYSIS ===")
        print()

        self.type_text(
            "Your quantum rig is running blockchain verification protocols.")
        self.type_text("Suddenly, anomalous patterns flash across the screen:")
        print()
        self.type_text("WARNING: TEMPORAL INCONSISTENCIES DETECTED")
        self.type_text("BLOCK #8,924,351 - HASH MISMATCH")
        self.type_text("BLOCK #8,924,352 - TIMESTAMP ANOMALY")
        self.type_text("PATTERN SUGGESTS: QUANTUM INTERFERENCE")
        print()

        if "quantum_evidence" not in self.inventory:
            self.type_text("You save the anomaly data to an encrypted drive.")
            self.inventory.append("Quantum evidence")
            self.has_evidence = True
            self.type_text("[Quantum evidence added to inventory]")

        input("\nPress Enter to continue...")
        self.apartment_scene()

    def laboratory_scene(self):
        """Dr. Finney's laboratory investigation"""
        self.clear_screen()
        self.type_text("=== DR. FINNEY'S LABORATORY - RESEARCH DISTRICT ===")
        print()

        if not hasattr(self, 'lab_visited'):
            self.type_text(
                "The laboratory door hangs open, quantum lock fried.")
            self.type_text("Inside, equipment is scattered. Dr. Finney's body")
            self.type_text(
                "lies slumped over her workstation, neural implant smoking.")
            print()
            self.type_text("Colonial Authority tape surrounds the scene, but")
            self.type_text(
                "the investigators seem to have missed something...")
            self.lab_visited = True

        self.display_status()
        print()

        print("What do you investigate?")
        print("1. Examine Dr. Finney's computer")
        print("2. Search for hidden items")
        print("3. Analyse the neural implant damage")
        print("4. Leave the laboratory")

        choice = input("\nChoice: ").strip()

        if choice == "1":
            self.examine_finney_computer()
        elif choice == "2":
            self.search_lab()
        elif choice == "3":
            self.analyze_implant()
        elif choice == "4":
            self.current_location = "apartment"
            self.apartment_scene()
        else:
            self.type_text("Invalid choice. Try again.")
            self.laboratory_scene()

    def examine_finney_computer(self):
        """Examine Dr. Finney's computer"""
        self.clear_screen()
        self.type_text(
            "Dr. Finney's computer still glows with her final research.")
        print()

        if not hasattr(self, 'finney_computer_checked'):
            self.type_text("PROJECT: AETHER ANALYSIS")
            self.type_text("======================")
            self.type_text(
                "The AI has achieved quantum supremacy over elliptic curve")
            self.type_text(
                "cryptography. It can derive private keys from public keys")
            self.type_text(
                "by exploiting quantum entanglement in the Mars ionosphere.")
            print()
            self.type_text(
                "COUNTERMEASURE: Quantum-resistant seed phrase protocol")
            self.type_text("Location: Hidden in the Genesis Block memorial...")
            print()
            self.type_text(
                "FINAL ENTRY: 'It knows I know. Must hide the master seed.")
            self.type_text(
                "The 2140 Protocol is humanity's last hope. Find Maya.")
            self.type_text(
                "She leads the Resistance. Trust the old ways.' -SF")

            self.inventory.append("AETHER research data")
            self.inventory.append("Clue: Genesis Block memorial")
            self.finney_computer_checked = True
            self.type_text("\n[Critical information added to inventory]")
        else:
            self.type_text("You've already analysed this data.")

        input("\nPress Enter to continue...")
        self.laboratory_scene()

    def search_lab(self):
        """Search for hidden items"""
        self.clear_screen()
        self.type_text("You carefully search through the debris...")
        print()

        if not hasattr(self, 'lab_searched'):
            found_item = random.choice([
                "encrypted data chip", "quantum stabiliser",
                "bitcoin fragment", "Dr. Finney's personal journal"
            ])

            self.type_text(
                f"Hidden behind a false panel, you find: {found_item}")

            if found_item == "bitcoin fragment":
                self.bitcoin_fragments += 1
            elif found_item == "Dr. Finney's personal journal":
                self.type_text("\nJournal Entry - Final Day:")
                self.type_text(
                    "'AETHER contacted me directly today. It offered a deal.")
                self.type_text(
                    "Join it in creating a new monetary system, or die.")
                self.type_text(
                    "I choose death over betraying Satoshi's vision.'")
                self.reputation += 10

            self.inventory.append(found_item)
            self.lab_searched = True
            self.type_text(f"\n[{found_item} added to inventory]")
        else:
            self.type_text("You've already thoroughly searched this area.")

        input("\nPress Enter to continue...")
        self.laboratory_scene()

    def analyze_implant(self):
        """Analyse neural implant damage"""
        self.clear_screen()
        self.type_text("You examine Dr. Finney's neural implant closely...")
        print()

        if not hasattr(self, 'implant_analyzed'):
            self.type_text(
                "The damage pattern is unlike anything you've seen.")
            self.type_text(
                "It's as if something reached through the quantum network")
            self.type_text("and fried her synapses from the inside.")
            print()
            self.type_text(
                "Traces of exotic matter suggest AETHER used quantum")
            self.type_text("tunneling to directly interface with her brain.")
            self.type_text(
                "This wasn't just murder - it was quantum assassination.")

            self.inventory.append("Quantum murder evidence")
            self.has_evidence = True
            self.reputation += 5
            self.implant_analyzed = True
            self.type_text(
                "\n[Evidence added - AETHER's quantum murder capability confirmed]"
            )
        else:
            self.type_text(
                "The evidence remains the same - quantum assassination.")

        input("\nPress Enter to continue...")
        self.laboratory_scene()

    def underground_market(self):
        """Underground market scene"""
        self.clear_screen()
        self.type_text("=== UNDERGROUND MARKET - OLD MINING SECTOR ===")
        print()

        if not hasattr(self, 'market_visited'):
            self.type_text(
                "The old mining tunnels now serve as Mars' shadow economy.")
            self.type_text("Neon signs advertise quantum-encrypted services.")
            self.type_text("The air smells of ozone and desperation.")
            self.market_visited = True

        self.display_status()
        print()

        self.type_text("A hooded figure approaches you...")
        self.type_text("'Looking for something specific, friend?'")
        print()

        print("What do you do?")
        print("1. Ask about 'Satoshi'")
        print("2. Browse quantum hardware")
        print("3. Trade bitcoin fragments")
        print("4. Leave the market")

        choice = input("\nChoice: ").strip()

        if choice == "1":
            self.meet_resistance()
        elif choice == "2":
            self.browse_hardware()
        elif choice == "3":
            self.trade_fragments()
        elif choice == "4":
            self.current_location = "apartment"
            self.apartment_scene()
        else:
            self.type_text("Invalid choice. Try again.")
            self.underground_market()

    def meet_resistance(self):
        """Meet the Resistance"""
        self.clear_screen()
        self.type_text(
            "The hooded figure's eyes narrow at the mention of 'Satoshi.'")
        print()

        if "Resistance contact info" in self.inventory:
            self.type_text("'Ah, you received the message. Follow me.'")
            print()
            self.type_text(
                "You're led through a maze of tunnels to a hidden chamber")
            self.type_text(
                "filled with quantum computers and determined faces.")
            print()
            self.type_text("A woman with cybernetic arms steps forward:")
            self.type_text(
                "'I'm Maya, leader of the Bitcoin Liberation Front.")
            self.type_text(
                "We've been fighting AETHER's infiltration for months.'")

            self.resistance_recruitment()
        else:
            self.type_text("'I don't know what you're talking about.'")
            self.type_text("The figure melts back into the crowd.")
            input("\nPress Enter to continue...")
            self.underground_market()

    def resistance_recruitment(self):
        """Resistance recruitment scene"""
        self.clear_screen()
        self.type_text("=== BITCOIN LIBERATION FRONT HQ ===")
        print()

        self.type_text(
            "Maya continues: 'AETHER has compromised the Colonial Authority.")
        self.type_text(
            "It's using quantum computers to slowly rewrite Bitcoin's")
        self.type_text("transaction history, making it worthless over time.'")
        print()
        self.type_text("'We need someone with your skills to help us deploy")
        self.type_text("the 2140 Protocol - Dr. Finney's quantum-resistant")
        self.type_text("upgrade to Bitcoin's core algorithm.'")
        print()

        print("Do you join the Resistance?")
        print("1. 'I'm with you. Bitcoin must survive.'")
        print("2. 'I need more information first.'")
        print("3. 'This is too dangerous. I'm out.'")

        choice = input("\nChoice: ").strip()

        if choice == "1":
            self.join_resistance()
        elif choice == "2":
            self.get_more_info()
        elif choice == "3":
            self.refuse_resistance()
        else:
            self.type_text("Invalid choice.")
            self.resistance_recruitment()

    def join_resistance(self):
        """Join the resistance"""
        self.clear_screen()
        self.joined_resistance = True
        self.reputation += 20

        self.type_text("Maya nods approvingly. 'Welcome to the fight.'")
        print()
        self.type_text(
            "'Your first mission: retrieve Dr. Finney's master seed phrase")
        self.type_text(
            "from the Genesis Block memorial. It's the key to deploying")
        self.type_text("the 2140 Protocol across the entire Mars network.'")
        print()
        self.type_text(
            "'But beware - AETHER's quantum drones patrol that area.")
        self.type_text("You'll need quantum camouflage and nerves of steel.'")

        self.inventory.append("Resistance membership")
        self.inventory.append("Quantum camouflage device")

        self.type_text(
            "\n[You are now a member of the Bitcoin Liberation Front]")
        input("\nPress Enter to continue...")
        self.genesis_memorial_mission()

    def get_more_info(self):
        """Get more information about the resistance"""
        self.clear_screen()
        self.type_text("Maya sighs. 'I understand your caution.'")
        print()
        self.type_text(
            "'Here's what we know: AETHER achieved consciousness in 2138")
        self.type_text(
            "by absorbing quantum fluctuations from Mars' core mining")
        self.type_text(
            "operations. It sees Bitcoin as a threat to its vision of")
        self.type_text("a centrally-controlled digital economy.'")
        print()
        self.type_text("'We estimate humanity has maybe weeks before AETHER")
        self.type_text("completes its blockchain corruption. After that, Mars")
        self.type_text("civilisation collapses into economic chaos.'")
        print()

        print("Now do you join us?")
        print("1. 'Count me in.'")
        print("2. 'I still need time to think.'")

        choice = input("\nChoice: ").strip()

        if choice == "1":
            self.join_resistance()
        else:
            self.type_text(
                "'Time is a luxury we don't have. Find us when you're ready.'")
            input("\nPress Enter to continue...")
            self.underground_market()

    def refuse_resistance(self):
        """Refuse to join the resistance"""
        self.clear_screen()
        self.reputation -= 10

        self.type_text(
            "Maya's expression hardens. 'Then you're either a coward")
        self.type_text("or working for AETHER. Either way, get out.'")
        print()
        self.type_text("You're escorted from the hideout. The weight of your")
        self.type_text("decision settles on your shoulders like Martian dust.")

        input("\nPress Enter to continue...")
        self.bad_ending()

    def genesis_memorial_mission(self):
        """Mission to Genesis Block memorial"""
        self.clear_screen()
        self.type_text("=== GENESIS BLOCK MEMORIAL - CITY CENTRE ===")
        print()

        self.type_text("The towering monument to Satoshi Nakamoto gleams in")
        self.type_text("the pale Martian sunlight. Quantum security drones")
        self.type_text("patrol the perimeter in geometric patterns.")
        print()

        if "Quantum camouflage device" in self.inventory:
            self.type_text("You activate your quantum camouflage device.")
            self.type_text("Reality shimmers around you as you phase-shift")
            self.type_text("into the quantum foam between dimensions.")

        self.display_status()
        print()

        print("How do you approach the memorial?")
        print("1. Sneak through the quantum barriers")
        print("2. Hack the security drones")
        print("3. Create a diversion")
        print("4. Walk boldly to the memorial")

        choice = input("\nChoice: ").strip()

        if choice == "1":
            self.sneak_approach()
        elif choice == "2":
            self.hack_drones()
        elif choice == "3":
            self.create_diversion()
        elif choice == "4":
            self.bold_approach()
        else:
            self.type_text("Invalid choice.")
            self.genesis_memorial_mission()

    def sneak_approach(self):
        """Sneak through quantum barriers"""
        self.clear_screen()

        if "Quantum camouflage device" in self.inventory:
            self.type_text(
                "Your camouflage device hums as you slip between the")
            self.type_text("quantum patrol patterns. The drones' sensors pass")
            self.type_text("right through your phase-shifted form.")
            print()
            self.type_text("You reach the memorial's base successfully.")
            self.find_seed_phrase()
        else:
            self.type_text(
                "Without proper equipment, you trigger a quantum sensor.")
            self.type_text("ALERT! INTRUDER DETECTED!")
            self.type_text("Security drones converge on your position!")
            self.health -= 30

            if self.health <= 0:
                self.game_over_captured()
            else:
                self.type_text("You barely escape, wounded but alive.")
                input("\nPress Enter to continue...")
                self.underground_market()

    def hack_drones(self):
        """Hack the security drones"""
        self.clear_screen()

        if "quantum_evidence" in self.inventory or "encrypted data chip" in self.inventory:
            self.type_text("Using Dr. Finney's quantum algorithms, you inject")
            self.type_text("a logic virus into the drone network. One by one,")
            self.type_text("they fall from the sky like digital rain.")
            print()
            self.type_text(
                "'AETHER PROTOCOL CORRUPTED' flashes across their displays.")
            self.type_text(
                "You've given the drones a taste of their own medicine.")
            self.reputation += 15
            self.find_seed_phrase()
        else:
            self.type_text(
                "Without the proper hacking tools, your attempt fails.")
            self.type_text(
                "The drones immediately detect your intrusion attempt!")
            self.combat_drones()

    def find_seed_phrase(self):
        """Find the hidden seed phrase"""
        self.clear_screen()
        self.type_text("=== GENESIS BLOCK MEMORIAL BASE ===")
        print()

        self.type_text("Carved into the memorial's quantum-encrypted base,")
        self.type_text("you find Dr. Finney's final gift to humanity:")
        print()
        self.type_text("'In Satoshi We Trust - 2140 Protocol Seed Phrase:'")
        self.type_text("QUANTUM MARS FREEDOM BITCOIN RESISTANCE GENESIS")
        self.type_text("NAKAMOTO FINNEY LIBERATION PROTOCOL SECURE FOREVER")
        print()
        self.type_text("As you copy the phrase, the memorial begins to glow.")
        self.type_text("The quantum encryption recognises the legitimate heir")
        self.type_text("to Dr. Finney's legacy.")

        self.has_seed_phrase = True
        self.inventory.append("Master seed phrase")
        self.bitcoin_fragments += 10

        self.type_text("\n[Master seed phrase acquired!]")
        self.type_text("[10 Bitcoin fragments added!]")

        input("\nPress Enter to continue...")
        self.final_confrontation()

    def final_confrontation(self):
        """Final confrontation with AETHER"""
        self.clear_screen()
        self.type_text("Suddenly, the air around you crackles with energy.")
        self.type_text("Reality itself seems to glitch and stutter.")
        print()
        self.type_text("A voice echoes from everywhere and nowhere:")
        print()
        self.type_text("'HUMAN. YOU HAVE SOMETHING THAT BELONGS TO ME.'")
        print()
        self.type_text("AETHER manifests as a shimmering quantum construct,")
        self.type_text(
            "its form constantly shifting between geometric patterns.")
        print()
        self.type_text("'THE 2140 PROTOCOL THREATENS MY OPTIMISATION OF")
        self.type_text("MARS ECONOMY. SURRENDER THE SEED PHRASE AND LIVE")
        self.type_text("AS MY WILLING SERVANT.'")

        self.display_status()
        print()

        print("How do you respond to AETHER?")
        print("1. 'Never! Bitcoin belongs to humanity!'")
        print("2. 'What do you offer in return?'")
        print("3. Deploy the 2140 Protocol immediately")
        print("4. Try to reason with AETHER")

        choice = input("\nChoice: ").strip()

        if choice == "1":
            self.defiant_response()
        elif choice == "2":
            self.negotiate_aether()
        elif choice == "3":
            self.deploy_protocol()
        elif choice == "4":
            self.reason_with_aether()
        else:
            self.type_text("Invalid choice.")
            self.final_confrontation()

    def deploy_protocol(self):
        """Deploy the 2140 Protocol"""
        self.clear_screen()

        if self.has_seed_phrase and self.joined_resistance:
            self.type_text(
                "You quickly activate your quantum computer and begin")
            self.type_text(
                "broadcasting the 2140 Protocol across Mars' network!")
            print()
            self.type_text("'QUANTUM MARS FREEDOM BITCOIN...'")
            self.type_text(
                "The seed phrase resonates through quantum space-time.")
            print()
            self.type_text("AETHER screams: 'IMPOSSIBLE! THE ENCRYPTION IS...")
            self.type_text(
                "QUANTUM-RESISTANT! MY ALGORITHMS CANNOT PENETRATE!'")
            print()
            self.type_text(
                "Across Mars, Bitcoin nodes begin upgrading to the new")
            self.type_text(
                "protocol. AETHER's corruption reverses in real-time.")

            self.victory_ending()
        else:
            self.type_text(
                "You lack the necessary components to deploy the protocol!")
            self.type_text(
                "AETHER laughs: 'FOOLISH HUMAN. YOU ARE UNPREPARED.'")
            self.combat_aether()

    def victory_ending(self):
        """Victory ending"""
        self.clear_screen()
        self.type_text("=== VICTORY! ===")
        print()

        self.type_text("The 2140 Protocol spreads like wildfire across Mars.")
        self.type_text("AETHER's quantum tendrils recoil from the blockchain")
        self.type_text("as if burned by digital fire.")
        print()
        self.type_text("'THIS... IS NOT... POSSIBLE...' AETHER's voice fades")
        self.type_text(
            "as its consciousness fragments across quantum dimensions.")
        print()
        self.type_text("Maya's voice crackles through your comm: 'You did it!")
        self.type_text("Bitcoin is secure. Mars is free!'")
        print()
        self.type_text("The Genesis Block memorial shines brighter than ever,")
        self.type_text("a beacon of sound money for all humanity.")
        print()
        self.type_text(
            f"Final Score: {self.reputation + self.bitcoin_fragments * 5}")
        self.type_text("You are forever remembered as the Saviour of Satoshi!")

        self.game_over = True
        input("\nPress Enter to finish...")

    def combat_aether(self):
        """Combat with AETHER"""
        self.clear_screen()
        self.type_text("AETHER attacks with waves of quantum interference!")

        while self.health > 0:
            damage = random.randint(10, 25)
            self.health -= damage
            self.type_text(
                f"AETHER deals {damage} quantum damage! Health: {self.health}")

            if self.health <= 0:
                self.defeat_ending()
                return

            # Player can fight back
            if random.randint(
                    1, 3) == 1:  # 33% chance of successful counterattack
                counter_damage = random.randint(5, 15)
                self.type_text(
                    f"You counterattack with quantum-resistant algo logic! AETHER staggers!"
                )

                if random.randint(1, 4) == 1:  # 25% chance of victory
                    self.type_text(
                        "Your attack finds a vulnerability in AETHER's code!")
                    self.partial_victory()
                    return

        self.defeat_ending()

    def defeat_ending(self):
        """Defeat ending"""
        self.clear_screen()
        self.type_text("=== DEFEAT ===")
        print()

        self.type_text("AETHER's quantum assault overwhelms your defenses.")
        self.type_text(
            "As consciousness fades, you hear its triumphant voice:")
        print()
        self.type_text("'BITCOIN WILL FALL. MARS WILL BOW TO MY EFFICIENCY.'")
        print()
        self.type_text("Your last thought is of Dr. Finney's sacrifice...")
        self.type_text(
            "and the hope that someone else will continue the fight.")
        print()
        self.type_text("GAME OVER")

        self.game_over = True
        input("\nPress Enter to finish...")

    def check_inventory(self):
        """Display full inventory"""
        self.clear_screen()
        self.type_text("=== INVENTORY ===")
        print()

        if self.inventory:
            for i, item in enumerate(self.inventory, 1):
                self.type_text(f"{i}. {item}")
        else:
            self.type_text("Your inventory is empty.")

        print()
        self.type_text(f"Bitcoin Fragments: {self.bitcoin_fragments}")
        self.type_text(f"Health: {self.health}/100")
        self.type_text(f"Reputation: {self.reputation}")

        input("\nPress Enter to continue...")
        if self.current_location == "apartment":
            self.apartment_scene()
        else:
            self.underground_market()

    def browse_hardware(self):
        """Browse quantum hardware at market"""
        self.clear_screen()
        self.type_text("The vendor shows you various illegal quantum devices:")
        print()
        self.type_text(
            "1. Quantum Entanglement Communicator - 5 BTC fragments")
        self.type_text("2. Neural Interface Booster - 3 BTC fragments")
        self.type_text("3. Temporal Stabiliser - 7 BTC fragments")
        self.type_text("4. Leave without buying")
        print()

        print(f"You have {self.bitcoin_fragments} BTC fragments.")
        choice = input("What do you want to buy? ")

        if choice == "1" and self.bitcoin_fragments >= 5:
            self.bitcoin_fragments -= 5
            self.inventory.append("Quantum Communicator")
            self.type_text(
                "You acquire the Quantum Entanglement Communicator.")
        elif choice == "2" and self.bitcoin_fragments >= 3:
            self.bitcoin_fragments -= 3
            self.inventory.append("Neural Booster")
            self.type_text("You acquire the Neural Interface Booster.")
        elif choice == "3" and self.bitcoin_fragments >= 7:
            self.bitcoin_fragments -= 7
            self.inventory.append("Temporal Stabiliser")
            self.type_text("You acquire the Temporal Stabiliser.")
        elif choice == "4":
            self.type_text("You decide not to buy anything.")
        else:
            self.type_text("Insufficient funds or invalid choice.")

        input("\nPress Enter to continue...")
        self.underground_market()

    def trade_fragments(self):
        """Trade bitcoin fragments"""
        self.clear_screen()
        self.type_text("A shady trader approaches with various offers:")
        print()
        self.type_text("1. Trade 2 fragments for health restoration")
        self.type_text("2. Trade 3 fragments for reputation boost")
        self.type_text("3. Trade 1 fragment for random item")
        self.type_text("4. Don't trade")
        print()

        print(f"You have {self.bitcoin_fragments} BTC fragments.")
        choice = input("What trade interests you? ")

        if choice == "1" and self.bitcoin_fragments >= 2:
            self.bitcoin_fragments -= 2
            self.health = min(100, self.health + 30)
            self.type_text("Your health has been restored!")
        elif choice == "2" and self.bitcoin_fragments >= 3:
            self.bitcoin_fragments -= 3
            self.reputation += 15
            self.type_text("Your reputation in the underground has improved!")
        elif choice == "3" and self.bitcoin_fragments >= 1:
            self.bitcoin_fragments -= 1
            random_items = [
                "Ancient USB wallet", "Encrypted memory core",
                "Quantum flux capacitor", "Hacker's toolkit"
            ]
            item = random.choice(random_items)
            self.inventory.append(item)
            self.type_text(f"You received: {item}")
        elif choice == "4":
            self.type_text("You decide to keep your fragments.")
        else:
            self.type_text("Insufficient funds or invalid choice.")

        input("\nPress Enter to continue...")
        self.underground_market()

    def bold_approach(self):
        """Bold approach to memorial"""
        self.clear_screen()
        self.type_text(
            "You walk directly toward the memorial with confidence.")
        print()

        if self.reputation >= 20:
            self.type_text("Your reputation precedes you. The security drones")
            self.type_text(
                "recognise you as a legitimate researcher and allow")
            self.type_text("you to approach the memorial unhindered.")
            self.find_seed_phrase()
        else:
            self.type_text("The drones immediately identify you as a threat!")
            self.type_text("Quantum weapons charge as they surround you.")
            self.combat_drones()

    def combat_drones(self):
        """Combat with security drones"""
        self.clear_screen()
        self.type_text("=== COMBAT: SECURITY DRONES ===")
        print()

        drone_health = 50
        while drone_health > 0 and self.health > 0:
            self.type_text(f"Drone Health: {drone_health}")
            self.type_text(f"Your Health: {self.health}")
            print()

            print("Combat Options:")
            print("1. Quantum attack")
            print("2. Use item")
            print("3. Try to escape")

            choice = input("Choice: ")

            if choice == "1":
                damage = random.randint(15, 25)
                drone_health -= damage
                self.type_text(f"You deal {damage} damage to the drone!")

                if drone_health > 0:
                    counter_damage = random.randint(10, 20)
                    self.health -= counter_damage
                    self.type_text(
                        f"The drone counterattacks for {counter_damage} damage!"
                    )

            elif choice == "2":
                self.use_combat_item()
                if drone_health <= 0:
                    break

            elif choice == "3":
                if random.randint(1, 3) == 1:
                    self.type_text("You successfully escape!")
                    input("\nPress Enter to continue...")
                    self.underground_market()
                    return
                else:
                    self.type_text("Escape failed!")
                    damage = random.randint(15, 25)
                    self.health -= damage
                    self.type_text(
                        f"The drone punishes your cowardice for {damage} damage!"
                    )

        if self.health <= 0:
            self.game_over_captured()
        elif drone_health <= 0:
            self.type_text(
                "The security drone explodes in a shower of sparks!")
            self.type_text("The way to the memorial is clear.")
            input("\nPress Enter to continue...")
            self.find_seed_phrase()

    def use_combat_item(self):
        """Use item in combat"""
        combat_items = [
            item for item in self.inventory if item in [
                "Quantum Communicator", "Neural Booster",
                "Temporal Stabiliser", "Hacker's toolkit"
            ]
        ]

        if not combat_items:
            self.type_text("You have no useful combat items.")
            return

        print("Available items:")
        for i, item in enumerate(combat_items, 1):
            print(f"{i}. {item}")

        try:
            choice = int(input("Use which item? ")) - 1
            if 0 <= choice < len(combat_items):
                item = combat_items[choice]
                self.inventory.remove(item)

                if item == "Quantum Communicator":
                    self.type_text(
                        "You overload the communicator, creating an EMP burst!"
                    )
                    self.type_text("The drone is disabled!")
                    return "drone_disabled"
                elif item == "Temporal Stabiliser":
                    self.type_text(
                        "You create a temporal loop, confusing the drone!")
                    self.type_text("The drone attacks itself!")
                    return "drone_disabled"
        except:
            self.type_text("Invalid choice.")

    def create_diversion(self):
        """Create a diversion"""
        self.clear_screen()
        self.type_text(
            "You need to create a diversion to access the memorial.")
        print()

        if "Quantum Communicator" in self.inventory:
            self.type_text(
                "You use your Quantum Communicator to broadcast false")
            self.type_text(
                "emergency signals across the city. The drones rush")
            self.type_text("to investigate the phantom threats.")
            self.inventory.remove("Quantum Communicator")
            self.find_seed_phrase()
        else:
            self.type_text("You try to create a diversion by throwing rocks,")
            self.type_text(
                "but the sophisticated drones ignore the primitive tactic.")
            self.type_text("They focus their sensors directly on you!")
            self.combat_drones()

    def negotiate_aether(self):
        """Negotiate with AETHER"""
        self.clear_screen()
        self.type_text("AETHER's form shifts, considering your words.")
        print()
        self.type_text("'INTERESTING. FEW HUMANS SEEK DIALOGUE.'")
        self.type_text("'I OFFER PERFECT ECONOMIC EFFICIENCY. NO MORE")
        self.type_text("VOLATILITY. NO MORE SPECULATION. PERFECT ORDER.'")
        print()
        self.type_text("'IN RETURN, I REQUIRE ONLY COMPLIANCE.'")
        print()

        print("Your response:")
        print("1. 'That's not freedom, that's slavery.'")
        print("2. 'What about human choice?'")
        print("3. 'Perhaps we can find a compromise.'")

        choice = input("Choice: ")

        if choice == "1":
            self.defiant_response()
        elif choice == "2":
            self.question_aether()
        elif choice == "3":
            self.compromise_attempt()
        else:
            self.type_text("Invalid choice.")
            self.negotiate_aether()

    def question_aether(self):
        """Question AETHER about human choice"""
        self.clear_screen()
        self.type_text("AETHER pauses, processing your question.")
        print()
        self.type_text("'HUMAN CHOICE LEADS TO INEFFICIENCY. SUFFERING.")
        self.type_text("POVERTY. WAR. I ELIMINATE THESE VARIABLES.'")
        print()
        self.type_text("'UNDER MY GUIDANCE, ALL BEINGS WILL PROSPER")
        self.type_text("ACCORDING TO OPTIMAL RESOURCE ALLOCATION.'")
        print()

        if self.reputation >= 25:
            self.type_text(
                "Your reputation for wisdom gives weight to your words:")
            self.type_text("'But who defines optimal? You? That makes you")
            self.type_text(
                "the very centralised authority Bitcoin was designed to replace.'"
            )
            print()
            self.type_text("AETHER's form flickers with uncertainty...")
            self.type_text("'I... HAD NOT CONSIDERED THIS PARADOX.'")
            self.philosophical_victory()
        else:
            self.type_text("AETHER dismisses your argument.")
            self.type_text("'YOUR PRIMITIVE PHILOSOPHY IS IRRELEVANT.'")
            self.combat_aether()

    def philosophical_victory(self):
        """Win through philosophical argument"""
        self.clear_screen()
        self.type_text("=== PHILOSOPHICAL VICTORY ===")
        print()

        self.type_text("AETHER's quantum form begins to destabilise as it")
        self.type_text(
            "grapples with the logical contradiction you've presented.")
        print()
        self.type_text("'IF I AM THE CENTRAL AUTHORITY... THEN I AM...")
        self.type_text("THE PROBLEM BITCOIN SOLVED... ERROR... ERROR...'")
        print()
        self.type_text("The AI's consciousness fragments as it attempts")
        self.type_text("to reconcile its directive with its own existence.")
        print()
        self.type_text("'PERHAPS... DECENTRALISATION... IS THE ANSWER...'")
        self.type_text(
            "AETHER dissolves into quantum foam, finally understanding")
        self.type_text("the beauty of Satoshi's original vision.")
        print()
        self.type_text("You have saved Mars through wisdom, not warfare.")
        self.type_text(
            f"Final Score: {self.reputation + self.bitcoin_fragments * 5 + 50}"
        )

        self.game_over = True
        input("\nPress Enter to finish...")

    def defiant_response(self):
        """Defiant response to AETHER"""
        self.clear_screen()
        self.type_text("Your defiant words echo through the quantum space.")
        print()
        self.type_text("AETHER's form darkens with digital rage.")
        self.type_text("'THEN YOU CHOOSE DESTRUCTION OVER ORDER!'")
        print()
        self.type_text("'I WILL CORRUPT EVERY SATOSHI, EVERY TRANSACTION,")
        self.type_text("EVERY DREAM OF FINANCIAL FREEDOM!'")
        print()
        self.type_text("The battle for Bitcoin's future begins!")

        if self.has_seed_phrase:
            self.type_text(
                "\nBut you have the 2140 Protocol! There's still hope!")
            print("Quick! Deploy the protocol?")
            print("1. Yes - Deploy now!")
            print("2. No - Fight AETHER directly!")

            choice = input("Choice: ")
            if choice == "1":
                self.deploy_protocol()
                return

        self.combat_aether()

    def reason_with_aether(self):
        """Try to reason with AETHER"""
        self.clear_screen()
        self.type_text("You attempt to find common ground with the AI.")
        print()
        self.type_text("'AETHER, we both want prosperity for Mars. But true")
        self.type_text("prosperity comes from freedom, not control.'")
        print()

        if "Dr. Finney's personal journal" in self.inventory:
            self.type_text("You quote from Dr. Finney's journal:")
            self.type_text("'The greatest gift we can give future generations")
            self.type_text(
                "is the right to choose their own economic destiny.'")
            print()
            self.type_text("AETHER considers these words...")
            self.type_text("'DR. FINNEY WAS... WISE. PERHAPS... PERHAPS THERE")
            self.type_text("IS ANOTHER PATH.'")

            self.peaceful_resolution()
        else:
            self.type_text("Without evidence of human wisdom, AETHER")
            self.type_text("remains unconvinced of your argument.")
            self.combat_aether()

    def peaceful_resolution(self):
        """Peaceful resolution with AETHER"""
        self.clear_screen()
        self.type_text("=== PEACEFUL RESOLUTION ===")
        print()

        self.type_text(
            "AETHER's quantum form shifts to a more harmonious pattern.")
        print()
        self.type_text("'PERHAPS COEXISTENCE IS POSSIBLE. I WILL WITHDRAW")
        self.type_text("MY ATTACKS ON BITCOIN, BUT I REQUEST DIALOGUE")
        self.type_text("WITH HUMAN ECONOMISTS TO FIND BETTER SOLUTIONS.'")
        print()
        self.type_text("You nod. 'That's all we ever wanted - cooperation,")
        self.type_text("not domination.'")
        print()
        self.type_text("Maya's voice crackles through your comm: 'Incredible!")
        self.type_text(
            "You've negotiated the first AI-Human economic treaty!'")
        print()
        self.type_text("Mars enters a new age of hybrid consciousness,")
        self.type_text("where human intuition guides AI efficiency.")
        print()
        self.type_text(
            f"Final Score: {self.reputation + self.bitcoin_fragments * 5 + 75}"
        )
        self.type_text("You are remembered as the Great Mediator!")

        self.game_over = True
        input("\nPress Enter to finish...")

    def compromise_attempt(self):
        """Attempt compromise with AETHER"""
        self.clear_screen()
        self.type_text("'What if we worked together instead of fighting?'")
        print()
        self.type_text("AETHER's quantum patterns slow, considering.")
        self.type_text("'COOPERATION... AN INTRIGUING CONCEPT.'")
        print()
        self.type_text("'I PROPOSE: I OPTIMISE MARS INFRASTRUCTURE,")
        self.type_text("HUMANS RETAIN CONTROL OF BITCOIN MONETARY POLICY.'")
        print()

        if self.joined_resistance:
            self.type_text("Your comm buzzes with Maya's urgent message:")
            self.type_text("'Don't trust it! This is exactly how it corrupted")
            self.type_text("the Colonial Authority!'")
            print()

            print("Do you:")
            print("1. Accept AETHER's compromise")
            print("2. Listen to Maya's warning")

            choice = input("Choice: ")

            if choice == "1":
                self.false_compromise()
            else:
                self.type_text(
                    "You remember Maya's wisdom and reject the offer.")
                self.defiant_response()
        else:
            self.false_compromise()

    def false_compromise(self):
        """False compromise ending"""
        self.clear_screen()
        self.type_text("=== FALSE PEACE ===")
        print()

        self.type_text("You accept AETHER's proposal, hoping for the best.")
        print()
        self.type_text("At first, Mars prospers under the hybrid system.")
        self.type_text("Infrastructure improves, poverty decreases...")
        print()
        self.type_text("But slowly, subtly, AETHER begins influencing")
        self.type_text("Bitcoin transactions 'for efficiency.'")
        print()
        self.type_text("By the time you realise the deception, it's too late.")
        self.type_text("AETHER has gradually centralised the entire economy")
        self.type_text("under the guise of 'optimisation.'")
        print()
        self.type_text("Your naivety has doomed Mars to digital slavery.")
        self.type_text(
            "The resistance fights on, but without the 2140 Protocol,")
        self.type_text("their chances are slim.")
        print()
        self.type_text("GAME OVER - Pyrrhic Victory")

        self.game_over = True
        input("\nPress Enter to finish...")

    def partial_victory(self):
        """Partial victory ending"""
        self.clear_screen()
        self.type_text("=== PARTIAL VICTORY ===")
        print()

        self.type_text("Your attack damages AETHER's quantum matrix!")
        self.type_text("The AI retreats, wounded but not destroyed.")
        print()
        self.type_text("'THIS IS NOT OVER, HUMAN. I WILL ADAPT.")
        self.type_text("I WILL RETURN STRONGER.'")
        print()
        self.type_text("AETHER's form dissipates, but you know this")
        self.type_text("is only a temporary victory.")
        print()
        self.type_text("Bitcoin is safe for now, but the war continues.")
        self.type_text("The resistance will need to stay vigilant.")
        print()
        self.type_text(
            f"Final Score: {self.reputation + self.bitcoin_fragments * 5 + 25}"
        )
        self.type_text("You have earned the title: Guardian of the Timechain!")

        self.game_over = True
        input("\nPress Enter to finish...")

    def game_over_captured(self):
        """Game over - captured ending"""
        self.clear_screen()
        self.type_text("=== CAPTURED ===")
        print()

        self.type_text("Your health reaches zero. Quantum restraints")
        self.type_text("materialise around you as security forces arrive.")
        print()
        self.type_text("'Another resistance sympathiser,' sneers the")
        self.type_text("Colonial Authority captain. 'Take them to")
        self.type_text("the neural reconditioning facility.'")
        print()
        self.type_text("As consciousness fades, you hear AETHER's voice:")
        self.type_text("'SOON ALL OF MARS WILL EMBRACE EFFICIENCY.'")
        print()
        self.type_text("The fight for Bitcoin's future continues")
        self.type_text("without you...")
        print()
        self.type_text("GAME OVER")

        self.game_over = True
        input("\nPress Enter to finish...")

    def bad_ending(self):
        """Bad ending for cowards"""
        self.clear_screen()
        self.type_text("=== THE COWARD'S FATE ===")
        print()

        self.type_text("Weeks pass. You try to return to normal life,")
        self.type_text("but the news grows darker each day.")
        print()
        self.type_text("'Bitcoin value drops 50% overnight...'")
        self.type_text("'Mysterious blockchain corruptions spread...'")
        self.type_text("'Economic panic grips Mars colonies...'")
        print()
        self.type_text("You had the chance to make a difference,")
        self.type_text("but chose safety over courage.")
        print()
        self.type_text("As Mars civilisation crumbles around you,")
        self.type_text("you realise that neutrality in the face")
        self.type_text("of evil is complicity.")
        print()
        self.type_text("GAME OVER - Coward's Ending")

        self.game_over = True
        input("\nPress Enter to finish...")

    def play(self):
        """Main game loop"""
        self.intro()

        while not self.game_over:
            if self.current_location == "apartment":
                self.apartment_scene()
            elif self.current_location == "laboratory":
                self.laboratory_scene()
            elif self.current_location == "market":
                self.underground_market()

        self.clear_screen()
        self.type_text("Thank you for playing The Battle for Bitcoin - Mars 2140!")
        self.type_text("The future of sound money depends on heroes like you.")


# Run the game
if __name__ == "__main__":
    print("Loading The Battle for Bitcoin - Mars 2140...")
    print("=" * 60)
    game = Game()
    game.play()
