class Move:
    def __init__(self, name, damage, priority, secondaryEffect, accuracy , type, category):
        self.name = name    # Name of the move
        self.damage = damage        # Damage of the move
        self.priority = priority    # Priority check, higher priority moves go first
        self.secondaryEffect = secondaryEffect  # Secondary Effect (Ej.. stat changes) 
        self.accuracy = accuracy    # Accuracy of a move (0 - 100)
        self.type = type            # Move Type
        self.category = category    # Special (SP), Physical(PH), Status (ST)
