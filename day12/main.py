# Namespaces: Local vs Global Scope
def increase_friends():
    # Modifying global variables
    # (Discouraged)
    global enemies
    enemies += 1
    # Local scope
    friends = 2
    # friends = 2
    print(f"friends inside function: {friends}")


friends = 1
enemies = 1
increase_friends()
# Global scope
# friends still 1
print(f"friends outside function: {friends}")
