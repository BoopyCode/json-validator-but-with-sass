#!/usr/bin/env python3
import json
import sys

def validate_with_sass(json_str):
    """Validates JSON but with the attitude you deserve at 2 AM."""
    
    # First, check if it's even trying
    if not json_str.strip():
        return "Oh, you gave me empty space. How avant-garde.\n"
    
    try:
        json.loads(json_str)
        return "\n✅ JSON is valid! (Surprisingly)\n"
        
    except json.JSONDecodeError as e:
        # Time for some tough love
        lines = json_str.split('\n')
        error_line = e.lineno - 1
        col = e.colno - 1
        
        # Build the sassy error message
        sass = [
            "\n❌ JSON ERROR - Let me translate that for you:\n",
            f"Line {e.lineno}, Column {e.colno}: {e.msg}",
            "\nHere's where things went wrong:\n",
        ]
        
        # Show context (but keep it brief)
        start = max(0, error_line - 1)
        end = min(len(lines), error_line + 2)
        
        for i in range(start, end):
            prefix = "→ " if i == error_line else "  "
            sass.append(f"{prefix}{lines[i]}")
            
            if i == error_line:
                # Point to the exact spot (approximately)
                pointer = " " * (col + 2) + "^"
                sass.append(f"  {pointer}")
        
        # Add some helpful(?) commentary
        sass.append("\n💡 Pro tip: ")
        
        if 'Unexpected token' in str(e):
            sass.append("That character doesn't belong there. Like socks with sandals.")
        elif 'Expecting' in str(e):
            sass.append("You forgot something. Like your keys. Or a closing bracket.")
        elif 'Extra data' in str(e):
            sass.append("Too much of a good thing. Like that third cup of coffee.")
        else:
            sass.append("Maybe try writing it on paper first? With crayons?")
        
        sass.append("\n")
        return "\n".join(sass)

def main():
    """Main function - handles file or stdin."""
    if len(sys.argv) > 1:
        # Read from file
        try:
            with open(sys.argv[1], 'r') as f:
                content = f.read()
        except FileNotFoundError:
            print(f"File '{sys.argv[1]}' not found. Did you imagine it?")
            return 1
    else:
        # Read from stdin
        content = sys.stdin.read()
    
    result = validate_with_sass(content)
    print(result)
    return 0 if "✅" in result else 1

if __name__ == "__main__":
    sys.exit(main())
