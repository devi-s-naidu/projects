print("Testing Scapy installation...")

try:
    try:
        import scapy
        print("✓ Scapy imported as 'scapy'")
    except ImportError:
        print("✗ Failed to import 'scapy'")
    
    try:
        import scapy.all
        print("✓ Scapy imported as 'scapy.all'")
    except ImportError:
        print("✗ Failed to import 'scapy.all'")
    
    try:
        from scapy.all import *
        print("✓ Imported all from 'scapy.all'")
    except ImportError:
        print("✗ Failed to import from 'scapy.all'")
    
    try:
        import pkg_resources
        version = pkg_resources.get_distribution("scapy").version
        print(f"✓ Scapy version: {version}")
    except:
        print("✓ Scapy version unknown")
        
    print("\nScapy test completed successfully!")
    
except Exception as e:
    print(f"\n✗ Error: {e}")
    print("\nTo install Scapy, run:")
    print("  pip install scapy")
    print("\nOn Windows, also install Npcap from: https://npcap.com/")