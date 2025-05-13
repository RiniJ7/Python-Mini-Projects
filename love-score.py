def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).lower()
    
    # Count TRUE letters
    t_count = combined_names.count('t')
    r_count = combined_names.count('r')
    u_count = combined_names.count('u')
    e_count = combined_names.count('e')
    
    true_total = t_count + r_count + u_count + e_count
    
    # Count LOVE letters
    l_count = combined_names.count('l')
    o_count = combined_names.count('o')
    v_count = combined_names.count('v')
    e_count = combined_names.count('e')
    
    love_total = l_count + o_count + v_count + e_count
    
    # Combine the scores into a 2-digit number
    love_score = int(str(true_total) + str(love_total))
    
    # Print the love score
    print(f"Your love score is: {love_score}")
    
    return love_score

# Example inputs
calculate_love_score("Angela Yu", "Jack Bauer")  # Should output 53
calculate_love_score("Kanye West", "Kim Kardashian")  # Should output 42
calculate_love_score("Brad Pitt", "Jennifer Aniston")  # Another example
calculate_love_score("Romeo", "Juliet")  # Classic example