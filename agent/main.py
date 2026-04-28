import json

# Load tree
with open("../tree/reflection-tree.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Convert list to dictionary for easy lookup
tree = {node["id"]: node for node in data["nodes"]}

current_node = "START"
state = {}

print("\n=== Daily Reflection Session ===")

while True:
    node = tree[current_node]
    
    if "text" in node:
        print("\n" + node["text"])
    
    # QUESTION NODE
    if node["type"] == "question":
        options = node["options"]
        
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")
        
        while True:
            try:
                choice = int(input("\nEnter choice (1-4): ")) - 1
                if 0 <= choice < len(options):
                    break
                else:
                    print("Invalid choice. Try again.")
            except:
                print("Enter a number.")
        
        selected = options[choice]
        state[current_node] = selected
        
        current_node = node["next"]
    
    # DECISION NODE
    elif node["type"] == "decision":
        last_answer = list(state.values())[-1]
        
        for rule in node["rules"]:
            if last_answer in rule["if"]:
                current_node = rule["goto"]
                break
    
    # AUTO NODES (start, reflection, bridge)
    elif node["type"] in ["start", "reflection", "bridge"]:
        input("\nPress Enter to continue...")
        current_node = node["next"]
    
    # SUMMARY NODE
    elif node["type"] == "summary":
        print("\n--- Your Reflection Summary ---\n")
    
        for q_id, answer in state.items():
            question_text = tree[q_id]["text"]
            print(f"{question_text}")
            print(f"→ {answer}\n")
    
        input("Press Enter to continue...")
        current_node = node["next"]
    
    # END NODE
    elif node["type"] == "end":
        print("\n=== Reflection complete ===\n")
        break