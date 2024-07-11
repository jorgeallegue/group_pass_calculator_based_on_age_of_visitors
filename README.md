# Group Pass Calculator Based on Age of Visitors

**Versions Used**:
- `pytest==8.2.2`
- `python==3.12.4`
- `getch==1.0`

## Exercise: Group Entrance Price Calculation

**Objective:**
Develop a program that calculates the total entrance price for a group of visitors to a zoo based on their ages. The program should also provide a detailed breakdown of prices by age group.

**Price Rules:**
- Children aged 2 years or younger: Free entry.
- Children aged 3 to 12 years: 14 euros.
- Adults aged 13 years and older: 23 euros.
- Seniors (65 years and older): 18 euros.

## Instructions:
1. **Data Entry:**
   - The program should prompt for the ages of group members one by one.
   - Data entry should terminate when an empty string is entered.

2. **Validation:**
   - Ensure that entered ages are positive integers.

3. **Price Calculation:**
   - Calculate the total price for the group based on the price rules.
   - Provide a detailed breakdown of the cost for each age range.

4. **Output:**
   - Upon completing data entry, display the total price for the group.
   - Show a detailed breakdown of prices by age group.

## Implementation Help:
You can use data structures like lists or tuples to store ages and prices as they are entered.

## Execution Example:
1. Enter visitor's age (leave blank to finish): 5
2. Enter visitor's age (leave blank to finish): 30
3. Enter visitor's age (leave blank to finish): 70
4. Enter visitor's age (leave blank to finish):
5. Total price for the group: 55 euros
6. Breakdown by ages:
   - Children (3-12 years): 1 x 14 euros = 14 euros
   - Adults (13-64 years): 1 x 23 euros = 23 euros
   - Seniors (65+ years): 1 x 18 euros = 18 euros

## Final Considerations:
- Ensure the program handles invalid inputs correctly and prompts for age re-entry if an incorrect value is entered.
- The program should be user-friendly and provide clear and accurate results.

## Aesthetics of the terminal:

"""
               1         2         3        
      1234567890123456789012345678901234567
01    TIPO             PU     Q       TOTAL
02    =====================================
03    BEBE (≤2)      0.00    99     9999.99
04    NINO (≤12)    14.00    99     9999.99
05    ADULTO (<65)  23.00    99     9999.99
06    JUBILADO      18.00    99     9999.99
07    -------------------------------------
08                          999    99999.99
09                          
10    EDAD: 
11    CONF
"""