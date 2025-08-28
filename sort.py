def sorting_stack(width, height, length, mass):
    """
    Sorts a package into STANDARD, SPECIAL, or REJECTED based on its dimensions and mass.
    width: Width of the package in cm.
    height: Height of the package in cm.
    length: Length of the package in cm.
    mass: Mass of the package in kg.
    Returns: "STANDARD", "SPECIAL", or "REJECTED"
    """
    volume = width * height * length
    
    is_bulky = volume >= 1000000 or width >= 150 or height >= 150 or length >= 150
    is_heavy = mass >= 20
    
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"
