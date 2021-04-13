# Namespaces: Local vs Global Scope
def increase_friends():
    # Local scope
    friends = 2
    # friends = 2
    print(f"friends inside function: {friends}")


friends = 1
increase_friends()
# Global scope
# friends still 1
print(f"friends outside function: {friends}")
