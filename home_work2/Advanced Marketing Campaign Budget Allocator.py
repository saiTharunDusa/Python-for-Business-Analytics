# This function calculates the increasing budget based on campaign_goal.
def selected_campaign_goal(campaign_goal_str, channels_dict):
    # if the camapaign_goal is Brand Awareness, then increasing the budget by 15%.
    if(campaign_goal_str == 'Brand Awareness'):
        value = channels_dict['Social Media']
        value += ((15 / 100) * value)
        channels_dict['Social Media'] = value
        value = channels_dict['Advertising']
        value += ((15 / 100) * value)
        channels_dict['Advertising'] = value
    # if the camapaign_goal is Lead Generating, then increasing the budget by 10%.
    elif(campaign_goal_str == 'Lead Generation'):
        value = channels_dict['Email Marketing']
        value += ((10 / 100) * value)
        channels_dict['Email Marketing'] = value
    # if the campaign_goal is sales, then increasing the budget by 5%.
    else:
        value = channels_dict['Social Media']
        value += ((5 / 100) * value)
        channels_dict['Social Media'] = value
        value = channels_dict['Email Marketing']
        value += ((5 / 100) * value)
        channels_dict['Email Marketing'] = value
        value = channels_dict['Advertising']
        value += ((5 / 100) * value)
        channels_dict['Advertising'] = value
        

# This function adjusts base budget based on target_audience.
def calculate_budget(target_audience_str, channels_dict):
    # increasing the budget slightly by 2%.
    if(target_audience_str == 'Gen Z'):
        value = channels_dict['Social Media']
        value += ((2 / 100) * value)
        channels_dict['Social Media'] = value
    elif(target_audience_str == 'Millennials'):
        value = channels_dict['Email Marketing']
        value += ((2 / 100) * value)
        channels_dict['Email Marketing'] = value
    else:
        value = channels_dict['Advertising']
        value += ((2 / 100) * value)
        channels_dict['Advertising'] = value
    

def main():
    # printing the heading. And storing the advertisement and their budget in a dictionary.
    print('Advanced Marketing Campaign Budget Allocator')
    channels_dict = {
        "Social Media" : 5000,
        "Email Marketing" : 3000,
        "Advertising" : 2000
        }
    initial_base_budget = 10000
    temp_var1 = 'Marketing Compaign'
    temp_var2 = 'Budget'
    print()
    print(f'{temp_var1:<25} {temp_var2:<25}')
    # printing the initial budget values.
    for item,val in channels_dict.items():
        print(f'{item:<25} {val:<25}')

    print()
    print(f'Initial Budget for the Marketing Campaign is: {initial_base_budget}')

    # storing the target_audience and campaign_goal in a dictionary so that it would be easy for user
    # to access it by typing index number related to target_audience and campaign_goal.
    target_audience_dict = {
        1 : 'Gen Z',
        2 : 'Millennials',
        3 : 'Gen X'
        }
    campaign_goal_dict = {
        1 : 'Brand Awareness',
        2 : 'Lead Generation',
        3 : 'Sales'
        }
    print()
    print('Choose the target_audience and campaign_goal with the below choices:')
    for item,val in target_audience_dict.items():
        print(f'{item:<5} {val:<5}')

    print()
    for item,val in campaign_goal_dict.items():
        print(f'{item:<5} {val:<5}')

    print()
    # taking inputs from the user.
    user_target_audience = int(input('Enter your target audience choice number: '))
    print()
    user_campaign_goal = int(input('Enter your campaign goal choice number: '))

    print()
    # calling the calculate_budget() function to adjust the base budget based on target_audience given by the user.
    print('Adjusting the base budget based on user_target_audience ')
    calculate_budget(target_audience_dict[user_target_audience], channels_dict)
    for item,val in channels_dict.items():
        print(f'{item:<5} {val:<5}')

    print()
    # calling the selected_campaign_goal() function to adjust the increasing budget based on campaign_goal given by the user.
    print('Increasing the budget values based on user_campaign_goal ')
    selected_campaign_goal(campaign_goal_dict[user_campaign_goal], channels_dict)
    for item,val in channels_dict.items():
        print(f'{item:<5} {val:<5}')

    # Since budgets of the advertisement campaigns gets updated due to target_audience and campaign_goal.
    # Therefore, caluculating the sum of allocated budget which would be useful in calculating the remaining budget.
    sum_of_allocated_budget = 0
    for val in channels_dict.values():
        sum_of_allocated_budget += val

    print()
    print(f'Total allocated budget is {sum_of_allocated_budget}')
    print(f'Initial budget was {initial_base_budget}')
    
    total_remaining_budget = sum_of_allocated_budget - initial_base_budget

    # printing the total remaining budget to the user.
    print(f'The total remainging budget is {total_remaining_budget}')



main()
